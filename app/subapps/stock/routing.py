 # -*- coding: utf-8 -*-
from flask import Blueprint,url_for,request
from flask import render_template,render_template_string
from EChartT import get_line_script,get_echarts_package,\
    generate_pie_data,get_pie_script

import datetime as dt
import tushare as ts#TODO the source should be redesigned for esay-change

stockRoute = Blueprint('stockRoute', __name__,
                     template_folder='templates', static_folder='static')


@stockRoute.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        code = request.args.get('code')
    else:
        code = request.form["code"]
    title = "个股 - 大盘 对比图"
    basic = ts.get_stock_basics()

    stock_basic = basic.ix[code]
    subtitle = [stock_basic[0],code]

    today = dt.datetime.now()
    start = today + dt.timedelta(days=-90)
    stock_90 = ts.get_hist_data(code,start=start.strftime('%Y-%m-%d'),end=today.strftime('%Y-%m-%d'))
    stock_data = stock_90.head(2).copy()
    stock_90 = stock_90.sort_index(ascending=True)

    sotck_sh_90 = ts.get_hist_data('sh',start=start.strftime('%Y-%m-%d'),end=today.strftime('%Y-%m-%d'))
    sotck_sh_90 = sotck_sh_90.sort_index(ascending=True)

    x_data = stock_90.index.values.tolist()
    y_data0 = stock_90.p_change.values.tolist()
    y_data1 = sotck_sh_90.p_change.values.tolist()


    script1 = get_line_script(template_name='normal_2_lines',
                             chart_id = "chart1",
                             title=title,x_data=x_data,
                             subtitle=subtitle[0] + " - 收盘价",
                             y_name0=subtitle[0],y_data0=y_data0,
                            y_name1="大盘指数",y_data1=y_data1,
                             )

    #新浪股吧词频
    tf = ts.get_sina_dd(code, today.strftime('%Y-%m-%d'))
    gf = tf.groupby('type')
    s = gf.volume.sum()
    l = {x:y for x,y in s.items()}
    data = generate_pie_data(l)
    script2 = get_pie_script("normal",
                             chart_id="chart2",
                             title="大单交易类别比例",
                             subtitle=subtitle[0]+subtitle[1],
                             data_category = list(l.keys()),
                             data=data)
    #新闻词频

    script3 = get_line_script(template_name='上下X轴图',
                              chart_id = "stock3",
                              title='上下X轴图',
                              subtitle='Demo')
    script4 = get_line_script(template_name='动态时间轴',
                              chart_id = "stock4",
                              title='动态时间轴')
    js_package = get_echarts_package()
    return render_template('stock/index.html',
                               stock_baisc = stock_basic,
                               stock_data = stock_data,
                                script = script1+script2)