import gc
import random


class eva:
    ...


class qtype(type):
    ...


def _void(*li, **d):
    ...


def _继承法添加(cls, f):
    class qqtype(qtype):
        def __del__(self):
            self.__del__ = _void
            f(self)
    base = cls.__bases__
    if base == (object,):
        base = eva,
    return qqtype(cls.__name__, base, dict(cls.__dict__))


def _均分(继承人, 资源):
    n = len(继承人)
    kv = [(k, v) for k, v in 资源.items() if not k.startswith('_')]
    for i, (k, v) in enumerate(kv):
        setattr(继承人[i % n], k, v)


def _亲戚(x):
    v = set()

    def 敌法师(x):
        if x in v or x is eva:
            return
        v.add(x)
        for i in [*x.__bases__, *x.__subclasses__()]:
            敌法师(i)
    敌法师(x)
    v.remove(x)
    return [i for i in v if not (isinstance(x, qtype) and '__del__' in i.__dict__ and i.__del__ is _void)]


def 长子继承制(x):
    def f(x):
        sub = x.__subclasses__()
        if sub:
            继承人 = [sub[0]]
        else:
            继承人 = [x.__bases__[0]]
        _均分(继承人, x.__dict__)
    return _继承法添加(x, f)


def 分割继承制(x):
    def f(x):
        sub = x.__subclasses__()
        if sub:
            继承人 = sub
        else:
            继承人 = [x.__bases__[0]]
        _均分(继承人, x.__dict__)
    return _继承法添加(x, f)


def 斯堪的纳维亚选举制(x):
    def 喜爱度(a, b):
        return sum([int(i in b.__name__) for i in a.__name__]) + random.random()/10

    def f(x):
        票数 = {x: 0 for x in _亲戚(x)}
        if not 票数:
            _均分([x.__bases__[0]], x.__dict__)
            return
        for i in gc.get_objects():
            if isinstance(i, type):
                投给 = max(票数, key=lambda x: 喜爱度(i, x))
                # print(f'{i.__name__} 投给 {投给.__name__}')
                票数[投给] += 1
        继承人 = [max(票数, key=lambda k: 票数[k])]
        for k, v in 票数.items():
            print(f'{k.__name__}: {v}票')
        _均分(继承人, x.__dict__)
    return _继承法添加(x, f)
