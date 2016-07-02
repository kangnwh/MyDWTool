from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject


class MagicType(EchartBaseObject):
    title = '''
            {
                line: '切换为折线图',
                bar: '切换为柱状图',
                stack: '切换为堆叠',
                tiled: '切换为平铺',
            }
    '''
    def __init__(self, show = 'true',
                        type = ["line",],
                        title = None,
                        icon = None,
                        iconStyle = None,
                        option = None,#TODO 不明白
                        seriesIndex = None):
        self.show = show
        self.type = type
        self.title = title if title else self.title
        self.icon = icon
        self.iconStyle = iconStyle
        self.option = option
        self.seriesIndex = seriesIndex


    def make_json(self):
        json = "magicType:{"
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "type:{type},".format(type=self.type) if self.type else ""
        json += "title:{title},".format(title=self.title) if self.title else ""
        json += "icon:'{icon}',".format(icon=self.icon) if self.icon else ""
        json += "iconStyle:'{iconStyle}',".format(iconStyle=self.iconStyle) if self.iconStyle else ""
        json += "option:'{option}',".format(option=self.option) if self.option else ""
        json += "seriesIndex:'{seriesIndex}',".format(seriesIndex=self.seriesIndex) if self.seriesIndex else ""
        json += "},"
        return json

    def __repr__(self):
        return self.make_json()
