import os
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# CSRF PROTECT
CSRF_ENABBED = True
SECRET_KEY = 'you-will-never-guess'

# OPENID
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]
