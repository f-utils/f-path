from f_path.mods.path_ import Path as Path_
from f_path.mods.func_ import *

class Path(Path_):
    exists   = exists
    basename = basename
    parent   = get_parent
    root     = get_root
    split    = split

    class File:
        read         = read
        read_binary  = read_binary
        write        = write
        write_binary = write_binary
        name         = filename
        extension    = extension

        r   = read
        rb  = read_binary
        w   = write
        wb  = write_binary
        n   = name
        ext = extension

        class Lines:
            list   = lines_list
            dict   = lines_dict
            count  = lines_count

        lines = Lines
        l     = lines

    class Dir:
        pass

    name = basename
    e    = exists
    file = File
    f    = file
    dir  = Dir
    d    = dir
