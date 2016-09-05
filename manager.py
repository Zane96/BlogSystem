# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'
import os
from app import creat_app, db
from flask_script import Manager, Shell
from app.models import User, Role

app = creat_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role)


manager.add_command('shell', Shell(make_shell_context))


if __name__ == '__main__':
    manager.run()