from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
from MyAPI.EChartsGen.options.Common.shadowBlur import ShadowBlur
from MyAPI.EChartsGen.options.Common.color import Color


class ItemStyle(EchartBaseObject):
    type_list=("normal","emphasis")
    def __init__(self, type="normal",
                       color = '自适应',
                        borderColor =Color('#000'),
                        borderWidth = 0,
                        shadowBlur = ShadowBlur(),
                        shadowColor = None,
                        shadowOffsetX = 0,
                        shadowOffsetY = 0,
                        opacity = None,
                 ):
        self.type = type if type in self.type_list else None
        self.color = color
        self.borderColor = borderColor
        self.borderWidth = borderWidth
        self.shadowBlur = shadowBlur
        self.shadowColor = shadowColor
        self.shadowOffsetX = shadowOffsetX
        self.shadowOffsetY = shadowOffsetY
        self.opacity = opacity



    def make_json(self):
        json = "itemStyle:{"
        json += "type:'{type}',".format(type=self.type) if self.type else ""
        json += "color:'{color}',".format(color=self.color) if self.color else ""
        json += "borderColor:'{borderColor}',".format(borderColor=self.borderColor) if self.borderColor else ""
        json += "borderWidth:{borderWidth},".format(borderWidth=self.borderWidth) if self.borderWidth else ""
        json += "{shadowBlur}".format(shadowBlur=self.shadowBlur) if self.shadowBlur else ""
        json += "shadowColor:'{shadowColor}',".format(shadowColor=self.shadowColor) if self.shadowColor else ""
        json += "shadowOffsetX:{shadowOffsetX},".format(shadowOffsetX=self.shadowOffsetX) if self.shadowOffsetX else ""
        json += "shadowOffsetY:{shadowOffsetY},".format(shadowOffsetY=self.shadowOffsetY) if self.shadowOffsetY else ""
        json += "{opacity}".format(opacity=self.opacity) if self.opacity else ""
        json += "},"
        return json
