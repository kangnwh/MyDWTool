from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject


class LegendDataCategory(EchartBaseObject):
    def __init__(self,
                 name='数据name',
                 icon='circle', #'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
                 textStyle = ''
                 ):
        self.name = name
        self.icon = icon
        self.textStyle = textStyle

    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")