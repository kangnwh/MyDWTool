 # -*- coding: utf-8 -*-
from  .echartError import echartError
from .series import series
class baseType(object):
    _x = list()
    _y = list()
    def __init__(self,html_id=None):
        self._html_id=html_id
        pass

    @property
    def  html_id(self):
       return self._html_id
    @html_id.setter
    def html_id(self,value):
        self._html_id = value

    @property
    def  x(self):
       return self._x

    @x.setter
    def x(self,value):
        if isinstance(value,series):
            self._x = value
        else:
            raise Exception("所给值不是series类型")

    @property
    def  y(self):
       return self._y

    def add_series(self,value):
        if isinstance(value,series):
            self._y.append(value)
        else:
            raise Exception("所给值不是series类型")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self,value):
        #TODO check whether the type is validated
        self._type = value

    def generate_cfg_json(self):
        raise Exception("请在子类中重写该函数")


    def __data_validate(self):
        x_l = self.x.data.__len__()
        for y_l in self.y:
            if x_l != y_l.data.__len__():
                raise Exception("请检查输入数据x,y的长度是否相等")
        return True

    def make_json(self):
        self.__data_validate()
        return self.generate_cfg_json()