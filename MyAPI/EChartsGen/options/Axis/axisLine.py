from MyAPI.EChartsGen.options.Common.lineStyle import LineStyle
from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject

class AxisLine(EchartBaseObject):
    def __init__(self,
                    show= 'true',
                    onZero= None,
                    lineStyle=LineStyle()
                 ):
        self.show	=	show                #是否显示，默认为true，设为false后下面都没意义了
        self.onZero	=	onZero              #定位到垂直方向的0值坐标上
        self.lineStyle	=	lineStyle       #属性lineStyle控制线条样式，（详见http://echarts.baidu.com/echarts2/doc/doc.html#LineStyle）
    def make_json(self):
        json = "axisLine:{"
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "onZero:{onZero},".format(onZero=self.onZero) if self.onZero else ""
        json += "{lineStyle}".format(lineStyle=self.lineStyle) if self.lineStyle else ""
        json += "},"
        return json
