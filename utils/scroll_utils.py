from appium.webdriver.common.appiumby import AppiumBy
import time


def scroll_and_find_by_text(driver, text, max_scroll=6):
    for i in range(max_scroll):

        elements = driver.find_elements(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().textContains("{text}")'
        )

        if elements:
            return elements[0]

        # lấy size màn hình
        size = driver.get_window_size()

        driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": size["width"] * 0.1,
                "top": size["height"] * 0.3,
                "width": size["width"] * 0.8,
                "height": size["height"] * 0.6,
                "direction": "down",
                "percent": 0.7
            }
        )

        time.sleep(1)  # chờ UI load

    # ❗ nếu không tìm thấy
    raise Exception(f"❌ Không tìm thấy element chứa text: {text}")