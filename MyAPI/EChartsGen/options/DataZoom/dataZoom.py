from MyAPI.EChartsGen.options.Common import EchartBaseObject


class DataZoom(EchartBaseObject):
    #TODO Toolbox中的datazoom,目前只支持直角坐标系
    def __init__(self, show =  True,
                        title =  {...},
                        icon =  {...},
                        iconStyle =  {...},
                        xAxisIndex =  ...,
                        yAxisIndex = ...):
        pass

    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")