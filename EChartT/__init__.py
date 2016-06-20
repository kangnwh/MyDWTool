import os
from .Common.common import render_chart

BASE_PATH = os.path.split(os.path.realpath(__file__))[0]
LINE_PATH = BASE_PATH + os.sep +"Line" + os.sep
ECHART_JS_PACKAGE = BASE_PATH + os.sep + "echarts.min.js"

def get_line_script(template_name,**kwargs):
    #print(kwargs)
    return render_chart(filename = (LINE_PATH+template_name+'.etmp'),para_dict=kwargs)



def get_echarts_package():
    return ECHART_JS_PACKAGE