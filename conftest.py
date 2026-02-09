import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # driver = webdriver.Chrome(options=options)

    yield driver

    attach.add_screenshot(driver)