import os
import numpy as npy
import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf  import PdfPages
from iofiles.onetwo.read_onetwo_files import read_state_file


def plot_state_file(fname):
    reportpath = os.path.join(os.path.abspath("."),"fastran_report")
    if not os.path.isdir(reportpath):
       os.system('mkdir %s' % reportpath)

    onetwopath = os.path.join(reportpath,"ONETWO")
    if not os.path.isdir(onetwopath):
       os.system('mkdir %s' % onetwopath)

    figurepath = os.path.join(onetwopath,"Figures")
    if not os.path.isdir(figurepath):
       os.system('mkdir %s' % figurepath)

    ONETWOfigs = PdfPages(os.path.join(figurepath,'onetwo_plots.pdf'))

    onetwo = read_state_file(fname)

    rho  = (onetwo['rho_grid']['data']     - onetwo['rho_grid']['data'][0])
    rho /= (onetwo['rho_grid']['data'][-1] - onetwo['rho_grid']['data'][0])

    fields = []
    fields.extend(['Te', 'Ti', 'ene', 'press','pressb','q_value'])
    fields.extend(['p_flux_elct','p_flux_ion'])
    fields.extend(['e_fluxe','e_fluxe_conv','e_fluxi','e_fluxi_conv'])

    for ifield in fields:
        fg = plt.figure(onetwo[ifield]['name'])
        ax = fg.add_subplot(111)
        ax.plot(rho,onetwo[ifield]['data'])
        ax.set_title(onetwo[ifield]['name'])
        ax.set_xlabel("$\\rho$")
        ax.set_ylabel("%s ($%s$)" % (onetwo[ifield]['name'], onetwo[ifield]['unit']))
        ONETWOfigs.savefig(fg)
        plt.close(fg)

    fields = []
    fields.extend(['enion','p_flux_conv','p_flux'])

    for ifield in fields:
        fg = plt.figure(onetwo[ifield]['name'])
        fg.suptitle(onetwo[ifield]['name'])
        ax = fg.add_subplot(111)
        for ind in range(onetwo['nion']['data']):
            if onetwo['namep']['data'][0,ind].decode('utf-8').strip() != '': 
                figlabel = "ion: %s" % onetwo['namep']['data'][0,ind].decode('utf-8')
                ax.plot(rho,onetwo[ifield]['data'][ind,:],label=figlabel)
        ax.set_xlabel("$\\rho$")
        ax.set_ylabel("%s ($%s$)" % (onetwo[ifield]['name'], onetwo[ifield]['unit']))
        ax.legend()
        ONETWOfigs.savefig(fg)
        plt.close(fg)

    ONETWOfigs.close()

if __name__ == "__main__":
    state_fname = "statefile_2.630000E+00.nc"
    plot_state_file(fname=state_fname)
