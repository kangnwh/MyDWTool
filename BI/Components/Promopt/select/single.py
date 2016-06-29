

class Single:

    def __init__(self,name,value_list,default=0):
        self
        pass

    def __repr__(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @property
    def value_list(self):
        return self._value_list

    @value_list.setter
    def value_list(self,value_list):
        try:
            if value_list.__len__() > 0:
                self._value_list = value_list
        except Exception:
            raise("value_list is not itera")
