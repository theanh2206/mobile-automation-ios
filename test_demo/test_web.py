from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()

options.add_argument("--disable-features=BlockInsecurePrivateNetworkRequests")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
try:
    wait = WebDriverWait(driver, 20)
    # 1. Mở website
    driver.get("https://accounts.viblo.asia/")
    
    # 2. Truyền username
    username_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Tên người dùng hoặc email']"))
    )
    time.sleep(2)
    username_input.send_keys("0383915355")

    # 3. Truyền password
    password_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Mật khẩu']"))
    )
    time.sleep(2)
    password_input.send_keys("Vutheanh2002@")

    # 4. Click button đăng nhập
    btn_login = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='button']//span[contains(text(),'Đăng nhập')]"))
    )
    btn_login.click()
    
    # 5. Bắt key đăng nhập thành công
    
    elements = wait.until(lambda d: d.find_elements(
    By.XPATH,
    "//h1[contains(text(),'Chào mừng')]"
    ))

    if len(elements) > 0:
        print("✅ LOGIN SUCCESS")
    else:
        print("❌ LOGIN FAILED")
    time.sleep(2)

finally:
    driver.quit()