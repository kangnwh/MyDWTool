from MyAPI.EChartsGen.options.Common import EchartBaseObject,TextStyle


class NameGap(EchartBaseObject):
    shape_list = list(('polygon','circle'))
    def __init__(self, textStyle = TextStyle(color="#333"),
                        splitNumber = 5,
                        shape = 'polygon',
                        scale = False,):
        self.textStyle = textStyle
        self.splitNumber = splitNumber

        if shape in self.shape_list:
            self.shape = shape
        else:
            exc = "shape必须是"
            for t in self.shape_list:
                exc = exc + t + ","
            exc += "之一"
            raise Exception(exc)

        self.scale = scale


    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")