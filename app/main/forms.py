# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(Form):
    #DataRequired用来确保提交的字段不为空
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')