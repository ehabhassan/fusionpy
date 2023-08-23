import sys
import numpy as npy

from iofiles.fastran.get_plasmastate import get_plasmastate

def write_from_instate_file(fname,shot_id,time_id):
    instate = get_plasmastate(instatefpath=fname)

    if type(shot_id) == str: shot_id = int(float(shot_id))
    if type(time_id) == str: time_id = int(float(time_id))
    
    fname = "te%06d.%05d" % (shot_id,time_id)
    records = npy.column_stack((instate['rho'],instate['Te']/1.602e-3))
    npy.savetxt(fname,records, fmt='%7.7E', delimiter='\t')

    fname = "ti%06d.%05d" % (shot_id,time_id)
    records = npy.column_stack((instate['rho'],instate['Ti']/1.602e-3))
    npy.savetxt(fname,records, fmt='%7.7E', delimiter='\t')

    fname = "ne%06d.%05d" % (shot_id,time_id)
    records = npy.column_stack((instate['rho'],instate['ne']*1.0e-19))
    npy.savetxt(fname,records, fmt='%7.7E', delimiter='\t')

    fname = "nc%06d.%05d" % (shot_id,time_id)
    records = npy.column_stack((instate['rho'],instate['nz']*1.0e-19))
    npy.savetxt(fname,records, fmt='%7.7E', delimiter='\t')

    fname = "zf%06d.%05d" % (shot_id,time_id)
    records = npy.column_stack((instate['rho'],instate['zeff']))
    npy.savetxt(fname,records, fmt='%7.7E', delimiter='\t')

    fname = "vt%06d.%05d" % (shot_id,time_id)
    records = npy.column_stack((instate['rho'],instate['omega']))
    npy.savetxt(fname,records, fmt='%7.7E', delimiter='\t')

    return 1


if __name__ == "__main__":
    write_from_instate_file(fname="instate",shot_id="101381",time_id="02630")

