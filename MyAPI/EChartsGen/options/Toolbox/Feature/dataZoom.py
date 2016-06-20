from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
from MyAPI.EChartsGen.options.DataZoom.dataZoomTitle import DataZoomTitle


class DataZoom(EchartBaseObject):
    def __init__(self, show = True,
                 title = DataZoomTitle(),
                 icon = None,
                 iconStyle = None,
                 xAxisIndex = None,
                 yAxisIndex = None):
        self.show = show
        self.title = title
        self.icon = icon
        self.iconStyle = iconStyle
        self.xAxisIndex = xAxisIndex
        self.yAxisIndex = yAxisIndex


    def make_json(self):
        json = "dataZoom:{"
        json += "show:true," if self.show else ""
        json += "{title}".format(title=self.title) if self.title else ""
        json += "icon:{icon},".format(icon=self.icon) if self.icon else ""
        json += "iconStyle:{iconStyle},".format(iconStyle=self.iconStyle) if self.iconStyle else ""
        json += "xAxisIndex:{xAxisIndex},".format(xAxisIndex=self.xAxisIndex) if self.xAxisIndex else ""
        json += "yAxisIndex:{yAxisIndex},".format(yAxisIndex=self.yAxisIndex) if self.yAxisIndex else ""
        json += "},"
        return json

    def __repr__(self):
        return self.make_json()
