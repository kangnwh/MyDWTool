#### Demo.xml ###
```XML
<?xml version="1.0" encoding="utf-8"?>
<configure>
    <parameter>
            <name>stock_code</name>
            <type>text</type>
            <desc>股票代码</desc>
            <default>0000001</default>
    </parameter>
    <dataset>
        <name>stock</name>
        <type>sql</type>
        <value>select top 90 * from stock.stock_hist where code='$stock_code' order by date desc</value>
        <engine>mssql+pymssql://xxxx:xxxx@127.0.0.1:1433/stock?charset=utf8</engine>
    </dataset>
    <dataset>
        <name>stock_list</name>
        <type>list</type>
        <value>000001,002340,300059,600570</value>
        <sep>,</sep>
    </dataset>

    <div class="container">
        <report_page>
            <h2><dsr>stock.iloc[0].p_change</dsr></h2>
        </report_page>

        <div class="row">
        <prompt_page>

            <prompt>stock_code</prompt>
            <submit>提交</submit>
        </prompt_page>
        </div>


        <report_page>
        <div class="row">
            <chart id="chart1"  class="col-md-6"  style="height:300px">
                <type>Line</type>
                <template>normal</template>
                <parameter name="chart_id">chart1</parameter>
                <parameter name="title">测试title</parameter>
                <parameter name="subtitle">测试subtitle</parameter>
                <parameter name="x_data"><dsr>stock.date.tolist()</dsr></parameter>
                <parameter name="y_data"><dsr>stock.open.tolist()</dsr></parameter>
            </chart>
            <table id="table1"  class="col-md-6"  style="height:300px"></table>
        </div>
        </report_page>
    </div>
</configure>


```


### 说明 ###

### parameter ###
报表内所使用的变量。每个变量需要一个 `<parameter></parameter>` 标签来定义。
#### 注意,在生成报表的时候需要传递这些参数的值,如果有任何缺失,则生成的报表只会显示promotion ####
用于做filter或者实现其他灵活变动，变量名在后边的定义中可以使用.
#### 例如在 `dataset` 的 `value` 中调用 *stock_code*: `$stock_code` ####
```XML
    <value>select top 90 * from stock.stock_hist where code='$stock_code' order by date desc</value>
```

> 每个*parameter*元素包含4个子元素：
> - *name* : parameter name,用于在下面的定义中直接调用
> - *desc* : 变量的描述
> - *type* : 显示promotion page时的控件类型，有以下几种定义：
>>>> *text* : 文本类型的提示框
>>>> *option* : 下拉列表型的提示框,使用这个类型的提示框需要定义下拉列表的值
>>>> *boolean* : checkbox类型的提示框

> - *default* : 变量的默认值


### dataset ###
定义数据来源。每个数据来源需要一个 `<dataset></dataset>` 标签来定义。
用于获得报表内所显示数据的来源，但是在处理时都会被转换成 `pandas.DataFrame` 类型的数据。在报表定义内使用dataset的 `name` 来随时调用数据。

#### 例如在h2中调用名为 *stock* 的 *dataset*  ####
> stock dataset中第一行的name列的值
```HTML
    <h2>股票名称:<dsr>stock.ix[0].name<dsr></h2>
```

> 每个*dataset*元素包含3个子元素：
> - *name* : data set name,用于在下面的定义中调用
> - *type* : data set的type,可以是以下集中之一 [*sql*,*list*,*file* ]
> - *value* : value的值根据type不同而有所不同
>>>> *sql* : 获得data set的sql，同时需要 `<engine>connect_string</engine>`来指定数据库
>>>> *file* : 数据文件的位置，同时需要`<filetype></filetype>`来制定文件类型。
>>>> *list* : 逗号分割的一个列表，同时需要指定`<sep></sep>`分隔符。默认是逗号


### prompt_page ###
用来定义报表提示框的布局
##### 注意! #####
> 当传递的报表参数不对时，则只显示prompt page用于填写相应参数，之后可以重新提交以显示报表。
````HTML
     <prompt_page>
            <prompt>stock_code</prompt>
            <submit>提交</submit>
        </prompt_page>
````

### report_page ###
用来定义报表内容的布局
##### 注意! #####
> 当传递的报表参数不对时，则report_page中包含的内容将会被忽略，当参数全部填写完成后重新提交则可以完成显示。

##### 注意! #####
> 数据会被转换成`pandas.DataFrame`,因此在使用的时候可以使用 `name.column_name`来访问某列的数据。详情请参考[Pandas文档](http://pandas.pydata.org/pandas-docs/stable/whatsnew.html)。
