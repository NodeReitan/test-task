from pages.base_page import BasePage

class TensorPage(BasePage):
    def __init__(self, browser, url='https://tensor.ru/'):
        super().__init__(browser, url)

    def block4_title(self, xpath='//*[text()="Сила в людях" and contains(@class, "tensor_ru-Index__card-title")]'):
        return self.find(xpath)

    def block4_button(self, xpath='//*[text()="Сила в людях" and contains(@class, "tensor_ru-Index__card-title")]/parent::*//*[text()="Подробнее"]'):
        return self.find(xpath)
