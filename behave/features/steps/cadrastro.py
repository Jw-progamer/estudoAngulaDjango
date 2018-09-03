import unicodedata
from behave import use_step_matcher
from behave import given
from behave import then
from behave import when
from time import sleep
from selenium.webdriver.common.keys import Keys

use_step_matcher("re")

def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError:
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode('utf-8')
    return str(text)

@when(r'digito os campos referentes a (.*)')
def inserts_value_in_field(context, type_realty):
    type_realty = strip_accents(type_realty)
    print('type_realty',type_realty)
    keys = getattr(context, type_realty).keys()
    for label in keys:
        value = getattr(context, type_realty).get(label)
        element_label = context.browser.find_element_by_xpath(
            f"//label[text()='{label}']"
        )
        if not element_label:
            raise EnvironmentError("Label not found")
        for_label = element_label.get_attribute("for")
        if not for_label:
            raise EnvironmentError("For in label not found")
        element = context.browser.find_element_by_id(for_label)
        if not element:
            raise EnvironmentError("Element not found")
        try:
            element.send_keys(value)
        except:
            element.click()
            option_selected = element.find_element_by_xpath(f".//option[text()='{value}']")
            option_selected.click()