from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject
from Useless.EChartsGen.options.Common.shadowBlur import ShadowBlur
from Useless.EChartsGen.options.Common.opacity import Opacity

class ShadowStyle(EchartBaseObject):
    def __init__(self, color = 'rgba(150,150,150,0)',
                        shadowBlur = ShadowBlur(),
                        shadowColor = None,
                        shadowOffsetX = 0,
                        shadowOffsetY = 0,
                        opacity = Opacity(1)):
        self.color = color
        self.shadowBlur = shadowBlur
        self.shadowColor = shadowColor
        self.shadowOffsetX = shadowOffsetX
        self.shadowOffsetY = shadowOffsetY
        self.opacity = opacity


    def make_json(self):
        json = "shadowStyle:{"
        json += "color:'{color}',".format(color=self.color) if self.color else ""
        json += "{shadowBlur}".format(shadowBlur=self.shadowBlur) if self.shadowBlur else ""
        json += "shadowColor:'{shadowColor}',".format(shadowColor=self.shadowColor) if self.shadowColor else ""
        json += "shadowOffsetX:{shadowOffsetX},".format(shadowOffsetX=self.shadowOffsetX) if self.shadowOffsetX else ""
        json += "shadowOffsetY:{shadowOffsetY},".format(shadowOffsetY=self.shadowOffsetY) if self.shadowOffsetY else ""
        json += "{opacity}".format(opacity=self.opacity) if self.opacity else ""
        json += "},"
        return json
