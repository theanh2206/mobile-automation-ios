import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.BuyPakagePage_page import BuyPakagePage
from pages.BasePage_page import BasePage

#Tìm kiếm gói cước/ dịch vụ bất kỳ trên thanh tìm kiếm
#TC40. Tìm kiếm gói cước tồn tại trong db
@pytest.mark.tc40
def test_search_package_D5(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.search_package("D5")
    buypakage.wait_for_result("D5")
    assert buypakage.is_result_displayed("D5")
#TC41. Tìm kiếm gói cước không tồn tại trong db
@pytest.mark.tc41
def test_search_package_TheAnh(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.search_package("Thế Anh")
    buypakage.wait_for_result("Lịch sử")
    assert buypakage.is_result_displayed("Lịch sử")
#TC43. Tìm kiếm dịch vụ tồn tại trong db
@pytest.mark.tc43
def test_search_services(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.search_package("MobiGames")
    buypakage.wait_for_result("MobiGames")
    assert buypakage.is_result_displayed("MobiGames")
#TC44. Tìm kiếm gói cước không tồn tại trong db
@pytest.mark.tc44
def test_search_services_TheAnh(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.search_package("Thế Anh")
    buypakage.wait_for_result("Lịch sử")
    assert buypakage.is_result_displayed("Lịch sử")
#TC45. Đăng ký gói cước ở thanh tìm kiếm
@pytest.mark.tc41
def test_register_pakage(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.search_package("D5")
    buypakage.click_card_D5()
    buypakage.click_register_d5()
    buypakage.input_otp("888888")
    buypakage.wait_for_result("Đăng ký gói cước thành công")
    assert buypakage.is_result_displayed("Đăng ký gói cước thành công")
#TC46. Huỷ gói cước ở thanh tìm kiếm
@pytest.mark.tc46
def test_unregister_pakage(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.search_package("D5")
    buypakage.wait_for_result("D5")
    buypakage.click_card_D5()
    buypakage.click_button_cancel()
    buypakage.click_button_continute()
    buypakage.input_otp("888888")
    buypakage.wait_for_result("Huỷ gói cước thành công")
    assert buypakage.is_result_displayed("Huỷ gói cước thành công")
#TC47. Tạo gói cước cá nhân
#1. Đăng ký bằng OTP
@pytest.mark.tc47
def test_create_pakage_OTP(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_personal_flex()
    buypakage.click_button_create_pakage()
    buypakage.click_payment_confirm()
    buypakage.input_otp("000000")
    buypakage.wait_for_result("Đăng ký gói cước thành công")
    assert buypakage.is_result_displayed("Đăng ký gói cước thành công")
#2. Đăng ký bằng mã pin
@pytest.mark.tc47_1
def test_create_pakage_PIN(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_personal_flex()
    buypakage.click_button_create_pakage()
    buypakage.click_payment_confirm()
    buypakage.input_otp("0000")
    buypakage.click_button_accept()
    buypakage.wait_for_result("Đăng ký gói cước thành công")
    assert buypakage.is_result_displayed("Đăng ký gói cước thành công")
#TC48. Tạo gói cước linh hoạt thời gian
@pytest.mark.tc48
def test_create_pakage_flex(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_time_flex()
    
    buypakage.wait_for_result("Gói cước linh hoạt thời gian")
    assert buypakage.is_result_displayed("Gói cước linh hoạt thời gian")