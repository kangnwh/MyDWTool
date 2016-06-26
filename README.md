# 项目介绍 #
本项目主要分为以下几个部分：
## 1. 基于ECharts可视化图形配置生成器 ##
> 主要是编写ECharts的相关option配置的template。该template可以完成大部分的图表工作，并预留一些参数入口作为调用template时自定义。

项目中模版放于 `BI/EChartT/<chart_type>/<template_name>.etmp`，目录中的模版可以根据需求自己定义，目前只有Line、Bar下面有个别模版可以使用。

使用方法：(以调用Line/normal为例)

1. 在HTML中引用`echart js`
    
    ```HTML
        <script src="PATH_OF_echarts.min.js"></script>
    ```
2. 在HTML中定义一个含有ID的HTML控件,例如
    
    ```HTML
        <div id="chart" style="height:300px"></div>
    ```
3. 在python中
    
    ```python
        from BI.EChartT import get_line_script 
    ```
4. 调用如下代码：
    
    ```python
    script1 = get_line_script(template_name='normal',
                              chart_id = "chart",
                              title='标题',
                              subtitle="平安银行 - 收盘价",
                              y_data= [1,2,3,4,5],
                              x_data= [12,20,12,124,344])
    ```
5. 将第三步中的到的结果`script1`加入到HTML

    ```HTML
        <script>{{ script1 }}</script>
    ```


## 2. 基于Bootstrap的表格生成器 ##
>Pending

## 3. 基于Tushare的简单A股股票分析 ##
>该模块用于展示上面两部分的成果，包含两个子模块
> + Stock_ETL -> 基于Tushare的股票数据load - 落地到本地数据库.
> + app/stock -> 前端web展示界面，通过股票代码查询，将尽量多的公司相关信息/分析结果展示在一个page上

### 安装方法 ###
1. 根据自己的主机等情况配置app/config.py
2. 建立文件app/db_info/no_git_file.py,并定义以下数据库相关的参数：

    ```python
        TARGET_DB_HOST ='192.168.0.117'
        TARGET_PORT = 1433
        TARGET_USERID = 'user_id'
        TARGET_PASSWORD= 'user_password'
        TARGET_DB_NAME= 'stock'
        TARGET_SCHEMA='stock'
    ```
3. 根据`Stock_ETL/mssql_ddls.sql`在自己的数据库中创建相关table.
4. 修改`Stock_ETL/config.py` 中的相关配置：

    ```python
        default_word_font_ttf = <字体文件ttf的路径> #word cloud所使用的字体文件。
        '由于字体文件比较大，没有上传到github中，朋友们可以自行配置该选项'
        wordcloud_path=<存放stock wordcloud图片的位置,用于前端> #默认配置是在app/subapps/stock/static/wordcloud
        default_dict=<jieba分词使用的自定义字典> #<默认的分词字典>
        exclude_words=<word cloud中不需要显示的词列表，可自行定义> #<word cloud中要除去的字符列表>
    ```
5. 使用以下命令导入数据

    ```python
        import Stock_ETL.backend_jobs as bj
        bj.daily_run()
    ```


## 4. 基于Pandas的简单ETL处理 ##
>Pending

## package requirement:
 - [x] xlwt
 - [x] openpyxl
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

