# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'
#配置文件

import os

basedir = os.path.abspath(os.path.dirname(__file__))

#app的config
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #在app生成的工厂函数中调用,延迟app实例的生成,从而搭配上不同的环境,方便测试和程序运行在不同的环境里面
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    @staticmethod
    def init_app(app):
        app.config['SECRET_KEY'] = Config.SECRET_KEY
        app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = Config.SQLALCHEMY_COMMIT_ON_TEARDOWN
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
        app.config['SQLALCHEMY_DATABASE_URI'] = DevelopmentConfig.SQLALCHEMY_DATABASE_URI

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    @staticmethod
    def init_app(app):
        app.config['SECRET_KEY'] = Config.SECRET_KEY
        app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = Config.SQLALCHEMY_COMMIT_ON_TEARDOWN
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
        app.config['SQLALCHEMY_DATABASE_URI'] = TestingConfig.SQLALCHEMY_DATABASE_URI

class ProductionConfig(Config):
    PRODYCTION = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    @staticmethod
    def init_app(app):
        app.config['SECRET_KEY'] = Config.SECRET_KEY
        app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = Config.SQLALCHEMY_COMMIT_ON_TEARDOWN
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
        app.config['SQLALCHEMY_DATABASE_URI'] = ProductionConfig.SQLALCHEMY_DATABASE_URI

#提供一个列表出来
config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,
    'default' : DevelopmentConfig
}