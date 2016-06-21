 # -*- coding: utf-8 -*-
from flask import Blueprint,url_for
from flask import render_template,render_template_string

import datetime as dt
import tushare as ts

tableRoute = Blueprint('tableRoute', __name__,
                     template_folder='templates', static_folder='static')


@tableRoute.route('/', methods=['GET', 'POST'])
def index():
    subtitle = ["恒生电子","600570"]
    today = dt.datetime.now()
    start = today + dt.timedelta(days=-90)
    stock = ts.get_hist_data(subtitle[1],start=start.strftime('%Y-%m-%d'),end=today.strftime('%Y-%m-%d'))
    stock.insert(0,stock.index.name,stock.index)
    return render_template('table_demo/index.html',data=stock)
    #return render_template_string(html,table=table )