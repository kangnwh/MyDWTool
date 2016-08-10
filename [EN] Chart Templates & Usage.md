# Chart Template & Usage #

## Template ##
[This](https://github.com/kangnwh/MyDWTool/blob/master/BI/Components/EChartT/Line/normal.etmp) is a demo for norma line chart.
Please note that all chart template are default based on ECharts. 

You can refer to [EChart Docs](http://echarts.baidu.com/examples.html) if you want to develop some more chart template.



## Usage: (Example for calling template Line/normal) ##

1. Refer `echart js` in your HTML template
    
    ```HTML
        <script src="PATH_OF_echarts.min.js"></script>
    ```
2. Define a HTML element with ID
    
    ```HTML
        <div id="chart" style="height:300px"></div>
    ```
3. Import get_line_script in your python script
    
    ```python
        from BI.EChartT import get_line_script 
    ```
4. Call the generator as below (provide template name and all parameters needed by the template)：
    
    ```python
    script1 = get_line_script(template_name='normal',
                              chart_id = "chart",
                              title='标题',
                              subtitle="平安银行 - 收盘价",
                              y_data= [1,2,3,4,5],
                              x_data= [12,20,12,124,344])
    ```
    
