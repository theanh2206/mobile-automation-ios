from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class HomePage(BasePage):

    # ===== LOCATORS =====
    SEARCH_BOX = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etSearch4x")
    SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    AVATA = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivAvatar")
    MENU = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivMenu")
    NOTIFICATION = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivNotification")
    DETAIL_D5 = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vms.com.vn.mymobifone:id/tvPackName" and @text="D5"]')
    REGISTER_BUTTON = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvRegister")
    CANCEL_BUTTON = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvCancelPackage")
    BUTTON_CONTINUTE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btContinue")
    BACKGROUND = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvBack")
    # ===== Locator trong thông tin sử dụng =========
    INFORMATION = (AppiumBy.ID, "vms.com.vn.mymobifone:id/llUsageInfos")
    INFOR_SUBCRIBER = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivArrowInfo")
    INFOR_LOOKUP = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/lineCheckCharges"]/android.widget.ImageView')
    BUTTON_BACK = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivBack")
    DEPOSITE_HISTORY = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/lineHistoryTopup"]/android.widget.ImageView')
    SUBCRIBER_HISTORY = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/lineHistoryPackage"]/android.widget.ImageView')
    BUTTON_BUY_PAKAGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvBuyPackage")
    BUTTON_REGISTER_KNDL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/bvRegKNDL")
    KNDL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivCardLoyalty")
#      ===== ACTION =====
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
                "percent": 0.7
                }
            )

            time.sleep(1)  # cho UI load

        raise Exception(f"❌ Không tìm thấy: {text}")
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
    # Hàm tìm kiếm gói cước
    def search_package(self, keyword):
        self.click(self.SEARCH_BOX)
        self.send_keys(self.SEARCH_INPUT, keyword)
    #Click button Back
    def click_button_back(self):
        self.click(self.BUTTON_BACK)
    #Click icon avata
    def click_avata(self):
        self.click(self.AVATA)    
    #Click icon Thông báo
    def click_notification(self):
        self.click(self.NOTIFICATION)
    #Click vào menu
    def click_menu(self):
        self.click(self.MENU)    
    #Click thông tin sử dung   
    def click_infomation(self):
        self.click(self.INFORMATION)
    #Click thông tin thuê bao    
    def click_infor_subcriber(self): 
        self.click(self.INFOR_SUBCRIBER)
    #Click Tra cứu thông tin cước
    def click_infor_lookup(self):
        self.click(self.INFOR_LOOKUP)
    #CLick icon Lịch sử nạp tiền
    def click_deposite_history(self):
        self.click(self.DEPOSITE_HISTORY)
    #CLick icon lịch sử gói cước
    def click_subcriber_history(self):
        self.click(self.SUBCRIBER_HISTORY)
    #Click button Mua thêm trong thông tin sử dụng
    def click_button_buy_pakage(self):
        self.click(self.BUTTON_BUY_PAKAGE)
    #Click button Đăng ký thẻ KNDL
    def click_button_register_KNDL(self):
        self.click(self.BUTTON_REGISTER_KNDL)
    #Click card KNDL (SĐT đã đăng ký KNDL)
    def click_card_kndl(self):
        self.click(self.KNDL)
    #Click thẻ gói cước D5
    def click_card_D5(self):
        self.click(self.DETAIL_D5)
    #Click button đăng ký D5
    def click_register_d5(self):
        self.click(self.REGISTER_BUTTON)
    #Click button Huỷ đăng ký
    def click_cancel_button(self):
        self.click(self.CANCEL_BUTTON)
    #Click button continute
    def click_button_continute(self):
        self.click(self.BUTTON_CONTINUTE)
        
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