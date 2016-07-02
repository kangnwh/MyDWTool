from Useless.EChartsGen.options.Common.color import EchartBaseObject,Color



class DataView(EchartBaseObject):
    def __init__(self, show = 'true',
                        title = '查看数据',
                        icon = None,
                        iconStyle = None,
                        readOnly = 'false',
                        optionToContent = None,
                        contentToOption = None,
                        lang = ['数据视图', '关闭', '刷新'],
                        backgroundColor = Color('#fff'),
                        textareaColor = Color('#fff'),
                        textareaBorderColor = Color('#333'),
                        textColor = Color('#000'),
                        buttonColor = Color('#c23531'),
                        buttonTextColor = Color('#fff')
                 ):
        self.show = show
        self.title = title
        self.icon = icon
        self.iconStyle = iconStyle
        self.readOnly = readOnly
        self.optionToContent = optionToContent
        self.contentToOption = contentToOption
        self.lang = lang
        self.backgroundColor = backgroundColor
        self.textareaColor = textareaColor
        self.textareaBorderColor = textareaBorderColor
        self.textColor = textColor
        self.buttonColor = buttonColor
        self.buttonTextColor = buttonTextColor


    def make_json(self):
        json = "dataView:{"
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "title:'{title}',".format(title=self.title) if self.title else ""
        json += "icon:'{icon}',".format(icon=self.icon) if self.icon else ""
        json += "iconStyle:'{iconStyle}',".format(iconStyle=self.iconStyle) if self.iconStyle else ""
        json += "readOnly:{readOnly},".format(readOnly=self.readOnly) if self.readOnly else ""
        json += "optionToContent:'{optionToContent}',".format(optionToContent=self.optionToContent) if self.optionToContent else ""
        json += "contentToOption:'{contentToOption}',".format(contentToOption=self.contentToOption) if self.contentToOption else ""
        json += "lang:{lang},".format(lang=self.lang) if self.lang else ""
        json += "backgroundColor:'{backgroundColor}',".format(backgroundColor=self.backgroundColor) if self.backgroundColor else ""
        json += "textareaColor:'{textareaColor}',".format(textareaColor=self.textareaColor) if self.textareaColor else ""
        json += "textareaBorderColor:'{textareaBorderColor}',".format(textareaBorderColor=self.textareaBorderColor) if self.textareaBorderColor else ""
        json += "textColor:'{textColor}',".format(textColor=self.textColor) if self.textColor else ""
        json += "buttonColor:'{buttonColor}',".format(buttonColor=self.buttonColor) if self.buttonColor else ""
        json += "buttonTextColor:'{buttonTextColor}',".format(buttonTextColor=self.buttonTextColor) if self.buttonTextColor else ""

        json += "},"
        return json

    def __repr__(self):
        return self.make_json()
