from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject


class Restore(EchartBaseObject):
    def __init__(self, show = 'true',
                        title = '还原',
                        icon = None,
                        iconStyle = None):
        self.show = show
        self.title = title
        self.icon = icon
        self.iconStyle = iconStyle


    def make_json(self):
        json = "restore:{"
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "title:'{title}',".format(title=self.title) if self.title else ""
        json += "icon:'{icon}',".format(icon=self.icon) if self.icon else ""
        json += "iconStyle:'{iconStyle}',".format(iconStyle=self.iconStyle) if self.iconStyle else ""
        json += "},"
        return json

    def __repr__(self):
        return self.make_json()
