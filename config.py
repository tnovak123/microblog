import os



class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://microblog:blog@localhost:8889/microblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    