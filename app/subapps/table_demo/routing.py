 # -*- coding: utf-8 -*-
from flask import Blueprint,request
from flask import render_template
import datetime as dt
from app.subapps.stock.models import templates_funcs as tf
import tushare as ts

tableRoute = Blueprint('tableRoute', __name__,
                     template_folder='templates', static_folder='static')


@tableRoute.route('/', methods=['GET', 'POST'])
def index():
    stock_code = None
    if request.method == 'GET':
        stock_name = request.args.get('stock_name')
        date = request.args.get('date')
        if not (stock_name and date):
            return render_template('table_demo/index_err.html')

        stock_code = tf.get_code_from_name(stock_name)
        date = request.args.get('date')
        date = date if date else ""
    stock_code = stock_code if stock_code else "600570"
    today = dt.datetime.now()
    start = today + dt.timedelta(days=-90)
    stock_pd = tf.get_deal_detail(stock_code,date)#ts.get_hist_data(subtitle[1],start=start.strftime('%Y-%m-%d'),end=today.strftime('%Y-%m-%d'))


    return render_template('table_demo/index.html',data=stock_pd)
    #return render_template_string(html,table=table )


@tableRoute.route('/model', methods=['GET', 'POST'])
def model():
    return render_template('table_demo/model.html')