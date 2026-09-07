import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def setup_browser():
    options = Options()

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.qa.guru/wd/hub",
        options=options
    )

    # driver = webdriver.Chrome(options=options)

    yield driver
