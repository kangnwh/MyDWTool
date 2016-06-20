from MyAPI.EChartsGen.options.Common import ValueDisplay,SplitArea,SplitLine,EchartBaseObject
from MyAPI.EChartsGen.options.Axis import axisLine,axisLabel,axisTick
from .indicator import Indicator

from MyAPI.EChartsGen.options.Radar import nameGap


class Radar(EchartBaseObject):
    def __init__(self, indicator, zlevel =  0,
                 z =  2,
                 center =  ['50%', '50%'],
                 radius =  '75%',
                 startAngle =  90,
                 name =  ValueDisplay(formatter="{value}"),
                 nameGap =  nameGap(),
                 silent =  True,
                 axisLine =  axisLine(),
                 axisTick =  axisTick(),
                 axisLabel = axisLabel(),
                 splitLine = SplitLine(),
                 splitArea = SplitArea(),
                 ):
        if isinstance(indicator,list) and isinstance(indicator[0], Indicator):
            self.indicator= indicator
        else:
            Exception("indicator必须是Indicator类型的List")
        self.zlevel = zlevel
        self.z = z
        self.center = center
        self.radius = radius
        self.startAngle = startAngle
        self.name = name
        self.nameGap = nameGap
        self.silent = silent
        self.axisLine = axisLine
        self.axisTick = axisTick
        self.axisLabel = axisLabel
        self.splitLine = splitLine
        self.splitArea = splitArea


    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")