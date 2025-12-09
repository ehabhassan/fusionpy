import os
import sys
import numpy
import matplotlib.pyplot as plt

from plot.savefig import to_pdf

from iofiles.tglf import read_ky_spectrum
from iofiles.tglf import read_sum_flux_spectrum
from iofiles.tglf import read_eigenvalue_spectrum


type_none = type(None)

def plot_particle_flux(fpath,show=False,setparam={}):
    if os.path.isdir(fpath):    fpath = os.path.join(fpath,"out.tglf.sum_flux_spectrum")
    elif os.path.isfile(fpath): pass
    path_to_file = os.path.dirname(fpath)

    if 'field'   in setparam: field   = setparam['field'  ]
    else:                     field   = None
    if 'species' in setparam: species = setparam['species']
    else:                     species = None

    if 'shotid' in setparam:     shotid = setparam['shotid']
    else:                        shotid = None
    if 'scale_ne' in setparam:   scale_ne = setparam['scale_ne']
    else:                        scale_ne = None
    if 'tokamakid'  in setparam: tokamakid = setparam['tokamakid']
    else:                        tokamakid = None
    if 'scale_sion' in setparam: scale_sion = setparam['scale_ne']
    else:                        scale_sion = None
    stitle = ""
    if type(tokamakid)  != type_none: stitle += "%s[" % tokamakid
    if type(shotid)     != type_none: stitle += "SHOTID: %s," % shotid
    if type(scale_ne)   != type_none: stitle += "SCALE_NE: %s," % scale_ne
    if type(scale_sion) != type_none: stitle += "SCALE_SION: %s" % scale_sion
    stitle += "]"

    ky     = read_ky_spectrum(path_to_file)
    fluxes = read_sum_flux_spectrum(path_to_file)


    fig = plt.figure("fluxes")
    fig.suptitle(stitle)
    fig.tight_layout(rect=[0.0,0.0,1.0,1.0])
    fig.subplots_adjust(wspace=0,hspace=0)

    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    if type(field) == type_none and type(species) == type_none:
       for fluxes_ind in fluxes:
           species = int(fluxes_ind[0])
           field   = int(fluxes_ind[1])
           zlabel  = "species(%s)-field(%s)" % (species, field)
           ax1.plot(ky,fluxes[fluxes_ind]['particle_flux'],label=zlabel)
           ax2.plot(ky,fluxes[fluxes_ind]['energy_flux'],  label=zlabel)
    else:
       fluxes_ind = '%d%d' % (int(species),int(field))
       plt.plot(ky,fluxes[fluxes_ind]['particle_flux'])

    ax1.legend()
    ax1.set_xticks([])
    ax1.set_title("TGLF Modes Particle and Energy Fluxes",fontsize=16)
    ax2.set_xlabel("$k_y$",fontsize=14)
    ax2.set_ylabel("$\\frac{\\chi}{\\chi_{GB}}$",fontsize=14)
    ax1.set_ylabel("$\\frac{\\Gamma}{\\chi_{GB}}$",fontsize=14)

    if show: plt.show()

    return fig
    

def plot_eigenvalues(fpath,show=False,setparam={}):
    if os.path.isdir(fpath):    fpath = os.path.join(fpath,"out.tglf.eigenvalue_spectrum")
    elif os.path.isfile(fpath): pass
    path_to_file = os.path.dirname(fpath)

    if 'shotid'     in setparam: shotid = setparam['shotid']
    else:                        shotid = None
    if 'scale_ne'   in setparam: scale_ne = setparam['scale_ne']
    else:                        scale_ne = None
    if 'tokamakid'  in setparam: tokamakid = setparam['tokamakid']
    else:                        tokamakid = None
    if 'scale_sion' in setparam: scale_sion = setparam['scale_ne']
    else:                        scale_sion = None

    stitle = ""
    if type(tokamakid)  != type_none: stitle += "%s[" % tokamakid
    if type(shotid)     != type_none: stitle += "SHOTID: %s," % shotid
    if type(scale_ne)   != type_none: stitle += "SCALE_NE: %s," % scale_ne
    if type(scale_sion) != type_none: stitle += "SCALE_SION: %s" % scale_sion
    stitle += "]"

    ky     = read_ky_spectrum(path_to_file)
    eigenvalues = read_eigenvalue_spectrum(path_to_file)

    fig = plt.figure("eigenvalues")
    fig.suptitle(stitle)
    fig.tight_layout(rect=[0.0,0.0,1.0,1.0])
    fig.subplots_adjust(wspace=0,hspace=0)

    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    for imode in range(eigenvalues['nmodes']):
        gamma = []
        omega = []
        for i in range(len(ky)):
            gamma.append(eigenvalues[i+1]['gamma'][imode])
            omega.append(eigenvalues[i+1]['omega'][imode])

        ax1.plot(ky,[i/j for (i,j) in zip(gamma,ky)],label="mode(%d)" % imode)
        ax2.plot(ky,[i/j for (i,j) in zip(omega,ky)])

    ax1.legend()
    ax1.set_xticks([])
    ax1.set_title("TGLF Modes Growth-rate and Frequency",fontsize=16)
    ax2.set_xlabel("$k_y$",fontsize=14)
    ax2.set_ylabel("$\\frac{\\omega}{k_y}$",fontsize=14)
    ax1.set_ylabel("$\\frac{\\gamma}{k_y}$",fontsize=14)

    if show: plt.show()

    return fig

if __name__ == "__main__":
   fpath = sys.argv[1]
   figs = []
   show_plot = False
   setparam = {}
  #setparam = {'tokamakid':'DIIID','shotid':'150139','scale_ne':1.0,'scale_sion':1.0}

   figs.append(plot_eigenvalues(  fpath,show=show_plot,setparam=setparam))
   figs.append(plot_particle_flux(fpath,show=show_plot,setparam=setparam))

   to_pdf(figs,fname="tglf_outputs.pdf")
