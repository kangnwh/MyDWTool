import string
import xml.dom.minidom


def render_chart(filename, para_dict):
    p_dict,scirpt = getConfig(filename)

    if checkParameters(p_dict, para_dict):
        t = string.Template(scirpt)
        script = t.safe_substitute(para_dict)
        return script
    else :
        exception = "\n请正确制定模版中的参数:\n"
        for (key,desc) in p_dict.items():
            exception += "\t{key}:{desc}\n".format(key=key,desc=desc)

        raise Exception(exception)


def getConfig(file):
    dom = xml.dom.minidom.parse(file)
    root = dom.documentElement
    p_list = root.getElementsByTagName('parameter')
    p_dict = {p.getElementsByTagName('name')[0].firstChild.data:
                 p.getElementsByTagName('desc')[0].firstChild.data
             for p in p_list}
    script = root.getElementsByTagName('script')[0].firstChild.wholeText
    return p_dict,script


def checkParameters(p_dict,para_dict):
    p_list = list(p_dict.keys())
    d = list(para_dict.keys())

    p_list.sort()
    d.sort()

    if p_list == d :
        return True
    else:
        return False