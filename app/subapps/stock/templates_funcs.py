import tushare as ts
import datetime as dt
from EChartT import  generate_pie_data

def get_index_data(code):

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

    #新浪股吧词频
    tf = ts.get_sina_dd(code, today.strftime('%Y-%m-%d'))
    gf = tf.groupby('type')
    s = gf.volume.sum()
    pie_l = {x:y for x,y in s.items()}
    pie_data = generate_pie_data(pie_l)

    return stock_basic,subtitle,stock_data,x_data,y_data0,y_data1,pie_l,pie_data