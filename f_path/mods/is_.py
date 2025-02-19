from pathlib import Path as Pathlib
from f_core import Globals as g
from f_path.mods.helper_ import is_path

class Is:
    @staticmethod
    def file(path):
        return Pathlib(path).is_file()

    @staticmethod
    def dir(path):
        return Pathlib(path).is_dir()

    @staticmethod
    def abs(path):
        return Pathlib(path).is_absolute()

    @staticmethod
    def rel(path):
        return not Pathlib(path).is_absolute()

    @staticmethod
    def posix(path):
        return Pathlib(path).as_posix() == str(Pathlib(path))

    @staticmethod
    def windows(path):
        return '\\' in str(Pathlib(path))

g.i.path = is_path
