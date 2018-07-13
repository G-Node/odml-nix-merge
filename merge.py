import sys
from convert import write_recurse
import nixio as nix
import odml
import neo


def printdepth(stuff, depth=0):
    print("\t"*depth, end="")
    print(stuff)


def print_nix_data(nf):
    for bl in nf.blocks:
        printdepth(bl.name)
        for grp in bl.groups:
            printdepth(grp.name, 1)
            for da in grp.data_arrays:
                printdepth(da.name, 2)
            for mt in grp.multi_tags:
                printdepth(mt.name, 2)


def print_md(p, depth=0):
    for sec in p.sections:
        printdepth(sec.name, depth)
        print_md(sec, depth+1)


def print_nix(nixfname):
    nf = nix.File(nixfname, mode=nix.FileMode.ReadOnly)
    print("::   DATA   ::")
    print_nix_data(nf)
    print(":: METADATA ::")
    print_md(nf)
    nf.close()


def print_odml(odmlfname):
    md = odml.load(odmlfname)
    print("::   ODML   ::")
    print_md(md)


def do_merge(nixfname, odmlfname):
    nf = nix.File(nixfname, mode=nix.FileMode.ReadWrite)
    md = odml.load(odmlfname)
    odmlnixsec = nf.create_section(odmlfname, "odML import")
    write_recurse(md.sections, odmlnixsec)
    nf.close()


def print_neo(nixfname):
    with neo.NixIO(nixfname) as io:
        neoblocks = io.read_all_blocks()

    for blk in neoblocks:
        printdepth(blk.annotations)
        for seg in blk.segments:
            printdepth(seg.annotations, 1)
            for child in seg.children:
                printdepth(child.annotations, 2)
        for chx in blk.channel_indexes:
            printdepth(chx.annotations, 1)
            for child in chx.children:
                printdepth(child.annotations, 2)


def main():
    nixfname = sys.argv[1]
    odmlfname = sys.argv[2]
    print_nix(nixfname)
    print_odml(odmlfname)
    print_neo(nixfname)


if __name__ == "__main__":
    main()
