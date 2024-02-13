import os
import sys
import numpy as npy
import matplotlib.pyplot as plt

from maths.interp        import interp

from iofiles.eqdsk       import qtor,jtot
from iofiles.eqdsk       import read_eqdsk_file
from iofiles.eqdsk       import psigrids,phigrids

from iofiles.plasmastate import get_plasmastate
from iofiles.plasmastate import get_instate_vars
from iofiles.plasmastate import read_instate_file

from matplotlib.backends.backend_pdf import PdfPages

def plot_instate_file(fpath):
    if type(fpath) not in [list,tuple]: fpath = [fpath]
    nstates = len(fpath)

    reportpath = os.path.join(os.path.abspath("."),"fastran_report")
    if not os.path.isdir(reportpath):
       os.system('mkdir %s' % reportpath)

    instatepath = os.path.join(reportpath,"INSTATE")
    if not os.path.isdir(instatepath):
       os.system('mkdir %s' % instatepath)

    figurepath = os.path.join(instatepath,"Figures")
    if not os.path.isdir(figurepath):
       os.system('mkdir %s' % figurepath)

    INSTATEfigs = PdfPages(os.path.join(figurepath,'instate_plots.pdf'))

    fields = []
    fields.extend(['ne','ni','nz','Te', 'Ti','omega','pressure'])
    fields.extend(['jpar','jbs','joh','jnb'])
    fields.extend(['penb','pinb','prad','pei','pohm','picx','pifus','pefus'])
    fields.extend(['wbeam','walpha','nbfast','nalpha'])

    instate = []
    for i in range(nstates):
        instate.append(get_plasmastate(ifpath=fpath[i]))
       #instate.append(read_instate_file(fpath=fpath[i]))

    for ifield in fields:
        fg = plt.figure(ifield)
        ax = fg.add_subplot(111)
        for i in range(nstates):
            ax.plot(instate[i]['rho'],instate[i][ifield],label = "state: %d" % i)
        ax.set_xlabel("$\\rho$")
        ax.set_ylabel(ifield)
        ax.legend()
        INSTATEfigs.savefig(fg)
        plt.close(fg)

    fg = plt.figure()
    ax = fg.add_subplot(111)
    for i in range(nstates):
        ax.plot(instate[i]['rlim'],instate[i]['zlim'],label = "state: %d" % i)
    ax.set_xlabel("$R$")
    ax.set_ylabel("$Z$")
    ax.legend()
    INSTATEfigs.savefig(fg)
    plt.close(fg)

    fg = plt.figure()
    ax = fg.add_subplot(111)
    for i in range(nstates):
        ax.plot(instate[i]['rbound'],instate[i]['zbound'],label = "state: %d" % i)
    ax.set_xlabel("$R$")
    ax.set_ylabel("$Z$")
    ax.legend()
    INSTATEfigs.savefig(fg)
    plt.close(fg)

    INSTATEfigs.close()

    return 1

