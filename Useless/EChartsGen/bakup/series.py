from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject


class series(EchartBaseObject):
    def __init__(self, value):
        pass

    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")