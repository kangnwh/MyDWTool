from Useless.EChartsGen.options.Common.echartBase import EchartBaseObject
from Useless.EChartsGen.options.Toolbox.Feature.dataZoom import DataZoom
from .dataView import DataView
from .magicType import MagicType
from .restore import Restore
from .saveAsImage import SaveAsImage


class Feature(EchartBaseObject):
    def __init__(self, dataZoom=DataZoom(),
                        dataView=DataView(),
                        magicType=MagicType(),
                        restore=Restore(),
                        saveAsImage=SaveAsImage()
                 ):
        self.dataZoom = dataZoom
        self.dataView = dataView
        self.magicType = magicType
        self.restore = restore
        self.saveAsImage = saveAsImage


    def make_json(self):
        json="feature:{"
        json += "{dataZoom}".format(dataZoom=self.dataZoom) if self.dataZoom else ""
        json += "{dataView}".format(dataView=self.dataView) if self.dataView else ""
        json += "{magicType}".format(magicType=self.magicType) if self.magicType else ""
        json += "{restore}".format(restore=self.restore) if self.restore else ""
        json += "{saveAsImage}".format(saveAsImage=self.saveAsImage) if self.saveAsImage else ""

        json += "},"

        return json

    def __repr__(self):
        return self.make_json()