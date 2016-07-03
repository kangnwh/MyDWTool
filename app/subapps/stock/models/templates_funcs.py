import datetime as dt

import pandas as pd
import tushare as ts

from BI.Components.EChartT import generate_pie_data
from app.db_info import Session,engine


def run_sql_via_pandas(sql):
    df = pd.read_sql(sql,engine)
    return df

def run_sql_via_sqlalchemy(sql):
    session = Session()
    r = session.execute(sql)
    result = r.fetchall()
    session.close()
    return result

def get_max_date(code):
    sql = """
    SELECT max([date]) as date
  FROM [stock].[stock_hist] where code='{code}'
    """.format(code=code)
    df = run_sql_via_sqlalchemy(sql)
    return df[0][0]


def get_code_from_name(name):
    sql="""
    SELECT code as code
      FROM [stock].[comp_basic] where name=N'{name}'
    """.format(name=name)
    df = run_sql_via_sqlalchemy(sql)
    print(df)
    return df[0][0]


def get_basic(code):
    sql = """
    SELECT [code]
      ,[name]
      ,[industry]
      ,[area]
      ,[pe]
      ,[outstanding]
      ,[totals]
      ,[totalAssets]
      ,[liquidAssets]
      ,[fixedAssets]
      ,[reserved]
      ,[reservedPerShare]
      ,[esp]
      ,[bvps]
      ,[pb]
      ,[timeToMarket]
  FROM [stock].[comp_basic] where code='{code}'
    """.format(code=code)
    basic = run_sql_via_pandas(sql)
    return basic

def get_one_stock_all(code,start,end):
    sql = """
    SELECT [code]
      ,[open]
      ,[high]
      ,[close]
      ,[low]
      ,[volume]
      ,[price_change]
      ,[p_change]
      ,[ma5]
      ,[ma10]
      ,[ma20]
      ,[v_ma5]
      ,[v_ma10]
      ,[v_ma20]
      ,[turnover]
      ,[date]
  FROM [stock].[stock_hist] where code='{code}' and date between '{start}' and '{end}' order by date
    """.format(code=code,start=start,end=end)
    df = run_sql_via_pandas(sql)
    return df

def get_deal_detail(code,date):
    df = ts.get_tick_data(code,date=date)
    df.columns = ["交易时间","成交价格","价格变动","成交手","成交金额","买卖类型"]
    return df


def get_index_data(code):

    stock_basic = get_basic(code).ix[0]

    subtitle = [stock_basic[1],code]

    max_date = get_max_date(code)#dt.datetime.now()
    max_date = dt.datetime.strptime(max_date,"%Y-%m-%d")
    start = max_date + dt.timedelta(days=-90)

    stock_90 = get_one_stock_all(code,start=start.strftime('%Y-%m-%d'),end=max_date.strftime('%Y-%m-%d'))
    stock_data = stock_90.tail(2).sort_values(by="date",ascending=False)

    sotck_sh_90 = get_one_stock_all('sh',start=start.strftime('%Y-%m-%d'),end=max_date.strftime('%Y-%m-%d'))#ts.get_hist_data('sh',start=start.strftime('%Y-%m-%d'),end=max_date.strftime('%Y-%m-%d'))

    x_data = stock_90.date.values.tolist()
    y_data0 = stock_90.p_change.values.tolist()
    y_data1 = sotck_sh_90.p_change.values.tolist()

    #大手买卖
    tf = ts.get_sina_dd(code,  stock_data.iloc[0]['date'])

    if  isinstance(tf,pd.DataFrame):
        gf = tf.groupby('type')
        s = gf.volume.sum()
        pie_l = {x:y for x,y in s.items()}
        pie_data = generate_pie_data(pie_l)
        category = list(pie_l.keys())
    else:
        category = ["没有数据",]
        pie_data = "[{name:'没有数据',value:1}]"

    return stock_basic,subtitle,stock_data,x_data,y_data0,y_data1,category,pie_data#,cloud_text
