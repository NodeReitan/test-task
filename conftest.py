from selenium import webdriver
import pytest

@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()
