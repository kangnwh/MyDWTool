from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
from ...Common import Color,TextStyle


class Continuous(EchartBaseObject):
    type = 'continuous'
    def __init__(self, min,
                 max,
                 range = 'null',
                 calculable = False,
                 realtime = True,
                 inverse = False,
                 precision = 0,
                 itemWidth = 20,
                 itemHeight = 140,
                 align = 'auto',
                 text = ("最大","最小"),
                 textGap = 10,
                 show = True,
                 dimension = 0,
                 seriesIndex = None,
                 hoverLink = True,
                 inRange = None,
                 outOfRange = None,
                 contoller = None,
                 zlevel = 0,
                 z = 4,
                 left = 0,
                 top = 'auto',
                 right = 'auto',
                 bottom = 0,
                 orient = 'vertical',
                 padding = 5,#TODO 可以接受int, list(int).__len__() =2 or 4
                 backgroundColor = 'rgba(0,0,0,0)',
                 borderColor = Color('#ccc'),
                 borderWidth = 0,
                 color = None,
                 textStyle = TextStyle(),
                 formatter = None,):
        type = type
        min = min
        max = max
        range = range
        calculable = calculable
        realtime = realtime
        inverse = inverse
        precision = precision
        itemWidth = itemWidth
        itemHeight = itemHeight
        align = align
        text = text
        textGap = textGap
        show = show
        dimension = dimension
        seriesIndex = seriesIndex
        hoverLink = hoverLink
        inRange = inRange
        outOfRange = outOfRange
        contoller = contoller
        zlevel = zlevel
        z = z
        left = left
        top = top
        right = right
        bottom = bottom
        orient = orient
        padding = padding
        backgroundColor = backgroundColor
        borderColor = borderColor
        borderWidth = borderWidth
        color = color
        textStyle = textStyle
        formatter = formatter


    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")