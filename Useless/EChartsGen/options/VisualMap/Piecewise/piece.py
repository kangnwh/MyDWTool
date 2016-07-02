from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject


class Piece(EchartBaseObject):
    def __init__(self, min,max,
                 symbol=None,
                 symbolSize=None,
                 color=None,
                 opacity=None,
                 colorAlpha=None,
                 colorLightness=None,
                 colorSaturation=None,
                 colorHue=None):
        self.min = min
        self.max = max
        self.symbol = symbol
        self.symbolSize = symbolSize
        self.color = color
        self.opacity = opacity
        self.colorAlpha = colorAlpha
        self.colorLightness = colorLightness
        self.colorSaturation = colorSaturation
        self.colorHue = colorHue


    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")