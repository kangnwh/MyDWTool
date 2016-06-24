# -*- coding:utf-8 -*-
import datetime as dt
import os

import pandas as pd
import tushare as ts

from logs import get_logger


def load_daily_data(session, begin_code="000000"):
    engine = session.get_bind()

    log_file = (os.getcwd() + os.sep + "logs" + os.sep + "load_daily_%s.log") % (dt.datetime.now().strftime('%Y-%m-%d'))
    logger = get_logger(log_file,'daily_load')

    logger.info('Daily load begin')
    logger.info("##########################################")

    # 获得上市公司的基本数据
    code_list = get_all_code_basic(session,begin_code)#load_comp_basic(session)
    #code_list = code_list[code_list.index >= begin_code]

    # 添加上证深证指数
    s = pd.DataFrame(index=['sh','sz'])
    code_list = code_list.append(s)

    # 获得数据库中所有股票的max date
    max_date_sql = "select code,max(date)  as max_date from stock.stock_hist group by code"

    # max_date_sql ="select code,max(date) as max_date from stock_hist group by code"
    max_date_df = pd.read_sql(max_date_sql, engine, columns=['code', 'max_date'])

    # 获得所有股票历史信息
    for index in code_list.index:
        row = code_list.iloc[index]
        logger.info(("Load data of code : %s ") % (row.code))
        logger.info(("Time to market : {timeToMarket} ").format(timeToMarket=row.timeToMarket))

        if not row.timeToMarket :
            logger.info(("Code : %s has not yet listed ") % (row.code))
            continue

        try:
            max_date = max_date_df[max_date_df.code == row.code].max_date.values[0]
            max_date = max_date if isinstance(max_date, dt.date) or isinstance(max_date,
                                                                               dt.datetime) else dt.datetime.strptime(
                    max_date, "%Y-%m-%d")
        except Exception as e:
            logger.info(("Code : %s has no history data ") % (row.code))
            max_date = dt.date(1900, 1, 1)


        next_date_py = max_date + dt.timedelta(days=1)
        next_date_str = next_date_py.strftime('%Y-%m-%d')

        # 从Tushare中拿数据
        one_stock = ts.get_hist_data(row.code, start=next_date_str)
        logger.info(("Max date in existing DW is : %s ") % (next_date_str))

        try:
            if row.code in ('sh', 'sz'):
                one_stock['turnover'] = 0
            one_stock['date'] = one_stock.index
            logger.info(("Code : %s has %d rows need to be inserted") % (row.code, one_stock.index.size))
        except Exception as e:
            logger.error(("Code : %s has something wrong from date %s ") % (row.code, next_date_str))
            break

        one_stock = one_stock.reset_index(drop=True)
        one_stock.insert(0, 'code', row.code, allow_duplicates=True)

        try:
            one_stock.to_sql('stock_hist', engine, index = False, schema='stock', if_exists='append')
            logger.info(("Code : %s updated successfully ") % (row.code))
            logger.info("##########################################")
        except Exception as e:
            logger.error(("Code : %s has something wrong for inserting %s ") % (row.code, next_date_str))
            break
        finally:
            session.close()


def load_comp_basic(session):
    log_file = (os.getcwd() + os.sep + "logs" + os.sep + "load_comp_basic_%s.log") % (
    dt.datetime.now().strftime('%Y-%m-%d'))
    logger = get_logger(log_file,'basic_load')

    logger.info('Daily company basic information load begin')
    logger.info("##########################################")

    logger.info("Begin load data from Tushare")
    # 获得上市公司的基本数据
    code_list = ts.get_stock_basics()
    code_list = code_list.sort_index()
    logger.info(("Get total %d stocks") % (code_list.index.__len__()))
    try:
        logger.info("Truncate table stock.comp_basic")
        session.execute(str("truncate table stock.comp_basic"))
        session.commit()

        logger.info("Insert data into table stock.comp_basic")
        code_list.insert(0,'code',code_list.index)
        code_list.timeToMarket  =code_list.timeToMarket.apply(lambda x:dt.datetime.strptime(x.__str__(),"%Y%m%d") if x !=0 else None)

        engine = session.get_bind()
        code_list.to_sql('comp_basic', engine, schema='stock', index=False, if_exists='append')

        logger.info("Load successfully")

        return code_list
    except Exception as e:
        logger.error("Error when get basic data")
        return pd.DataFrame()
    finally:
        session.close()

def get_all_code_basic(session,begin_code="000000"):
    sql = "select * from [stock].[comp_basic] where code>={code}".format(code=begin_code)
    df = pd.read_sql(sql,session.get_bind())
    return df