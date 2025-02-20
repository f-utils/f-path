from pathlib import Path as Pathlib
from f_path.mods.err_ import IsNotPath

def  is_path(x):
    if isinstance(x, str):
        try:
            Pathlib(x).resolve()
            return True
        except Exception:
            return False
    return isinstance(x, Pathlib)

def check_path(*args):
    for x in args:
        if not is_path(x):
            raise IsNotPath(f"'{x}' is not a path.")
