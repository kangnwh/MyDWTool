from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject
from .Common import TextStyle,Color,AxisLine,AxisLabel,AxisTick,SplitLine,SplitArea,Data


class RadiusAxis(EchartBaseObject):
    def __init__(self, polarIndex= 0,
                 type= 'value',
                 name= '请在类RadiusAxis使用name=来设置极坐标名称',
                 nameLocation= 'start',
                 nameTextStyle= TextStyle(color = Color('#fff')),
                 nameGap= 15,
                 inverse= False,
                 boundaryGap= None,
                 min= 'auto',
                 max= 'auto',
                 scale= False,
                 splitNumber= 5,
                 minInterval= 0,
                 interval= None,  #TODO 根据轴的类别不同需要不同设置
                        silent= True,
                 axisLine= AxisLine(),
                 axisTick= AxisTick(),
                 axisLabel= AxisLabel(),
                 splitLine= SplitLine(),
                 splitArea= SplitArea,
                 data = Data()  #TODO 在类目轴中才生效
                 ):
        self.polarIndex = polarIndex
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
        raise Exception("请重写make_json函数来生成对应属性的json数据")