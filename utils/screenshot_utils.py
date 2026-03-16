import os

def take_screenshot(driver, name):

    os.makedirs("reports/screenshots", exist_ok=True)

    driver.save_screenshot(
        f"reports/screenshots/{name}.png"
    )