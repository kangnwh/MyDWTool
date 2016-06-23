import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker


TARGET_DB_HOST = '192.168.0.117'
TARGET_PORT = 1433
TARGET_USERID = 'biuser'
TARGET_PASSWORD= 'bi@2016'
TARGET_DB_NAME= 'stock'
TARGET_SCHEMA='stock'

connect_str =(('mssql+pymssql://%s:%s@%s:%s/%s?charset=utf8') % (TARGET_USERID,TARGET_PASSWORD,TARGET_DB_HOST,TARGET_PORT,TARGET_DB_NAME))

engine = sa.create_engine(connect_str)

Session = sessionmaker(bind=engine)