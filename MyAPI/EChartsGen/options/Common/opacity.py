from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject


class Opacity(EchartBaseObject):
    def __init__(self,value):
        if(value >=0 and value<=1):
            self.opacity = value
        else:
            raise Exception("opacity的值必须介于0到1之间")

    def make_json(self):
        json = "opacity:{opacity},".format(opacity=self.opacity) if self.opacity else ""
        return json

    def __repr__(self):
        return self.make_json()
