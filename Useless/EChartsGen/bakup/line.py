 # -*- coding: utf-8 -*-
from .baseType import baseType
import json

class line(baseType):
    def __init__(self,html_id=None):
        self.type = 'line'
        self.html_id = html_id

    def generate_cfg_json(self,
                          text='使用text=来设置title'
                          ):
        title={'text':text}
        tooltip={'trigger':'axis'}
        legend={'data':['收盘价']}
        toolbox={'show':'true',
                    'feature':
                    {
                        'mark':{'mark':'true'},
                        'dataZoom' : {'show': 'true'},
                        'dataView': {'show': 'true', 'readOnly': 'false'},
                        'magicType' : {'show': 'true', 'type': ['line', 'bar']},
                        'restore' : {'show': 'true'},
                        'saveAsImage' : {'show': 'true'}
                    }}
        dataZoom={'show': 'true','realtime' : 'true','start':80,'end':100}
        xAxis=[{
            'type':self.x.type,
            'data':self.x.data
            }]

        yAxis=[{
            'type':'value',
            'axisLabel':{'formatter':'{value}￥'}
        }]
        series=[
            {'name':self.y[0].name,
            'type':self.y[0].type,
            'data':self.y[0].data
            }
        ]
        d_json={
            'title':title,
            'tooltip':tooltip,
            'legend':legend,
            'toolbox':toolbox,
            'dataZoom':dataZoom,
            'xAxis':xAxis,
            'yAxis':yAxis,
            'Series':series
            }
        return json.dumps(d_json)
