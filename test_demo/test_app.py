import time
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ========= CONFIG =========
DEVICE_UDID = "auto"
BUNDLE_ID = "vms.com.MyMobifone"   # ⚠️ sửa theo inspector
PHONE_NUMBER = "0931791607"
OTP_CODE = "888888"
APPIUM_URL = "http://127.0.0.1:4723"

TEAM_ID = "2LSM987Q67"  # ✅ đã set theo bạn

# ========= DRIVER SETUP =========
options = XCUITestOptions()

options.platform_name = "iOS"
options.device_name = "iPhone 13"
options.udid = DEVICE_UDID
options.automation_name = "XCUITest"

# 👉 app
options.bundle_id = BUNDLE_ID

# 👉 signing (đúng config của bạn)
options.xcode_org_id = TEAM_ID
options.xcode_signing_id = "Apple Development"
options.updated_wda_bundle_id = "com.truong.wda"

# 👉 WDA reuse
options.use_prebuilt_wda = True
options.use_new_wda = False

# 👉 giữ trạng thái
options.no_reset = True
options.new_command_timeout = 300

driver = webdriver.Remote(APPIUM_URL, options=options)

print("✅ CONNECTED SUCCESSFULLY")

wait = WebDriverWait(driver, 20)

# ========= TEST STEPS =========
try:
    # 1️⃣ Click Đăng nhập
    wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Đăng nhập"])[2]')
        )
    ).click()

    # 2️⃣ Nhập số điện thoại
    phone_input = wait.until(
    EC.presence_of_element_located(
        (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField')
    )
)

    phone_input.click()

    # Lấy text hiện tại
    current_value = phone_input.get_attribute("value")

    # Xóa từng ký tự
    for _ in range(len(current_value)):
        phone_input.send_keys("\b")

    # Nhập số mới
    phone_input.send_keys("0931791607")

    # 1️⃣ Click Đăng nhập
    wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Đăng nhập"])[2]')
        )
    ).click()

    # 4️⃣ Nhập OTP
    otp_inputs = wait.until(
        EC.presence_of_all_elements_located(
            (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField')
        )
    )

    for i, digit in enumerate(OTP_CODE):
        otp_inputs[i].send_keys(digit)

    print("✅ LOGIN OTP TEST PASSED")

except Exception as e:
    print("❌ LOGIN OTP TEST FAILED")
    print(e)
    raise

finally:
    time.sleep(2)
    driver.quit()