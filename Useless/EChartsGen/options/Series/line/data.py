from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject
from Useless.EChartsGen.options.Series.line.line import Label
from Useless.EChartsGen.options.Series.line.itemStyle import ItemStyle

class Data(EchartBaseObject):
    symbol_list =('circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow')
    def __init__(self, name,
                        value_list,
                        symbol = 'circle',
                        symbolSize = 4,
                        symbolRotate = None,
                        symbolOffset = [0, 0],
                        label = None,
                        itemStyle = None
                 ):
        self.name = name
        self.value_list = value_list
        self.symbol = symbol if symbol in self.symbol_list else None
        self.symbolSize = symbolSize
        self.symbolRotate = symbolRotate
        self.symbolOffset = symbolOffset
        self.label = label
        self.itemStyle = itemStyle


    def make_json(self):
        json = "data:{"
        json += "name:'{name}',".format(name=self.name) if self.name else ""
        json += "value:{value_list},".format(value_list=self.value_list) if self.value_list else ""
        json += "symbol:'{symbol}',".format(symbol=self.symbol) if self.symbol else ""
        json += "symbolSize:{symbolSize},".format(symbolSize=self.symbolSize) if self.symbolSize else ""
        json += "symbolRotate:{symbolRotate},".format(symbolRotate=self.symbolRotate) if self.symbolRotate else ""
        json += "symbolOffset:{symbolOffset},".format(symbolOffset=self.symbolOffset) if self.symbolOffset else ""
        json += "{label}".format(label=self.label) if self.label else ""
        json += "{itemStyle}".format(itemStyle=self.itemStyle) if self.itemStyle else ""
        json += "},"
        return json