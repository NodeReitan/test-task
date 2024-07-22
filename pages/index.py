from pages.base_page import BasePage

class IndexPage(BasePage):
    def __init__(self, browser, url='https://sbis.ru/'):
        super().__init__(browser, url)
        self.url = url

    def contactButtonClick(self):
        self.find('//div[contains(@class, "sbisru-Header")]//*[text()="Контакты"]').click()
