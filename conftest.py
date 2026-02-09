import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def setup_browser():
    options = Options()
    driver = webdriver.Chrome(options=options)

    yield driver
