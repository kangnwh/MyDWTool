# -*- coding: utf-8 -*-
from flask import Blueprint, request, url_for
from flask import render_template
from BI.EChartT import get_line_script, get_pie_script
from app.subapps.stock.models.templates_funcs import get_index_data
from .forms.code_select import StockCode

stockRoute = Blueprint('stockRoute', __name__,
                       template_folder='templates', static_folder='static')


@stockRoute.route('/', methods=['GET', 'POST'])
def index():
    code_form = StockCode()
    if request.method == 'GET':
        return render_template('stock/index_err.html', form=code_form)

    else:
        if code_form.validate_on_submit():
            code = code_form.code.data
        else:
            return render_template('stock/index_err.html', form=code_form)

    code = code if code else "000001"
    title = "个股 - 大盘 对比图"
    stock_basic, subtitle, stock_data, x_data, y_data0, y_data1, category, pie_data = get_index_data(code)

    word_cloud = url_for("stockRoute.static", filename="wordcloud/{code}.png".format(code=code))

    script1 = get_line_script(template_name='normal_2_lines',
                              chart_id="chart1",
                              title=title, x_data=x_data,
                              subtitle=subtitle[0] + " - 收盘价",
                              y_name0=subtitle[0], y_data0=y_data0,
                              y_name1="大盘指数", y_data1=y_data1,
                              )

    script2 = get_pie_script("normal",
                             chart_id="chart2",
                             title="大单交易类别比例",
                             subtitle=subtitle[0] + subtitle[1],
                             data_category=category,
                             data=pie_data)
    # 新闻词频

    script3 = get_line_script(template_name='上下X轴图',
                              chart_id="stock3",
                              title='上下X轴图',
                              subtitle='Demo')
    script4 = get_line_script(template_name='动态时间轴',
                              chart_id="stock4",
                              title='动态时间轴')

    return render_template('stock/index.html', form=code_form,
                           stock_baisc=stock_basic,
                           stock_data=stock_data,
                           script=script1 + script2,
                           wordcloud=word_cloud)
