import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = "teamspirit3209@gmail.com"
    MAIL_PASSWORD = "2787831ra"
    ADMINS = ['studyformcbp1906@gmail.com']
    MS_TRANSLATOR_KEY = "31eb21cf642f4ac994a09665d748972f"
    POSTS_PER_PAGE=25
    LANGUAGES = ['en','es','ru']