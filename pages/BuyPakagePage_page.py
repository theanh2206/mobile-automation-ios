from pages.BasePage_page import BasePage
from pages.LocatorPage_page import LocatorPage



class BuyPakagePage(BasePage):
    locators = LocatorPage()
    
    #Search gói cước trên thanh tìm kiếm
    def search_package(self, keyword):
        self.click(self.locators.SEARCH_BOX)
        self.send_keys(self.locators.SEARCH_INPUT, keyword)
        
        
     
     
     
     
     
        
    #         ===== VERIFY =====
    def wait_for_result(self, keyword):
        self.wait_for_text(keyword)

    def is_result_displayed(self, keyword):
        return self.is_text_displayed(keyword)