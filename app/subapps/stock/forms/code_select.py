from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
import re
from app.db_info import Session

def stock_exist_valid(code):
    if(code in ('sz','sh')):
        return True
    sql = "select code,name from [stock].[comp_basic] where code='{code}'".format(code=code)
    s = Session()
    r = s.execute(sql).fetchall()
    return r.__len__() > 0



def stock_code_validator(form,field):
        if (not re.match(r'^\d{6}$',field.data)) and (field.data not in ('sz','sh')) :
            raise ValidationError("不是有效的股票代码:请输入有效的6位股票代码")
        else:
            if not stock_exist_valid(field.data):
                raise ValidationError("不是有效的股票代码:请输入有效的6为股票代码")

class StockCode(Form):
    code = StringField('股票代码', validators=[DataRequired(message='请输入股票代码'),stock_code_validator])

