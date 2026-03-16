from pages.test_scenarios_page import ScenariosPage


def test_alerts_handling(driver):

    scenarios = ScenariosPage(driver)

    scenarios.open_scenarios_page()

    scenarios.handle_alert()
    scenarios.handle_confirm()
    scenarios.handle_prompt("Automation")

    assert scenarios.verify_alert_result()


def test_frames_and_tabs(driver):

    driver.get("https://the-internet.herokuapp.com/iframe")

    driver.switch_to.frame("mce_0_ifr")

    assert "Your content goes here" in driver.page_source