def plot_instate_geqdsk_files(ifpath,gfpath):
    reportpath = os.path.join(os.path.abspath("."),"fastran_report")
    if not os.path.isdir(reportpath):
       os.system('mkdir %s' % reportpath)

    instatepath = os.path.join(reportpath,"INSTATE")
    if not os.path.isdir(instatepath):
       os.system('mkdir %s' % instatepath)

    figurepath = os.path.join(instatepath,"Figures")
    if not os.path.isdir(figurepath):
       os.system('mkdir %s' % figurepath)

    INSTATEfigs = PdfPages(os.path.join(figurepath,'instate_geqdsk_plots.pdf'))

    geqdsk  = read_eqdsk_file(fpath=gfpath)
    calc_qtor = qtor()
    calc_psigrids = psigrids()
    calc_phigrids = phigrids()

    calc_qtor(    geqdsk,ps_update=True)
    calc_psigrids(geqdsk,ps_update=True)
    calc_phigrids(geqdsk,ps_update=True)

    calc_iterp = interp()
    geqdsk['qtor']     = calc_iterp(geqdsk['rhopsi'],geqdsk['qpsi'],    geqdsk['rhotor'])
    geqdsk['pprime']   = calc_iterp(geqdsk['rhopsi'],geqdsk['pprime'],  geqdsk['rhotor'])
    geqdsk['ffprime']  = calc_iterp(geqdsk['rhopsi'],geqdsk['ffprime'], geqdsk['rhotor'])
    geqdsk['pressure'] = calc_iterp(geqdsk['rhopsi'],geqdsk['pressure'],geqdsk['rhotor'])

    instate = get_plasmastate(ifpath=ifpath,gfpath=gfpath)
  # instate = read_instate_file(fpath=ifpath)

    fg = plt.figure()
    ax = fg.add_subplot(111)
    ax.plot(geqdsk['rhotor'],geqdsk[ "qtor"],label = "geqdsk")
    ax.plot(instate['rho'],  instate["q"],label = "instate")
    ax.set_xlabel("$\\rho$")
    ax.set_ylabel("q")
    ax.legend()
    INSTATEfigs.savefig(fg)
    plt.close(fg)

  # fg = plt.figure()
  # ax = fg.add_subplot(111)
  # ax.plot(geqdsk['rhotor'],geqdsk[ "jtot"],label = "geqdsk")
  # ax.plot(instate['rho'],  instate["jpar"],label = "instate")
  # ax.set_xlabel("$\\rho$")
  # ax.set_ylabel("jtot")
  # ax.legend()
  # INSTATEfigs.savefig(fg)
  # plt.close(fg)

    fg = plt.figure()
    ax = fg.add_subplot(111)
    ax.plot(geqdsk['rhotor'],geqdsk[ "pressure"],label = "geqdsk")
    ax.plot(instate['rho'],  instate["pressure"],label = "instate")
    ax.set_xlabel("$\\rho$")
    ax.set_ylabel("pressure")
    ax.legend()
    INSTATEfigs.savefig(fg)
    plt.close(fg)

    fg = plt.figure()
    ax = fg.add_subplot(111)
    ax.plot(geqdsk['rhotor'],geqdsk[ "pprime"],label = "geqdsk")
    ax.plot(instate['rho'],  instate["pprime"],label = "instate")
    ax.set_xlabel("$\\rho$")
    ax.set_ylabel("pprime")
    ax.legend()
    INSTATEfigs.savefig(fg)
    plt.close(fg)

    fg = plt.figure()
    ax = fg.add_subplot(111)
    ax.plot(geqdsk['rhotor'],geqdsk[ "ffprime"],label = "geqdsk")
    ax.plot(instate['rho'],  instate["ffprime"],label = "instate")
    ax.set_xlabel("$\\rho$")
    ax.set_ylabel("ffprime")
    ax.legend()
    INSTATEfigs.savefig(fg)
    plt.close(fg)

    fg = plt.figure()
    ax = fg.add_subplot(111)
    ax.plot(geqdsk['rlimit'],geqdsk[ 'zlimit'],label = "geqdsk")
    ax.plot(instate['rlim'], instate['zlim'],  label = "instate")
    ax.set_xlabel("$R$")
    ax.set_ylabel("$Z$")
    ax.legend()
    INSTATEfigs.savefig(fg)
    plt.close(fg)

    fg = plt.figure()
    ax = fg.add_subplot(111)
    ax.plot(geqdsk[ 'rbound'],geqdsk[ 'zbound'],label = "geqdsk")
    ax.plot(instate['rbound'],instate['zbound'],label = "instate")
    ax.set_xlabel("$R$")
    ax.set_ylabel("$Z$")
    ax.legend()
    INSTATEfigs.savefig(fg)
    plt.close(fg)

    INSTATEfigs.close()

    return 1

if __name__ == "__main__":
    geqdsk_fname01  = "../../Discharges/DIIID/DIIID150139/g150139.02026"
    instate_fname01 = "../testsuite/state_files/instate_d3d_150139.20259"
    instate_fname02 = "../iofiles/instate_d3d_150139.20259"
  # plot_instate_geqdsk_files(ifpath=instate_fname,gfpath=geqdsk_fname)
    plot_instate_file([instate_fname01,instate_fname02])
