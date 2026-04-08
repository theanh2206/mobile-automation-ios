import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.DealsPage_page import DealsPage

#TC71. Tìm kiếm gói cước có trong DB
@pytest.mark.tc71
def test_search_package_D5(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.search_package("D5")
    dealspage.wait_for_result("D5")
    assert dealspage.is_result_displayed("D5")  
#TC72. Tìm kiếm gói cước không có trong DB
@pytest.mark.tc72
def test_search_package_D5(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.search_package("Thế Anh")
    dealspage.wait_for_result("Lịch sử")
    assert dealspage.is_result_displayed("Lịch sử")  
#TC73. Kiểm tra mẹo tích điểm/chi tiết mẹo tích điểm
@pytest.mark.tc73
def test_save_point(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.click_save_point()
    dealspage.click_list_save_point(1)
    dealspage.wait_for_result("Nạp tiền điện thoại tích điểm")
    dealspage.press_back()
    dealspage.click_list_save_point(2)
    dealspage.wait_for_result("Đăng ký gói cước tích điểm")
    dealspage.press_back()
    dealspage.click_list_save_point(3)
    dealspage.wait_for_result("Tích điểm khi mua sắm online")
    dealspage.press_back()
    dealspage.click_list_save_point(4)
    dealspage.wait_for_result("Chương trình khuyến mãi")
    dealspage.press_back()
    assert dealspage.is_result_displayed("Tích điểm cực dễ cùng MyPoint")  
#TC74. Kiểm tra lịch sử điểm
@pytest.mark.tc74
def test_point_history(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.click_point_history()
    dealspage.click_list_point_history(1)
    dealspage.click_close()
    dealspage.click_by_text("Tiêu điểm")
    dealspage.click_list_point_history(1)
    dealspage.click_close()
    assert dealspage.is_result_displayed("Lịch sử điểm")  
    
#TC75. Kiểm tra lịch sử đơn hàng
@pytest.mark.tc75
def test_point_history(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.click_cart_history()
    dealspage.click_by_text("Chờ xử lý")
    dealspage.click_by_text("Tạm duyệt")
    dealspage.click_by_text("Đã hoàn")
    dealspage.click_by_text("Đã hủy")
    assert dealspage.is_result_displayed("Không tìm thấy dữ liệu")  

