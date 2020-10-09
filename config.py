import os
basedir = os.path.abspath(os.path.dirname(__name__))


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir, "ToDo.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
