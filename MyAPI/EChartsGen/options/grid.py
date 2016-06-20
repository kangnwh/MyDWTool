from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
from MyAPI.EChartsGen.options.Common.shadowBlur import ShadowBlur
from MyAPI.EChartsGen.options.Common.color import Color


class Grid(EchartBaseObject):
    def __init__(self, show= 'false',
                 zlevel= 0,
                 z= 2,
                 left= 'auto',
                 top= 60,
                 right= '10%',
                 bottom= 60,
                 width= 'auto',
                 height= 'auto',
                 containLabel= 'false',
                 backgroundColor= 'transparent',
                 borderColor= Color('#ccc'),
                 borderWidth= 1,
                 shadowBlur= ShadowBlur(),
                 shadowColor= None, # Color(),
                 shadowOffsetX= 0,
                 shadowOffsetY= 0):
        self.show	=	show
        self.zlevel	=	zlevel
        self.z	=	z
        self.left	=	left
        self.top	=	top
        self.right	=	right
        self.bottom	=	bottom
        self.width	=	width
        self.height	=	height
        self.containLabel	=	containLabel
        self.backgroundColor	=	backgroundColor
        self.borderColor	=	borderColor
        self.borderWidth	=	borderWidth
        self.shadowBlur	=	shadowBlur
        self.shadowColor	=	shadowColor
        self.shadowOffsetX	=	shadowOffsetX
        self.shadowOffsetY	=	shadowOffsetY

    def make_json(self):
        json = "grid:{"
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "zlevel:{zlevel},".format(zlevel=self.zlevel) if self.zlevel else ""
        json += "z:{z},".format(z=self.z) if self.z else ""
        json += "left:'{left}',".format(left=self.left) if self.left else ""
        json += "top:'{top}',".format(top=self.top) if self.top else ""
        json += "right:'{right}',".format(right=self.right) if self.right else ""
        json += "bottom:'{bottom}',".format(bottom=self.bottom) if self.bottom else ""
        json += "width:'{width}',".format(width=self.width) if self.width else ""
        json += "height:'{height}',".format(height=self.height) if self.height else ""
        json += "containLabel:{containLabel},".format(containLabel=self.containLabel) if self.containLabel else ""
        json += "backgroundColor:'{backgroundColor}',".format(backgroundColor=self.backgroundColor) if self.backgroundColor else ""
        json += "borderColor:'{borderColor}',".format(borderColor=self.borderColor) if self.borderColor else ""
        json += "borderWidth:{borderWidth},".format(borderWidth=self.borderWidth) if self.borderWidth else ""
        json += "{shadowBlur}".format(shadowBlur=self.shadowBlur) if self.shadowBlur else ""
        json += "shadowColor:'{shadowColor}',".format(shadowColor=self.shadowColor) if self.shadowColor else ""
        json += "shadowOffsetX:{shadowOffsetX},".format(shadowOffsetX=self.shadowOffsetX) if self.shadowOffsetX else ""
        json += "shadowOffsetY:{shadowOffsetY},".format(shadowOffsetY=self.shadowOffsetY) if self.shadowOffsetY else ""
        json += "},"
        return json
