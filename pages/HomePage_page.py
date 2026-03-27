from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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
    BUTTON_CANCEL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvCancelPackage")
    BUTTON_CONTINUTE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btContinue")
    BACKGROUND = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvBack")
    BUTTON_SEE_ALL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvSeeAll")
    RECHARGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvRecharge")
    
    #---Dịch vụ mobigames
    MOBIGAMES_DETAIL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivThumb")
    MOBIGAMES_REGISTER1 = (AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="vms.com.vn.mymobifone:id/tvRegister"])[1]')
    MOBIGAMES_REGISTER2 = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btContinue")
    MOBIGAME_UNREGISTER = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vms.com.vn.mymobifone:id/tvRegister" and @text="Hủy"]')
    #---Gói cước của bạn
    BUTTON_EXTEND = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvExtendPackage")
    BUTTON_CANCEL_EXTEND = (AppiumBy.ID,"vms.com.vn.mymobifone:id/tvCancelExtendPackage")
    DETAIL_MY_PAKAGE = (AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="vms.com.vn.mymobifone:id/rlPB4"]')
    BUTTON_CONFIRM_EXTEND = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvConfirmExtend")
    BUTTON_CONFIRM_CANCEL_EXTEND = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvConfirmCancelExtend")
    #-- Thông tin sử dụng/tiện ích nổi bật
    CVQT = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[1]')
    KNDL1 = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[4]')
    VTC83 = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[5]')
    KHS = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[6]')
    BUTTON_BACK_LEFT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivLeftIcon")
    #--Tiện ích của bạn
    
    
    BTN_CANCEL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btCancel")
    INFORMATION = (AppiumBy.ID, "vms.com.vn.mymobifone:id/llUsageInfos")
    INFOR_SUBCRIBER = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivArrowInfo")
    INFOR_LOOKUP = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/lineCheckCharges"]/android.widget.ImageView')
    BUTTON_BACK = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivBack")
    DEPOSITE_HISTORY = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/lineHistoryTopup"]/android.widget.ImageView')
    SUBCRIBER_HISTORY = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/lineHistoryPackage"]/android.widget.ImageView')
    BUTTON_BUY_PAKAGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvBuyPackage")
    BUTTON_REGISTER_KNDL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/bvRegKNDL")
    KNDL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivCardLoyalty")
    # Hẹn roaming
    BUTTON_RESHEDULE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnDoiLichHen")
    BUTTON_CANCEL_SCHEDULE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnHuyRoaming")
    BUTTON_SUBMIT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnSubmit")
    ET_TIME = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etTime")
    #Đổi số điện thoại con
    CHANGE_NUMBER = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/llChangeNumber"]/android.widget.ImageView')
    NEW_NUMBER = (AppiumBy.XPATH, '(//android.widget.RelativeLayout[@resource-id="vms.com.vn.mymobifone:id/rlView"])[2]')
    ADD_PHONE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlAddPhone")
    INPUT_PHONE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etPhoneNumber")
    BUTTON_ACCEPT =(AppiumBy.ID, "vms.com.vn.mymobifone:id/btAccept")
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
                    "percent": 0.6
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
    # Hàm click mua gói
    def click_recharge(self):
        self.click(self.RECHARGE)
    #Click Mobigame
    #----Register
    def click_mobigames_detail(self):
        self.click(self.MOBIGAMES_DETAIL)
    def click_mobigames_register1(self):
        self.click(self.MOBIGAMES_REGISTER1)
    def click_mobigames_register2(self):
        self.click(self.MOBIGAMES_REGISTER2)
    #----Unregister
    def click_mobigames_unregister(self):
        self.click(self.MOBIGAME_UNREGISTER)
    
    #Click button Back
    def click_button_back(self):
        self.click(self.BUTTON_BACK)
    #Click button Xem tất cả
    def click_button_see_all(self):
        self.click(self.BUTTON_SEE_ALL)
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
    def click_button_cancel(self):
        self.click(self.BUTTON_CANCEL)
    #Click button continute
    def click_button_continute(self):
        self.click(self.BUTTON_CONTINUTE)
    #-----Gói cước của bạn-------
    def click_button_extend(self):
        self.click(self.BUTTON_EXTEND)
    def click_button_cancel_extend(self):
        self.click(self.BUTTON_CANCEL_EXTEND)
    def click_detail_my_pakage(self):
        self.click(self.DETAIL_MY_PAKAGE)    
    def click_button_confirm_cancel_extend(self):
        self.click(self.BUTTON_CONFIRM_CANCEL_EXTEND)
    def click_button_confirm_extend(self):
        self.click(self.BUTTON_CONFIRM_EXTEND)
    #---Hẹn roaming ------
    def click_button_reschedule(self):
        self.click(self.BUTTON_RESHEDULE)
    def click_button_cancel_schedule(self):
        self.click(self.BUTTON_CANCEL_SCHEDULE)
    def click_button_submit(self):
        self.click(self.BUTTON_SUBMIT)
    def et_time(self, keword):
        self.click(self.ET_TIME)
        self.send_keys(self.ET_TIME, keword)
    #Thông tin sử dụng/Tiện ích nổi bật
    def click_kndl1(self):
        self.click(self.KNDL1)
    def click_cvqt(self):
        self.click(self.CVQT)    
    def click_vtc83(self):
        self.click(self.VTC83)
    def click_khs(self):
        self.click(self.KHS)
    def click_button_back_left(self):
        self.click(self.BUTTON_BACK_LEFT)
        
    # Tiện ích của bạn
    def click_icon(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[{index}]')
        self.click(locator)
    def click_btn_cancel(self):
        self.click(self.BTN_CANCEL)
        
    # Đổi số điện thoại con
    def click_change_number(self):
        self.click(self.CHANGE_NUMBER)
    def click_new_number(self):
        self.click(self.NEW_NUMBER)
    def add_phone(self, keyword):
        self.click(self.ADD_PHONE)
        self.send_keys(self.INPUT_PHONE, keyword)
    def click_button_accept(self):
        self.click(self.BUTTON_ACCEPT)
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