import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.BuyPakagePage_page import BuyPakagePage

@pytest.mark.tc40
def test_search_package_D5(driver):
    homepage = BuyPakagePage(driver)
    homepage.search_package("D5")
    homepage.wait_for_result("D5")
    assert homepage.is_result_displayed("D5")