odML NIX merge
==============

Script for merging odML trees into existing or new NIX files.

For now simply prints the tree structure of the provided files. If calling the script from the command line, the first argument should be a NIX file and the second an odML file.

Requires [convert.py](https://github.com/G-Node/odml-to-nix/blob/master/convert.py) from [odml-to-nix](https://github.com/G-Node/odml-to-nix/) (included as submodule: clone with `git clone --recursive`). The function that does the actual conversion is from here.
