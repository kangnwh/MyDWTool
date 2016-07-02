from Useless.EChartsGen.options.Axis import axisLine
from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject
from ..Axis import axisTick, axisLabel
from ..Common import TextStyle,Color


class ParallelAxisDefault(EchartBaseObject):
    type_list = ('value','category','time','log')
    def __init__(self, data, type = 'value',
                 name = '',
                 nameLocation = 'start',
                 nameTextStyle = TextStyle(color=Color('#fff'),fontSize=12),
                 nameGap = 15,
                 inverse = False,
                 boundaryGap = None,
                 min = 'auto',
                 max = 'auto',
                 scale = False,
                 splitNumber = 5,
                 minInterval = 0,
                 interval = ...,
                 silent = True,
                 axisLine = axisLine(),
                 axisTick = axisTick(),
                 axisLabel = axisLabel(),
                 ):
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
        self.data = data


    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")