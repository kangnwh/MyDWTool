#import xml.etree.ElementTree as ET
from lxml import etree
import pandas as pd,string
import sqlalchemy as sa
from BI.Components.EChartT import generate_chart

def render_report(report_path,**kwargs):
    #TODO add report xml format link
    #TODO use #data_set# to mark where any dataset should be called. and we can use any pd.DataFrame functions such as #pd.iloc[0].column01#,
    #TODO  or together with parameters like #pd.iloc[0].$dynamic_column#
    #TODO and to implement  functions listed above, we need to do the parameter replace first and then use isinstance(eval("str_before_dot"),pd.DataFrame) to ensure
    #TODO the dataset does be a pd.DataFrame before we use eval("whole_dataset_str")
    """
    generate report according to the report definition from an xml
    :param report_path: xml file with report definition. the please check the format here
    :param kwargs: dict like parameters which will fill in the report
    :return:
    """
    tree = etree.parse(report_path)
    root = tree.getroot()

    #initial dataset dict
    variables = locals()
    #initial script str
    all_scripts = ""

    #get all parameter definitions and remove parameter elements
    parameters = get_parameters(root)
    for p in root.findall("parameter"):
        root.remove(p)


    if check_parameters(parameters,kwargs):
        #get all data set
        for d in root.findall("dataset"):
            name,data = get_data_from_dataset(d,**kwargs)

            variables[name] = data

            #delete dataset elements for display
            root.remove(d)

        #fill all dataset data
        for dsr in root.iter("dsr"):
            r_text = fill_parameters(dsr.text, **kwargs)
            pd_name = r_text.split(".")[0]
            if pd_name in variables.keys() :
                if isinstance(eval(pd_name),pd.DataFrame):
                    value = eval(r_text)
                    dsr.text = value_to_string(value)
                    dsr_parent = dsr.getparent()
                    new_text = dsr_parent.text if dsr_parent.text else ""
                    for e_one_pd in dsr_parent.iterchildren():
                        new_text += e_one_pd.text if e_one_pd.text else ""
                        dsr_parent.remove(e_one_pd)
                    #print(etree.tounicode(dsr_parent))
                    dsr_parent.text = new_text
                else:
                    raise Exception("the dataset reference {r_text} is not validated !".format(r_text=r_text))
            else:
                raise Exception("the dataset reference {r_text} is not defined !".format(r_text=r_text))

        #TODO parse all table elements
        for t in root.findall("table"):
            pass

        #parse all chart elements
        for c in root.iter("chart"):
            #get chart type
            e_type = c.find("type")
            type = fill_parameters(e_type.text, **kwargs)
            c.remove(e_type)

            #get template name
            e_tempalte = c.find("template")
            template_name = fill_parameters(e_tempalte.text, **kwargs)
            c.remove(e_tempalte)

            #set parameter dict
            sub_parameters = dict()
            for sp in c.findall("parameter"):
                #get parameter name
                p_name = fill_parameters(sp.get("name"), **kwargs)
                #get parameter content after parameter replacement
                p_text = fill_parameters(sp.text, **kwargs)
                sub_parameters[p_name]=p_text
                c.remove(sp)

            #generate script
            all_scripts += generate_chart(type=type,template_name=template_name,kwargs=sub_parameters)
            c.tag = "div"

        e_script = etree.Element("script",{'type':'text/javascript'})
        e_script.text = all_scripts
        root.append(e_script)
        root.tag="div"
        return etree.tounicode(root,method="html")
    else :
        exception = "\n请正确制定模版中的参数:\n"
        for (key,desc) in parameters.items():
            exception += "\t{key}:{desc}\n".format(key=key,desc=desc)

        raise Exception(exception)



def get_data_from_dataset(dataset,**kwargs):
    """
    get data from dataset definition
    :param dataset: an xml elemen type data which should defined as below：
    定义数据来源。每个数据来源需要一个`<dataset></dataset>`标签来定义。
    用于获得报表内所显示数据的来源，但是在处理时都会被转换成`pandas.DataFrame`类型的数据。在报表定义内使用dataset的`name`来随时调用数据。
    > 每个*dataset*元素包含3个子元素：
    > - *name* : data set name,用于在下面的定义中调用
    > - *type* : data set的type,可以是以下集中之一 [*sql*,*list*,*file* ]
    > - *value* : value的值根据type不同而有所不同
         *sql* : 获得data set的sql，同时需要 `<engine>connect_string</engine>`来指定数据库
         *file* : 数据文件的位置,同时需要提供<filetype></filetype>来确定文件类型
         *list* : 数据的字典形式,同时需要提供<sep></sep>来确定分隔符，默认是逗号
    :return:
        names：report xml 中定义的dataset的变量名
        data: 数据的pd.DataFrames类型
    """

    if isinstance(dataset,etree._Element):
        name = fill_parameters(dataset.find("name").text, **kwargs)
        type = fill_parameters(dataset.find("type").text, **kwargs)
        value = fill_parameters(dataset.find("value").text, **kwargs)


        #check dataset type and generate data into pd.DataFrame type
        if type == 'sql':
            #if type is sql then read data from a database identified by the <engine></engine> element
            engine_str = fill_parameters(dataset.find("engine").text, **kwargs)
            sql = value
            return name,get_data_from_sql(engine_str,sql)#{name:get_data_from_sql(engine_str,sql)}

        elif type == 'list':
            #if type is list then return a python list
            list_str = value
            sep = fill_parameters(dataset.find("sep").text, **kwargs)
            sep = sep if sep else ","
            return name,get_data_from_list(list_str,sep)#{name:get_data_from_list(list_str,sep)}

        elif type =='file':
            #if type is file then parse the file according to different <filetype></filetype>
            file_path = value
            filetype = dataset.find("filetype").text
            return name,get_data_from_file(file_path,filetype)#{name:get_data_from_file(file_path,filetype)}

    else:
        raise Exception("get_data_from_dataset(dataset)中传递的dataset参数不是xml.ElementTree类型")
    pass


def get_data_from_sql(engine_str,sql):
    #TODO None handle
    engine = sa.create_engine(engine_str)
    return pd.read_sql(sql,engine)


def get_data_from_list(str,sep):
    #TODO None handle
    return str.split(",")


def get_data_from_file(file,filetype):
    #TODO None handle
    #TODO different file type
    return "need development"


def check_parameters(p_dict,para_dict):
    '''
    check whether the given parameter sets is equal to the parameter set defined in *.etmp files
    :param p_dict: parameter sets defined in *.etmp
    :param para_dict: parmeter sets given by function caller
    :return: True if equal
    '''
    p_list = list(p_dict.keys())
    d = list(para_dict.keys())

    p_list.sort()
    d.sort()

    if p_list == d :
        return True
    else:
        return False


def get_parameters(root):
    # dom = xml.dom.minidom.parse(file)
    # root = dom.documentElement
    p_list = root.findall('parameter')
    p_dict = {p.find('name').text:
                 p.find('desc').text
             for p in p_list}
    return p_dict


def fill_parameters(org_value, **kwargs):
    value = value_to_string(org_value)
    try:
        org_value_t = string.Template(value)
        return org_value_t.safe_substitute(kwargs) if org_value else ""
    except Exception:
        print(value)


def value_to_string(value):
    if isinstance(value,int):
        value = "%d" % value
    elif isinstance(value,float):
        value = "%.3f" % value
    elif isinstance(value,list):
        value = value.__repr__()
    return value