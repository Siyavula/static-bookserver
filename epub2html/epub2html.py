import sys
import os
import zipfile

from lxml import etree

try:
    import docopt
except ImportError:
    print("Could not find docopt, please install using: sudo easy-install docopt")
    sys.exit(1)


__tempfolder = "_temp"

def unzip_epub_into_temp(source_filename, dest_dir=__tempfolder):
    """ Extract the epub contents into a temporary folder
    """
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)


def clean_temp_folder():
    import shutil

    shutil.rmtree(__tempfolder)


if __name__ == "__main__":
    args = sys.argv

    print(args)

    unzip_epub_into_temp(args[1])
    clean_temp_folder()
