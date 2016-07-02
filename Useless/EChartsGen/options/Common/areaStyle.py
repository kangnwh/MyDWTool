from Useless.EChartsGen.options.Common.shadowBlur import ShadowBlur
from Useless.EChartsGen.options.Common.color import Color
from Useless.EChartsGen.options.Common.opacity import Opacity,EchartBaseObject

class AreaStyle(EchartBaseObject):
    def __init__(self, color = ['rgba(250,250,250,0.3)','rgba(200,200,200,0.3)'],
                        shadowBlur = ShadowBlur(),
                        shadowColor = Color(),
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
        json = "areaStyle:{"
        json += "color:{color},".format(color=self.color) if self.color else ""
        json += "{shadowBlur}".format(shadowBlur=self.shadowBlur) if self.shadowBlur else ""
        json += "shadowColor:'{shadowColor}',".format(shadowColor=self.shadowColor) if self.shadowColor else ""
        json += "shadowOffsetX:{shadowOffsetX},".format(shadowOffsetX=self.shadowOffsetX) if self.shadowOffsetX else ""
        json += "shadowOffsetY:{shadowOffsetY},".format(shadowOffsetY=self.shadowOffsetY) if self.shadowOffsetY else ""
        json += "{opacity}".format(opacity=self.opacity) if self.opacity else ""
        json += "},"
        return json
