import pytest
from pages.PersonalProfilePage_page import PersonalProfile

#TC106. Click các icon dịch vụ của tôi
@pytest.mark.tc106
def test_click_my_services(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(1)
    personalprofile.wait_for_result("Thông tin thuê bao")
    personalprofile.press_back()
    personalprofile.click_my_services(2)
    personalprofile.wait_for_result("Lịch sử thanh toán")
    personalprofile.press_back()
    personalprofile.click_my_services(3)
    personalprofile.wait_for_result("Cập nhật thông tin")
    personalprofile.press_back()
    personalprofile.click_my_services(4)
    personalprofile.wait_for_result("hạn mức cước")
    personalprofile.press_back()
    personalprofile.click_my_services(5)
    personalprofile.wait_for_result("Multi-sim")
    personalprofile.press_back()
    personalprofile.click_my_services(6)
    personalprofile.press_back()
    personalprofile.click_my_services(7)
    personalprofile.wait_for_result("Điều khoản")
    personalprofile.press_back()
    personalprofile.click_my_services(8)
    personalprofile.wait_for_result("Cài đặt")
    personalprofile.press_back()
    personalprofile.click_my_services(9)
    personalprofile.wait_for_result("Khuyến mại")
    personalprofile.press_back()
    personalprofile.click_my_services(10)
    personalprofile.press_back()
    assert personalprofile.is_result_displayed("Hồ sơ cá nhân")
#TC107. Click button refesh trong thông tin thuê bao
@pytest.mark.tc107
def test_click_button_refesh(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(1)
    personalprofile.click_button_refesh()
    assert personalprofile.is_result_displayed("Thông tin thuê bao")
#TC108. Click button Xem chi tiết
@pytest.mark.tc108
def test_click_button_detail(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(1)
    personalprofile.click_button_detail()
    assert personalprofile.is_result_displayed("Xác thực thông tin")

#TC109. Liên kết với tài khoản google
@pytest.mark.tc109
def test_link_google(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(1)
    personalprofile.scroll_to_element("Liên kết với tài khoản Google")
    personalprofile.click_by_text("Liên kết với tài khoản Google")
    personalprofile.wait_for_result("Xác thực thông tin")
    assert personalprofile.is_result_displayed("Xác thực thông tin")
#TC110. Liên kết với tài khoản google
@pytest.mark.tc110
def test_click_button_delete_account(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(1)
    personalprofile.scroll_to_element("Xóa tài khoản")
    personalprofile.click_button_delete()
    personalprofile.wait_for_result("Xác nhận")
    assert personalprofile.is_result_displayed("Xác nhận")
#Lịch sử thanh toán
#TC111. Click xem chi tiết 1 giao dịch 
@pytest.mark.tc111
def test_click_button_delete_account(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(2)
    personalprofile.wait_for_result("Lịch sử")
    assert personalprofile.is_result_displayed("Lịch sử")

#TC112. Kiểm tra tab hoá đơn điện tử trong lịch sử thanh toán 
@pytest.mark.tc112
def test_check_tab_invoice(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(2)
    personalprofile.click_by_text("Hóa đơn điện tử")
    personalprofile.click_select_date()
    personalprofile.wait_for_result("THÁNG")
    personalprofile.select_date(3, 2026)
    personalprofile.click_button_ok()
    personalprofile.click_by_text("Hoá đơn")
    personalprofile.click_by_text("Phiếu thu")
    personalprofile.click_by_text("Xem hoá đơn")
    personalprofile.wait_for_result("Lịch sử")
    assert personalprofile.is_result_displayed("Lịch sử")
#TC113. Kiểm tra lọc tháng trong lịch sử thanh toán 
@pytest.mark.tc113
def test_check_tab_invoice1(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(2)
    personalprofile.click_icon_bin()
    personalprofile.select_month(3)
    personalprofile.click_button_back()
    personalprofile.click_button_fillter()
    personalprofile.wait_for_result("Lịch sử")
    assert personalprofile.is_result_displayed("Lịch sử")

#TC114. Kiểm tra cập nhật thông tin 
@pytest.mark.tc114
def test_update_infor(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(3)
    personalprofile.click_button_update()
    personalprofile.input_otp("888888")
    personalprofile.wait_for_result("Chữ ký")
    assert personalprofile.is_result_displayed("Chữ ký")

#TC115. Kiểm tra hạn mức cước
@pytest.mark.tc115
def test_limit_cuoc(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(4)
    personalprofile.wait_for_result("Các hạn mức cước")
    assert personalprofile.is_result_displayed("Các hạn mức cước")

#TC116. Kiểm tra Multi-sim
@pytest.mark.tc116
def test_ckeck_multi_sim(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(5)
    personalprofile.wait_for_result("Số thuê bao")
    assert personalprofile.is_result_displayed("Số thuê bao")
#TC117. Kiểm tra đổi e-sim
@pytest.mark.tc117
def test_change_esim(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(6)
    personalprofile.wait_for_result("Thiết bị của bạn không hỗ trợ eSIM")
    assert personalprofile.is_result_displayed("Thiết bị của bạn không hỗ trợ eSIM")
#TC118. Kiểm tra auto-pay
@pytest.mark.tc118
def test_check_autopay(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(7)
    personalprofile.add_phone()
    personalprofile.click_buttom_confirm()
    personalprofile.click_buttom_confirm()
    personalprofile.wait_for_result("Thêm thẻ thanh toán")
    assert personalprofile.is_result_displayed("Thêm thẻ thanh toán")

#TC119. Kiểm tra cài đặt
@pytest.mark.tc119
def test_check_setting(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(8)
    
    personalprofile.wait_for_result("AutoPay")
    assert personalprofile.is_result_displayed("AutoPay")