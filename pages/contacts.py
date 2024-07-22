from pages.base_page import BasePage

class ContactPage(BasePage):
    def __init__(self, browser, url='https://sbis.ru/contacts'):
        super().__init__(browser, url)

    def bunner(self, xpath='//*[contains(@class, "sbisru-Contacts__logo-tensor") and not(contains(@class, "sbisru-link"))]'):
        return self.find(xpath)

    def region_chooser_text(self, xpath='//*[contains(@class, "sbis_ru-Region-Chooser") and not(contains(@class, "sbisru-Footer__region"))]/span'):
        return self.find(xpath)

    def contact_list_items(self, xpath='//*[contains(@class, "sbisru-Contacts-List__item")]'):
        return self.find_elements(xpath)

