#### Demo.xml ###
```XML
<?xml version="1.0" encoding="utf-8"?>
<configure>
    <parameter>
            <name>stock_code</name>
            <type>text</type>
            <desc>Stock Code</desc>
            <default>0000001</default>
    </parameter>
    <dataset>
        <name>stock</name>
        <type>sql</type>
        <value>select top 90 * from stock.stock_hist where code='$stock_code' order by date desc</value>
        <engine>mssql+pymssql://xxxx:xxxx@xxx.xxx.xxx.xxx:xxx/xxx?charset=utf8</engine>
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
            <submit>Submit</submit>
        </prompt_page>
        </div>


        <report_page>
        <div class="row">
            <chart id="chart1"  class="col-md-6"  style="height:300px">
                <type>Line</type>
                <template>normal</template>
                <parameter name="chart_id">chart1</parameter>
                <parameter name="title">Test Title</parameter>
                <parameter name="subtitle">Test Subtitle</parameter>
                <parameter name="x_data"><dsr>stock.date.tolist()</dsr></parameter>
                <parameter name="y_data"><dsr>stock.open.tolist()</dsr></parameter>
            </chart>
            <table id="table1"  class="col-md-6"  style="height:300px"></table>
        </div>
        </report_page>
    </div>
</configure>
```


### Introduction ###

### parameter ###
These tags define all parameters that will be used in the report xml.Every parameter should be surrounded by tag `<parameter></parameter>` 
All these parameters can be used in anyother positions of the report xml for flexibility.

Below is an example :
#### Using parameter *stock_code* in *dataset SQLs*  ####
```XML
    <value>select top 90 * from stock.stock_hist where code='$stock_code' order by date desc</value>
```
Please note :
> Every *parameter* should have 3 subelements:
> - *name* : parameter name, you can use this parameter by putting *$name* anywhere you want.
> - *desc* : a sample description of this parameter, this description will be show in the prompt page.
> - *default* : this is optional, you can put a default for this parameter here.


### dataset ###
This tag defines a dataset(datasource) that will be used in report xml. Every source should be defined and surrounded by tag `<dataset></dataset>` .

The Report Generator will parse dataset tags into a *pandas.DataFrame* instance. You can refer to this source anywhere you want in the report xml.And of course, you can use all *pandas.DataFrame* functions and features .

Below is an example: 

#### Using dataset named *stock* in tag H2 ####
```HTML
    <h2>Stock Name:<dsr>stock.ix[0].name<dsr></h2>
```

Please note: 
> Every *dataset* should contain 3 subelements: 
> - *name* : dataset name,you can use this dataset by putting *<dsr>name.features</dsr>* anywhere you want. 
> - *type* : type of the dataset, this value should be one of the three : [*sql*,*list*,*file* ]
> - *value* : the Report Generator will try to get the value based on the type of this dataset.
>>>> - if *type = sql* : then tags `<sql>sql_stat</sql>` and `<engine>connect_string</engine>` must be defined. The Report Generator will using  *sql_stat* and *connect_string* to get the source data into a *pandas.DataFrame* instance.
>>>> - if *type = file* : then tag `<filetype></filetype>` must be defined to indicate the data file type.(Plan to support XLS,XLSX,CSV,DEL,JSON,XML)
>>>> - if *type = list* : then tag `<sep></sep>` can be defined or the Report Generator will use comma(,) for default.



##### Attention ! #####
> As all dataset will be translated into an instance of `pandas.DataFrame` , you can use all `pandas.DataFrame` features(such as refer to a column using `dataset.column_name`, or the first row using `dataset.iloc[0]`). More information about Pandas pelase refer to [Pandas Docs](http://pandas.pydata.org/pandas-docs/stable/whatsnew.html)。





