import os
from .Common.common import render_chart
from wordcloud import WordCloud
import jieba
import time

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
    return render_chart(filename = (BASE_PATH + os.sep +"Pie" + os.sep + template_name+'.etmp'),para_dict=kwargs)


def pd_to_dict(df):
    # TODO 将pd.dataframe转化成dict
    pass


def get_word_cloud(word,
                   font_path='F:\\simheittf\\simhei.ttf',
                   width=400,
                   height=200,
                   margin=5,
                   ranks_only=False,
                   prefer_horizontal=0.9,
                   mask=None,
                   scale=1,
                   color_func=None,
                   max_words=200,
                   stopwords=None,
                   random_state=None,
                   background_color='white',
                   max_font_size=None):
    wc = WordCloud(font_path=font_path,width=width,height=height,margin=margin,ranks_only=ranks_only,
                   prefer_horizontal=prefer_horizontal,mask=mask,scale=scale,max_words=max_words,
                   stopwords=stopwords,random_state=random_state,background_color=background_color,max_font_size=max_font_size#,color_func=color_func
                )
    after = ' '.join(jieba.cut(word))
    print(after)
    file = "{BASE_PATH}{sep}WordCloud{sep}{ts}.png".format( BASE_PATH=BASE_PATH ,sep=os.sep,ts=time.time())
    wc.generate(after)
    wc.to_file(file)
    return file