from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
from MyAPI.EChartsGen.options.Series.line.label import Label
from MyAPI.EChartsGen.options.Common.lineStyle import LineStyle,Color

class MarkLine(EchartBaseObject):
    def __init__(self,data0,data1, symbol = 'circle',
                        symbolSize = 2,
                        precision = 2,
                        label = Label(),
                        lineType = 'normal',
                        lineStyle = LineStyle(), #TODO 少了一个参数curveness,以后解决
                        animation = 'true',
                        animationDuration = 1000,
                        animationEasing = 'cubicOut',
                        animationDelay = 0,
                        animationDurationUpdate = 300,
                        animationEasingUpdate = 'cubicOut',
                        animationDelayUpdate = 0
                 ):
        self.data0= data0
        self.data1= data1
        self.symbol = symbol
        self.symbolSize = symbolSize
        self.precision = precision
        self.label = label
        self.lineType = lineType
        self.lineStyle = lineStyle
        self.animation = animation
        self.animationDuration = animationDuration
        self.animationEasing = animationEasing
        self.animationDelay = animationDelay
        self.animationDurationUpdate = animationDurationUpdate
        self.animationEasingUpdate = animationEasingUpdate
        self.animationDelayUpdate = animationDelayUpdate

    @property
    def data0(self):
        return self._data0
    @data0.setter
    def data0(self,value):
        if isinstance(value,MarkLineData):
            self._data0 = value
        else:
            raise Exception("必须使用EChartsGen.options.Series.line.markLine.MarkLineData的实例来赋值data参数")

    @property
    def data1(self):
        return self._data1
    @data1.setter
    def data1(self,value):
        if isinstance(value,MarkLineData):
            self._data1 = value
        else:
            raise Exception("必须使用EChartsGen.options.Series.line.markLine.MarkLineData的实例来赋值data参数")


    def make_json(self):
        json = "markLine:{"

        json += "symbol:{symbol},".format(symbol=self.symbol) if self.symbol else ""
        json += "symbolSize:{symbolSize},".format(symbolSize=self.symbolSize) if self.symbolSize else ""
        json += "precision:{precision},".format(precision=self.precision) if self.precision else ""
        json += "label:{label},".format(label=self.label) if self.label else ""
        json += "lineType:{lineType},".format(lineType=self.lineType) if self.lineType else ""
        json += "lineStyle:{lineStyle},".format(lineStyle=self.lineStyle) if self.lineStyle else ""
        json += "animation:{animation},".format(animation=self.animation) if self.animation else ""
        json += "animationDuration:{animationDuration},".format(animationDuration=self.animationDuration) if self.animationDuration else ""
        json += "animationEasing:{animationEasing},".format(animationEasing=self.animationEasing) if self.animationEasing else ""
        json += "animationDelay:{animationDelay},".format(animationDelay=self.animationDelay) if self.animationDelay else ""
        json += "animationDurationUpdate:{animationDurationUpdate},".format(animationDurationUpdate=self.animationDurationUpdate) if self.animationDurationUpdate else ""
        json += "animationEasingUpdate:{animationEasingUpdate},".format(animationEasingUpdate=self.animationEasingUpdate) if self.animationEasingUpdate else ""
        json += "animationDelayUpdate:{animationDelayUpdate},".format(animationDelayUpdate=self.animationDelayUpdate) if self.animationDelayUpdate else ""
        json += "data:{"
        json += "{data0}".format(data0=self.data0) if self.data0 else ""
        json += "{data1}".format(data1=self.data1) if self.data1 else ""
        json += "},},"
        return json


class MarkLineData(EchartBaseObject):
    def __init__(self,pos,
                        type = None,
                        valueIndex = None,
                        valueDim = None,
                        coord = None,
                        x =None,
                        y = None,
                        value = None,
                        symbol ='circle',
                        symbolSize = 2,
                        symbolRotate = None,
                        symbolOffset = [0, 0],
                        lineStyle = LineStyle(color=Color("#000")),
                        label = Label()
                 ):
        self.pos= pos
        self.type = type
        self.valueIndex = valueIndex
        self.valueDim = valueDim
        self.coord = coord
        self.x = x
        self.y = y
        self.value = value
        self.symbol = symbol
        self.symbolSize = symbolSize
        self.symbolRotate = symbolRotate
        self.symbolOffset = symbolOffset
        self.lineStyle = lineStyle
        self.label = label

    @property
    def coord(self):
        return self._coord

    @coord.setter
    def coord(self,value):
        if isinstance(value,tuple):
            self._coord = value
        else:
            raise Exception("必须使用[x,y]或者[radius, angle]来赋值coord参数")


    def make_json(self):
        json = "{pos}".format(pos=self.pos)+":{"
        json += "type:'{type}',".format(type=self.type) if self.type else ""
        json += "valueIndex:{valueIndex},".format(valueIndex=self.valueIndex) if self.valueIndex else ""
        json += "valueDim:'{valueDim}',".format(valueDim=self.valueDim) if self.valueDim else ""
        json += "coord:{coord},".format(coord=self.coord) if self.coord else ""
        json += "x:'{x}',".format(x=self.x) if self.x else ""
        json += "y:'{y}',".format(y=self.y) if self.y else ""
        json += "value:'{value}',".format(value=self.value) if self.value else ""
        json += "symbol:'{symbol}',".format(symbol=self.symbol) if self.symbol else ""
        json += "symbolSize:{symbolSize},".format(symbolSize=self.symbolSize) if self.symbolSize else ""
        json += "symbolRotate:'{symbolRotate}',".format(symbolRotate=self.symbolRotate) if self.symbolRotate else ""
        json += "symbolOffset:{symbolOffset},".format(symbolOffset=self.symbolOffset) if self.symbolOffset else ""
        json += "{lineStyle}".format(lineStyle=self.lineStyle) if self.lineStyle else ""
        json += "{label}".format(label=self.label) if self.label else ""
        json += "},"
        return json

