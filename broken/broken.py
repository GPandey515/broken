#!/usr/bin/env python

r"""
   ___ ___  ___  _  _____ _  _   _    ___ _  _ _  __
 | _ ) _ \/ _ \| |/ / __| \| | | |  |_ _| \| | |/ /
 | _ \   / (_) | ' <| _|| .` | | |__ | || .` | ' < 
 |___/_|_\\___/|_|\_\___|_|\_| |____|___|_|\_|_|\_\
                                                                                                                                                                                                                                                                                                                  
brokenlink generates brokenlink url from the command line for you
Usage:
  brokenlink [FILE_NAME]
  brokenlink (-h | --help)
  brokenlink --version
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import os
import sys

from docopt import docopt

from sets import Set
import csv

_author_ = "noones"
__version__ = '0.0.1'

    
NO_SUCH_HOST = "12007"
brokenlinks = []
filtered_broken = Set()

filenameOut = []
filenameIn = []

_ROOT = os.path.abspath(os.path.dirname(__file__))


def _get_data_dir(path):
    '''Returns the path to the directory matching the passed `path`.'''
    return os.path.dirname(os.path.join(_ROOT, 'data', path))

def _fileRead():
  '''Checks the status 12007 on index 2 of TSV file 
      append if status 12007 found to a list and
      removes duplicate links
  '''
  filenameIn.append(sys.argv[1])
  (prefix, sep, suffix) = filenameIn[0].rpartition('.')
  temp = prefix + "_output.txt"
  filenameOut.append(temp)
  print filenameIn[0] + "\n" +filenameOut[0]
  with open(filenameIn[0]) as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
      if line[1]==NO_SUCH_HOST:
        brokenlinks.append(line[0])
        print line[0]
  global filtered_broken
  filtered_broken = Set(brokenlinks)


def _writefile():
  '''outputs filtered broken links in a simple text file'''
  global filtered_broken
  with open(filenameOut[0], "w") as f:
    f.write('\n'.join(filtered_broken))


def main():
    '''brokenlink generates brokenlink url from the command line for you'''
    arguments = docopt(__doc__, version=__version__)
    if sys.argv[1]:
      _fileRead()
      _writefile()
    elif sys.argv[0]:
      print(__doc__)
    else:
      print(__doc__)

if __name__ == '__main__':
    main()