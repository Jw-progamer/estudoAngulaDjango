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


use_step_matcher("re")
@given(u'que estou no caminho (.*)')
def openPage(context, url):
    try:
        revista = context.browser.get(str(url))
        assert True
    except Exception as e:
        raise EnvironmentError(e)


use_step_matcher("parse")
@step(u'coloco "{dados}" no campo "{campo}"')
def inputComplete(context, dados, campo):
    form = context.browser.find_element_by_xpath(f"//input[@id = '{campo}']")
    if form is not None:
        try:
            form.send_keys(dados)
        except:
            raise EnvironmentError("Problema ao inserir os campos")
    else:
        raise EnvironmentError(f"Campo '{campo}' não foi encontrado")


use_step_matcher("parse")
@step(u'coloco "{dados}" na caixa {caixa}')
def inputTextBoxComplete(context, dados, caixa):
    form = context.browser.find_element_by_xpath(
        f"//textarea[@id = '{caixa}']")
    if form is not None:
        try:
            form.click();
            form.send_keys(dados)
        except:
            raise EnvironmentError("Problema ao inserir os campos")
    else:
        raise EnvironmentError(f"Campo '{caixa}' não foi encontrado")


use_step_matcher("re")
@then(u'clico no botao (.*)')
def buttonClick(context, nome_botao):
    button = context.browser.find_element_by_xpath(
        f"//input[@id = '{nome_botao}']")
    if button is not None:
        try:
            button.click()
        except:
            raise EnvironmentError("Problema ao clicar no botão")
    else:
        raise EnvironmentError(f"Campo '{nome_botao}' não foi encontrado")


use_step_matcher("parse")
@then(u'devo visualizar o título "{revistas}"')
def seeList(context, revistas):
    label = context.browser.find_element_by_xpath(
        f"//h1[contains(text(),'{revistas}')]")
    if label is None:
        raise EnvironmentError(f"{revistas} nao encontrado.")

use_step_matcher("parse")
@then(u'devo visualizar o texto "{revistas}"')
def seeList(context, revistas):
    label = context.browser.find_element_by_xpath(
        f"//li[contains(text(),'{revistas}')]")
    if label is None:
        raise EnvironmentError(f"{revistas} nao encontrado.")