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
#1. Đăng ký bằng OTP
@pytest.mark.tc48
def test_create_pakage_flex_OTP(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_time_flex()
    buypakage.click_register_button2()
    buypakage.click_payment_confirm()
    buypakage.input_otp("000000")
    buypakage.wait_for_result("Đăng ký gói cước thành công")
    assert buypakage.is_result_displayed("Đăng ký gói cước thành công")
#2. Đăng ký bằng mã PIN
@pytest.mark.tc48_1
def test_create_pakage_flex_PIN(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_time_flex()
    buypakage.click_register_button2()
    buypakage.click_payment_confirm()
    buypakage.input_otp("0000")
    buypakage.click_button_accept()
    buypakage.wait_for_result("Đăng ký gói cước thành công")
    assert buypakage.is_result_displayed("Đăng ký gói cước thành công")
    
#TC49. Tìm kiếm gói bằng gói cước/quốc gia
@pytest.mark.tc49
def test_find_pakage(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.click_search_by_key("")
    buypakage.click_search_country()
    buypakage.send_key_country("Japan")
    buypakage.wait_for_result("Nhật Bản")
    buypakage.click_country("Nhật Bản")
    buypakage.click_button_apply()
    buypakage.wait_for_result("Tạo gói cước data roaming linh hoạt")
    assert buypakage.is_result_displayed("Tạo gói cước data roaming linh hoạt")
    
#TC50. Click kiểm tra cước chuyến đi
@pytest.mark.tc50
def test_click_check(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.click_check_trip()
    buypakage.wait_for_result("Bật dịch vụ CVQT")
    assert buypakage.is_result_displayed("Bật dịch vụ CVQT")
    
#TC51. Click gói cước quốc tế phổ biến
@pytest.mark.tc51
def test_popular_country(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.click_popular_country(1)
    buypakage.wait_for_result("Tìm kiếm gói cước")
    buypakage.press_back()
    buypakage.click_popular_country(2)
    buypakage.wait_for_result("Tìm kiếm gói cước")
    buypakage.press_back()
    buypakage.click_popular_country(3)
    buypakage.wait_for_result("Tìm kiếm gói cước")
    buypakage.press_back()
    buypakage.click_popular_country(4)
    buypakage.wait_for_result("Tìm kiếm gói cước")
    buypakage.press_back()
    buypakage.click_popular_country(5)
    buypakage.wait_for_result("Tìm kiếm gói cước")
    buypakage.press_back()
    buypakage.click_popular_country(6)
    buypakage.wait_for_result("Tìm kiếm gói cước")
    buypakage.press_back()
    buypakage.wait_for_result("Gói cước quốc tế phổ biến")
    assert buypakage.is_result_displayed("Gói cước quốc tế phổ biến")
    
#TC52. Đăng ký tạo gói cước data roaming linh hoạt
#1. Đăng ký gói roaming
@pytest.mark.tc52
def test_create_pakage_roaming(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.click_pakage_roaming()
    buypakage.scroll_to_element("Đăng ký")
    buypakage.click_create_pakage_roaming()
    buypakage.click_register_d5()
    buypakage.click_payment_confirm()
    buypakage.input_otp("000000")
    buypakage.wait_for_result("Đăng ký gói cước thành công")
    assert buypakage.is_result_displayed("Đăng ký gói cước thành công")
#2. Đăng ký gói xung đột
@pytest.mark.tc52_1
def test_create_pakage_roaming1(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.click_pakage_roaming()
    buypakage.scroll_to_element("Đăng ký")
    buypakage.click_create_pakage_roaming()
    buypakage.click_register_d5()
    buypakage.click_payment_confirm()
    buypakage.click_button_continute()
    buypakage.input_otp("888888")
    buypakage.wait_for_result("Đăng ký gói cước thất bại")
    assert buypakage.is_result_displayed("Đăng ký gói cước thất bại")
    
#TC53. Huỷ gói cước data roaming linh hoạt
@pytest.mark.tc53
def test_cancel_pakage_roaming(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.click_pakage_roaming()
    buypakage.scroll_to_element("Đăng ký")
    buypakage.click_create_pakage_roaming()
    buypakage.click_button_cancel()
    buypakage.input_otp()
    buypakage.wait_for_result("Huỷ gói cước thành công")
    assert buypakage.is_result_displayed("Huỷ gói cước thành công")


