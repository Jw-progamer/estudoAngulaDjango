import os
import logging
import time
from factories import factory
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIREFOX_DRIVER_PATH = os.path.join(BASE_DIR, 'drives')

os.environ['PATH'] = "{}:{}".format(os.environ['PATH'], FIREFOX_DRIVER_PATH)
print(os.environ['PATH'])


def get_firefox(context):
    print(FIREFOX_DRIVER_PATH)
    logging.info("iniciando o firefox")
    firefox_option = FirefoxOptions()
    firefox_option.add_argument('--incognito')
    return webdriver.Firefox(
        firefox_options=firefox_option
    )


def instance_revista(context, scenario):
    if "cadrasta uma revista" in scenario:
        context.revista = factory.Revista().data


def before_all(context):
    context.browser = get_firefox(context)
    context.browser.implicitly_wait(5)


def before_scenario(context, scenario):
    instance_revista(context, scenario)


def before_step(context, step):
    time.sleep(1)


def after_all(context):
    context.browser.close()
