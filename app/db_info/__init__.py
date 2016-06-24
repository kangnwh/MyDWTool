import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from .no_git_file import TARGET_USERID, TARGET_PASSWORD, TARGET_DB_HOST, TARGET_PORT, TARGET_DB_NAME

connect_str =(('mssql+pymssql://%s:%s@%s:%s/%s?charset=utf8') % (TARGET_USERID,TARGET_PASSWORD,TARGET_DB_HOST,TARGET_PORT,TARGET_DB_NAME))

engine = sa.create_engine(connect_str)

Session = sessionmaker(bind=engine)