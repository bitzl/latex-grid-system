from __future__ import print_function
from zipfile import ZipFile
from fabric.api import local
from os import path

class Package(ZipFile):
    def __init__(self, name, folder):
        ZipFile.__init__(self, name, 'w')
        self.folder = folder
    
    def add(self, name, new_name=None):
        if new_name == None:
            new_name = name
        self.write(name, path.join(self.folder, new_name))


def zip(zipfile='grid-system.zip'):
    with Package(zipfile, 'grid-system') as zip:
        zip.add('grid-system.pdf')
        zip.add('grid-system.sty')
        zip.add('grid-system.tex')
        zip.add('README.md', 'README')
        zip.add('LICENSE')


def build_missing_pdf():
    if not path.exists('grid-system.pdf'):
        local('pdflatex grid-system')


def default():
    build_missing_pdf()
    zip()
