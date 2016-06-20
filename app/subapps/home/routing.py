 # -*- coding: utf-8 -*-
from flask import Blueprint,url_for
from flask import render_template

from MyAPI.EChartsGen import MyEChartsAPI
from MyAPI.EChartsGen.options.Series.line.data import Data as line_data

from EChartT import get_line_script,get_echarts_package

homeRoute = Blueprint('homeRoute', __name__,
                     template_folder='templates', static_folder='static')


@homeRoute.route('/', methods=['GET', 'POST'])
def index():

    return render_template('home/index.html')