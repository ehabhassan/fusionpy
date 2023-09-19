import sys
import numpy   as npy
import netCDF4 as ncdf

import matplotlib.pyplot as plt

from iofiles.fastran.get_plasmastate import get_plasmastate

ncfname = "statefile_2.630000E+00.nc"
instate = "instate"

ncfid = ncdf.Dataset(ncfname)

ncfvars = ncfid.variables.keys()
for ncfvar in ncfvars:
    print(ncfvar)
    try:
       print(ncfid.variables[ncfvar].getncattr('units'))
    except AttributeError:
        pass
    print(ncfid.variables[ncfvar].getncattr('long_name'))
    pausing = input()

#print(ncfvars)
#ncData = ncfid.variables['press'][:]
#ncUnit = ncfid.variables['press'].getncattr('units')
#ncInfo = ncfid.variables['press'].getncattr('long_name')
#print(ncUnit,ncInfo)
#ncData = ncfid.variables['curpar'][:]
#ncUnit = ncfid.variables['curpar'].getncattr('units')
#ncInfo = ncfid.variables['curpar'].getncattr('long_name')
#print(ncUnit,ncInfo)

sys.exit()

nrho = ncfid.variables['nj'][:]
rho = (npy.arange(1.0,nrho+1) - 1.0)/(nrho - 1.0)

TiData = ncfid.variables['Ti'][:]
TeData = ncfid.variables['Te'][:]
neData = ncfid.variables['ene'][:]
PtData = ncfid.variables['press'][:]
JpData = ncfid.variables['curpar'][:]

instate = get_plasmastate(instatefpath="instate")

fig = plt.figure("profiles")
ax1 = fig.add_subplot(411)
ax1.plot(rho,TeData,label="ONETWO")
ax1.plot(instate['rho'],instate['Te']/1.602e3,linestyle="--",label="INSTATE")
ax1.set_ylabel("$T_e$")
ax2 = fig.add_subplot(412)
ax2.plot(rho,neData,label="ONETWO")
ax2.plot(instate['rho'],instate['ne'],linestyle="--",label="INSTATE")
ax2.set_ylabel("$n_e$")
ax3 = fig.add_subplot(413)
ax3.plot(rho,PtData,label="ONETWO")
ax3.plot(instate['rho'],instate['pressure'],linestyle="--",label="INSTATE")
ax3.set_ylabel("$P_T$")
ax4 = fig.add_subplot(414)
ax4.plot(rho,JpData,label="ONETWO")
ax4.plot(instate['rho'],instate['jpar'],linestyle="--",label="INSTATE")
ax4.set_ylabel("$J_p$")
plt.show()

sys.exit()

psi  = ncfid.variables['psi'][:]
rho  = ncfid.variables['rho_grid'][:]
BCTR = ncfid.variables['btgeom'][:]
psir = ncfid.variables['psir_grid'][:]

print(TeData)
print(TeUnit)
print(TeInfo.split("*")[1].strip())

