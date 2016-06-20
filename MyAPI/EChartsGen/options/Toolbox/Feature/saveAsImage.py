from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject


class SaveAsImage(EchartBaseObject):
    def __init__(self, type = 'png',
                        name = None,
                        backgroundColor = 'auto',
                        excludeComponents = ['toolbox'],
                        show = 'true',
                        title = '保存为图片',
                        icon = None,
                        iconStyle = None,
                        pixelRatio = 1):
        self.type = type
        self.name = name
        self.backgroundColor = backgroundColor
        self.excludeComponents = excludeComponents
        self.show = show
        self.title = title
        self.icon = icon
        self.iconStyle = iconStyle
        self.pixelRatio = pixelRatio


    def make_json(self):
        json = "saveAsImage:{"
        json += "type:'{type}',".format(type=self.type) if self.type else ""
        json += "name:'{name}',".format(name=self.name) if self.name else ""
        json += "backgroundColor:'{backgroundColor}',".format(backgroundColor=self.backgroundColor) if self.backgroundColor else ""
        json += "excludeComponents:{excludeComponents},".format(excludeComponents=self.excludeComponents) if self.excludeComponents else ""
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "title:'{title}',".format(title=self.title) if self.title else ""
        json += "icon:'{icon}',".format(icon=self.icon) if self.icon else ""
        json += "iconStyle:'{iconStyle}',".format(iconStyle=self.iconStyle) if self.iconStyle else ""
        json += "pixelRatio:'{pixelRatio}',".format(pixelRatio=self.pixelRatio) if self.pixelRatio else ""
        json += "},"
        return json

    def __repr__(self):
        return self.make_json()
