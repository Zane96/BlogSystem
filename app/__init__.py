# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'

from flask import Flask
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

#app实例的生成函数
def creat_app(config_name):
    app = Flask(__name__)
    #获得不同的config实例(环境)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    #注册main模块的蓝本到app实例中
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


