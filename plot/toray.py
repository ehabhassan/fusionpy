import os
import sys
import numpy as npy
import matplotlib.pyplot as plt

from glob import glob
from plot.savefig       import to_pdf
from iofiles.eqdsk      import read_eqdsk_file
from iofiles.toray      import read_toray_file

def plot_toray_outputs(torayfpath,eqdskfpath):
    if os.path.isdir(torayfpath):
       toraydata = read_toray_file(fpath=torayfpath)
    if toraydata:
       if os.path.isfile(eqdskfpath):
          eqdskdata = read_eqdsk_file(eqdskfpath)
       minind = npy.argmin(abs(abs(toraydata['jec']['data'])-npy.max(abs(toraydata['jec']['data']))))
       if   toraydata['jec']['data'][minind] < 0.0: continue
       elif toraydata['rho']['data'][minind] < 0.2 or toraydata['rho']['data'][minind] > 0.8: continue
       fig1 = plt.figure("EC-Current")
       ax11 = fig1.add_subplot(211)
       ax12 = fig1.add_subplot(212)
       fig2 = plt.figure("Tracing")
       ax21 = fig2.add_subplot(331)
       ax22 = fig2.add_subplot(332)
       ax23 = fig2.add_subplot(333)
       ax24 = fig2.add_subplot(334)
       ax25 = fig2.add_subplot(335)
       ax26 = fig2.add_subplot(336)
       ax27 = fig2.add_subplot(337)
       ax28 = fig2.add_subplot(338)
       ax29 = fig2.add_subplot(339)
       titletxt = ("X=%3.2f,Z=%3.2f,$\\phi$=%3.2f,$\\theta$=%3.2f"
                   % (toraydata['x0']['data'][0],
                      toraydata['z0']['data'][0],
                      toraydata['angrid2']['data'][0],
                      toraydata['angrid1']['data'][0]))
       fig1.suptitle(titletxt)
       fig2.suptitle(titletxt)

       ax11.plot(toraydata['rho']['data'],toraydata['jec']['data'],label='TORAY:JEC')
       ax12.plot(toraydata['rho']['data'],toraydata['pec']['data'],label='TORAY:PEC')

       ax11.set_ylabel("$J_{ECRH}$")
       ax12.set_ylabel("$P_{ECRH}$")
       ax12.set_xlabel("$\\rho$")

       ax11.set_xticks([])

       ax11.legend()
    
       ax21.plot(eqdskdata['rbound']*1.0e2,eqdskdata['zbound']*1.0e2)
       ax22.plot(eqdskdata['rbound']*1.0e2,eqdskdata['zbound']*1.0e2)
       ax23.plot(eqdskdata['rbound']*1.0e2,eqdskdata['zbound']*1.0e2)
       ax24.plot(eqdskdata['rbound']*1.0e2,eqdskdata['zbound']*1.0e2)
       ax25.plot(eqdskdata['rbound']*1.0e2,eqdskdata['zbound']*1.0e2)
       ax26.plot(eqdskdata['rbound']*1.0e2,eqdskdata['zbound']*1.0e2)
       ax27.plot(eqdskdata['rbound']*1.0e2,eqdskdata['zbound']*1.0e2)
       ax28.plot(eqdskdata['rbound']*1.0e2,eqdskdata['zbound']*1.0e2)
       ax29.plot(eqdskdata['rbound']*1.0e2,eqdskdata['zbound']*1.0e2)
       for iray in range(48):
           ax21.tricontourf(toraydata['wr']['data'][iray,:],toraydata['wz']['data'][iray,:],toraydata['delpwr']['data'][iray,:])
           ax22.tricontourf(toraydata['wr']['data'][iray,:],toraydata['wz']['data'][iray,:], toraydata['curds']['data'][iray,:])
           ax23.tricontourf(toraydata['wr']['data'][iray,:],toraydata['wz']['data'][iray,:], toraydata['svgrpdc']['data'][iray,:])
           ax24.tricontourf(toraydata['wr']['data'][iray,:],toraydata['wz']['data'][iray,:],  toraydata['arcs']['data'][iray,:])
           ax25.tricontourf(toraydata['wr']['data'][iray,:],toraydata['wz']['data'][iray,:],  toraydata['sene']['data'][iray,:])
           ax26.tricontourf(toraydata['wr']['data'][iray,:],toraydata['wz']['data'][iray,:],   toraydata['ste']['data'][iray,:])
           ax27.tricontourf(toraydata['wr']['data'][iray,:],toraydata['wz']['data'][iray,:],   toraydata['wnpar']['data'][iray,:])
           ax28.tricontourf(toraydata['wr']['data'][iray,:],toraydata['wz']['data'][iray,:],   toraydata['wnper']['data'][iray,:])
           ax29.tricontourf(toraydata['wr']['data'][iray,:],toraydata['wz']['data'][iray,:],   toraydata['sbtot']['data'][iray,:])
    
       ax21.set_ylabel("Z")
       ax24.set_ylabel("Z")
       ax27.set_ylabel("Z")
       ax27.set_xlabel("R")
       ax28.set_xlabel("R")
       ax29.set_xlabel("R")
    
       ax21.set_xticks([])
       ax22.set_xticks([])
       ax23.set_xticks([])
       ax24.set_xticks([])
       ax25.set_xticks([])
       ax26.set_xticks([])
    
       text_x = 50.0
       text_z = max(eqdskdata['zbound'])*1.0e2-50.0
       ax21.text(text_x,text_z,fontsize="8",s="Ray Power")
       ax22.text(text_x,text_z,fontsize="8",s="Driven Current")
       ax23.text(text_x,text_z,fontsize="8",s="Group Velocity")
       ax24.text(text_x,text_z,fontsize="8",s="Ray ARC")
       ax25.text(text_x,text_z,fontsize="8",s="Density Along Ray")
       ax26.text(text_x,text_z,fontsize="8",s="Temperature Along Ray")
       ax27.text(text_x,text_z,fontsize="8",s="Parallel Refractive Index")
       ax28.text(text_x,text_z,fontsize="8",s="Perpendicular Refractive Index")
       ax29.text(text_x,text_z,fontsize="8",s="Magnetic Field Strength")
    
       ax22.set_yticks([])
       ax25.set_yticks([])
       ax28.set_yticks([])
    
       ax23.yaxis.tick_right()
       ax23.yaxis.set_label_position("right")
       ax26.yaxis.tick_right()
       ax26.yaxis.set_label_position("right")
       ax29.yaxis.tick_right()
       ax29.yaxis.set_label_position("right")
    
       fig1.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
       fig1.subplots_adjust(wspace=0,hspace=0)
    
       fig2.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
       fig2.subplots_adjust(wspace=0,hspace=0)
    
       figobjs = (fig1,fig2)
       plt.close(fig1,fig2)
    
    to_pdf(figobjs,fname=isimpath,category='TORAY')

sys.exit()

