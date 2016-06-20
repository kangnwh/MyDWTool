from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject


class AxisType(EchartBaseObject):
    type_list = ('value','category','time','log')
    def __init__(self, value):
        if value in self.type_list:
            self.type = value
        else:
            exc = "axis的type必须是"
            for t in self.type_list:
                exc = exc + t + ","
            exc += "之一"
            raise Exception(exc)

    def make_json(self):
        json = "type:'{type}',".format(type=self.type) if self.type else ""
        return json