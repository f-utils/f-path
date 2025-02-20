from f_path.mods.path_ import Path as Path_
from f_path.mods.func_ import *
from f_path.mods.err_ import *

class Path(Path_):
    exists   = exists
    cwd      = cwd
    basename = basename
    parent   = get_parent
    root     = get_root
    split    = split
    join     = join
    copy     = copy
    move     = move
    remove   = remove
    touch    = make_file
    mkdir    = make_dir
    link     = make_link
    chmod    = chmod

    class File:
        read         = read
        read_binary  = read_binary
        write        = write
        write_binary = write_binary
        name         = filename
        extension    = extension
        make         = make_file

        r     = read
        rb    = read_binary
        w     = write
        wb    = write_binary
        n     = name
        ext   = extension
        mk    = make
        touch = mk
        new   = touch

        class Lines:
            list   = lines_list
            dict   = lines_dict
            count  = lines_count

        lines = Lines
        l     = lines

    class Dir:
        depth = depth
        name  = dirname
        make  = make_dir

        n  = name
        mk = make

        class Lister:
            all    = list_all
            files  = list_files
            dirs   = list_dirs
            mounts = list_mounts
            links  = list_links
            def __call__(self, dir, kind='all'):
                return _list(dir, kind)

        class Finder:
            any    = find_any
            files  = find_files
            dirs   = find_dirs
            links  = find_links
            mounts = find_mounts
            def __call__(self, dir, pattern='*', kind='any', mindepth=0, maxdepth=float('inf')):
                return find(dir, pattern, kind, mindepth, maxdepth)

        list = Lister
        ls   = list
        find = Finder

    class Err:
        IsNotPath     = IsNotPath
        IsNotFile     = IsNotFile
        IsNotDir      = IsNotDir
        IsNotSymlink  = IsNotSymlink
        IsNotAbsolute = IsNotAbsolute
        IsNotRelative = IsNotRelative
        IsNotMount    = IsNotMount
        IsNotPosix    = IsNotPosix
        IsNotWindows  = IsNotWindows
        NotExist      = NotExist
        AlreadyExist  = AlreadyExist

    e    = exists
    pwd  = cwd
    name = basename
    base = basename
    cp   = copy
    mv   = move
    rm   = remove
    mkf  = touch
    mkd  = mkdir
    ln   = link
    file = File
    f    = file
    dir  = Dir
    d    = dir
    err  = Err
