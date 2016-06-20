from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject


class Parallel(EchartBaseObject):
    def __init__(self, zlevel = 0,
                        z = 2,
                        left = 'auto',
                        top = 60,
                        right = 80,
                        bottom = 60,
                        width = 'auto',
                        height = 'auto',
                        layout = 'horizontal',
                        parallelAxisDefault =None):
        self.zlevel = zlevel
        self.z = z
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.width = width
        self.height = height
        self.layout = layout
        self.parallelAxisDefault = parallelAxisDefault


    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")