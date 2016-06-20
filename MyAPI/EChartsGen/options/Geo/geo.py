from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
#TODO 优先级较低，暂时不实现

class Geo(EchartBaseObject):
    def __init__(self, show = True,
                        map = '',
                        roam = False,
                        center = [...],
                        zoom = 1,
                        scaleLimit = {...},
                        nameMap = {...},
                        selectedMode = False,
                        label = {...},
                        itemStyle = {...},
                        zlevel = 0,
                        z = 2,
                        left = 'auto',
                        top = 'auto',
                        right = 'auto',
                        bottom = 'auto',
                        regions = [{...}],
                        silent = False):
        pass

    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")