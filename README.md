
```
  /$$$$$$      /$$ /$$ /$$      
 /$$__  $$    | $$|__/| $$      
| $$  \__/    | $$ /$$| $$$$$$$ 
| $$$$ /$$$$$$| $$| $$| $$__  $$
| $$_/|______/| $$| $$| $$  \ $$
| $$          | $$| $$| $$  | $$
| $$          | $$| $$| $$$$$$$/
|__/          |__/|__/|_______/

------------------------------------------
Replace the above with the name of the lib. Use figlet font 'bigmoney-ne'.
> https://patorjk.com/software/taag/#p=display&f=Big%20Money-ne&t=f-lib
Altenativelly, install 'figlet' and font 'bigmoney-ne':
> figlet: http://www.figlet.org/figlet-man.html
> font: https://github.com/xero/figlet-fonts/blob/master/Big%20Money-ne.flf 
------------------------------------------
```                       

# About

`f-{lib}` is the  `f-utils` lib that does something.
- website: [futils.org/libs/f-{lib}](https://futils.org/libs/f-{lib})
- contact: [futils@gmx.ie](mailto:futils@gmx.ie)
- discord: [coolab](https://discord.gg/waANUyCUGE)

# Structure

```
f_{lib}/
  |-- __init__.py .............. import main.py
  |-- main.py .................. import modules
  `-- mods/
       |-- module1.py .......... does something
       |-- module2.py .......... does some other thing
       `-- ... 
```

# Install

The installation is from the branches `main` and `dev` of this repository.

- With `pip`:
```bash
# main branch
/path/to/venv/bin/pip install git+https://github.com/f-utils/f-{lib}
# dev branch
/path/to/venv/bin/pip install git+https://github.com/f-utils/f-{lib}/tree/dev
```

For other installation methods, see [futils.org/install](https://futils.org/install).

# Usage

The lib provides the class `{Lib}`. We suggest to import it as:

```python
from f_{lib} import {Lib} as {lib}
```

For more details, see [futils.org/libs/f-{lib}](https://futils.org/libs/f-{lib}).

# Contributing

- Open issues in [f-utils/.issues](https://github.com/f-utils/.issues).
- Join our [Discord](https://discord.gg/waANUyCUGE) server.
- See [CONTRIBUTING](https://github.com/f-utils/.github/blob/main/CONTRIBUTING.md).

# License

This lib is [licensed](./LICENSE) under `BSD 3-Clause`.
