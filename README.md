# 项目介绍 #
本项目主要分为以下几个部分：
## 1. 基于ECharts可视化图形配置生成器 ##
> 主要是编写ECharts的相关option配置的template。该template可以完成大部分的图表工作，并预留一些参数入口作为调用template时自定义。

项目中模版放于 `BI/EChartT/<chart_type>/<template_name>.etmp`，目录中的模版可以根据需求自己定义，目前只有Line、Bar下面有个别模版可以使用。

使用方法：(以调用Line/normal为例)
0. 在HTML中引用`echart js`
    ```
     <script src="PATH_OF_echarts.min.js"></script>
    ```
1. 在HTML中定义一个含有ID的HTML控件(例如`<div id="chart" style="height:300px"></div>`)
2. 在python中`from BI.EChartT import get_line_script `
3. 调用如下代码：
    ```python
    script1 = get_line_script(template_name='normal',
                              chart_id = "chart",
                              title='标题',
                              subtitle="平安银行 - 收盘价",
                              y_data= [1,2,3,4,5],
                              x_data= [12,20,12,124,344])
    ```
4. 将第三步中的到的结果`script1`加入到HTML的`<script>{{ script1 }}</script>`中


## 2. 基于Bootstrap的表格生成器 ##
>Pending

## 3. 基于Tushare的简单A股股票分析 ##
>该模块用于展示上面两部分的成果，包含两个子模块
>* Stock_ETL -> 基于Tushare的股票数据load - 落地到本地数据库.
>* app/stock -> 前端web展示界面，通过股票代码查询，将尽量多的公司相关信息/分析结果展示在一个page上

## 4. 基于Pandas的简单ETL处理 ##
>Pending

## package requirement:
- [x] python 3.5
- [x] pymssql
- [x] pandas
- [x] xlwt
- [x] openpyxl
- [x] xlsxwriter
- [x] sqlalchemy
- [x] xlrd
- [x] flask
- [x] flask-wtf
- [x] flask-bootstrap
- [x] tushare

