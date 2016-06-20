from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject,Color,ShadowBlur,Opacity


class IconStyle(EchartBaseObject):
    def __init__(self, color = '自适应',
                        borderColor = Color('#666'),
                        borderWidth = 1,
                        shadowBlur = ShadowBlur(),
                        shadowColor = None,
                        shadowOffsetX = 0,
                        shadowOffsetY = 0,
                        opacity = Opacity(1)):
        self.color = color
        self.borderColor = borderColor
        self.borderWidth = borderWidth
        self.shadowBlur = shadowBlur
        self.shadowColor = shadowColor
        self.shadowOffsetX = shadowOffsetX
        self.shadowOffsetY = shadowOffsetY
        self.opacity = opacity


    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")