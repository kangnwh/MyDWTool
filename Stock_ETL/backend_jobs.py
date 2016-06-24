from Stock_ETL import tu_api as ta
from .mssql_info import Session


def daily_run(begin_code="000000"):
    ta.load_daily_data(Session(), begin_code=begin_code)


if __name__ =="main":
    daily_run()

