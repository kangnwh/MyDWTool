from Useless.EChartsGen.options.Common import EchartBaseObject


class Opacity(EchartBaseObject):
    def __init__(self, value):
        pass

    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")