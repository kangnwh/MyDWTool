from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject
from .piece import Piece
from ...Common import TextStyle


class Piecewise(EchartBaseObject):
    type = 'piecewise',
    def __init__(self, splitNumber = 5,
                        pieces = (Piece(0,None),),
                        categories = ("类别1",),
                        min =None,
                        max = None,
                        selectedMode = 'multiple',
                        inverse = False,
                        precision = None,
                        itemWidth = 20,
                        itemHeight = 14,
                        align = 'auto',
                        text = ("最大","最小"),
                        textGap = 10,
                        itemGap = 10,
                        itemSymbol = 'roundRect',
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
                        padding = 5,
                        backgroundColor = 'rgba(0,0,0,0)',
                        borderColor = '#ccc',
                        borderWidth = 0,
                        color = None,
                        textStyle = TextStyle(),
                        formatter = None):
        self.splitNumber = splitNumber
        self.pieces = pieces
        self.categories = categories
        self.min = min
        self.max = max
        self.selectedMode = selectedMode
        self.inverse = inverse
        self.precision = precision
        self.itemWidth = itemWidth
        self.itemHeight = itemHeight
        self.align = align
        self.text = text
        self.textGap = textGap
        self.itemGap = itemGap
        self.itemSymbol = itemSymbol
        self.show = show
        self.dimension = dimension
        self.seriesIndex = seriesIndex
        self.hoverLink = hoverLink
        self.inRange = inRange
        self.outOfRange = outOfRange
        self.contoller = contoller
        self.zlevel = zlevel
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.orient = orient
        self.padding = padding
        self.backgroundColor = backgroundColor
        self.borderColor = borderColor
        self.borderWidth = borderWidth
        self.color = color
        self.textStyle = textStyle
        self.formatter = formatter


    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")