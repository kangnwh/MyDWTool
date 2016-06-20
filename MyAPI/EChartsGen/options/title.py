from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
from MyAPI.EChartsGen.options.Common.shadowBlur import ShadowBlur
from MyAPI.EChartsGen.options.Common.textStyle import TextStyle
from MyAPI.EChartsGen.options.Common.color import Color
from .subtextStyle import SubtextStyle


class Title(EchartBaseObject):
    def __init__(self,
                 show= 'true',
                 text= None,
                 link= None,
                 target= 'blank',
                 textStyle= TextStyle(),
                 subtext= None,
                 sublink= None,
                 subtarget= 'blank',
                 subtextStyle= SubtextStyle(),
                 padding= 5,
                 itemGap= 5,
                 zlevel= 0,
                 z= 2,
                 left= 'auto',
                 top= 'auto',
                 right= 'auto',
                 bottom= 'auto',
                 backgroundColor= 'transparent',
                 borderColor= Color('#ccc'),
                 borderWidth= 1,
                 shadowBlur= ShadowBlur(),
                 shadowColor=Color(),
                 shadowOffsetX= 0,
                 shadowOffsetY= 0
                 ):
        self.show             =	show
        self.text             =	text
        self.link             =	link
        self.target           =	target
        self.textStyle        =	textStyle
        self.subtext          =	subtext
        self.sublink          =	sublink
        self.subtarget        =	subtarget
        self.subtextStyle     =	subtextStyle
        self.padding          =	padding
        self.itemGap          =	itemGap
        self.zlevel           =	zlevel
        self.z                =	z
        self.left             =	left
        self.top              =	top
        self.right            =	right
        self.bottom           =	bottom
        self.backgroundColor  =	backgroundColor
        self.borderColor      =	borderColor
        self.borderWidth      =	borderWidth
        self.shadowBlur       =	shadowBlur
        self.shadowColor      =	shadowColor
        self.shadowOffsetX    =	shadowOffsetX
        self.shadowOffsetY    = shadowOffsetY

    def make_json(self):
        json = "title:{"
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "text:'{text}',".format(text=self.text) if self.text else ""
        json += "link:'{link}',".format(link=self.link) if self.link else ""
        json += "target:'{target}',".format(target=self.target) if self.target else ""
        json += "{textStyle}".format(textStyle=self.textStyle) if self.textStyle else ""
        json += "subtext:'{subtext}',".format(subtext=self.subtext) if self.subtext else ""
        json += "sublink:'{sublink}',".format(sublink=self.sublink) if self.sublink else ""
        json += "subtarget:{subtarget},".format(subtarget=self.subtarget) if self.subtarget else ""
        json += "subtextStyle:{subtextStyle},".format(subtextStyle=self.subtextStyle) if self.subtextStyle else ""
        json += "padding:{padding},".format(padding=self.padding) if self.padding else ""
        json += "itemGap:{itemGap},".format(itemGap=self.itemGap) if self.itemGap else ""
        json += "zlevel:{zlevel},".format(zlevel=self.zlevel) if self.zlevel else ""
        json += "z:{z},".format(z=self.z) if self.z else ""
        json += "left:'{left}',".format(left=self.left) if self.left else ""
        json += "top:'{top}',".format(top=self.top) if self.top else ""
        json += "right:'{right}',".format(right=self.right) if self.right else ""
        json += "bottom:'{bottom}',".format(bottom=self.bottom) if self.bottom else ""
        json += "backgroundColor:'{backgroundColor}',".format(backgroundColor=self.backgroundColor) if self.backgroundColor else ""
        json += "borderColor:'{borderColor}',".format(borderColor=self.borderColor) if self.borderColor else ""
        json += "borderWidth:{borderWidth},".format(borderWidth=self.borderWidth) if self.borderWidth else ""
        json += "{shadowBlur}".format(shadowBlur=self.shadowBlur) if self.shadowBlur else ""
        json += "shadowColor:'{shadowColor}',".format(shadowColor=self.shadowColor) if self.shadowColor else ""
        json += "shadowOffsetX:{shadowOffsetX},".format(shadowOffsetX=self.shadowOffsetX) if self.shadowOffsetX else ""
        json += "shadowOffsetY:{shadowOffsetY},".format(shadowOffsetY=self.shadowOffsetY) if self.shadowOffsetY else ""
        json +="},"
        return json

