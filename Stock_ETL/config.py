from BI.EChartT import BASE_PATH
import os


default_word_font_ttf = BASE_PATH+os.sep+"WordCloud"+os.sep + "幼圆.ttf"
default_dict = BASE_PATH+os.sep+"WordCloud"+os.sep+"dict"+os.sep+"dict.txt"
wordcloud_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + os.sep + "app" + os.sep + "subapps" + os.sep + "stock" + os.sep + "static" + os.sep + "wordcloud"
exclude_words = ["公司","有限公司","本司","议案","股东","集团","债券","Ltd","投票","本次","方案","通过","登记","交易","公告","方式","意见","独立","关于","内容","项目","信息",
                 "相关","文件","地区","技术","证券","时间","设置","先生","重大","其他","标的","管理","金额","总数","报告","出席"]