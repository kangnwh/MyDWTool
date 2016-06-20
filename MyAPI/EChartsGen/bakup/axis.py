
class axis():
    def __init__(self,
                type = None        ,#坐标轴类型，横轴默认为类目型'category'，纵轴默认为数值型'value.可选'category' | 'value' | 'time' | 'log'
                show = None        ,#显示策略，可选为：true（显示） | false（隐藏）
                z = None           ,#二级层叠控制，同一个canvas（相同zlevel）上z越高约靠顶层。
                position = None    ,#坐标轴类型，横轴默认为类目型'bottom'，纵轴默认为数值型'left'，可选为：'bottom' | 'top' | 'left' | 'right'
                name = None        ,#坐标轴名称，默认为空
                nameLocation = None,#坐标轴名称位置，默认为'end'，可选为：'start' | 'end'
                boundaryGap = True ,#类目起始和结束两端空白策略，见下图，默认为true留空，false则顶头
                min = None         ,#指定的最小值，eg: 0，默认无，会自动根据具体数值调整，指定后将忽略boundaryGap[0]
                max = None         ,#指定的最大值，eg: 100，默认无，会自动根据具体数值调整，指定后将忽略boundaryGap[1]
                scale = False      ,#脱离0值比例，放大聚焦到最终_min，_max区间
                splitNumber = None ,#分割段数，不指定时根据min、max算法调整
                logLabelBase = None,#axis.type === 'log'时生效。指定时，axisLabel显示为指数形式，如指定为4时，axisLabel可显示为4²、4³。不指定时，显示为普通形式，如 1,000,000
                logPositive = None ,#axis.type === 'log'时生效。指明是否使用反向log数轴（从而支持value为负值）。默认自适应，即如果value全为负值，则logPositive自动设为false，否则为true。
                axisLine = None    ,#坐标轴线，默认显示
         ):
        _type =type
        _show =show
        _z =z
        _position =position
        _name =name
        _nameLocation =nameLocation
        _boundaryGap =boundaryGap
        _min =min
        _max =max
        _scale =scale
        _splitNumber =splitNumber
        _logLabelBase =logLabelBase
        _logPositive =logPositive
        _axisLine =axisLine





class axisTick:
    _show = True

    pass