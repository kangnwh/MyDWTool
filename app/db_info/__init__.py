 # -*- coding: utf-8 -*-
import sqlalchemy

DB_HOST = ''
PORT = 1
USERID = ''
PASSWORD= ''
DB_NAME= ''


#target_conn = pymssql.connect(host =TARGET_DB_HOST, database =TARGET_DB_NAME, user=TARGET_USERID, password=TARGET_PASSWORD)

source_conn_str=(('mssql+pymssql://%s:%s@%s:%s/%s?charset=utf8') % (USERID,PASSWORD,DB_HOST,PORT,DB_NAME))
source_engine = sqlalchemy.create_engine(source_conn_str)
