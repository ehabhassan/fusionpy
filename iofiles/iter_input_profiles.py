import os
import sys
import numpy

import linecache

type_none = type(None)

def line_burst(string):
    records = string.split()
    print(records)

    return 1

def read_profiles_file(fpath,setParams={}):
    profiles = {}
    iline = 0
    while True:
          record = linecache.getline(fpath,iline)
          if   "#" in record: line_burst(record)
          elif len(record) == 0: break
          iline += 1

    return profiles

if __name__ == "__main__":
   fpath = sys.argv[1]
   profile_data = read_profiles_file(fpath)
