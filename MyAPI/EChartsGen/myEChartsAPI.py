 # -*- coding: utf-8 -*-
from MyAPI.EChartsGen.options.Common import echartBase as EchartBaseObject


class MyEChartsAPI:
    def __init__(self,
                 #echart_path= "http://echarts.baidu.com/build/dist",
                 echart_src= "http://echarts.baidu.com/build/dist/echarts.js",
                 seriesColorList=None,
                 backgroundColor=None,
                 animation=True,
                 animationDuration = 1000,
                 animationEasing = 'cubicOut',
                 animationDelay = 0,
                 animationDurationUpdate = 300,
                 animationEasingUpdate = 'cubicOut',
                 animationDelayUpdate = 0):
        #self.echart_path = echart_path
        self.echart_src = echart_src
        self._echart_list=list()
        self._seriesColorList = seriesColorList
        self._backgroundColor = backgroundColor
        self._animationDuration = animationDuration
        self._animationEasing = animationEasing
        self._animationDelay = animationDelay
        self._animationDurationUpdate = animationDurationUpdate
        self._animationEasingUpdate = animationEasingUpdate
        self._animationDelayUpdate = animationDelayUpdate

    @property
    def echart_src(self):
        return self._echart_src

    @echart_src.setter
    def echart_src(self,value):
        self._echart_src = value

    @property
    def echart_path(self):
        return self._echart_path

    @echart_path.setter
    def echart_path(self,value):
        self._echart_path = value

    @property
    def echart_list(self):
        return self._echart_list

    def append_echart(self,value):
        if isinstance(value,EchartBaseObject):
            self._echart_list.append(value)
        else:
            raise Exception("添加的echart不是合适的EChart类型")

    def __get_required_items(self):
        if self.echart_list.__len__() == 0:
            raise Exception("No EChart instance inserted !")
        require_items = "'echarts'"
        unique = set(x.type for x in self.echart_list)
        for item in unique:
            require_items += ",'echarts/chart/{type}'".format(type=item)
        return require_items

    def __get_options_set_scripts(self):
        scripts=""
        for chart in self.echart_list:
            scripts += "ec.init(document.getElementById('{html_id}')).setOption({json_data}); ".format(html_id=chart.html_id,json_data = chart.make_json())
        return scripts

    def make_js(self):
        whole_scripts = """
    <script src="%s"></script>
    <script type="text/javascript">
        %s
    </script>""" % (self.echart_src,self.__get_options_set_scripts())
        return whole_scripts