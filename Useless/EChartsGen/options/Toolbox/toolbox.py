from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject
from .Feature.feature import Feature


class Toolbox(EchartBaseObject):
    def __init__(self, show = 'true',
                        orient = 'horizontal',
                        itemSize = 15,
                        itemGap = 10,
                        showTitle = 'true',
                        feature = Feature(),
                        iconStyle =None,
                        zlevel = 0,
                        z = 2,
                        left = 'auto',
                        top = 'auto',
                        right = 'auto',
                        bottom = 'auto',
                        width = 'auto',
                        height = 'auto'):
        self.show = show
        self.orient = orient
        self.itemSize = itemSize
        self.itemGap = itemGap
        self.showTitle = showTitle
        self.feature = feature
        self.iconStyle = iconStyle
        self.zlevel = zlevel
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.width = width
        self.height = height


    def make_json(self):
        json = "toolbox:{"
        json += "show:{show},".format(show=self.show) if self.show else ""
        json += "orient:'{orient}',".format(orient=self.orient) if self.orient else ""
        json += "itemSize:{itemSize},".format(itemSize=self.itemSize) if self.itemSize else ""
        json += "itemGap:{itemGap},".format(itemGap=self.itemGap) if self.itemGap else ""
        json += "showTitle:{showTitle},".format(showTitle=self.showTitle) if self.showTitle else ""
        json += "{feature}".format(feature=self.feature) if self.feature else ""
        json += "iconStyle:{iconStyle},".format(iconStyle=self.iconStyle) if self.iconStyle else ""
        json += "zlevel:{zlevel},".format(zlevel=self.zlevel) if self.zlevel else ""
        json += "z:{z},".format(z=self.z) if self.z else ""
        json += "left:'{left}',".format(left=self.left) if self.left else ""
        json += "top:'{top}',".format(top=self.top) if self.top else ""
        json += "right:'{right}',".format(right=self.right) if self.right else ""
        json += "bottom:'{bottom}',".format(bottom=self.bottom) if self.bottom else ""
        json += "width:'{width}',".format(width=self.width) if self.width else ""
        json += "height:'{height}',".format(height=self.height) if self.height else ""
        json += "},"
        return json