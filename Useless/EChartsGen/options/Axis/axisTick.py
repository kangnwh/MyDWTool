from Useless.EChartsGen.options.Common.lineStyle import LineStyle
from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject

class AxisTick(EchartBaseObject):
    def __init__(self, show= 'true',
                    interval= 'auto',
                    inside= 'false',
                    length= 5,
                    lineStyle= LineStyle()):
        self.show = show
        self.interval = interval
        self.inside = inside
        self.length = length
        self.lineStyle = lineStyle



    def make_json(self):
        json = "axisTick:{"
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "interval:'{interval}',".format(interval=self.interval) if self.interval else ""
        json += "inside:{inside},".format(inside=self.inside) if self.inside else ""
        json += "length:{length},".format(length=self.length) if self.length else ""
        json += "{lineStyle}".format(lineStyle=self.lineStyle) if self.lineStyle else ""
        json += "},"
        return json
