from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
from .itemStyle import ItemStyle
from .label import Label


class MarkPoint(EchartBaseObject):
    def __init__(self, data ,symbol = 'pin',
                        symbolSize = 50,
                        symbolRotate = ...,
                        symbolOffset = [0, 0],
                        label = Label(),
                        itemStyle = ItemStyle(),
                        animation = 'true',
                        animationDuration = 1000,
                        animationEasing = 'cubicOut',
                        animationDelay = 0,
                        animationDurationUpdate = 300,
                        animationEasingUpdate = 'cubicOut',
                        animationDelayUpdate = 0
                 ):
        self.data = data
        self.symbol = symbol
        self.symbolSize = symbolSize
        self.symbolRotate = symbolRotate
        self.symbolOffset = symbolOffset
        self.label = label
        self.itemStyle = itemStyle
        self.animation = animation
        self.animationDuration = animationDuration
        self.animationEasing = animationEasing
        self.animationDelay = animationDelay
        self.animationDurationUpdate = animationDurationUpdate
        self.animationEasingUpdate = animationEasingUpdate
        self.animationDelayUpdate = animationDelayUpdate
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,value):
        if isinstance(value,MarkPointData):
            self._data = value
        else:
            raise Exception("必须使用EChartsGen.options.Series.line.markPoint.MarkPointData的实例来赋值data参数")

    def make_json(self):
        json = "markPoint:{"
        json += "symbol:'{symbol}',".format(symbol=self.symbol) if self.symbol else ""
        json += "symbolSize:{symbolSize},".format(symbolSize=self.symbolSize) if self.symbolSize else ""
        json += "symbolRotate:'{symbolRotate}',".format(symbolRotate=self.symbolRotate) if self.symbolRotate else ""
        json += "symbolOffset:{symbolOffset},".format(symbolOffset=self.symbolOffset) if self.symbolOffset else ""
        json += "{label}".format(label=self.label) if self.label else ""
        json += "{itemStyle}".format(itemStyle=self.itemStyle) if self.itemStyle else ""
        json += "animation:{animation},".format(animation=self.animation) if self.animation else ""
        json += "animationDuration:{animationDuration},".format(animationDuration=self.animationDuration) if self.animationDuration else ""
        json += "animationEasing:'{animationEasing}',".format(animationEasing=self.animationEasing) if self.animationEasing else ""
        json += "animationDelay:{animationDelay},".format(animationDelay=self.animationDelay) if self.animationDelay else ""
        json += "animationDurationUpdate:{animationDurationUpdate},".format(animationDurationUpdate=self.animationDurationUpdate) if self.animationDurationUpdate else ""
        json += "animationEasingUpdate:'{animationEasingUpdate}',".format(animationEasingUpdate=self.animationEasingUpdate) if self.animationEasingUpdate else ""
        json += "animationDelayUpdate:{animationDelayUpdate},".format(animationDelayUpdate=self.animationDelayUpdate) if self.animationDelayUpdate else ""
        json += "{data}".format(data=self.data) if self.data else ""
        json += "},"
        return json



class MarkPointData(EchartBaseObject):
    def __init__(self,coord,name = '标注名称',
                        type = None,
                        valueIndex = None,
                        valueDim = None,
                        x = None,
                        y = None,
                        value = None,
                        symbol = 'circle',
                        symbolSize = 10,
                        symbolRotate = None,
                        symbolOffset = [0, 0],
                        itemStyle = ItemStyle(),
                        label = Label()
                 ):
        self.name = name
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
        self.itemStyle = itemStyle
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
        json = "data:{"
        json += "coord:{coord},".format(coord=self.coord) if self.coord else ""
        json += "name:'{name}',".format(name=self.name) if self.name else ""
        json += "type:'{type}',".format(type=self.type) if self.type else ""
        json += "valueIndex:{valueIndex},".format(valueIndex=self.valueIndex) if self.valueIndex else ""
        json += "valueDim:'{valueDim}',".format(valueDim=self.valueDim) if self.valueDim else ""
        json += "x:'{x}',".format(x=self.x) if self.x else ""
        json += "y:'{y}',".format(y=self.y) if self.y else ""
        json += "value:'{value}',".format(value=self.value) if self.value else ""
        json += "symbol:'{symbol}',".format(symbol=self.symbol) if self.symbol else ""
        json += "symbolSize:{symbolSize},".format(symbolSize=self.symbolSize) if self.symbolSize else ""
        json += "symbolRotate:{symbolRotate},".format(symbolRotate=self.symbolRotate) if self.symbolRotate else ""
        json += "symbolOffset:{symbolOffset},".format(symbolOffset=self.symbolOffset) if self.symbolOffset else ""
        json += "{itemStyle}".format(itemStyle=self.itemStyle) if self.itemStyle else ""
        json += "{label}".format(label=self.label) if self.label else ""
        json += "},"
        return json
