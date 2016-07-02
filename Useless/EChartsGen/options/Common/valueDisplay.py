from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject


class ValueDisplay(EchartBaseObject):
    def __init__(self, show = True,
                        formatter = None):
        self.show = show
        self.formatter = formatter

    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")