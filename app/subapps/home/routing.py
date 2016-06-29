 # -*- coding: utf-8 -*-
from flask import Blueprint
from flask import render_template

homeRoute = Blueprint('homeRoute', __name__,
                     template_folder='templates', static_folder='static')


@homeRoute.route('/', methods=['GET', 'POST'])
def index():

    return render_template('home/index.html')