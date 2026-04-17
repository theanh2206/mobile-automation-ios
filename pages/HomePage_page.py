from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage_page import BasePage
from pages.LocatorPage_page import LocatorPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.common.exceptions import NoSuchElementException
import time


class HomePage(BasePage):
    locators = LocatorPage()
    def click_button_by_text(self, text, index=1):
        xpath = f'(//XCUIElementTypeButton[@name="{text}"])[{index}]'
        element = self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath)))
        element.click()

    def click_by_text(self, text, index=1):
        xpath = f'(//XCUIElementTypeStaticText[@name="{text}"])[{index}]'
        element = self.driver.find_element(AppiumBy.XPATH, xpath)
        element.click()
    def click_by_image(self, text, index=1):
        xpath = f'(//XCUIElementTypeImage[@name="{text}"])[{index}]'
        element = self.driver.find_element(AppiumBy.XPATH, xpath)
        element.click()
    # Hàm scroll tới phần tử cụ thể
    def scroll_to_element1(self, text, max_scroll=6):
        for i in range(max_scroll):
            print(f"🔍 Lần {i+1}: tìm '{text}'")

            elements = self.driver.find_elements(
                AppiumBy.IOS_PREDICATE,
                f'name CONTAINS[c] "{text}" OR label CONTAINS[c] "{text}" OR value CONTAINS[c] "{text}"'
            )

            if elements:
                return elements[0]

            try:
                scroll_view = self.driver.find_element(
                    AppiumBy.IOS_CLASS_CHAIN,
                    '**/XCUIElementTypeScrollView'
                )

                self.driver.execute_script(
                    "mobile: scroll",
                    {
                        "element": scroll_view.id,
                        "direction": "down"
                    }
                )
            except Exception as e:
                print("⚠️ Không tìm thấy scroll view:", e)

            time.sleep(1)

        raise Exception(f"❌ Không tìm thấy: {text}")
    #--Hàm scroll dọc
    def scroll_to_element2(self, text, max_scroll=6):
        for i in range(max_scroll):
            print(f"🔍 Lần {i+1}: tìm '{text}'")
            elements = self.driver.find_elements(
                AppiumBy.IOS_PREDICATE,
                f'name CONTAINS[c] "{text}" OR label CONTAINS[c] "{text}"'
            )
            if elements:
                element = elements[0]
                if element.is_displayed():
                    print("✅ Đã hiển thị trên màn hình")
                    return element
                else:
                    print("⚠️ Tìm thấy nhưng chưa visible → scroll tiếp")
            print("👉 Swipe...")
            self.driver.execute_script("mobile: swipe", {"direction": "up"})
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
    
    def close_side_menu_ios(self):
        size = self.driver.get_window_size()
        self.driver.tap([
            (int(size['width'] * 0.9), int(size['height'] * 0.5))
        ])
    #Swipe banner ngang
    def swipe_banner(self, times=1, delay=0.5):
        try:
            banner = self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeCollectionView'
            )
            indicator = self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypePageIndicator'
            )
        except:
            raise Exception("❌ Không tìm thấy banner hoặc indicator")
        prev_value = indicator.get_attribute("value")
        for i in range(times):
            print(f"👉 Swipe lần {i+1}")
            self.driver.execute_script("mobile: swipe", {
                "element": banner.id,
                "direction": "left"
            })
            time.sleep(delay)
            current_value = indicator.get_attribute("value")
            # 👉 Nếu swipe mà không đổi → stop sớm
            if current_value == prev_value:
                print("⛔ Banner không đổi → dừng sớm")
                break
            prev_value = current_value
    #----------Hàm nhập OTP-----------
    def input_otp(self, otp_code):
        otp_inputs = self.wait.until(
            EC.presence_of_all_elements_located(
                (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField')
        )
    )
        for i, digit in enumerate(otp_code):
            otp_inputs[i].send_keys(digit)
    # Hàm scroll tới phần tử cụ thể
    def scroll_to_element3(self, text, max_scroll=6):
        for _ in range(max_scroll):
            elements = self.driver.find_elements(
                AppiumBy.ACCESSIBILITY_ID, text
        )
            if elements:
                return elements[0]

            self.driver.execute_script("mobile: swipe", {"direction": "up"})

        raise Exception(f"Không tìm thấy {text}")
    # Hàm tìm kiếm gói cước
    def search_package(self, keyword):
        self.click(self.locators.SEARCH_BOX)
        self.send_keys(self.locators.SEARCH_INPUT, keyword)
    #Click tiện ích nổi bật
    def click_icon_utilities(self, index):
        locator = (By.XPATH, f'//XCUIElementTypeScrollView/XCUIElementTypeOther[7]/XCUIElementTypeCollectionView/XCUIElementTypeCell[{index}]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
        self.click(locator)
    def click_icon_utilities1(self, index):
        locator = (By.XPATH, f'//XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView/XCUIElementTypeCell[{index}]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
        self.click(locator)

    def click_button_close1(self):
        self.click(self.locators.BUTTON_CLOSE1) 
    def click_button_back1(self):
        self.click(self.locators.BUTTON_BACK1)


    # Hàm click mua gói
    def click_recharge(self):
        self.click(self.locators.RECHARGE)
    #Click butto tất cả tiện ích
    def click_view_all_utils(self):
        self.click(self.locators.VIEW_ALL_UTILS)
    #Click Mobigame
    #----Register
    def click_mobigames_detail(self):
        self.click(self.locators.MOBIGAMES_DETAIL)
    def click_mobigames_register1(self):
        self.click(self.locators.MOBIGAMES_REGISTER1)
    def click_mobigames_register2(self):
        self.click(self.locators.MOBIGAMES_REGISTER2)
    #----Unregister
    def click_mobigames_unregister(self):
        self.click(self.locators.MOBIGAME_UNREGISTER)
    
    #Click button Back
    def click_button_back(self):
        self.click(self.locators.BUTTON_BACK)
    #Click button Xem tất cả
    def click_button_see_all(self):
        self.click(self.locators.BUTTON_SEE_ALL)
    #Click icon avata
    def click_avata(self):
        self.click(self.locators.AVATA)    
    #Click icon Thông báo
    def click_notification(self):
        self.click(self.locators.NOTIFICATION)
    #Click banner
    def click_banner(self):
        self.click(self.locators.BANNER)
    #Click vào menu
    def click_menu(self):
        self.click(self.locators.MENU)    
    #Click thông tin sử dung   
    def click_infomation(self):
        self.click(self.locators.INFORMATION)
    #Click thông tin thuê bao    
    def click_infor_subcriber(self): 
        self.click(self.locators.INFOR_SUBCRIBER)
    #Click Tra cứu thông tin cước
    def click_infor_lookup(self):
        self.click(self.locators.INFOR_LOOKUP)
    #CLick icon Lịch sử nạp tiền
    def click_deposite_history(self):
        self.click(self.locators.DEPOSITE_HISTORY)
    #CLick icon lịch sử gói cước
    def click_subcriber_history(self):
        self.click(self.locators.SUBCRIBER_HISTORY)
    #Click button Mua thêm trong thông tin sử dụng
    def click_button_buy_pakage(self):
        self.click(self.locators.BUTTON_BUY_PAKAGE)
    #Click button Đăng ký thẻ KNDL
    def click_button_register_KNDL(self):
        self.click(self.locators.BUTTON_REGISTER_KNDL)
    #Click card KNDL (SĐT đã đăng ký KNDL)
    def click_card_kndl(self):
        self.click(self.locators.KNDL)
    #Click thẻ gói cước D5
    def click_card_D5(self):
        self.click(self.locators.DETAIL_D5)
    #Click button đăng ký D5
    def click_register_d5(self):
        self.click(self.locators.REGISTER_BUTTON)
    #Click button Huỷ đăng ký
    def click_button_cancel(self):
        self.click(self.locators.BUTTON_CANCEL)
    #Click button continute
    def click_button_continute(self):
        self.click(self.locators.BUTTON_CONTINUTE)
    #-----Gói cước của bạn-------
    def click_button_extend(self):
        self.click(self.locators.BUTTON_EXTEND)
    def click_button_cancel_extend(self):
        self.click(self.locators.BUTTON_CANCEL_EXTEND)
    def click_detail_my_pakage(self):
        self.click(self.locators.DETAIL_MY_PAKAGE)    
    def click_button_confirm_cancel_extend(self):
        self.click(self.locators.BUTTON_CONFIRM_CANCEL_EXTEND)
    def click_button_confirm_extend(self):
        self.click(self.locators.BUTTON_CONFIRM_EXTEND)
    #---Hẹn roaming ------
    def click_button_reschedule(self):
        self.click(self.locators.BUTTON_RESHEDULE)
    def click_button_cancel_schedule(self):
        self.click(self.locators.BUTTON_CANCEL_SCHEDULE)
    def click_button_submit(self):
        self.click(self.locators.BUTTON_SUBMIT)
    def et_time(self, keword):
        self.click(self.locators.ET_TIME)
        self.send_keys(self.locators.ET_TIME, keword)
    #Thông tin sử dụng/Tiện ích nổi bật
    def click_kndl1(self):
        self.click(self.locators.KNDL1)
    def click_cvqt(self):
        self.click(self.locators.CVQT)    
    def click_vtc83(self):
        self.click(self.locators.VTC83)
    def click_khs(self):
        self.click(self.locators.KHS)
    def click_button_back_left(self):
        self.click(self.locators.BUTTON_BACK_LEFT)
        
    # Tiện ích của bạn
    def click_icon(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[{index}]')
        self.click(locator)
    def click_btn_cancel(self):
        self.click(self.locators.BTN_CANCEL)
    #Click dịch vụ nổi bật
    def click_avata_contact(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivAvatarContact"])[{index}]')
        self.click(locator)
        
    # Đổi số điện thoại con
    def click_change_number(self):
        self.click(self.locators.CHANGE_NUMBER)
    def click_new_number(self):
        self.click(self.locators.NEW_NUMBER)
    def add_phone(self, keyword):
        self.send_keys(self.locators.INPUT_PHONE, keyword)
    def click_button_accept(self):
        self.click(self.locators.BUTTON_ACCEPT)
    #Close menu
    def close_menu(self):
        self.tap_outside()
    def press_back(self):
        return super().press_back()
    #Check popup Huỷ gói cước thành công
    def is_check_popup_unregister(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(
                (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvMsg")
            )
        )
            return True
        except:
            return False

#         ===== VERIFY =====
    def wait_for_result(self, keyword):
        self.wait_for_text(keyword)

    def is_result_displayed(self, keyword):
        return self.is_text_displayed(keyword)