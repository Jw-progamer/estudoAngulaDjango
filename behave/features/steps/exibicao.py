from behave import *

@given("que estou no caminho file:///home/josias/Documentos/revistas/web-app/index.html")
def openIndex(context):
    context.browser.get('file:///home/josias/Documentos/revistas/web-app/index.html')

@then("devo visualizar a lista \"lista_de _revistas\"")
def step_impl(context):
    assert context.failed is False