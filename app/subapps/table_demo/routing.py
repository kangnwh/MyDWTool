 # -*- coding: utf-8 -*-
from flask import Blueprint
from flask import render_template
import datetime as dt
from app.subapps.stock.models import templates_funcs as tf

tableRoute = Blueprint('tableRoute', __name__,
                     template_folder='templates', static_folder='static')


@tableRoute.route('/', methods=['GET', 'POST'])
def index():
    subtitle = ["恒生电子","600570"]
    today = dt.datetime.now()
    start = today + dt.timedelta(days=-90)
    stock = tf.get_one_stock_for_table(subtitle[1],start=start.strftime('%Y-%m-%d'),end=today.strftime('%Y-%m-%d'))#ts.get_hist_data(subtitle[1],start=start.strftime('%Y-%m-%d'),end=today.strftime('%Y-%m-%d'))
    return render_template('table_demo/index.html',data=stock)
    #return render_template_string(html,table=table )


@tableRoute.route('/model', methods=['GET', 'POST'])
def model():
    return render_template('table_demo/model.html')