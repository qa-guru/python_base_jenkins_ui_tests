import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": '128.0',
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # driver = webdriver.Chrome(options=options)

    yield driver

    attach.add_screenshot(driver)
    attach.add_page_source(driver)
    attach.add_console_logs(driver)
    attach.add_video(driver)

    driver.quit()
