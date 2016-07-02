from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject
from Useless.EChartsGen.options.Common.color import Color
from Useless.EChartsGen.options.Common.opacity import Opacity
from Useless.EChartsGen.options.Common.shadowBlur import ShadowBlur


class LineStyle(EchartBaseObject):
    type_list=('solid','dashed','dotted')
    def __init__(self,color= Color('#333'),
                    width= 1,
                    type= 'solid',
                    shadowBlur= ShadowBlur(shadowColor= 'rgba(0, 0, 0, 0.5)',shadowBlur= 10),
                    shadowColor= Color(),
                    shadowOffsetX= 0,
                    shadowOffsetY= 0,
                    opacity= Opacity(1)
                 ):
        self.color = color
        self.width = width
        self.type = type if type in self.type_list else None
        self.shadowBlur = shadowBlur
        self.shadowColor = shadowColor
        self.shadowOffsetX = shadowOffsetX
        self.shadowOffsetY = shadowOffsetY
        self.opacity = opacity


    def make_json(self):
        json = "lineStyle:{"
        json += "color:'{color}',".format(color=self.color) if self.color else ""
        json += "width:{width},".format(width=self.width) if self.width else ""
        json += "type:'{type}',".format(type=self.type) if self.type else ""
        json += "{shadowBlur}".format(shadowBlur=self.shadowBlur) if self.shadowBlur else ""
        json += "shadowColor:'{shadowColor}',".format(shadowColor=self.shadowColor) if self.shadowColor else ""
        json += "shadowOffsetX:{shadowOffsetX},".format(shadowOffsetX=self.shadowOffsetX) if self.shadowOffsetX else ""
        json += "shadowOffsetY:{shadowOffsetY},".format(shadowOffsetY=self.shadowOffsetY) if self.shadowOffsetY else ""
        json += "{opacity}".format(opacity=self.opacity) if self.opacity else ""
        json += "},"
        return json
