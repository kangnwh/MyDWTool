from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject
from Useless.EChartsGen.options.Common.lineStyle import LineStyle,Color
from Useless.EChartsGen.options.Common.areaStyle import AreaStyle
from .itemStyle import ItemStyle
from .label import Label


class line_series(EchartBaseObject):
    type = 'line'
    def __init__(self, data,name = "使用line_series进行自定义",
                        coordinateSystem = 'cartesian2d',
                        xAxisIndex = 0,
                        yAxisIndex = 0,
                        polarIndex = 0,
                        symbol = 'emptyCircle',
                        symbolSize = 4,
                        symbolRotate = None,
                        symbolOffset = [0, 0],
                        showSymbol = 'true',
                        showAllSymbol = 'false',
                        hoverAnimation = 'true',
                        legendHoverLink = 'true',
                        stack = None,
                        connectNulls = 'false',
                        clipOverflow = 'true',
                        label = Label(),
                        itemStyle = ItemStyle(),
                        lineStyle = LineStyle(color=Color("#000"),width=0),
                        areaStyle = AreaStyle(color=Color("#000")),
                        smooth = 'false',
                        smoothMonotone = "x",
                        sampling = None,
                        markPoint = None,
                        markLine = None,
                        zlevel = 0,
                        z = 2,
                        silent = 'false',
                        animation = 'true',
                        animationDuration = 1000,
                        animationEasing = 'linear',
                        animationDelay = 0,
                        animationDurationUpdate = 300,
                        animationEasingUpdate = 'cubicOut',
                        animationDelayUpdate = 0):
        self.data = data
        self.name = name
        self.coordinateSystem = coordinateSystem
        self.xAxisIndex = xAxisIndex
        self.yAxisIndex = yAxisIndex
        self.polarIndex = polarIndex
        self.symbol = symbol
        self.symbolSize = symbolSize
        self.symbolRotate = symbolRotate
        self.symbolOffset = symbolOffset
        self.showSymbol = showSymbol
        self.showAllSymbol = showAllSymbol
        self.hoverAnimation = hoverAnimation
        self.legendHoverLink = legendHoverLink
        self.stack = stack
        self.connectNulls = connectNulls
        self.clipOverflow = clipOverflow
        self.label = label
        self.itemStyle = itemStyle
        self.lineStyle = lineStyle
        self.areaStyle = areaStyle
        self.smooth = smooth
        self.smoothMonotone = smoothMonotone
        self.sampling = sampling
        self.markPoint = markPoint
        self.markLine = markLine
        self.zlevel = zlevel
        self.z = z
        self.silent = silent
        self.animation = animation
        self.animationDuration = animationDuration
        self.animationEasing = animationEasing
        self.animationDelay = animationDelay
        self.animationDurationUpdate = animationDurationUpdate
        self.animationEasingUpdate = animationEasingUpdate
        self.animationDelayUpdate = animationDelayUpdate


    def make_json(self):
        json = "{type:'line',"

        json += "name:'{name}',".format(name=self.name) if self.name else ""
        json += "coordinateSystem:'{coordinateSystem}',".format(coordinateSystem=self.coordinateSystem) if self.coordinateSystem else ""
        json += "xAxisIndex:{xAxisIndex},".format(xAxisIndex=self.xAxisIndex) if self.xAxisIndex else ""
        json += "yAxisIndex:{yAxisIndex},".format(yAxisIndex=self.yAxisIndex) if self.yAxisIndex else ""
        json += "polarIndex:{polarIndex},".format(polarIndex=self.polarIndex) if self.polarIndex else ""
        json += "symbol:'{symbol}',".format(symbol=self.symbol) if self.symbol else ""
        json += "symbolSize:{symbolSize},".format(symbolSize=self.symbolSize) if self.symbolSize else ""
        json += "symbolRotate:'{symbolRotate}',".format(symbolRotate=self.symbolRotate) if self.symbolRotate else ""
        json += "symbolOffset:{symbolOffset},".format(symbolOffset=self.symbolOffset) if self.symbolOffset else ""
        json += "showSymbol:{showSymbol},".format(showSymbol=self.showSymbol) if self.showSymbol else ""
        json += "showAllSymbol:{showAllSymbol},".format(showAllSymbol=self.showAllSymbol) if self.showAllSymbol else ""
        json += "hoverAnimation:{hoverAnimation},".format(hoverAnimation=self.hoverAnimation) if self.hoverAnimation else ""
        json += "legendHoverLink:{legendHoverLink},".format(legendHoverLink=self.legendHoverLink) if self.legendHoverLink else ""
        json += "stack:{stack},".format(stack=self.stack) if self.stack else ""
        json += "connectNulls:{connectNulls},".format(connectNulls=self.connectNulls) if self.connectNulls else ""
        json += "clipOverflow:{clipOverflow},".format(clipOverflow=self.clipOverflow) if self.clipOverflow else ""
        json += "{label}".format(label=self.label) if self.label else ""
        json += "{itemStyle}".format(itemStyle=self.itemStyle) if self.itemStyle else ""
        json += "{lineStyle}".format(lineStyle=self.lineStyle) if self.lineStyle else ""
        json += "{areaStyle}".format(areaStyle=self.areaStyle) if self.areaStyle else ""
        json += "smooth:{smooth},".format(smooth=self.smooth) if self.smooth else ""
        json += "smoothMonotone:'{smoothMonotone}',".format(smoothMonotone=self.smoothMonotone) if self.smoothMonotone else ""
        json += "sampling:'{sampling}',".format(sampling=self.sampling) if self.sampling else ""
        json += "{markPoint}".format(markPoint=self.markPoint) if self.markPoint else ""
        json += "{markLine}".format(markLine=self.markLine) if self.markLine else ""
        json += "zlevel:{zlevel},".format(zlevel=self.zlevel) if self.zlevel else ""
        json += "z:{z},".format(z=self.z) if self.z else ""
        json += "silent:{silent},".format(silent=self.silent) if self.silent else ""
        json += "animation:{animation},".format(animation=self.animation) if self.animation else ""
        json += "animationDuration:{animationDuration},".format(animationDuration=self.animationDuration) if self.animationDuration else ""
        json += "animationEasing:'{animationEasing}',".format(animationEasing=self.animationEasing) if self.animationEasing else ""
        json += "animationDelay:{animationDelay},".format(animationDelay=self.animationDelay) if self.animationDelay else ""
        json += "animationDurationUpdate:{animationDurationUpdate},".format(animationDurationUpdate=self.animationDurationUpdate) if self.animationDurationUpdate else ""
        json += "animationEasingUpdate:'{animationEasingUpdate}',".format(animationEasingUpdate=self.animationEasingUpdate) if self.animationEasingUpdate else ""
        json += "animationDelayUpdate:{animationDelayUpdate},".format(animationDelayUpdate=self.animationDelayUpdate) if self.animationDelayUpdate else ""
        json += "{data}".format(data=self.data) if self.data else ""

        json += "},"
        return json
