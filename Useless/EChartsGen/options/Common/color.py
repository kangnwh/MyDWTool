from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject

class Color(EchartBaseObject):
    def __init__(self,color='#aaa'):
        self.color = color

    def make_json(self):
        return self.color

    def __repr__(self):
        return self.make_json()