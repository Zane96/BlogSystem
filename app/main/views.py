# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'

#main模块的视图函数
from flask import render_template, session, redirect, url_for, flash, request
from datetime import datetime
from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods = ['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['know'] = False
        else:
            session['know'] = True

        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            name = '姓名不对'
            string = name.decode('utf-8')
            flash(string)
        session['name'] = form.name.data
        #把每次post请求重定向成get请求,避免刷新页面的时候要求重新提交表单
        return redirect(url_for('main.index'))
    user_agent = request.headers.get('User-Agent')
    form.name.data = ''
    return render_template('index.html', current_time = datetime.utcnow(), name = session.get('name'),
                           form = form, know = session.get('know', False)) + " " + user_agent

@main.route('/users/<name>')
def user(name):
    return render_template('user.html', name = name)