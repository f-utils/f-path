from pathlib import Path as Pathlib
from f_core import Globals as g
from f_path.mods.helper_ import is_path, check_path

class Is:
    @staticmethod
    def file(path):
        check_path(path)
        return Pathlib(path).is_file()

    @staticmethod
    def dir(path):
        check_path(path)
        return Pathlib(path).is_dir()

    @staticmethod
    def symlink(path):
        check_path(path)
        return Pathlib(path).is_symlink()
    link = symlink

    @staticmethod
    def mountpoint(path):
        check_path(path)
        return Pathlib(path).is_mount()
    mount = mountpoint

    @staticmethod
    def absolute(path):
        check_path(path)
        return Pathlib(path).is_absolute()
    abs = absolute

    @staticmethod
    def relative(path):
        check_path(path)
        return not Pathlib(path).is_absolute()
    rel = relative

    @staticmethod
    def posix(path):
        check_path(path)
        return Pathlib(path).as_posix() == str(Pathlib(path))
    unix = posix

    @staticmethod
    def windows(path):
        check_path(path)
        return '\\' in str(Pathlib(path))

g.i.path = is_path
