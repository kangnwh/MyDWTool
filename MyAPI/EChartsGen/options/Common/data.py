from .echartBase import EchartBaseObject
from .textStyle import TextStyle
from .color import Color

class Data(EchartBaseObject):
    def __init__(self,
                 value = ('Demo01', 'Demo02', 'Demo03', 'Demo04', 'Demo05', 'Demo06', 'Demo07'),
                 value_style =  (None,TextStyle(fontSize=20,color=Color("#FF0000")),None,None,None,None,None)
                 ):
        self.value = value
        if value_style:
            self.value_style = value_style
        else :
            self.value_style = list()
            for i in value:
                self.value_style.append(None)

    def make_json(self):
        json = "data:["
        for i in range(self.value.__len__()):
            if isinstance(self.value_style[i],TextStyle):

                json = json + "{"+"value:'{value}',{textStyle}".format(value=self.value[i],textStyle=self.value_style[i])+"},"
            else:
                json += "'{value}',".format(value=self.value[i])
        json += "],"
        return json

