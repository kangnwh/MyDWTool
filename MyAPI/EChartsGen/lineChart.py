from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
from MyAPI.EChartsGen.options.Common.data import Data
from MyAPI.EChartsGen.options.Tooltip.tooltip import Tooltip
from MyAPI.EChartsGen.options.grid import Grid
from MyAPI.EChartsGen.options.Toolbox.toolbox import Toolbox #finishe
from MyAPI.EChartsGen.options.title import Title
from MyAPI.EChartsGen.options.Axis.xaxis import xAxis
from MyAPI.EChartsGen.options.Axis.yaxis import yAxis
from .options.Series.line import line_data

class LineChart(EchartBaseObject):
    def __init__(self, title, x_data, x_type="category", y_data=None):
        self.title = title
        self._tooltip = Tooltip(trigger="axis")
        self._grid = Grid()
        self.xAxis = (x_data,x_type)
        self.yAxis = y_data
        self._series = None
        self._toolbox = Toolbox()

    def appendDataByList(self,data,name="请在appendDataByList时指定名称"):
        s = line_data(name=name,value_list=data)
        self._series.append(s)

    def appendDataByLineSeries(self,s):
        self._series.append(s)

    @property
    def series(self):
        if self._series:
            return self._series
        else:
            raise Exception("使用appendDataByLineSeries(Series)或者appendDataByList(data_list,serie_name)添加series数据后才能生成json")

    @property
    def xAxis(self):
        return self._xAxis
    @xAxis.setter
    def xAxis(self,x_list):
        if x_list:
            if isinstance(x_list, xAxis):
                self._xAxis = x_list
            elif isinstance(x_list,tuple) and isinstance(x_list[0],Data):
                self._xAxis = xAxis(type=x_list[1], data=x_list[0])
            else:
                raise Exception("请使用x_data指定x轴:1. 使用（EChartsGen.options.Common.data.Data,list_type）or 2.使用EChartsGen.options.Axis.xaxis.xAxis类实例")
        else:
            raise Exception("请使用x_data指定x轴:1. 使用（EChartsGen.options.Common.data.Data,list_type）or 2.使用EChartsGen.options.Axis.xaxis.xAxis类实例")

    @property
    def yAxis(self):
        return self._yAxis

    @yAxis.setter
    def yAxis(self,value):
        if value:
            if isinstance(value, yAxis):
                self._yAxis = value
            else:
                raise Exception("yAxis类型不对")
        else:
            self._yAxis = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        if isinstance(value,Title):
            self._title = value
        elif isinstance(value,str):
            self._title = Title(text=value)
        else:
            raise Exception("Line Chart中Title值不合要求")

    def make_json(self):

        json = "option:{"
        json += "{_title}".format(_title=self._title) if self._title else ""
        json += "{_toolbox}".format(_toolbox=self._toolbox) if self._toolbox else ""
        json += "{_tooltip}".format(_tooltip=self._tooltip) if self._tooltip else ""
        json += "{_grid}".format(_grid=self._grid) if self._grid else ""
        json += "{_xAxis}".format(_xAxis=self.xAxis) if self.xAxis else ""
        json += "{_yAxis}".format(_yAxis=self.yAxis) if self.yAxis else ""
        json += "{_series}".format(_series=self.series) if self.series else ""

        json += "},"
        return json