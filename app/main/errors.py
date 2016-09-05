# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'

from . import main
from flask import render_template

@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500