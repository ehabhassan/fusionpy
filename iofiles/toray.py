import os
import sys
import numpy as npy

from netCDF4          import Dataset
from plot.colors      import *
from iofiles.Namelist import Namelist

def read_output_file(fpath):
    ncfpath = os.path.join(fpath,"toray.nc")
    if ncfpath and os.path.isfile(ncfpath):
        print(CGREEN + "FINDING TORAY OUTPUT AT %s: PASSED" % (fpath) + CEND)
    else:
        print(CRED   + "FINDING TORAY OUTPUT AT %s: FAILED" % (fpath) + CEND)
        return {}
    try:
        cdffh = Dataset(ncfpath, mode='r')
    except OSError:
        print(CRED + "READING TORAY OUTPUT AT %s: FAILED" % (fpath) + CEND)
        return {}

    toray = {}
    for name, variable in cdffh.variables.items():
        toray[name]                  = {}
        toray[name]['data']          = cdffh.variables[name][:]
        if hasattr(variable, "unit"):
            toray[name]['unit']     = getattr(variable, "units")
        else:
            toray[name]['unit']     = ""
        if hasattr(variable, "long_name"):
            toray[name]['long_name']     = getattr(variable, "long_name")
        else:
            toray[name]['long_name']     = ""


    infpath = os.path.join(fpath,"intoray")
    if os.path.isfile(infpath):
       intoray = Namelist(infpath)
    else:
       print("TORAY INPUT NOT FOUND in %s" % fpath)

    toray['rho'] = {}
    toray['rho']['data'] = toray['xrho']['data']

    toray['nrho'] = {}
    toray['nrho']['data'] = toray['ledge']['data']

    toray['jec'] = {}
    toray['jec']['data'] = npy.zeros(toray['nrho']['data'])
    toray['jec']['unit'] = "A/M^2/W"

    toray['pec'] = {}
    toray['pec']['data'] = npy.zeros(toray['nrho']['data'])
    toray['jec']['unit'] = "W/M^2/W"

    for ind in range(1,toray['nrho']['data']-1):
        toray['jec']['data'][ind] = 0.5 * (toray['currf']['data'][ind]  + toray['currf']['data'][ind-1])  * 1.0e4
        toray['pec']['data'][ind] = 0.5 * (toray['weecrh']['data'][ind] + toray['weecrh']['data'][ind-1]) * 1.0e6

    toray['jec']['data'] *= float(intoray['intoray']['rfpow'][0])*1.0e-6
    toray['jec']['data'][ 0]  = toray['jec']['data'][1]
    toray['jec']['data'][-1] = 0.0

    toray['pec']['data'] *= float(intoray['intoray']['rfpow'][0])*1.0e-6
    toray['pec']['data'][ 0] = toray['pec']['data'][1]
    toray['pec']['data'][-1] = 0.0

    return toray

