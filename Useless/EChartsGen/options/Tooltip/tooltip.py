from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject
from Useless.EChartsGen.options.Tooltip.axisPointer import AxisPointer
from Useless.EChartsGen.options.Common.textStyle import Color,TextStyle


class Tooltip(EchartBaseObject):
    def __init__(self, show = 'true',
                        showContent = 'true',
                        trigger = 'axis',
                        triggerOn = 'mousemove',
                        alwaysShowContent = 'false',
                        showDelay = 0,
                        hideDelay = 100,
                        enterable = 'true',
                        position = None,
                        transitionDuration = 0.4,
                        formatter = "{b}: {c}", #check http://echarts.baidu.com/option.html#tooltip.formatter for detail
                        backgroundColor = 'rgba(50,50,50,0.7)',
                        borderColor = Color('#333'),
                        borderWidth = 0,
                        padding = 5,
                        textStyle = TextStyle(),
                        extraCssText ='box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);',
                        axisPointer = AxisPointer()
                 ):
        self.show = show
        self.showContent = showContent
        self.trigger = trigger
        self.triggerOn = triggerOn
        self.alwaysShowContent = alwaysShowContent
        self.showDelay = showDelay
        self.hideDelay = hideDelay
        self.enterable = enterable
        self.position = position
        self.transitionDuration = transitionDuration
        self.formatter = formatter
        self.backgroundColor = backgroundColor
        self.borderColor = borderColor
        self.borderWidth = borderWidth
        self.padding = padding
        self.textStyle = textStyle
        self.extraCssText = extraCssText
        self.axisPointer = axisPointer


    def make_json(self):
        json = "tooltip:{"
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "showContent:{showContent},".format(showContent=self.showContent) if self.showContent else ""
        json += "trigger:'{trigger}',".format(trigger=self.trigger) if self.trigger else ""
        json += "triggerOn:'{triggerOn}',".format(triggerOn=self.triggerOn) if self.triggerOn else ""
        json += "alwaysShowContent:{alwaysShowContent},".format(alwaysShowContent=self.alwaysShowContent) if self.alwaysShowContent else ""
        json += "showDelay:{showDelay},".format(showDelay=self.showDelay) if self.showDelay else ""
        json += "hideDelay:{hideDelay},".format(hideDelay=self.hideDelay) if self.hideDelay else ""
        json += "enterable:{enterable},".format(enterable=self.enterable) if self.enterable else ""
        json += "position:{position},".format(position=self.position) if self.position else ""
        json += "transitionDuration:{transitionDuration},".format(transitionDuration=self.transitionDuration) if self.transitionDuration else ""
        json += "formatter:'{formatter}',".format(formatter=self.formatter) if self.formatter else ""
        json += "backgroundColor:'{backgroundColor}',".format(backgroundColor=self.backgroundColor) if self.backgroundColor else ""
        json += "borderColor:'{borderColor}',".format(borderColor=self.borderColor) if self.borderColor else ""
        json += "borderWidth:{borderWidth},".format(borderWidth=self.borderWidth) if self.borderWidth else ""
        json += "padding:{padding},".format(padding=self.padding) if self.padding else ""
        json += "{textStyle}".format(textStyle=self.textStyle) if self.textStyle else ""
        json += "extraCssText:'{extraCssText}',".format(extraCssText=self.extraCssText) if self.extraCssText else ""
        json += "{axisPointer}".format(axisPointer=self.axisPointer) if self.axisPointer else ""
        json += "},"
        return json