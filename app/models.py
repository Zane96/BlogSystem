# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'
from . import db

#数据库orm模型

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    #建立一对多关系,在users表总添加一个role属性,如果是1对1关系,那么需要将userlist设为False
    users = db.relationship('User', backref = 'role', lazy = 'dynamic')

    #相当于java类里面的toStrig()
    def __repr__(self):
        return '(Role %s)' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)
    #添加一个外键和Rola关系在一起
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '(User %s)' % self.username
