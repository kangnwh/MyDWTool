from Useless.EChartsGen.options.Axis.axisType import AxisType
from Useless.EChartsGen.options.Axis.axisLine import AxisLine
from Useless.EChartsGen.options.Axis.axisTick import AxisTick
from Useless.EChartsGen.options.Axis.axisLabel import AxisLabel
from Useless.EChartsGen.options.Common.textStyle import TextStyle
from Useless.EChartsGen.options.Common.splitLine import SplitLine
from Useless.EChartsGen.options.Common.splitArea import SplitArea
from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject


class xAxis(EchartBaseObject):
    #TODO Data 可以是list
    def __init__(self, data, gridIndex= 0,
                         position= 'bottom',
                         type= AxisType('category'),
                         name= '在xAxis在中使用name=来设置name',
                         nameLocation= 'start',
                         nameTextStyle= TextStyle(color='#fff', fontSize=12),
                         nameGap= 15,
                         inverse= 'false',
                         boundaryGap= None,
                         min= 'auto',
                         max= 'auto',
                         scale= 'false',
                         splitNumber= 5,
                         minInterval= 0,
                         interval= None,
                         silent= 'true',
                         axisLine= AxisLine(),
                         axisTick= AxisTick(),
                         axisLabel= AxisLabel(),
                         splitLine= SplitLine(),
                         splitArea= SplitArea()
                 ):
        self.gridIndex = gridIndex
        self.position = position
        self.type = type
        self.name = name
        self.nameLocation = nameLocation
        self.nameTextStyle = nameTextStyle
        self.nameGap = nameGap
        self.inverse = inverse
        self.boundaryGap = boundaryGap
        self.min = min
        self.max = max
        self.scale = scale
        self.splitNumber = splitNumber
        self.minInterval = minInterval
        self.interval = interval
        self.silent = silent
        self.axisLine = axisLine
        self.axisTick = axisTick
        self.axisLabel = axisLabel
        self.splitLine = splitLine
        self.splitArea = splitArea
        self.data = data

    def make_json(self):
        json = "xAxis:{"
        json += "{data}".format(data=self.data) if self.data else ""
        json += "gridIndex:{gridIndex},".format(gridIndex=self.gridIndex) if self.gridIndex else ""
        json += "position:'{position}',".format(position=self.position) if self.position else ""
        json += "{type}".format(type=self.type) if self.type else ""
        json += "name:'{name}',".format(name=self.name) if self.name else ""
        json += "nameLocation:'{nameLocation}',".format(nameLocation=self.nameLocation) if self.nameLocation else ""
        json += "{nameTextStyle}".format(nameTextStyle=self.nameTextStyle) if self.nameTextStyle else ""
        json += "nameGap:{nameGap},".format(nameGap=self.nameGap) if self.nameGap else ""
        json += "inverse:{inverse},".format(inverse=self.inverse) if self.inverse else ""
        json += "boundaryGap:'{boundaryGap}',".format(boundaryGap=self.boundaryGap) if self.boundaryGap else ""
        json += "min:'{min}',".format(min=self.min) if self.min else ""
        json += "max:'{max}',".format(max=self.max) if self.max else ""
        json += "scale:{scale},".format(scale=self.scale) if self.scale else ""
        json += "splitNumber:{splitNumber},".format(splitNumber=self.splitNumber) if self.splitNumber else ""
        json += "minInterval:{minInterval},".format(minInterval=self.minInterval) if self.minInterval else ""
        json += "interval:{interval},".format(interval=self.interval) if self.interval else ""
        json += "silent:{silent},".format(silent=self.silent) if self.silent else ""
        json += "{axisLine}".format(axisLine=self.axisLine) if self.axisLine else ""
        json += "{axisTick}".format(axisTick=self.axisTick) if self.axisTick else ""
        json += "{axisLabel}".format(axisLabel=self.axisLabel) if self.axisLabel else ""
        json += "{splitLine}".format(splitLine=self.splitLine) if self.splitLine else ""
        json += "{splitArea}".format(splitArea=self.splitArea) if self.splitArea else ""
        json += "},"
        return json