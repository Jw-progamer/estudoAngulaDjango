from behave import *
import time

# -- SETUP: Use cfparse as default matcher
# from behave import use_step_matcher
# step_matcher("cfparse")
from behave import use_step_matcher

# -- SELECT DEFAULT STEP MATCHER: Use "re" matcher as default.
# use_step_matcher("parse")
# use_step_matcher("cfparse")
# use_step_matcher("re")



@given(u'que estou no caminho "{url}"')
def openIndex(context, url):
   
    try:
        revista = context.browser.get(str(url))
        assert True
    except Exception as e:
        raise EnvironmentError(e)
     

@then(u'devo visualizar o texto "{revistas}"')
def seeList(context, revistas):
    print("Contexto: ",dir(context.browser))
    label = context.browser.find_element_by_xpath(f"//label[text() ='{revistas}']")
    if label is None:
        raise EnvironmentError(f"{revistas} nao encontrado.")