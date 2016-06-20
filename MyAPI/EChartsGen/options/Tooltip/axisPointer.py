from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
from MyAPI.EChartsGen.options.Tooltip.crossStyle import CrossStyle
from MyAPI.EChartsGen.options.Tooltip.shadowStyle import ShadowStyle
from MyAPI.EChartsGen.options.Common.lineStyle import LineStyle,Color


class AxisPointer(EchartBaseObject):
    type_list =('line','cross','shadow')
    def __init__(self, type = 'line',
                        axis = 'auto',
                        animation = 'true',
                        animationDuration = 1000,
                        animationEasing = 'cubicOut',
                        animationDelay = 0,
                        animationDurationUpdate = 300,
                        animationEasingUpdate = 'cubicOut',
                        animationDelayUpdate = 0,
                        lineStyle = LineStyle(color=Color('#555')),
                        crossStyle = CrossStyle(color=Color('#555')),
                        shadowStyle = ShadowStyle()
                 ):
        self.type = type
        self.axis = axis
        self.animation = animation
        self.animationDuration = animationDuration
        self.animationEasing = animationEasing
        self.animationDelay = animationDelay
        self.animationDurationUpdate = animationDurationUpdate
        self.animationEasingUpdate = animationEasingUpdate
        self.animationDelayUpdate = animationDelayUpdate
        self.lineStyle = lineStyle
        self.crossStyle = crossStyle
        self.shadowStyle = shadowStyle


    def make_json(self):
        json = "axisPointer:{"

        json += "type:'{type}',".format(type=self.type) if self.type else ""
        json += "axis:'{axis}',".format(axis=self.axis) if self.axis else ""
        json += "animation:{animation},".format(animation=self.animation) if self.animation else ""
        json += "animationDuration:{animationDuration},".format(animationDuration=self.animationDuration) if self.animationDuration else ""
        json += "animationEasing:'{animationEasing}',".format(animationEasing=self.animationEasing) if self.animationEasing else ""
        json += "animationDelay:{animationDelay},".format(animationDelay=self.animationDelay) if self.animationDelay else ""
        json += "animationDurationUpdate:{animationDurationUpdate},".format(animationDurationUpdate=self.animationDurationUpdate) if self.animationDurationUpdate else ""
        json += "animationEasingUpdate:'{animationEasingUpdate}',".format(animationEasingUpdate=self.animationEasingUpdate) if self.animationEasingUpdate else ""
        json += "animationDelayUpdate:{animationDelayUpdate},".format(animationDelayUpdate=self.animationDelayUpdate) if self.animationDelayUpdate else ""
        json += "{lineStyle}".format(lineStyle=self.lineStyle) if self.lineStyle else ""
        json += "{crossStyle}".format(crossStyle=self.crossStyle) if self.crossStyle else ""
        json += "{shadowStyle}".format(shadowStyle=self.shadowStyle) if self.shadowStyle else ""
        json += "},"

        return json

    def __repr__(self):
        return self.make_json()
