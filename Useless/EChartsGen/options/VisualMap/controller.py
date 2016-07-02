from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject


class Controller(EchartBaseObject):
    def __init__(self, inRange = None,outOfRange = None):
        self.inRange = inRange
        self.outOfRange = outOfRange

    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")