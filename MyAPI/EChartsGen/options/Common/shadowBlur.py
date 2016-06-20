from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject

class ShadowBlur(EchartBaseObject):
    def __init__(self,
                 shadowColor= 'rgba(0, 0, 0, 0.5)',
                 shadowBlur= 10):
        self.shadowColor= shadowColor
        self.shadowBlur= shadowBlur


    def make_json(self):
        json = "shadowBlur:{"
        json += "shadowColor:'{shadowColor}',".format(shadowColor=self.shadowColor) if self.shadowColor else ""
        json += "shadowBlur:{shadowBlur},".format(shadowBlur=self.shadowBlur) if self.shadowBlur else ""
        json += "},"

        return json

    def __repr__(self):
        return self.make_json()
