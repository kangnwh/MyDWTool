from Useless.EChartsGen.options.Common import EchartBaseObject


class Indicator(EchartBaseObject):

    def __init__(self, name = "请在Indicator的name中指定雷达指示器的名称",
                        max = None,
                        min = 0,
                        scale = False,):
        self.name = name
        self.max = max
        self.min = min


    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")