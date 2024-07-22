from pages.base_page import BasePage

class AboutPage(BasePage):
    def __init__(self, browser, url='https://tensor.ru/about'):
        super().__init__(browser,url)

    def block3_images(self, xpath='//*[text()="Работаем" and contains(@class, "tensor_ru-About__block-title")]/parent::*/parent::*//img'):
        return self.find_elements(xpath)