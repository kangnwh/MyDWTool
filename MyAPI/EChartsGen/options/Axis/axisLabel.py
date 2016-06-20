from MyAPI.EChartsGen.options.Common.textStyle import TextStyle
from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
class AxisLabel(EchartBaseObject):
    def __init__(self, show = 'true',
                 interval = 'auto',
                 inside = 'false',
                 rotate = 0,
                 margin = 8,
                 formatter = None,
                 textStyle = TextStyle()):
        self.show = show
        self.interval = interval
        self.inside = inside
        self.rotate = rotate
        self.margin = margin
        self.formatter = formatter
        self.textStyle = textStyle


    def make_json(self):
        json = "axisLabel:{"
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "interval:'{interval}',".format(interval=self.interval) if self.interval else ""
        json += "inside:{inside},".format(inside=self.inside) if self.inside else ""
        json += "rotate:{rotate},".format(rotate=self.rotate) if self.rotate else ""
        json += "margin:{margin},".format(margin=self.margin) if self.margin else ""
        json += "formatter:{formatter},".format(formatter=self.formatter) if self.formatter else ""
        json += "{textStyle}".format(textStyle=self.textStyle) if self.textStyle else ""
        json += "},"
        return json
