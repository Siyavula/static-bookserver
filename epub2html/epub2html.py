import sys
import os
import zipfile
import shutil

from lxml import etree
try:
    import docopt
except ImportError:
    print("Could not find docopt, please install using: sudo easy-install docopt")
    sys.exit(1)

import settings


class EpubReader:
    def __init__(self):
        ''' Class to parse and convert epub into set of static web pages.
        '''
        self.settings = settings.settings
        self._tempfolder = settings.settings["tempfolder"] 
        self._sitefolder = settings.settings["sitefolder"] 

        return None


    def readEpub(self, epub):
        ''' Open epub and write it to a folder where it will be served statically.
        Output folder is specified in settings.py
        '''

        self.unzip_epub_into_temp(epub)

        return None


    def unzip_epub_into_temp(self, source_filename, dest_dir=None):
        ''' Extract the epub contents into a temporary folder
        '''
        if dest_dir is None:
            dest_dir = self._tempfolder

        with zipfile.ZipFile(source_filename) as zf:
            zf.extractall(dest_dir)

        return None


    def clean_temp_folder(self):
        ''' Clean up the temp folder
        '''
        shutil.rmtree(self._tempfolder)

        return None



if __name__ == "__main__":
    args = sys.argv

    epubreader = EpubReader()
    epubreader.readEpub(sys.argv[1])
    epubreader.clean_temp_folder()
