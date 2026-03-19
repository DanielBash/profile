"""- Default settings template"""

# -- importing modules
from pathlib import Path

# -- flask settings
PORT = 8080  # running port
HOST = '0.0.0.0'  # on what host to run app
SECRET_KEY = 'unsecure-secret-key'  # app secret key for cryptography. sessions, for example

# -- app settings
DEBUG = False  # is app run in debug mode?
PRINT_CONSTANTS = True  # do we need to print settings when initializing?

# -- sqlalchemy database settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # database connection uri
TEMPLATE_PATH = Path('templates')  # templates folder path

# -- blueprints settings
BASE_BLUEPRINTS = ['main', 'index']  # blueprints that can be handled without url prefix

# -- permissions settings
PERMISSION_GROUPS = {
    'admin': {
        'VIEW_ADMIN_PANEL': True,
        'SEND_MAIL_MESSAGES': True,
        'PUBLUSH_POSTS': True,
    },
    'user': {
        'VIEW_ADMIN_PANEL': False,
        'SEND_MAIL_MESSAGES': True,
        'PUBLUSH_POSTS': True,
    }
}

# -- admin credentials
ADMIN_PASSWORD = 'password'
ADMIN_USERNAME = 'daniel'
ADMIN_PERMISSION_GROUP = 'admin'
ADMIN_EMAIL = 'hidden@example.com'
ADMIN_BIO = 'I am the admin and the creator of this website.'
ADMIN_STATUS = 'Working on something great...'

# -- users default settings
DEFAULT_PERMISSION_GROUP = 'user'
DEFAULT_STATUS = 'Friend'
DEFAULT_BIO = f'I am a friend of the {ADMIN_USERNAME}.'

# -- front end estetics
# - pagination
MESSAGES_PAGINATION = 20
POSTS_PAGINATION = 10
