# Project Introduction #
There are several parts of this project：
## 1. Chart Generator based on based on EChart ##
> All charts can be defined via a XML template(include customized parameters and styles) and the chart generator component can generate the JavaScript code which can be used directly in HTML (according to the template and data you provided) .

> Find more information about the chart template [here](https://github.com/kangnwh/MyDWTool/blob/master/%5BEN%5D%20Chart%20Templates%20&%20Usage.md).


All charts templates are stored under `BI/EChartT/<chart_type>/<template_name>.etmp`. Also you can define whatever template you want here.
>> Note : Only few templates under Line and Bar can be used for now.


## 2. Table Generator based on Bootstrap ##
> Pending

> Find more information about the table template [here](https://github.com/kangnwh/MyDWTool/blob/master/%5BEN%5D%20Table%20Templates%20&%20Usage.md).

## 3. Report generator based on XML,HTML and Chart Generator & Table Generator ##
> This is a simple report generator module that can use above table & chart generator.

> Find more information about the report template [here](https://github.com/kangnwh/MyDWTool/blob/master/%5BEN%5D%20Report%20Templates%20&%20Usage.md).

## 4. Simple report system of China stock ##
> This module contains above 2 parts and is consist of 2 submodules:
> + Stock_ETL -> This is a ETL process based on pandas and Tushare, data will be loaded into a local database via Tushare API.
> + app/stock -> A web reporting system. This module is designed to display as many analytical information (tables and charts) as possible. You can query the information by providing the stock code.


### Installation ###
1. Install the packages below:
 - [x] xlwt
 - [x] lxml
 - [x] numpy
 - [x] pandas
 - [x] sqlalchemy
 - [x] pymssql
 - [x] xlrd
 - [x] flask
 - [x] flask-wtf
 - [x] flask-bootstrap
 - [x] tushare
 - [x] wordcloud
 - [x] pillow
 - [x] jieba

2. Modify the configuration file under `app/config.py`
3. Create a database configuration file at `app/db_info/no_git_file.py` and define below variables:

    ```python
        TARGET_DB_HOST ='192.168.0.117'
        TARGET_PORT = 1433
        TARGET_USERID = 'user_id'
        TARGET_PASSWORD= 'user_password'
        TARGET_DB_NAME= 'stock'
        TARGET_SCHEMA='stock'
    ```
4. Create database tables according to `Stock_ETL/mssql_ddls.sql`.
5. Modify the wordcloud configuration file at `Stock_ETL/config.py`：

    ```python
        default_word_font_ttf = <font file(ttf file)> #The font file that used by word cloud.
        'The font file is a little bigger so I don't upload it to github. You can find any font you like to config this'
        wordcloud_path=<path to store the wordcloud pictures> #Default path is app/subapps/stock/static/wordcloud
        default_dict=<the default dictionary used by jieba package> 
        exclude_words=<a list contains the words that can be ingored when generate word cloud pictures>
    ```
5. Using below commands to import stock data

    ```python
        import Stock_ETL.backend_jobs as bj
        bj.daily_run()
    ```


## 5. ETL Process based on Pandas ##
> Pending



