from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject
from Useless.EChartsGen.options.Common.lineStyle import LineStyle

class SplitLine(EchartBaseObject):
    def __init__(self, show = 'true',
                        interval = 'auto',
                        lineStyle = LineStyle()):
        self.show = show
        self.interval = interval
        self.lineStyle = lineStyle


    def make_json(self):
        json = "splitLine:{"
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "interval:'{interval}',".format(interval=self.interval) if self.interval else ""
        json += "{lineStyle}".format(lineStyle=self.lineStyle) if self.lineStyle else ""
        json += "},"
        return json
