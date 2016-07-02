from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject
from Useless.EChartsGen.options.Common.shadowBlur import ShadowBlur
from Useless.EChartsGen.options.Common.color import Color
from Useless.EChartsGen.options.Common.opacity import Opacity
from Useless.EChartsGen.options.Common.textStyle import TextStyle



class CrossStyle(EchartBaseObject):
    type_list=('solid','dashed','dotted')
    def __init__(self,color= Color('#333'),
                    width= 1,
                    type= 'dashed',
                    shadowBlur= ShadowBlur(shadowColor= 'rgba(0, 0, 0, 0.5)',shadowBlur= 10),
                    shadowColor= Color(),
                    shadowOffsetX= 0,
                    shadowOffsetY= 0,
                    opacity= Opacity(1),
                    textStyle=TextStyle(color=Color('#333'))
               ):
        self.color = color
        self.width = width
        self.type = type if type in self.type_list else None
        self.shadowBlur = shadowBlur
        self.shadowColor = shadowColor
        self.shadowOffsetX = shadowOffsetX
        self.shadowOffsetY = shadowOffsetY
        self.opacity = opacity
        self.textStyle = textStyle


    def make_json(self):
        json = "crossStyle:{"
        json += "color:'{color}',".format(color=self.color) if self.color else ""
        json += "width:{width},".format(width=self.width) if self.width else ""
        json += "type:'{type}',".format(type=self.type) if self.type else ""
        json += "{shadowBlur}".format(shadowBlur=self.shadowBlur) if self.shadowBlur else ""
        json += "shadowColor:'{shadowColor}',".format(shadowColor=self.shadowColor) if self.shadowColor else ""
        json += "shadowOffsetX:{shadowOffsetX},".format(shadowOffsetX=self.shadowOffsetX) if self.shadowOffsetX else ""
        json += "shadowOffsetY:{shadowOffsetY},".format(shadowOffsetY=self.shadowOffsetY) if self.shadowOffsetY else ""
        json += "{opacity}".format(opacity=self.opacity) if self.opacity else ""
        json += "{textStyle}".format(textStyle=self.textStyle) if self.textStyle else ""
        json += "},"
        return json
    #
    # def __repr__(self):
    #     return self.make_json()