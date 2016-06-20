from app.MyAPI.EChartsGen.options.Common.TextStyle import TextStyle

from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
from MyAPI.EChartsGen.options.Common.shadowBlur import ShadowBlur
from .Common import Color
from .legendDataCategory import LegendDataCategory


class Legend(EchartBaseObject):
    def __init__(self,
                 show= True,
                 zlevel= 0,
                 z= 2,
                 left= 'auto',
                 top= 'auto',
                 right= 'auto',
                 bottom= 'auto',
                 width= 'auto',
                 height= 'auto',
                 orient= 'horizontal',
                 align= 'auto',
                 padding= 5,
                 itemGap= 10,
                 itemWidth= 25,
                 itemHeight= 14,
                 formatter= None,
                 selectedMode= True,
                 selected= dict(),
                 textStyle= TextStyle(),
                 data= LegendDataCategory(),
                 backgroundColor= 'transparent',
                 borderColor= Color('#ccc'),
                 borderWidth= 1,
                 shadowBlur= ShadowBlur(),
                 shadowColor=Color(),
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
        self.orient	=	orient
        self.align	=	align
        self.padding	=	padding
        self.itemGap	=	itemGap
        self.itemWidth	=	itemWidth
        self.itemHeight	=	itemHeight
        self.formatter	=	formatter
        self.selectedMode	=	selectedMode
        self.selected	=	selected
        self.textStyle	=	textStyle
        self.data	=	data
        self.backgroundColor	=	backgroundColor
        self.borderColor	=	borderColor
        self.borderWidth	=	borderWidth
        self.shadowBlur	=	shadowBlur
        self.shadowColor	=	shadowColor
        self.shadowOffsetX	=	shadowOffsetX
        self.shadowOffsetY	=	shadowOffsetY

    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")