from pages.BasePage_page import BasePage
from pages.LocatorPage_page import LocatorPage
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class BuyPakagePage(BasePage):
    locators = LocatorPage()
    #Click tab Mua gói
    def click_buy_pakage(self):
        self.click(self.locators.BUY_PAKAGE)
    
    #Search gói cước trên thanh tìm kiếm
    def search_package(self, keyword):
        self.click(self.locators.SEARCH_BOX)
        self.send_keys(self.locators.SEARCH_INPUT, keyword)
    #Click thẻ gói cước D5
    def click_card_D5(self):
        self.click(self.locators.DETAIL_D5)
    #Click vào menu
    def click_menu(self):
        self.click(self.locators.MENU)   
    #Click button đăng ký D5
    def click_register_d5(self):
        self.click(self.locators.REGISTER_BUTTON)
    #Click button Huỷ đăng ký
    def click_button_cancel(self):
        self.click(self.locators.BUTTON_CANCEL)
    #Click button continute
    def click_button_continute(self):
        self.click(self.locators.BUTTON_CONTINUTE)
    #Click icon tạo gói cước cá nhân
    def click_personal_flex(self):
        self.click(self.locators.PERSONAL_FLEX)
    def click_time_flex(self):
        self.click(self.locators.TIME_FLEX)
    def click_icon_cvqt(self):
        self.click(self.locators.ICON_CVQT)
    def click_button_create_pakage(self):
        self.click(self.locators.BUTTON_CREATE_PAKAGE)
    def click_payment_confirm(self):
        self.click(self.locators.PAYMENT_CONFIRM)
    #----------Hàm nhập OTP-----------
    def input_otp(self, otp_code):
        otp_inputs = self.wait.until(
            EC.presence_of_all_elements_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@text="_"]')
        )
    )

        otp_inputs[0].click()
        time.sleep(0.5)

        for digit in otp_code:
            self.driver.press_keycode(7 + int(digit))

        self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout")
        )
    )
    #Back lại bước vừa xong 
    def press_back(self):
        return super().press_back()
    # Hàm scroll tới phần tử cụ thể
    def scroll_to_element(self, text, max_scroll=6):
        size = self.driver.get_window_size()

        for i in range(max_scroll):
            print(f"🔍 Lần {i+1}: tìm '{text}'")

            elements = self.driver.find_elements(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().textContains("{text}")'
                )

            if elements:
                return elements[0]

           # scroll mỗi vòng
            self.driver.execute_script(
                "mobile: scrollGesture",
                {
                "left": int(size["width"] * 0.1),
                "top": int(size["height"] * 0.3),
                "width": int(size["width"] * 0.8),
                "height": int(size["height"] * 0.6),
                "direction": "down",
                "percent": 0.7,
                "speed": 500
                }
            )

            time.sleep(1)  # cho UI load

        raise Exception(f"❌ Không tìm thấy: {text}")
    #--Hàm scroll dọc
    def scroll_to_element1(self, text, max_scroll=6):
        size = self.driver.get_window_size()

        for i in range(max_scroll):
            print(f"🔍 Lần {i+1}: tìm '{text}'")

            try:
                element = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR,
                     f'new UiSelector().textContains("{text}")')
                    )
                )
                print(f"✅ Tìm thấy '{text}'")
                return element
            except:
                pass
            WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.ScrollView"))
                                                )
        # 👉 Scroll
            self.driver.execute_script(
                "mobile: scrollGesture",
                    {
                    "left": int(size["width"] * 0.2),
                    "top": int(size["height"] * 0.5),
                    "width": int(size["width"] * 0.6),
                    "height": int(size["height"] * 0.3),
                    "direction": "up",
                    "percent": 0.6,
                    "speed": 600
                    }
                    )       
            time.sleep(1)

        raise Exception(f"❌ Không tìm thấy: {text}")
    #--------------Hàm scroll ngang
    def scroll_horizontal_utils(self, direction="left", times=1):
        carousel = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
            By.XPATH,
            '//androidx.recyclerview.widget.RecyclerView[@resource-id="vms.com.vn.mymobifone:id/rvUtils"]'
            ))
        )

        for _ in range(times):
            loc = carousel.location
            size = carousel.size

            self.driver.execute_script("mobile: swipeGesture", {
                "left": loc["x"],
                "top": loc["y"],
                "width": size["width"],
                "height": size["height"],
                "direction": direction,
                "percent": 0.8
            })
    #Swipe banner ngang
    def swipe_banner(self, times=1, duration=1200, delay=0.5):
        try:
            banner = self.driver.find_element(
            By.ID, "vms.com.vn.mymobifone:id/rlSliderBannerHome"
        )
        except NoSuchElementException:
            raise Exception("❌ Không tìm thấy banner để swipe")
        location = banner.location
        size = banner.size
    # 👉 Tối ưu khoảng cách swipe (gần full width)
        start_x = int(location['x'] + size['width'] * 0.95)
        end_x = int(location['x'] + size['width'] * 0.05)
        y = int(location['y'] + size['height'] / 2)
        for i in range(times):
            print(f"👉 Swipe lần {i+1}")
            self.driver.swipe(start_x, y, end_x, y, duration)
            time.sleep(delay)
        
    #         ===== VERIFY =====
    def wait_for_result(self, keyword):
        self.wait_for_text(keyword)

    def is_result_displayed(self, keyword):
        return self.is_text_displayed(keyword)