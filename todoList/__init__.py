import os


# dir variables
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATES_DIR = BASE_DIR + '/templates'

# constant strings
ADD_TODO_ITEM_TEXT = 'Add TODO item:'
ADD_TODO_BUTTON = 'Create'

URL_ROOT = '/'
URL_DEL_ITEM = '/del/(\d+)'

# DB info
DB_DBN = 'postgres'
DB_HOST = '127.0.0.1'
DB_SCHEMA = 'todos'
DB_USER = 'michelle'
DB_PASSWD = 'mix'


# url mappings
URLS = (
    URL_ROOT, 'Index',
    URL_DEL_ITEM, 'Delete'
)
