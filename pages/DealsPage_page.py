from pages.BasePage_page import BasePage
from pages.LocatorPage_page import LocatorPage
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class DealsPage(BasePage):
    locators = LocatorPage()
    #Click icon Ưu đãi
    def click_icon_deals(self, index):
        locator = (By.XPATH, f'//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/bottomBar"]/android.widget.LinearLayout/android.widget.FrameLayout[{index}]')
        self.click(locator)
    #Search gói cước trên thanh tìm kiếm
    def search_package(self, keyword):
        self.click(self.locators.SEARCH_DEALS)
        self.click(self.locators.SEARCH_BOX1)
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
    def click_button_continute1(self):
        self.click(self.locators.BUTTON_CONTINUTE1)
    #Back lại bước vừa xong 
    def press_back(self):
        return super().press_back()
    #Ẩn bàn phím
    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except:
            try:
                self.driver.back()
            except:
                try:
                    self.driver.tap([(100, 100)])
                except:
                    pass
    #Mẹo tích điểm
    #Click icon Ưu đãi
    def click_save_point(self):
        self.click(self.locators.SAVE_POINT)
    def click_list_save_point(self, index):
        locator = (By.XPATH, f'//androidx.recyclerview.widget.RecyclerView[@resource-id="vms.com.vn.mymobifone:id/rcvTipsMyPoint"]/android.widget.RelativeLayout[{index}]/android.widget.FrameLayout/android.widget.LinearLayout')
        self.click(locator)
    
    
    
    
    
    
    
    
    #         ===== VERIFY =====
    def wait_for_result(self, keyword):
        self.wait_for_text(keyword)

    def is_result_displayed(self, keyword):
        return self.is_text_displayed(keyword)