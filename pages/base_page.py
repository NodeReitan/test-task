from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, browser, url=''):
        self.browser = browser
        self.url = url

    def get(self, url):
        self.browser.get(url)

    def find(self, xpath):
        return self.browser.find_element(By.XPATH, xpath)

    def find_elements(self, xpath):
        return self.browser.find_elements(By.XPATH, xpath)

    def open(self):
        self.get(self.url)

    def go_to_last_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def check_url(self):
        return self.browser.current_url == self.url

    def scroll_down(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def find_elemet_by_text(self, text):
        return self.find(f'//*[text()="{text}"]')
