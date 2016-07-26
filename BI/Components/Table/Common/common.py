import string
import xml.dom.minidom


def render_table(filename, para_dict):
    p_dict,scirpt = get_config(filename)

    if check_parameters(p_dict, para_dict):
        t = string.Template(scirpt)
        script = t.safe_substitute(para_dict)
        return script
    else :
        exception = "\n请正确制定模版中的参数:\n"
        for (key,desc) in p_dict.items():
            exception += "\t{key}:{desc}\n".format(key=key,desc=desc)

        exception += "\n传递的参数：\n"
        for (key) in para_dict.keys():
            exception += "{key},".format(key=key)

        raise Exception(exception)


def get_config(file):
    '''
    get parameters and script information from *.etmp files
    :param file:
    :return:
    '''
    dom = xml.dom.minidom.parse(file)
    root = dom.documentElement
    p_list = root.getElementsByTagName('parameter')
    p_dict = {p.getElementsByTagName('name')[0].firstChild.data:
                 p.getElementsByTagName('desc')[0].firstChild.data
             for p in p_list}
    script = root.getElementsByTagName('html')[0].firstChild.wholeText
    return p_dict,script


def check_parameters(p_dict, para_dict):
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