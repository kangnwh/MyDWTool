from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError
import re,tushare as ts

def stock_code_validator(form,field):
        if not re.match(r'^\d{6}$',field.data) :
            raise ValidationError("不是有效的股票代码:请输入有效的6位股票代码")
        else:
            all = ts.get_stock_basics()
            if not field.data in all.index:
                raise ValidationError("不是有效的股票代码:请输入有效的6为股票代码")

class StockCode(Form):
    code = StringField('股票代码', validators=[DataRequired(message='请输入股票代码'),stock_code_validator])

