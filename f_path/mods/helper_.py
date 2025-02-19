from pathlib import Path as Pathlib

def  is_path(x):
    if isinstance(x, str):
        try:
            Pathlib(x).resolve()
            return True
        except Exception:
            return False
    return isinstance(x, Pathlib)
