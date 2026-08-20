import os
import sys
import glob

import matplotlib.pyplot as plt

from fusionpy.plot.colors import CRED,CEND,CGREEN,markers,colors
from fusionpy.iofiles.plasmastate import read_instate_file

def read_xfastran_log_file(path_to_file):
    errors_ne = []
    errors_te = []
    errors_ti = []
    success_flag = False
    if os.path.isdir(path_to_file):
       path_to_file = os.path.join(path_to_file,"xfastran.log")
    if os.path.isfile(path_to_file):
       fhand = open(path_to_file,"r")
       lines = fhand.readlines()
       if "done" in lines[-1].strip(): success_flag = True
       for iline in lines:
          #if "res_n=" in iline:
           if "relax" in iline:
              errors_te.append(float(iline.split()[2].split("=")[1]))
              errors_ti.append(float(iline.split()[3].split("=")[1]))
              errors_ne.append(float(iline.split()[4].split("=")[1]))
    errors = {'errors_ne':errors_ne,'errors_te':errors_te,'errors_ti':errors_ti}
    return errors,success_flag

if __name__=="__main__": 
   path_to_files = sys.argv[1:]
   fig = plt.figure("Error in FASTRAN Solver",dpi=200)
   ax1 = fig.add_subplot(311)
   ax2 = fig.add_subplot(312)
   ax3 = fig.add_subplot(313)
   for path_to_file in path_to_files:
       if os.path.isdir(path_to_file):
          path_to_instate_file = glob.glob(os.path.join(path_to_file,"i??????.?????"))[0]
          instate_data = read_instate_file(path_to_instate_file)
          plt_title = "%s %s %s" % (instate_data['tokamak_id'][0],instate_data['shot_id'][0],instate_data['time_id'][0])
          scale_se_ionization = instate_data['scale_se_ionization'][0]
       file_ind = path_to_files.index(path_to_file)
       errors,success_flag = read_xfastran_log_file(path_to_file)
       if success_flag:
          print(CGREEN+path_to_file+CEND)
          plt_label = "$f_{n_i}$ = %s" % scale_se_ionization
          ax1.plot(errors['errors_ne'],label=plt_label,linestyle="-",marker="",color=colors[file_ind])
          ax2.plot(errors['errors_te'],label=plt_label,linestyle="-",marker="",color=colors[file_ind])
          ax3.plot(errors['errors_ti'],label=plt_label,linestyle="-",marker="",color=colors[file_ind])
       else:
          print(CRED+path_to_file+CEND)
          ax1.plot(errors['errors_ne'],label=plt_lable,linestyle="",marker=markers[file_ind],color="red")
          ax2.plot(errors['errors_te'],label=plt_lable,linestyle="",marker=markers[file_ind],color="red")
          ax3.plot(errors['errors_ti'],label=plt_lable,linestyle="",marker=markers[file_ind],color="red")
   ax1.legend(ncol=3,loc="upper right",fontsize="8")
   ax1.set_xticks([])
   ax2.set_xticks([])
   ax3.set_xlabel('Number of Iterations')
   ax1.set_ylabel('Err($n_e$)')
   ax2.set_ylabel('Err($T_e$)')
   ax3.set_ylabel('Err($T_i$)')
   ax1.set_title(plt_title,fontsize=8)
   fig.suptitle("Time-Traces of Errors in FASTRAN Simulation",fontsize=10)
   fig.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
   fig.subplots_adjust(wspace=0,hspace=0)
   plt.show()


