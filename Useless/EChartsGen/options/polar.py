from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject


class Polar(EchartBaseObject):
    def __init__(self, zlevel = 0,
                        z = 2,
                        center = ['50%', '50%'],
                        radius = ['50%','0%']):
        self.zlevel = zlevel
        self.z = z
        self.center = center
        self.radius = radius


    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")