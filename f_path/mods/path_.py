from pathlib import Path as Pathlib
from f_core import Globals as g
from f_path.mods.is_ import Is

class _Path(type):
    def __instancecheck__(cls, instance):
        return g.i.path(instance)

class Path(metaclass=_Path):
    def __new__(cls, path):
        instance = object.__new__(cls)
        instance._path = Pathlib(path).resolve()
        return instance

    Is  = Is
    is_ = Is
    i   = is_
