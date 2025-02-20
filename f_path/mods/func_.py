from f import f
from f_core import t, o
from pathlib import Path as _Path
from f_path.mods.is_ import Is as i
from f_path.mods.helper_ import check_path
from os.path import splitext, splitdrive
from os.path import exists as _exists
from shutil import copy2, copytree

@t.TF
def exists(path: str) -> bool:
    check_path(path)
    return _exists(path)

@t.TF
def read(file: str, encoding: str = 'utf-8') -> [str, bytes]:
    check_path(file)
    if i.file(file):
        if encoding == 'bin' or encoding == 'binary':
            with open(file, 'rb') as f:
                content = f.read()
            return content
        else:
            with open(file, 'r', encoding=encoding) as f:
                content = f.read()
            return content
    else:
        raise AttributeError(f"'{file}' is not an existing file.")

@t.TF
def read_binary(file: str) -> bytes:
    return read(file, 'bin')

@t.TF
def write(content: str, file: str, encoding: str ='utf-8', overwrite: bool = True) -> type(None):
    check_path(file)
    if encoding == 'bin' or encoding == 'binary':
        with open(file, 'wb', encoding=encoding) as f:
            f.write(content)
    elif overwrite:
        with open(file, 'w', encoding=encoding) as f:
            f.write(content)
    else:
        with open(file, 'a', encoding=encoding) as f:
            f.write(content)

@t.TF
def write_binary(file: str) -> type(None):
    return write(file, 'bin')

@t.TF
def basename(path: str) -> str:
    check_path(path)
    return _Path(path).name

@t.TF
def filename(file: str) -> str:
    check_path(file)
    name, _ = os.path.splitext(bn(x))
    return name

@t.TF
def extension(file: str) -> str:
    check_path(file)
    _, ext = os.path.splitext(bn(x))
    return ext

@t.TF
def lines_list(file: str, encoding: str = 'utf-8') -> list:
    check_path(file)
    if i.file(file):
        return read(file, encoding).splitlines()
    else:
        raise AttributeError(f"'{file}' is not an existing file.")

@t.TF
def lines_dict(file: str, encoding: str = 'utf-8') -> dict:
    check_path(file)
    if i.file(file):
        lines_dict = {}
        with open(file, 'r', encoding=encoding) as f:
            for line_number, line_content in enumerate(f, start=1):
                lines_dict[line_number] = line_content.rstrip('\n')
        return lines_dict
    else:
        raise AttributeError(f"'{file}' is not an existing file.")

@t.TF
def lines_count(file: str, encoding: str = 'utf-8') -> int:
    check_path(file)
    with open(file, 'r', encoding=encoding) as f:
        return sum(1 for _ in f)

@t.TF
def get_parent(path: str, N: int = 1) -> str:
    check_path(path)
    for _ in range(N):
        path = str(_Path(path).parent)
    return path

@t.TF
def get_root(path: str) -> str:
    check_path(path)
    if i.windows(path):
        root, _ = os.path.splitdrive(_Path(path))
        return root
    else:
        parts = _Path(path).parts
        if len(parts) > 1:
            return f"/{parts[1]}"
        return '/'

@t.TF
def split(path: str) -> list:
    check_path(path)
    return list(_Path(path).parts)

@t.TF
def join(*paths: str) -> str:
    check_path(*paths)
    return str(_Path(*paths))

@t.TF
def here(path: str) -> str:
    check_path(path)
    return str(_Path(join(get_parent(__file__), path)).resolve())

@t.TF
def copy_file(file: str, path: str) -> type(None):
    check_path(file, path)
    if i.file(file):
        if i.dir(path):
            file_name = basename(file)
            shutil.copy2(file, join(path, file_name))
        else:
            shutil.copy2(file, path)
    else:
        raise FileExistsError(f"The file '{input_path}' does not exists.")
