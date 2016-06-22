import sqlalchemy

TARGET_DB_HOST = '218.88.13.118'
TARGET_PORT = 49196
TARGET_USERID = 'sa'
TARGET_PASSWORD= 'jj@2014'
TARGET_DB_NAME= 'BIdb'
TARGET_SCHEMA='bi'

target_conn_str=(('mssql+pymssql://%s:%s@%s:%s/%s?charset=utf8') % (TARGET_USERID,TARGET_PASSWORD,TARGET_DB_HOST,TARGET_PORT,TARGET_DB_NAME))
target_engine = sqlalchemy.create_engine(target_conn_str)