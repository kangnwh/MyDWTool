from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
from MyAPI.EChartsGen.options.Common.areaStyle import AreaStyle

class SplitArea(EchartBaseObject):
    def __init__(self, interval = 'auto',
                        show = 'true',
                        areaStyle = AreaStyle()):
        self.interval = interval
        self.show = show
        self.areaStyle = areaStyle


    def make_json(self):
        json = "splitArea:{"
        json += "interval:'{interval}',".format(interval=self.interval) if self.interval else ""
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "{areaStyle}".format(areaStyle=self.areaStyle) if self.areaStyle else ""
        json += "},"
        return json
