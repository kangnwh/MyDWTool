from MyAPI.EChartsGen.options.Axis.axisLine import AxisLine
from MyAPI.EChartsGen.options.Axis.axisTick import AxisTick
from MyAPI.EChartsGen.options.Axis.axisLabel import AxisLabel
from MyAPI.EChartsGen.options.Common.splitLine import SplitLine
from MyAPI.EChartsGen.options.Common.splitArea import SplitArea
from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject

class AngleAxis(EchartBaseObject):
    def __init__(self, data, polarIndex = 0,
                 startAngle = 90,
                 clockwise = True,
                 type = 'category',
                 boundaryGap = None,  #TODO 根据轴类别不同，应不同对待
                        min = 'auto',
                 max = 'auto',
                 scale = False,
                 splitNumber = 5,
                 minInterval = 0,
                 interval = None,  #TODO 根据轴类别不同，应不同对待
                        silent = True,
                 axisLine = AxisLine(),
                 axisTick = AxisTick(),
                 axisLabel = AxisLabel(),
                 splitLine = SplitLine(),
                 splitArea = SplitArea(),
                 ):
        self.polarIndex = polarIndex
        self.startAngle = startAngle
        self.clockwise = clockwise
        self.type = type
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
        raise Exception("请重写make_json函数来生成对应属性的json数据")