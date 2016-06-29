# 该工具是基于pandas的报表工具： #
|-
使用这个模块来生成报表：
1. 设计报表的Jinja2 template
2. 设计一个xml文件，这个文件需要包含如下内容:
    |- 使用的dataset，需要指定dataset的以下属性(attributes):
        ==>name,该name会在step 1中的Jinja2 template中直接以python变量的形式被调用
        ==>type,可以是如下其中一项
            data(真实数据),
            sql(从db中取数据所用的sql),此时需要指定额外属性 engine(包含数据库的连接字符串)
            file(数据文件),此时需要指定额外属性 file_type(制定文件的类型，例如csv,json,excel...)#TODO需要为每个文件类型写函数
    |- reportTemplate，该报表所使用的step 1中建立的Jinja2的模版