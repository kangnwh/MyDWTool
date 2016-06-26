from Stock_ETL import tu_api as ta
from Stock_ETL.mssql_info import Session
from Stock_ETL.config import default_dict,exclude_words,wordcloud_path,default_word_font_ttf


def daily_run(begin_code="000000"):
    ta.generate_wordcloud_png(Session(), png_path=wordcloud_path, default_word_font_ttf=default_word_font_ttf,
                              default_dict=default_dict, stopwords=exclude_words, begin_code=begin_code, max_font_size=60)
    ta.load_comp_basic(Session())
    ta.load_daily_data(Session(), begin_code=begin_code)


if __name__ =="main":
    daily_run()

