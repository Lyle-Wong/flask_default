# -*- coding=utf-8 -*-

import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    MONGODB_HOST = '127.0.0.1'
    MONGODB_DB = 'qray_report'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'lwang'
    MONGODB_PASSWORD = 'password'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'develop': DevelopmentConfig,
    'default':ProductionConfig
}
