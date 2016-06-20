from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject


class DataZoomTitle(EchartBaseObject):
    def __init__(self, zoom="区域缩放",back="区域缩放还原"):
        self.zoom = zoom
        self.back = back

    def make_json(self):
        json="title:{"
        json+="zoom:'{zoom}',".format(zoom=self.zoom) if self.zoom else ""
        json+="back:'{back}',".format(back=self.back) if self.back else ""
        json+="},"
        return json

    def __repr__(self):
        return self.make_json()