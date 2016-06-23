import sqlalchemy
from .mssql_info import Session
from Stock_ETL import tu_api as ta

def daily_run(begin_code="000000"):
    ta.load_daily_data(Session)


if __name__ =="main":
    daily_run()

