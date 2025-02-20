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

def symbolic_to_octal(mode):
    permission_mapping = {'r': 4, 'w': 2, 'x': 1, '-': 0}
    splits = [mode[0:3], mode[3:6], mode[6:9]]
    octal_value = 0
    for i, part in enumerate(splits):
        part_value = sum(permission_mapping[ch] for ch in part)
        octal_value = (octal_value << 3) + part_value
    return octal_value
