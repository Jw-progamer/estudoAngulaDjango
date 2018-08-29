from behave import *
import time

@given("que estou no caminho file:///home/josias/Documentos/revistas/web-app/index.html")
def openIndex(context):
    try:
        revista = context.browser.get('file:///home/josias/Documentos/revistas/web-app/index.html')
        assert True
    except Exception as e:
        raise EnvironmentError(e)
     

@then("devo visualizar o texto \"revistas em estoque\"")
def seeList(context):
    assert context.failed is False