from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
from MyAPI.EChartsGen.options.Common.textStyle import TextStyle,Color


class Label(EchartBaseObject):
    type_list=("normal","emphasis")
    position_list=('top','left','right','bottom','inside','insideLeft','insideRight','insideTop','insideBottom','insideTopLeft','insideBottomLeft','insideTopRight','insideBottomRight')
    def __init__(self, type="normal",
                        show = 'false',
                        position = 'top',
                        formatter = '{b}: {c}',
                        textStyle = TextStyle(color=Color("#fff"),fontSize=12)
                 ):
        self.type = type if type in self.type_list else None
        self.show = show
        self.position = position if position in self.position_list else None
        self.formatter = formatter
        self.textStyle = textStyle


    def make_json(self):
        json ="label:{"
        json += "type:'{type}',".format(type=self.type) if self.type else ""
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "position:'{position}',".format(position=self.position) if self.position else ""
        json += "formatter:'{formatter}',".format(formatter=self.formatter) if self.formatter else ""
        json += "{textStyle}".format(textStyle=self.textStyle) if self.textStyle else ""
        json += "},"
        return json
