from pages.index import IndexPage
from pages.contacts import ContactPage
from pages.elements import Elements
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_second_script(browser):
    index_page = IndexPage(browser)
    index_page.open()
    index_page.contactButtonClick()

    contacts_page = ContactPage(browser)

    region_chooser = contacts_page.region_chooser_text()
    region_chooser_text = region_chooser.text
    assert region_chooser_text == 'Ярославская обл.'

    contact_list_items =contacts_page.contact_list_items()
    contact_list_text = Elements(contact_list_items).get_text_elements
    assert len(contact_list_text) > 0

    region_chooser.click()
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//body'), '41 Камчатский край'))
    contacts_page.find_elemet_by_text('41 Камчатский край').click()

    WebDriverWait(browser, 10).until(EC.title_is('СБИС Контакты — Камчатский край'))
    new_region_chooser = contacts_page.region_chooser_text()
    new_contact_list_items = contacts_page.contact_list_items()

    assert new_region_chooser.text == 'Камчатский край'
    assert Elements(new_contact_list_items).get_text_elements != contact_list_text
    assert browser.current_url == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
    assert browser.title == 'СБИС Контакты — Камчатский край'
