 # -*- coding: utf-8 -*-
from flask import Blueprint,request
from flask import render_template
import datetime as dt
from app.subapps.stock.models import templates_funcs as tf
from flask_login import login_required

tableRoute = Blueprint('tableRoute', __name__,
                     template_folder='templates', static_folder='static')


@tableRoute.route('/', methods=['GET', 'POST'])
@login_required
def index():
    stock_code = None
    if request.method == 'GET':
        stock_name = request.args.get('stock_name')
        date = request.args.get('date')
        if not (stock_name and date):
            return render_template('table_demo/index_err.html',message="请指定股票名称和交易日期")

        stock_code = tf.get_code_from_name(stock_name)

    stock_code = stock_code if stock_code else "600570"
    today = dt.datetime.now()
    start = today + dt.timedelta(days=-90)
    stock_pd = tf.get_deal_detail(stock_code,date)#ts.get_hist_data(subtitle[1],start=start.strftime('%Y-%m-%d'),end=today.strftime('%Y-%m-%d'))
    if stock_pd.index.__len__() == 3:
        return  render_template('table_demo/index_err.html',message="指定股票名称在该日期内没有数据")

    return render_template('table_demo/index_simple.html',data=stock_pd)
    #return render_template_string(html,table=table )


@tableRoute.route('/model', methods=['GET', 'POST'])
@login_required
def model():
    return render_template('table_demo/model.html')