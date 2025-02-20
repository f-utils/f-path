from f import f
from f_core import t, o
from pathlib import Path as _Path
from f_path.mods.is_ import Is as i
from f_path.mods.helper_ import check_path
from os.path import splitext, splitdrive
from os.path import exists as _exists
from os import remove as _remove
from os import walk as _walk
from shutil import copy2, copytree, rmtree
from shutil import move as _move
from fnmatch import fnmatch
from f_path.mods.err_ import (
    IsNotFile,
    IsNotDir,
    NotExist
)

@t.TF
def exists(path: str) -> bool:
    check_path(path)
    return _exists(path)

@t.TF
def cwd() -> str:
    return str(_Path().cwd())

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
        raise IsNotFile(f"'{file}' is not an existing file.")

@t.TF
def read_binary(file: str) -> bytes:
    return read(file, 'bin')

@t.TF
def write(content: str, file: str, encoding: str ='utf-8', overwrite: bool = True) -> type(None):
    check_path(file)
    if i.file(file):
        if encoding == 'bin' or encoding == 'binary':
            with open(file, 'wb', encoding=encoding) as f:
                f.write(content)
        elif overwrite:
            with open(file, 'w', encoding=encoding) as f:
                f.write(content)
        else:
            with open(file, 'a', encoding=encoding) as f:
                f.write(content)
    else:
        raise IsNotFile(f"'{file}' is not an existing file.")

@t.TF
def write_binary(file: str) -> type(None):
    return write(file, 'bin')

@t.TF
def basename(path: str) -> str:
    check_path(path)
    return _Path(path).name

@t.TF
def dirname(dir: str) -> str:
    check_path(dir)
    if i.dir(dir):
        return basename(dir)
    else:
        raise IsNotDir(f"'{dir}' is not an existing directory.")

@t.TF
def filename(file: str) -> str:
    check_path(file)
    if i.file(file):
        name, _ = splitext(basename(file))
        return name
    else:
        raise IsNotFile(f"'{file}' is not an existing file.")

@t.TF
def extension(file: str) -> str:
    check_path(file)
    if i.file(file):
        _, ext = splitext(basename(file))
        return ext
    else:
        raise IsNotFile(f"'{file}' is not an existing file.")

@t.TF
def lines_list(file: str, encoding: str = 'utf-8') -> list:
    check_path(file)
    if i.file(file):
        return read(file, encoding).splitlines()
    else:
        raise IsNotFile(f"'{file}' is not an existing file.")

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
        raise IsNotFile(f"'{file}' is not an existing file.")

@t.TF
def lines_count(file: str, encoding: str = 'utf-8') -> int:
    check_path(file)
    if i.file(file):
        with open(file, 'r', encoding=encoding) as f:
            return sum(1 for _ in f)
    else:
        raise IsNotFile(f"'{file}' is not an existing file.")

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
        root, _ = splitdrive(_Path(path))
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
def copy(src: str, dst: str) -> type(None):
    check_path(src, dst)
    if not exists(src):
        raise NotExist(f"The source path '{src}'  does not exist.")
    if i.dir(src):
        copytree(src, dst)
    else:
        copy2(src, dst)

@t.TF
def move(src: str, dst: str) -> type(None):
    check_path(src, dst)
    if not exists(src):
        raise NotExist(f"The source path '{src}' does not exist.")
    _move(src, dst)

@t.TF
def remove(path: str) -> type(None):
    check_path(path)
    if not exists(path):
        raise NotExist(f"The path '{path}' does not exist.")
    if i.dir(path):
        rmtree(path)
    else:
        _remove(path)

@t.TF
def list_all(dir: str) -> list:
    check_path(dir)
    if i.dir(dir):
        return list(j for j in _Path(dir).iterdir())
    else:
        raise IsNotDir(f"'{dir}' is not a directory.")

@t.TF
def list_files(dir: str) -> list:
    check_path(dir)
    if i.dir(dir):
        return list(j for j in _Path(dir).iterdir() if i.file(j))
    else:
        raise IsNotDir(f"'{dir}' is not a directory.")

@t.TF
def list_dirs(dir: str) -> list:
    check_path(dir)
    if i.dir(dir):
        return list(j for j in _Path(dir).iterdir() if i.dir(j))
    else:
        raise IsNotDir(f"'{dir}' is not a directory.")

