# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'
#通过Blueprint进行项目模块分化,作用是给路由提供一个像app一样的全局实例

from flask import Blueprint

#main模块
main = Blueprint('main', __name__)

#末项引入视图函数,防止循环引入
from . import views, errors