 # -*- coding: utf-8 -*-
 import datetime as dt

 import tushare as ts
 from flask import Blueprint
 from flask import render_template

 from BI.EChartT import get_line_script

 chartRoute = Blueprint('chartRoute', __name__,
                     template_folder='templates', static_folder='static')


@chartRoute.route('/', methods=['GET', 'POST'])
def index():

    title = "普通折线图"
    subtitle = ["恒生电子","600570"]
    today = dt.datetime.now()
    start = today + dt.timedelta(days=-90)
    stock_data = ts.get_hist_data(subtitle[1], start=start.strftime('%Y-%m-%d'), end=today.strftime('%Y-%m-%d'))
    stock_data = stock_data.sort()
    x_data = stock_data.index.values.tolist()
    script1 = get_line_script(template_name='normal',
                              chart_id = "stock1",
                              title=title,
                              subtitle=subtitle[0] + " - 收盘价",
                              y_data= stock_data.close.values.tolist(),
                              x_data=x_data)
    script2 = get_line_script(template_name='折线面积图',
                              chart_id = "stock2",
                              title="折线面积图",
                              subtitle=subtitle[0] + " - 换手率",
                              x_data = x_data,
                              y_data =  stock_data.turnover.values.tolist(),
                              series_name = "XX数据"
                              )

    script3 = get_line_script(template_name='上下X轴图',
                              chart_id = "stock3",
                              title='上下X轴图',
                              subtitle='Demo')
    script4 = get_line_script(template_name='动态时间轴',
                              chart_id = "stock4",
                              title='动态时间轴')

    return render_template('chart_demo/index.html',
                           script=script1+script2+script3+script4
                           )