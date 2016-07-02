from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject
from ...options.Common.opacity import Opacity

class Range(EchartBaseObject):
    def __init__(self, color=None,
                        symbolSize=None,
                        opacity=Opacity(1),
                        colorAlpha = None,
                        colorLightness = None,colorSaturation = None,colorHue = None):
        self.color = color
        self.symbolSize = symbolSize
        self.opacity = opacity

        self.colorAlpha = colorAlpha
        self.colorLightness = colorLightness
        self.colorSaturation = colorSaturation
        self.colorHue = colorHue


    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")