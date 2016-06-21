import os
from .Common.common import render_chart
import pandas as pd

BASE_PATH = os.path.split(os.path.realpath(__file__))[0]
ECHART_JS_PACKAGE = BASE_PATH + os.sep + "echarts.min.js"


def get_line_script(template_name, **kwargs):
    # print(kwargs)
    return render_chart(filename=(BASE_PATH + os.sep + "Line" + os.sep + template_name + '.etmp'), para_dict=kwargs)


def get_echarts_package():
    return ECHART_JS_PACKAGE


def generate_pie_data(df):
    """
    :param df: 添加的数据必须是dict,并且是以下样式{"category1":value1,"category2":value2,...,}
    :return:
    """
    if isinstance(df, dict):
        new_data = "["
        #dict = ({value: key, name: value} for (key, value) in df.items())
        for (name, value) in df.items():
            new_data += "{value:%d,name:'%s'}," % (value,name)
        #dict = ["{value: $value, name: $name}".format(value=value,name=name) for (name, value) in df.items()]
        new_data += "]"
        return new_data
    else:
        raise Exception('添加的数据必须是dict,并且是以下样式{"category1":value1,"category2":value2,...,}')

def get_pie_script(template_name, **kwargs):
    """
    :param template_name: 要使用的pie图形的temp name(不需要后缀)
    :param kwargs: 其他要传递给模版的变量使用 variable=value的形式传入
    :return: pie图的javascript代码
    """
    # new_data = []
    #
    # if  series_names.__len__() != data_list.__len__():
    #     raise Exception("series_names与data_list长度不匹配")
    #     return
    # if not isinstance(data_list, list):
    #     raise Exception("data必须是一个dict,样式如下:{'series_name':pd.DataFrame}")
    #     return
    #
    # for i in range(0, data_list.__len__()):
    #     if isinstance(data_list[i], pd.DataFrame):
    #         if data_list[i].columns.__len__() != 2:
    #             raise Exception("data list中的每一项的列数必须是2，并且第一列是category name,第二列是值。")
    #         else:
    #             dict = ({'value': value.values[1], 'name': value.values[0]} for (key, value) in data_list[i].items())
    #             new_data += dict
    #             kwargs[series_names[i]] = new_data
    #     else:
    #         raise Exception("data list中的数据必须是pandas.DataFrame的实例。")
    # print(kwargs)
    return render_chart(filename = (BASE_PATH + os.sep +"Pie" + os.sep + template_name+'.etmp'),para_dict=kwargs)


def pd_to_dict(df):
    # TODO 将pd.dataframe转化成dict
    pass
