#### 该项目是一个使用python开发的开源报表工具。主要依赖以下开源项目： ####
 - [x] Bootstarp 3
 - [x] Pandas
 - [x] Flask
 - [x] ECharts
 

#### 在未来会逐渐加入以下功能： ####

1. 建立简单的flask web server作为报表展现的载体。
2. 各个单独模块的开发，主要包括以下内容：
> - 基于`EChart`的各种图表实现的模版化，达到在使用图表的时候只需要传入少量参数。模版可以根据需要自定义。
> - 基于`Pandas`和`Bootstrap`的表格的模版化，同样以使用时仅需少量参数为目的。
> - 基于xml的报表定义，在xml中定义数据源，定义报表格式，定义引用的表格或者图表的模版等。

3. 完善flask功能并加入对不同报表的简单权限管理。

#### 接下来的工作 ####
1. 参数的prompt输入和submit。



#### 开发日志： ####
2016-07-02 ：
> - 完成xml报表模版的设计
> - 使用xml定义的报表完成一个可展示的页`url:5001/report/`
> - 完成整个report由自定义xml -> html的prase过程,具体的demo和format定义可参照
> `app/subapp/reporting/templates/report/demo.xml`


2016-06-28 ：
> - 完成了简单的EChart Line,Pie的个别模版
> - 完成了EChart 模版->可用JavaScript的转换
> 

2016-06-25：
> - 完成了flask web server的搭建
> - 完成了EChart模版基本定义的设置，可以在BI/EChartT/Line/normal.etmp中找到最基本的模版




