from pages.index import IndexPage
from pages.contacts import ContactPage
from pages.about import AboutPage
from pages.tensor import TensorPage
from pages.elements import Elements


def test_first_script(browser):
    index_page = IndexPage(browser)
    index_page.open()
    index_page.contactButtonClick()

    contacts_page = ContactPage(browser)
    contacts_page.bunner().click()
    contacts_page.go_to_last_tab()

    tensor_page = TensorPage(browser)
    assert tensor_page.block4_title()

    tensor_page.scroll_down(tensor_page.block4_button())
    tensor_page.block4_button().click()

    about_page = AboutPage(browser)
    assert about_page.check_url()

    block3_images = Elements(about_page.block3_images())
    assert block3_images.compare_size
