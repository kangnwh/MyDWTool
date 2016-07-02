



class EchartBaseObject():
    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")

    def __repr__(self):
        return self.make_json()