@t.TF
def list_links(dir: str) -> list:
    check_path(dir)
    if i.dir(dir):
        return list(j for j in _Path(dir).iterdir() if i.link(j))
    else:
        raise IsNotDir(f"'{dir}' is not a directory.")

@t.TF
def list_mounts(dir: str) -> list:
    check_path(dir)
    if i.dir(dir):
        return list(j for j in _Path(dir).iterdir() if i.mount(j))
    else:
        raise IsNotDir(f"'{dir}' is not a directory.")

@t.TF
def _list(dir: str, kind: str = 'all') -> list:
    if kind == 'all':
        return list_all(dir)
    elif kind == 'file' or kind == 'files' or kind == 'f':
        return list_files(dir)
    elif kind == 'dir' or kind == 'dirs' or kind == 'd':
        return list_dirs(dir)
    elif kind == 'link' or kind == 'links' or kind == 'l':
        return list_links(dir)
    elif kind == 'mount' or kind == 'mounts' or kind == 'm':
        return list_mounts(dir)
    else:
        raise ValueError('kind must be None, "file", "dir", "link", or "mount"')

@t.TF
def find(dir: str, pattern: str = '*', kind: str = 'any', mindepth: int = 0, maxdepth: float = float('inf')) -> list:
    check_path(dir)
    if i.dir(dir):
        _dir = _Path(dir)
        matches = []
        for root, dirs, files in _walk(dir):
            current_depth = _Path(root).relative_to(_dir).parts.__len__()
            if current_depth < mindepth:
                continue
            if current_depth > maxdepth:
                dirs[:] = []
                continue
            entries = []
            if kind in ['any', 'Any', 'a', 'file', 'files', 'f']:
                entries.extend((root, f) for f in files)
            if kind in ['any', 'Any', 'dir', 'dirs', 'd']:
                entries.extend((root, d) for d in dirs)

            for root, name in entries:
                entry_path = _Path(root) / name
                if fnmatch(name, pattern) and \
                   (((kind == 'file' or kind == 'files' or kind == 'f') and i.file(entry_path)) or
                    ((kind == 'dir' or kind == 'dirs' or kind == 'd') and i.dir(entry_path)) or
                    ((kind == 'link' or kind == 'links' or kind == 'l') and i.link(entry_path)) or
                    ((kind == 'mount' or kind == 'mounts' or kind == 'm') and i.mount(entry_path)) or
                    (kind == 'any' or kind == 'Any' or kind == 'a')):
                    matches.append(str(entry_path))
        return matches
    else:
        raise IsNotDir(f"'{dir}' is not an existing directory")

@t.TF
def find_any(dir: str, pattern: str = '*', mindepth: int = 0, maxdepth: float = float('inf')) -> list:
    return find(dir, pattern=pattern, mindepth=mindepth, maxdepth=maxdepth, kind='any')

@t.TF
def find_files(dir: str, pattern: str = '*', mindepth: int = 0, maxdepth: float = float('inf')) -> list:
    return find(dir, pattern=pattern, mindepth=mindepth, maxdepth=maxdepth, kind='file')

@t.TF
def find_dirs(dir: str, pattern: str = '*', mindepth: int = 0, maxdepth: float = float('inf')) -> list:
    return find(dir, pattern=pattern, mindepth=mindepth, maxdepth=maxdepth, kind='dir')

@t.TF
def find_links(dir: str, pattern: str = '*', mindepth: int = 0, maxdepth: float = float('inf')) -> list:
    return find(dir, pattern=pattern, mindepth=mindepth, maxdepth=maxdepth, kind='link')

@t.TF
def find_mounts(dir: str, pattern: str = '*', mindepth: int = 0, maxdepth: float = float('inf')) -> list:
    return find(dir, pattern=pattern, mindepth=mindepth, maxdepth=maxdepth, kind='mount')

@t.TF
def depth(dir: str) -> int:
    check_path(dir)
    if i.dir(dir):
        def max_depth(path, current_depth):
            subdirs = list_dirs(str(path))
            if not subdirs:
                return current_depth
            return max(max_depth(subdir, current_depth + 1) for subdir in subdirs)
        return max_depth(_Path(dir), 0)
    else:
        raise IsNotDir(f"'{dir}' is not an existing directory.")

