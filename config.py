import os



class Config(object):
    # Secret Key that prevents cross site code injection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Posts per page setting
    POSTS_PER_PAGE = 25
    # Debug feature
    DEBUG = True
    # Database interface settings
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://microblog:blog@localhost:8889/microblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # Mail notification settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL-PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com', 'error-messages@server.com']
