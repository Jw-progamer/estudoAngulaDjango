import os

APP_PROTOCOL = 'https'
APP_HOST = 'http://127.0.0.1:8000/'
APP_BASE_URL = f'{APP_PROTOCOL}://{APP_HOST}'

#C:\Users\NicoleDev\Desktop\workspace\projeto01\source\blog\behave\drivers

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_DIR, 'error.log')

LANGUAGE = 'pt_BR'

BROWSER_NAME = os.environ.get('BROWSER_NAME', 'firefox').upper()

# set geckodriver drives folders in path
geckodriver_path = os.path.join(BASE_DIR, 'drivers')
if os.environ['PATH'].find(geckodriver_path) == -1:
   os.environ['PATH'] = ':'.join((os.environ['PATH'], geckodriver_path))