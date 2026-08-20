import os
import sys
import copy

import numpy as npy
import matplotlib.pyplot as plt

from fusionpy.plot.colors         import CRED,CEND,CGREEN,markers,colors,styles
from fusionpy.plot.savefig        import to_pdf
from fusionpy.iofiles.plasmastate import read_instate_file

type_none = type(None)

def get_line_count(path_to_file):
    import subprocess
    if os.path.isfile(path_to_file):
        result = subprocess.run(['wc', '-l', path_to_file], stdout=subprocess.PIPE, text=True)
    else:
        IOError("FATAL IOError: FILE:{path_to_file} NOT FOUND.")
    nlines = int(result.stdout.split()[0])
    return nlines

def read_transport_conv_file(path_to_file):
    transport_errors = get_transport_errors()
    transport_errors_names = list(transport_errors.keys())

    transport_fields = get_transport_fields()
    transport_fields_names = list(transport_fields.keys())

    if os.path.isdir(path_to_file):
       path_to_file = os.path.join(path_to_file,"transport_conv.dat")

    fhands = open(path_to_file, "r")
    contents = fhands.readlines()
    nlines = len(contents)
    fhands.close()

    transport_timetrace_errors = {}
    transport_timetrace_fields = {}

    iline = 0
    while True:
        content = contents[iline].split()
        if 'step' in content:
           step = content[2]
           iter = content[4]
           nrec = int(content[9].split('=')[1])+1

           if step not in transport_timetrace_errors: transport_timetrace_errors[step] = copy.deepcopy(transport_errors)
           if step not in transport_timetrace_fields: transport_timetrace_fields[step] = {}
           if iter not in transport_timetrace_fields[step]: transport_timetrace_fields[step][iter] = copy.deepcopy(transport_fields)

           for res_name in transport_errors_names:
           	if type(transport_timetrace_errors[step][res_name]['data']) == type_none: transport_timetrace_errors[step][res_name]['data'] =      [float(content[5].split('=')[1])]
           	else:                                                                     transport_timetrace_errors[step][res_name]['data'].extend([float(content[5].split('=')[1])])
           iline += 1
           fields = contents[iline].split()
           for irec in range(nrec):
               iline += 1
               content = contents[iline].split()
               for fld_name in transport_fields_names:
                    fld_ind = transport_fields_names.index(fld_name)
                    if type(transport_timetrace_fields[step][iter][fld_name]['data']) == type_none: transport_timetrace_fields[step][iter][fld_name]['data'] =      [float(content[fld_ind])]
                    else:                                                                           transport_timetrace_fields[step][iter][fld_name]['data'].extend([float(content[fld_ind])])
        iline += 1
        if iline >= nlines: break

    return transport_timetrace_errors,transport_timetrace_fields

def get_transport_errors():
    transport_errors = {}

    transport_errors['res_e'] = {}
    transport_errors['res_e']['data'] = None
    transport_errors['res_e']['name'] = "Err($T_e$)"
    transport_errors['res_e']['info'] = "Numerical Error in Electron Temperature"
    transport_errors['res_e']['unit'] = None
    transport_errors['res_e']['symb'] = "$\\epsilon(T_e)$"

    transport_errors['res_i'] = {}
    transport_errors['res_i']['data'] = None
    transport_errors['res_i']['name'] = "Err($T_i$)"
    transport_errors['res_i']['info'] = "Numerical Error in Ion Temperature"
    transport_errors['res_i']['unit'] = None
    transport_errors['res_i']['symb'] = "$\\epsilon(T_i)$"

    transport_errors['res_n'] = {}
    transport_errors['res_n']['data'] = None
    transport_errors['res_n']['name'] = "Err($n_e$)"
    transport_errors['res_n']['info'] = "Numerical Error in Electron Density"
    transport_errors['res_n']['unit'] = None
    transport_errors['res_n']['symb'] = "$\\epsilon(n_e)$"

    transport_errors['res_v'] = {}
    transport_errors['res_v']['data'] = None
    transport_errors['res_v']['name'] = "Err($\\upsilon$)"
    transport_errors['res_v']['info'] = "Numerical Error in Velocity"
    transport_errors['res_v']['unit'] = None
    transport_errors['res_v']['symb'] = "$\\epsilon(\\upsilon)$"

    return transport_errors


def get_transport_fields():
    transport_fields = {}

    transport_fields['k'] = {}
    transport_fields['k']['data'] = None
    transport_fields['k']['name'] = None
    transport_fields['k']['info'] = "Order"
    transport_fields['k']['unit'] = None
    transport_fields['k']['symb'] = None

    transport_fields['rho_n'] = {}
    transport_fields['rho_n']['data'] = None
    transport_fields['rho_n']['name'] = "Poloidal Magnetic Flux"
    transport_fields['rho_n']['info'] = "Normalized Poloidal Magnetic Flux"
    transport_fields['rho_n']['unit'] = None
    transport_fields['rho_n']['symb'] = "$\\rho_{\\psi_n}$"

    transport_fields['te'] = {}
    transport_fields['te']['data'] = None
    transport_fields['te']['name'] = "Electron Temperature"
    transport_fields['te']['info'] = "Electron Temperature"
    transport_fields['te']['unit'] = "keV"
    transport_fields['te']['symb'] = "$T_e$"

    transport_fields['te_y1'] = {}
    transport_fields['te_y1']['data'] = None
    transport_fields['te_y1']['name'] = None
    transport_fields['te_y1']['info'] = None
    transport_fields['te_y1']['unit'] = None
    transport_fields['te_y1']['symb'] = None

    transport_fields['ti'] = {}
    transport_fields['ti']['data'] = None
    transport_fields['ti']['name'] = "Ion Temperature"
    transport_fields['ti']['info'] = "Ion Temperature"
    transport_fields['ti']['unit'] = "keV"
    transport_fields['ti']['symb'] = "$T_i$"

    transport_fields['ti_y1'] = {}
    transport_fields['ti_y1']['data'] = None
    transport_fields['ti_y1']['name'] = None
    transport_fields['ti_y1']['info'] = None
    transport_fields['ti_y1']['unit'] = None
    transport_fields['ti_y1']['symb'] = None

    transport_fields['ne'] = {}
    transport_fields['ne']['data'] = None
    transport_fields['ne']['name'] = "Electron Density"
    transport_fields['ne']['info'] = "Electron Density"
    transport_fields['ne']['unit'] = "$#/m^3$"
    transport_fields['ne']['symb'] = "$n_e$"

    transport_fields['ne_y1'] = {}
    transport_fields['ne_y1']['data'] = None
    transport_fields['ne_y1']['name'] = None
    transport_fields['ne_y1']['info'] = None
    transport_fields['ne_y1']['unit'] = None
    transport_fields['ne_y1']['symb'] = None

    transport_fields['rv'] = {}
    transport_fields['rv']['data'] = None
    transport_fields['rv']['name'] = None
    transport_fields['rv']['info'] = None
    transport_fields['rv']['unit'] = None
    transport_fields['rv']['symb'] = None

    transport_fields['rv_y1'] = {}
    transport_fields['rv_y1']['data'] = None
    transport_fields['rv_y1']['name'] = None
    transport_fields['rv_y1']['info'] = None
    transport_fields['rv_y1']['unit'] = None
    transport_fields['rv_y1']['symb'] = None

    transport_fields['z_e'] = {}
    transport_fields['z_e']['data'] = None
    transport_fields['z_e']['name'] = None
    transport_fields['z_e']['info'] = None
    transport_fields['z_e']['unit'] = None
    transport_fields['z_e']['symb'] = None

    transport_fields['z_i'] = {}
    transport_fields['z_i']['data'] = None
    transport_fields['z_i']['name'] = None
    transport_fields['z_i']['info'] = None
    transport_fields['z_i']['unit'] = None
    transport_fields['z_i']['symb'] = None

    transport_fields['z_n'] = {}
    transport_fields['z_n']['data'] = None
    transport_fields['z_n']['name'] = None
    transport_fields['z_n']['info'] = None
    transport_fields['z_n']['unit'] = None
    transport_fields['z_n']['symb'] = None

    transport_fields['z_v'] = {}
    transport_fields['z_v']['data'] = None
    transport_fields['z_v']['name'] = None
    transport_fields['z_v']['info'] = None
    transport_fields['z_v']['unit'] = None
    transport_fields['z_v']['symb'] = None

    transport_fields['turb_e'] = {}
    transport_fields['turb_e']['data'] = None
    transport_fields['turb_e']['name'] = None
    transport_fields['turb_e']['info'] = None
    transport_fields['turb_e']['unit'] = None
    transport_fields['turb_e']['symb'] = None

    transport_fields['turb_i'] = {}
    transport_fields['turb_i']['data'] = None
    transport_fields['turb_i']['name'] = None
    transport_fields['turb_i']['info'] = None
    transport_fields['turb_i']['unit'] = None
    transport_fields['turb_i']['symb'] = None

    transport_fields['turb_n'] = {}
    transport_fields['turb_n']['data'] = None
    transport_fields['turb_n']['name'] = None
    transport_fields['turb_n']['info'] = None
    transport_fields['turb_n']['unit'] = None
    transport_fields['turb_n']['symb'] = None

    transport_fields['turb_v'] = {}
    transport_fields['turb_v']['data'] = None
    transport_fields['turb_v']['name'] = None
    transport_fields['turb_v']['info'] = None
    transport_fields['turb_v']['unit'] = None
    transport_fields['turb_v']['symb'] = None

    transport_fields['neo_e'] = {}
    transport_fields['neo_e']['data'] = None
    transport_fields['neo_e']['name'] = None
    transport_fields['neo_e']['info'] = None
    transport_fields['neo_e']['unit'] = None
    transport_fields['neo_e']['symb'] = None

    transport_fields['neo_i'] = {}
    transport_fields['neo_i']['data'] = None
    transport_fields['neo_i']['name'] = None
    transport_fields['neo_i']['info'] = None
    transport_fields['neo_i']['unit'] = None
    transport_fields['neo_i']['symb'] = None

    transport_fields['neo_n'] = {}
    transport_fields['neo_n']['data'] = None
    transport_fields['neo_n']['name'] = None
    transport_fields['neo_n']['info'] = None
    transport_fields['neo_n']['unit'] = None
    transport_fields['neo_n']['symb'] = None

    transport_fields['neo_v'] = {}
    transport_fields['neo_v']['data'] = None
    transport_fields['neo_v']['name'] = None
    transport_fields['neo_v']['info'] = None
    transport_fields['neo_v']['unit'] = None
    transport_fields['neo_v']['symb'] = None

    transport_fields['chi_e'] = {}
    transport_fields['chi_e']['data'] = None
    transport_fields['chi_e']['name'] = None
    transport_fields['chi_e']['info'] = None
    transport_fields['chi_e']['unit'] = None
    transport_fields['chi_e']['symb'] = None

    transport_fields['chi_i'] = {}
    transport_fields['chi_i']['data'] = None
    transport_fields['chi_i']['name'] = None
    transport_fields['chi_i']['info'] = None
    transport_fields['chi_i']['unit'] = None
    transport_fields['chi_i']['symb'] = None

    transport_fields['chi_n'] = {}
    transport_fields['chi_n']['data'] = None
    transport_fields['chi_n']['name'] = None
    transport_fields['chi_n']['info'] = None
    transport_fields['chi_n']['unit'] = None
    transport_fields['chi_n']['symb'] = None

    transport_fields['chi_v'] = {}
    transport_fields['chi_v']['data'] = None
    transport_fields['chi_v']['name'] = None
    transport_fields['chi_v']['info'] = None
    transport_fields['chi_v']['unit'] = None
    transport_fields['chi_v']['symb'] = None

    transport_fields['chik_e'] = {}
    transport_fields['chik_e']['data'] = None
    transport_fields['chik_e']['name'] = None
    transport_fields['chik_e']['info'] = None
    transport_fields['chik_e']['unit'] = None
    transport_fields['chik_e']['symb'] = None

    transport_fields['chik_i'] = {}
    transport_fields['chik_i']['data'] = None
    transport_fields['chik_i']['name'] = None
    transport_fields['chik_i']['info'] = None
    transport_fields['chik_i']['unit'] = None
    transport_fields['chik_i']['symb'] = None

    transport_fields['chik_n'] = {}
    transport_fields['chik_n']['data'] = None
    transport_fields['chik_n']['name'] = None
    transport_fields['chik_n']['info'] = None
    transport_fields['chik_n']['unit'] = None
    transport_fields['chik_n']['symb'] = None

    transport_fields['chik_v'] = {}
    transport_fields['chik_v']['data'] = None
    transport_fields['chik_v']['name'] = None
    transport_fields['chik_v']['info'] = None
    transport_fields['chik_v']['unit'] = None
    transport_fields['chik_v']['symb'] = None

    transport_fields['fluxe'] = {}
    transport_fields['fluxe']['data'] = None
    transport_fields['fluxe']['name'] = None
    transport_fields['fluxe']['info'] = None
    transport_fields['fluxe']['unit'] = None
    transport_fields['fluxe']['symb'] = None

    transport_fields['fluxi'] = {}
    transport_fields['fluxi']['data'] = None
    transport_fields['fluxi']['name'] = None
    transport_fields['fluxi']['info'] = None
    transport_fields['fluxi']['unit'] = None
    transport_fields['fluxi']['symb'] = None

    transport_fields['fluxn'] = {}
    transport_fields['fluxn']['data'] = None
    transport_fields['fluxn']['name'] = None
    transport_fields['fluxn']['info'] = None
    transport_fields['fluxn']['unit'] = None
    transport_fields['fluxn']['symb'] = None

    transport_fields['fluxm'] = {}
    transport_fields['fluxm']['data'] = None
    transport_fields['fluxm']['name'] = None
    transport_fields['fluxm']['info'] = None
    transport_fields['fluxm']['unit'] = None
    transport_fields['fluxm']['symb'] = None

    transport_fields['fluxe_k'] = {}
    transport_fields['fluxe_k']['data'] = None
    transport_fields['fluxe_k']['name'] = None
    transport_fields['fluxe_k']['info'] = None
    transport_fields['fluxe_k']['unit'] = None
    transport_fields['fluxe_k']['symb'] = None

    transport_fields['fluxi_k'] = {}
    transport_fields['fluxi_k']['data'] = None
    transport_fields['fluxi_k']['name'] = None
    transport_fields['fluxi_k']['info'] = None
    transport_fields['fluxi_k']['unit'] = None
    transport_fields['fluxi_k']['symb'] = None

    transport_fields['fluxn_k'] = {}
    transport_fields['fluxn_k']['data'] = None
    transport_fields['fluxn_k']['name'] = None
    transport_fields['fluxn_k']['info'] = None
    transport_fields['fluxn_k']['unit'] = None
    transport_fields['fluxn_k']['symb'] = None

    transport_fields['fluxm_k'] = {}
    transport_fields['fluxm_k']['data'] = None
    transport_fields['fluxm_k']['name'] = None
    transport_fields['fluxm_k']['info'] = None
    transport_fields['fluxm_k']['unit'] = None
    transport_fields['fluxm_k']['symb'] = None

    transport_fields['fluxe_turb'] = {}
    transport_fields['fluxe_turb']['data'] = None
    transport_fields['fluxe_turb']['name'] = None
    transport_fields['fluxe_turb']['info'] = None
    transport_fields['fluxe_turb']['unit'] = None
    transport_fields['fluxe_turb']['symb'] = None

    transport_fields['fluxi_turb'] = {}
    transport_fields['fluxi_turb']['data'] = None
    transport_fields['fluxi_turb']['name'] = None
    transport_fields['fluxi_turb']['info'] = None
    transport_fields['fluxi_turb']['unit'] = None
    transport_fields['fluxi_turb']['symb'] = None

    transport_fields['fluxn_turb'] = {}
    transport_fields['fluxn_turb']['data'] = None
    transport_fields['fluxn_turb']['name'] = None
    transport_fields['fluxn_turb']['info'] = None
    transport_fields['fluxn_turb']['unit'] = None
    transport_fields['fluxn_turb']['symb'] = None

    transport_fields['fluxm_turb'] = {}
    transport_fields['fluxm_turb']['data'] = None
    transport_fields['fluxm_turb']['name'] = None
    transport_fields['fluxm_turb']['info'] = None
    transport_fields['fluxm_turb']['unit'] = None
    transport_fields['fluxm_turb']['symb'] = None

    transport_fields['fluxe_neo'] = {}
    transport_fields['fluxe_neo']['data'] = None
    transport_fields['fluxe_neo']['name'] = None
    transport_fields['fluxe_neo']['info'] = None
    transport_fields['fluxe_neo']['unit'] = None
    transport_fields['fluxe_neo']['symb'] = None

    transport_fields['fluxi_neo'] = {}
    transport_fields['fluxi_neo']['data'] = None
    transport_fields['fluxi_neo']['name'] = None
    transport_fields['fluxi_neo']['info'] = None
    transport_fields['fluxi_neo']['unit'] = None
    transport_fields['fluxi_neo']['symb'] = None

    transport_fields['fluxn_neo'] = {}
    transport_fields['fluxn_neo']['data'] = None
    transport_fields['fluxn_neo']['name'] = None
    transport_fields['fluxn_neo']['info'] = None
    transport_fields['fluxn_neo']['unit'] = None
    transport_fields['fluxn_neo']['symb'] = None

    transport_fields['fluxm_neo'] = {}
    transport_fields['fluxm_neo']['data'] = None
    transport_fields['fluxm_neo']['name'] = None
    transport_fields['fluxm_neo']['info'] = None
    transport_fields['fluxm_neo']['unit'] = None
    transport_fields['fluxm_neo']['symb'] = None

    transport_fields['qtar_e'] = {}
    transport_fields['qtar_e']['data'] = None
    transport_fields['qtar_e']['name'] = None
    transport_fields['qtar_e']['info'] = None
    transport_fields['qtar_e']['unit'] = None
    transport_fields['qtar_e']['symb'] = None

    transport_fields['qtar_i'] = {}
    transport_fields['qtar_i']['data'] = None
    transport_fields['qtar_i']['name'] = None
    transport_fields['qtar_i']['info'] = None
    transport_fields['qtar_i']['unit'] = None
    transport_fields['qtar_i']['symb'] = None

    transport_fields['qtar_n'] = {}
    transport_fields['qtar_n']['data'] = None
    transport_fields['qtar_n']['name'] = None
    transport_fields['qtar_n']['info'] = None
    transport_fields['qtar_n']['unit'] = None
    transport_fields['qtar_n']['symb'] = None

    transport_fields['qtar_m'] = {}
    transport_fields['qtar_m']['data'] = None
    transport_fields['qtar_m']['name'] = None
    transport_fields['qtar_m']['info'] = None
    transport_fields['qtar_m']['unit'] = None
    transport_fields['qtar_m']['symb'] = None

    transport_fields['gbdiv_e'] = {}
    transport_fields['gbdiv_e']['data'] = None
    transport_fields['gbdiv_e']['name'] = None
    transport_fields['gbdiv_e']['info'] = None
    transport_fields['gbdiv_e']['unit'] = None
    transport_fields['gbdiv_e']['symb'] = None

    transport_fields['gbdiv_i'] = {}
    transport_fields['gbdiv_i']['data'] = None
    transport_fields['gbdiv_i']['name'] = None
    transport_fields['gbdiv_i']['info'] = None
    transport_fields['gbdiv_i']['unit'] = None
    transport_fields['gbdiv_i']['symb'] = None

    transport_fields['gbdiv_n'] = {}
    transport_fields['gbdiv_n']['data'] = None
    transport_fields['gbdiv_n']['name'] = None
    transport_fields['gbdiv_n']['info'] = None
    transport_fields['gbdiv_n']['unit'] = None
    transport_fields['gbdiv_n']['symb'] = None

    transport_fields['gbdiv_v'] = {}
    transport_fields['gbdiv_v']['data'] = None
    transport_fields['gbdiv_v']['name'] = None
    transport_fields['gbdiv_v']['info'] = None
    transport_fields['gbdiv_v']['unit'] = None
    transport_fields['gbdiv_v']['symb'] = None

    return transport_fields

def get_tglf_transport_fields():
    tglf_transport_fields = {}

    tglf_transport_fields['k'] = {}
    tglf_transport_fields['k']['data'] = None
    tglf_transport_fields['k']['name'] = "Order"
    tglf_transport_fields['k']['info'] = "Record Order in Iteration"
    tglf_transport_fields['k']['unit'] = None
    tglf_transport_fields['k']['symb'] = None

    tglf_transport_fields['rho_n'] = {}
    tglf_transport_fields['rho_n']['data'] = None
    tglf_transport_fields['rho_n']['name'] = "Poloidal Magnetic Flux"
    tglf_transport_fields['rho_n']['info'] = None
    tglf_transport_fields['rho_n']['unit'] = None
    tglf_transport_fields['rho_n']['symb'] = "$\\rho_{\\psi_n}$"

    tglf_transport_fields['as0'] = {}
    tglf_transport_fields['as0']['data'] = None
    tglf_transport_fields['as0']['name'] = "Species-0 Array of Densities"
    tglf_transport_fields['as0']['info'] = "Fraction of Species-0 Density to Electron Density"
    tglf_transport_fields['as0']['unit'] = None
    tglf_transport_fields['as0']['symb'] = "$\\frac{n_0}{n_e}$"

    tglf_transport_fields['as1'] = {}
    tglf_transport_fields['as1']['data'] = None
    tglf_transport_fields['as1']['name'] = "Species-1 Array of Densities"
    tglf_transport_fields['as1']['info'] = "Fraction of Species-1 Density to Electron Density"
    tglf_transport_fields['as1']['unit'] = None
    tglf_transport_fields['as1']['symb'] = "$\\frac{n_1}{n_e}$"

    tglf_transport_fields['as2'] = {}
    tglf_transport_fields['as2']['data'] = None
    tglf_transport_fields['as2']['name'] = "Species-2 Array of Densities"
    tglf_transport_fields['as2']['info'] = "Fraction of Species-0 Density to Electron Density"
    tglf_transport_fields['as2']['unit'] = None
    tglf_transport_fields['as2']['symb'] = "$\\frac{n_2}{n_e}$"

    tglf_transport_fields['taus0'] = {}
    tglf_transport_fields['taus0']['data'] = None
    tglf_transport_fields['taus0']['name'] = "Species-0 Array of Temperatures"
    tglf_transport_fields['taus0']['info'] = "Fraction of Species-0 Temperature to Electron Temperature"
    tglf_transport_fields['taus0']['unit'] = None
    tglf_transport_fields['taus0']['symb'] = "$\\frac{T_0}{T_e}$"

    tglf_transport_fields['taus1'] = {}
    tglf_transport_fields['taus1']['data'] = None
    tglf_transport_fields['taus1']['name'] = "Species-1 Array of Temperatures"
    tglf_transport_fields['taus1']['info'] = "Fraction of Species-1 Temperature to Electron Temperature"
    tglf_transport_fields['taus1']['unit'] = None
    tglf_transport_fields['taus1']['symb'] = "$\\frac{T_1}{T_e}$"

    tglf_transport_fields['taus2'] = {}
    tglf_transport_fields['taus2']['data'] = None
    tglf_transport_fields['taus2']['name'] = "Species-2 Array of Temperatures"
    tglf_transport_fields['taus2']['info'] = "Fraction of Species-2 Temperature to Electron Temperature"
    tglf_transport_fields['taus2']['unit'] = None
    tglf_transport_fields['taus2']['symb'] = "$\\frac{T_2}{T_e}$"

    tglf_transport_fields['rlns0'] = {}
    tglf_transport_fields['rlns0']['data'] = None
    tglf_transport_fields['rlns0']['name'] = "Ion Species-0 Normalized Density ($n_0$) Gradients"
    tglf_transport_fields['rlns0']['info'] = "Ion Species-0 Array of Normalized Density ($n_0$) Gradients"
    tglf_transport_fields['rlns0']['unit'] = None
    tglf_transport_fields['rlns0']['symb'] = "$-\\frac{a}{n_0}\\frac{dn_0}{dr}$"

    tglf_transport_fields['rlns1'] = {}
    tglf_transport_fields['rlns1']['data'] = None
    tglf_transport_fields['rlns1']['name'] = "Ion Species-1 Normalized Density ($n_1$) Gradients"
    tglf_transport_fields['rlns1']['info'] = "Ion Species-1 Array of Normalized Density ($n_1$) Gradients"
    tglf_transport_fields['rlns1']['unit'] = None
    tglf_transport_fields['rlns1']['symb'] = "$-\\frac{a}{n_1}\\frac{dn_1}{dr}$"

    tglf_transport_fields['rlns2'] = {}
    tglf_transport_fields['rlns2']['data'] = None
    tglf_transport_fields['rlns2']['name'] = "Ion Species-2 Normalized Density ($n_2$) Gradients"
    tglf_transport_fields['rlns2']['info'] = "Ion Species-2 Array of Normalized Density ($n_2$) Gradients"
    tglf_transport_fields['rlns2']['unit'] = None
    tglf_transport_fields['rlns2']['symb'] = "$-\\frac{a}{n_2}\\frac{dn_2}{dr}$"

    tglf_transport_fields['rlts0'] = {}
    tglf_transport_fields['rlts0']['data'] = None
    tglf_transport_fields['rlts0']['name'] = "Ion Species-0 Normalized Temperature ($T_0$) Gradient"
    tglf_transport_fields['rlts0']['info'] = "Ion Species-0 Array of Normalized Temperature ($T_0$) Gradient"
    tglf_transport_fields['rlts0']['unit'] = None
    tglf_transport_fields['rlts0']['symb'] = "$-\\frac{a}{T_0}\\frac{dT_0}{dr}$"

    tglf_transport_fields['rlts1'] = {}
    tglf_transport_fields['rlts1']['data'] = None
    tglf_transport_fields['rlts1']['name'] = "Ion Species-1 Normalized Temperature ($T_1$) Gradient"
    tglf_transport_fields['rlts1']['info'] = "Ion Species-1 Array of Normalized Temperature ($T_1$) Gradient"
    tglf_transport_fields['rlts1']['unit'] = None
    tglf_transport_fields['rlts1']['symb'] = "$-\\frac{a}{T_1}\\frac{dT_1}{dr}$"

    tglf_transport_fields['rlts2'] = {}
    tglf_transport_fields['rlts2']['data'] = None
    tglf_transport_fields['rlts2']['name'] = "Ion Species-2 Normalized Temperature ($T_2$) Gradient"
    tglf_transport_fields['rlts2']['info'] = "Ion Species-2 Array of Normalized Temperature ($T_1$) Gradient"
    tglf_transport_fields['rlts2']['unit'] = None
    tglf_transport_fields['rlts2']['symb'] = "$-\\frac{a}{T_2}\\frac{dT_2}{dr}$"

    tglf_transport_fields['vpar0'] = {}
    tglf_transport_fields['vpar0']['data'] = None
    tglf_transport_fields['vpar0']['name'] = "Ion Species-0 Parallel Velocities"
    tglf_transport_fields['vpar0']['info'] = "Ion Species-0 Array of Parallel Velocities"
    tglf_transport_fields['vpar0']['unit'] = None
    tglf_transport_fields['vpar0']['symb'] = "$SIGN(I_{tor})\\frac{R_{maj}V_{tor}}{Rc_s_0}$"

    tglf_transport_fields['vpar1'] = {}
    tglf_transport_fields['vpar1']['data'] = None
    tglf_transport_fields['vpar1']['name'] = "Ion Species-1 Parallel Velocities"
    tglf_transport_fields['vpar1']['info'] = "Ion Species-0 Array of Parallel Velocities"
    tglf_transport_fields['vpar1']['unit'] = None
    tglf_transport_fields['vpar1']['symb'] = "$SIGN(I_{tor})\\frac{R_{maj}V_{tor}}{Rc_s_1}$"

    tglf_transport_fields['vpar2'] = {}
    tglf_transport_fields['vpar2']['data'] = None
    tglf_transport_fields['vpar2']['name'] = "Ion Species-2 Parallel Velocities"
    tglf_transport_fields['vpar2']['info'] = "Ion Species-0 Array of Parallel Velocities"
    tglf_transport_fields['vpar2']['unit'] = None
    tglf_transport_fields['vpar2']['symb'] = "$SIGN(I_{tor})\\frac{R_{maj}V_{tor}}{Rc_s_2}$"

    tglf_transport_fields['vpar_shear0'] = {}
    tglf_transport_fields['vpar_shear0']['data'] = None
    tglf_transport_fields['vpar_shear0']['name'] = "Ion Species-0 Normalized Parallel Velocity Gradient"
    tglf_transport_fields['vpar_shear0']['info'] = "Ion Species-0 Normalized Parallel Velocity Gradient"
    tglf_transport_fields['vpar_shear0']['unit'] = None
    tglf_transport_fields['vpar_shear0']['symb'] = "$SIGN{I_{tor}}R_{maj}\\frac{\\partial}{\\partial r}(\\frac{V_{tor}}{R})\\frac{a}{c_s_0}$"

    tglf_transport_fields['vpar_shear1'] = {}
    tglf_transport_fields['vpar_shear1']['data'] = None
    tglf_transport_fields['vpar_shear1']['name'] = "Ion Species-1 Normalized Parallel Velocity Gradient"
    tglf_transport_fields['vpar_shear1']['info'] = "Ion Species-1 Normalized Parallel Velocity Gradient"
    tglf_transport_fields['vpar_shear1']['unit'] = None
    tglf_transport_fields['vpar_shear1']['symb'] = "$SIGN{I_{tor}}R_{maj}\\frac{\\partial}{\\partial r}(\\frac{V_{tor}}{R})\\frac{a}{c_s_1}$"

    tglf_transport_fields['vpar_shear2'] = {}
    tglf_transport_fields['vpar_shear2']['data'] = None
    tglf_transport_fields['vpar_shear2']['name'] = "Ion Species-2 Normalized Parallel Velocity Gradient"
    tglf_transport_fields['vpar_shear2']['info'] = "Ion Species-2 Normalized Parallel Velocity Gradient"
    tglf_transport_fields['vpar_shear2']['unit'] = None
    tglf_transport_fields['vpar_shear2']['symb'] = "$SIGN{I_{tor}}R_{maj}\\frac{\\partial}{\\partial r}(\\frac{V_{tor}}{R})\\frac{a}{c_s_2}$"

    tglf_transport_fields['vexb'] = {}
    tglf_transport_fields['vexb']['data'] = None
    tglf_transport_fields['vexb']['name'] = "Normalized Toroidal ExB Velocity Doppler Shift"
    tglf_transport_fields['vexb']['info'] = "Normalized Toroidal ExB Velocity Doppler Shift"
    tglf_transport_fields['vexb']['unit'] = None
    tglf_transport_fields['vexb']['symb'] = "$\\upsilon_{ExB}$"

    tglf_transport_fields['vexb_shear'] = {}
    tglf_transport_fields['vexb_shear']['data'] = None
    tglf_transport_fields['vexb_shear']['name'] = "Normalized Toroidal ExB Velocity Doppler Shift Gradient"
    tglf_transport_fields['vexb_shear']['info'] = "Normalized Toroidal ExB Velocity Doppler Shift Gradient"
    tglf_transport_fields['vexb_shear']['unit'] = None
    tglf_transport_fields['vexb_shear']['symb'] = "$-SIGN(I_{tor})\\frac{r}{ABS(q)}\\frac{\\partial}{\\partial r}(\\frac{\\upsilon_{ExB}}{R})\\frac{a}{c_s}$"

    tglf_transport_fields['betae'] = {}
    tglf_transport_fields['betae']['data'] = None
    tglf_transport_fields['betae']['name'] = "Normalized Pressure defined with respect to $B_{unit}$"
    tglf_transport_fields['betae']['info'] = "Normalized Pressure defined with respect to $B_{unit}$"
    tglf_transport_fields['betae']['unit'] = None
    tglf_transport_fields['betae']['symb'] = "$\\beta_e$"

    tglf_transport_fields['xnue'] = {}
    tglf_transport_fields['xnue']['data'] = None
    tglf_transport_fields['xnue']['name'] = "Normalized Electron-Ion Collision Frequency"
    tglf_transport_fields['xnue']['info'] = "Normalzied Electron-Ion Collision Frequency"
    tglf_transport_fields['xnue']['unit'] = None
    tglf_transport_fields['xnue']['symb'] = "$\\frac{\\upsilon_{ei}}{c_s/a}$"

    tglf_transport_fields['zeff'] = {}
    tglf_transport_fields['zeff']['data'] = None
    tglf_transport_fields['zeff']['name'] = "Effective Ion Charge"
    tglf_transport_fields['zeff']['info'] = "Effective Ion Charge"
    tglf_transport_fields['zeff']['unit'] = None
    tglf_transport_fields['zeff']['symb'] = "$Z_{eff}$"

    tglf_transport_fields['debye'] = {}
    tglf_transport_fields['debye']['data'] = None
    tglf_transport_fields['debye']['name'] = "Debye Length/Gyroradius"
    tglf_transport_fields['debye']['info'] = "Debye Length/Gyroradius"
    tglf_transport_fields['debye']['unit'] = None
    tglf_transport_fields['debye']['symb'] = "$\\frac{\\lambda}{\\rho_{ce}}$"

    tglf_transport_fields['beta_loc'] = {}
    tglf_transport_fields['beta_loc']['data'] = None
    tglf_transport_fields['beta_loc']['name'] = None
    tglf_transport_fields['beta_loc']['info'] = None
    tglf_transport_fields['beta_loc']['unit'] = None
    tglf_transport_fields['beta_loc']['symb'] = None

    tglf_transport_fields['rmin_loc'] = {}
    tglf_transport_fields['rmin_loc']['data'] = None
    tglf_transport_fields['rmin_loc']['name'] = "Flux Surface Centroid Minor Radius"
    tglf_transport_fields['rmin_loc']['info'] = "Flux Surface Centroid Minor Radius"
    tglf_transport_fields['rmin_loc']['unit'] = None
    tglf_transport_fields['rmin_loc']['symb'] = "$r/a$"

    tglf_transport_fields['rmaj_loc'] = {}
    tglf_transport_fields['rmaj_loc']['data'] = None
    tglf_transport_fields['rmaj_loc']['name'] = "Flux Surface Centroid Major Radius"
    tglf_transport_fields['rmaj_loc']['info'] = "Flux Surface Centroid Major Radius"
    tglf_transport_fields['rmaj_loc']['unit'] = None
    tglf_transport_fields['rmaj_loc']['symb'] = "$R_{maj}/a$"

    tglf_transport_fields['zmaj_loc'] = {}
    tglf_transport_fields['zmaj_loc']['data'] = None
    tglf_transport_fields['zmaj_loc']['name'] = "Flux Surface Centroid Elevation"
    tglf_transport_fields['zmaj_loc']['info'] = "Flux Surface Centroid Elevation"
    tglf_transport_fields['zmaj_loc']['unit'] = None
    tglf_transport_fields['zmaj_loc']['symb'] = "$Z_{maj}/a$"

    tglf_transport_fields['drmindx_loc'] = {}
    tglf_transport_fields['drmindx_loc']['data'] = None
    tglf_transport_fields['drmindx_loc']['name'] = None
    tglf_transport_fields['drmindx_loc']['info'] = None
    tglf_transport_fields['drmindx_loc']['unit'] = None
    tglf_transport_fields['drmindx_loc']['symb'] = "$\\frac{\\partial r}{\\partial x}$"

    tglf_transport_fields['drmajdx_loc'] = {}
    tglf_transport_fields['drmajdx_loc']['data'] = None
    tglf_transport_fields['drmajdx_loc']['name'] = None
    tglf_transport_fields['drmajdx_loc']['info'] = None
    tglf_transport_fields['drmajdx_loc']['unit'] = None
    tglf_transport_fields['drmajdx_loc']['symb'] = "$\\frac{\\partial R_{maj}}{\\partial x}$"

    tglf_transport_fields['dzmajdx_loc'] = {}
    tglf_transport_fields['dzmajdx_loc']['data'] = None
    tglf_transport_fields['dzmajdx_loc']['name'] = None
    tglf_transport_fields['dzmajdx_loc']['info'] = None
    tglf_transport_fields['dzmajdx_loc']['unit'] = None
    tglf_transport_fields['dzmajdx_loc']['symb'] = "$\\frac{\\partial Z_{maj}}{\\partial x}$"

    tglf_transport_fields['kappa_loc'] = {}
    tglf_transport_fields['kappa_loc']['data'] = None
    tglf_transport_fields['kappa_loc']['name'] = "Elongation of Flux Surface"
    tglf_transport_fields['kappa_loc']['info'] = "Elongation of Flux Surface"
    tglf_transport_fields['kappa_loc']['unit'] = None
    tglf_transport_fields['kappa_loc']['symb'] = "$\\kappa$"

    tglf_transport_fields['s_kappa_loc'] = {}
    tglf_transport_fields['s_kappa_loc']['data'] = None
    tglf_transport_fields['s_kappa_loc']['name'] = "Shear in Elongation"
    tglf_transport_fields['s_kappa_loc']['info'] = "Shear in Elongation"
    tglf_transport_fields['s_kappa_loc']['unit'] = None
    tglf_transport_fields['s_kappa_loc']['symb'] = "$\\frac{r}{\\kappa}\\frac{\\partial{\\kappa}}{\\partial{r}}$"

    tglf_transport_fields['delta_loc'] = {}
    tglf_transport_fields['delta_loc']['data'] = None
    tglf_transport_fields['delta_loc']['name'] = "Triangularity of Flux Surface"
    tglf_transport_fields['delta_loc']['info'] = "Triangularity of Flux Surface"
    tglf_transport_fields['delta_loc']['unit'] = None
    tglf_transport_fields['delta_loc']['symb'] = "$\\delta$"

    tglf_transport_fields['s_delta_loc'] = {}
    tglf_transport_fields['s_delta_loc']['data'] = None
    tglf_transport_fields['s_delta_loc']['name'] = "Shear in Triangularity"
    tglf_transport_fields['s_delta_loc']['info'] = None
    tglf_transport_fields['s_delta_loc']['unit'] = None
    tglf_transport_fields['s_delta_loc']['symb'] = 

    tglf_transport_fields['zeta_loc'] = {}
    tglf_transport_fields['zeta_loc']['data'] = None
    tglf_transport_fields['zeta_loc']['name'] = "Squarness of Flux Surface"
    tglf_transport_fields['zeta_loc']['info'] = "Squarness of Flux Surface"
    tglf_transport_fields['zeta_loc']['unit'] = None
    tglf_transport_fields['zeta_loc']['symb'] = "$\\zeta$"

    tglf_transport_fields['s_zeta_loc'] = {}
    tglf_transport_fields['s_zeta_loc']['data'] = None
    tglf_transport_fields['s_zeta_loc']['name'] = "Shear of Squarness"
    tglf_transport_fields['s_zeta_loc']['info'] = "Shear of Squarness"
    tglf_transport_fields['s_zeta_loc']['unit'] = None
    tglf_transport_fields['s_zeta_loc']['symb'] = "$r\\frac{\\partial\\zeta}{\\partial r}$"

    tglf_transport_fields['q_loc'] = {}
    tglf_transport_fields['q_loc']['data'] = None
    tglf_transport_fields['q_loc']['name'] = "Absolute Value of Safety Factor"
    tglf_transport_fields['q_loc']['info'] = "Absolute Value of Safety Factor"
    tglf_transport_fields['q_loc']['unit'] = None
    tglf_transport_fields['q_loc']['symb'] = "$|q|$"

    tglf_transport_fields['q_prime_loc'] = {}
    tglf_transport_fields['q_prime_loc']['data'] = None
    tglf_transport_fields['q_prime_loc']['name'] = None
    tglf_transport_fields['q_prime_loc']['info'] = None
    tglf_transport_fields['q_prime_loc']['unit'] = None
    tglf_transport_fields['q_prime_loc']['symb'] = "$\\frac{q^2a^2}{r^2}\\hat{s}$"

    tglf_transport_fields['p_prime_loc'] = {}
    tglf_transport_fields['p_prime_loc']['data'] = None
    tglf_transport_fields['p_prime_loc']['name'] = None
    tglf_transport_fields['p_prime_loc']['info'] = None
    tglf_transport_fields['p_prime_loc']['unit'] = None
    tglf_transport_fields['p_prime_loc']['symb'] = "$\\frac{qa^2}{rB^2_{unit}}\\frac{\\partial p}{\\partial r}$"

    tglf_transport_fields['rmin_sa'] = {}
    tglf_transport_fields['rmin_sa']['data'] = None
    tglf_transport_fields['rmin_sa']['name'] = "Normalized Minor Radius of Flux Surface"
    tglf_transport_fields['rmin_sa']['info'] = "Normalized Minor Radius of Flux Surface"
    tglf_transport_fields['rmin_sa']['unit'] = None
    tglf_transport_fields['rmin_sa']['symb'] = "$r\a$"

    tglf_transport_fields['rmaj_sa'] = {}
    tglf_transport_fields['rmaj_sa']['data'] = None
    tglf_transport_fields['rmaj_sa']['name'] = "Normalized Major Radius of Flux Surface"
    tglf_transport_fields['rmaj_sa']['info'] = "Normalized Major Radius of Flux Surface"
    tglf_transport_fields['rmaj_sa']['unit'] = None
    tglf_transport_fields['rmaj_sa']['symb'] = "$R_{maj}/a$"

    tglf_transport_fields['q_sa'] = {}
    tglf_transport_fields['q_sa']['data'] = None
    tglf_transport_fields['q_sa']['name'] = "Absolute Value of Safety Factor"
    tglf_transport_fields['q_sa']['info'] = "Absolute Value of Safety Factor"
    tglf_transport_fields['q_sa']['unit'] = None
    tglf_transport_fields['q_sa']['symb'] = "$|q|$"

    tglf_transport_fields['shat_sa'] = {}
    tglf_transport_fields['shat_sa']['data'] = None
    tglf_transport_fields['shat_sa']['name'] = "Magnetic Shear"
    tglf_transport_fields['shat_sa']['info'] = "Magnetic Shear"
    tglf_transport_fields['shat_sa']['unit'] = None
    tglf_transport_fields['shat_sa']['symb'] = "$\\hat{s}$"

    tglf_transport_fields['alpha_sa'] = {}
    tglf_transport_fields['alpha_sa']['data'] = None
    tglf_transport_fields['alpha_sa']['name'] = "Normalized Pressure Gradient"
    tglf_transport_fields['alpha_sa']['info'] = "Normalized Pressure Gradient"
    tglf_transport_fields['alpha_sa']['unit'] = None
    tglf_transport_fields['alpha_sa']['symb'] = "$\\alpha$"

    tglf_transport_fields['xwell_sa'] = {}
    tglf_transport_fields['xwell_sa']['data'] = None
    tglf_transport_fields['xwell_sa']['name'] = "Magnetic Well"
    tglf_transport_fields['xwell_sa']['info'] = "Magnetic Well"
    tglf_transport_fields['xwell_sa']['unit'] = None
    tglf_transport_fields['xwell_sa']['symb'] = "$\\chi_{well}$"

    tglf_transport_fields['fluxe'] = {}
    tglf_transport_fields['fluxe']['data'] = None
    tglf_transport_fields['fluxe']['name'] = "Electron Thermal Flux"
    tglf_transport_fields['fluxe']['info'] = "Electron Thermal Flux"
    tglf_transport_fields['fluxe']['unit'] = None
    tglf_transport_fields['fluxe']['symb'] = "$\\Gamma_e$"

    tglf_transport_fields['fluxi'] = {}
    tglf_transport_fields['fluxi']['data'] = None
    tglf_transport_fields['fluxi']['name'] = "Ion Thermal Flux"
    tglf_transport_fields['fluxi']['info'] = "Ion Thermal Flux"
    tglf_transport_fields['fluxi']['unit'] = None
    tglf_transport_fields['fluxi']['symb'] = "$\\Gamma_i$"

    tglf_transport_fields['fluxn'] = {}
    tglf_transport_fields['fluxn']['data'] = None
    tglf_transport_fields['fluxn']['name'] = "Particle Flux"
    tglf_transport_fields['fluxn']['info'] = "Particle Flux"
    tglf_transport_fields['fluxn']['unit'] = None
    tglf_transport_fields['fluxn']['symb'] = "$\\Gamma_n$"

    tglf_transport_fields['fluxv'] = {}
    tglf_transport_fields['fluxv']['data'] = None
    tglf_transport_fields['fluxv']['name'] = "Velocity Flux"
    tglf_transport_fields['fluxv']['info'] = "Velocity Flux"
    tglf_transport_fields['fluxv']['unit'] = None
    tglf_transport_fields['fluxv']['symb'] = "$\\Gamma_v$"

    tglf_transport_fields['chie'] = {}
    tglf_transport_fields['chie']['data'] = None
    tglf_transport_fields['chie']['name'] = "Electron Thermal Diffusivity"
    tglf_transport_fields['chie']['info'] = "Electron Thermal Diffusivity"
    tglf_transport_fields['chie']['unit'] = None
    tglf_transport_fields['chie']['symb'] = "$D_e$"

    tglf_transport_fields['chii'] = {}
    tglf_transport_fields['chii']['data'] = None
    tglf_transport_fields['chii']['name'] = "Ion Thermal Diffusivity"
    tglf_transport_fields['chii']['info'] = "Ion Thermal Diffusivity"
    tglf_transport_fields['chii']['unit'] = None
    tglf_transport_fields['chii']['symb'] = "$D_i$"

    tglf_transport_fields['chin'] = {}
    tglf_transport_fields['chin']['data'] = None
    tglf_transport_fields['chin']['name'] = "Particle Diffusivity"
    tglf_transport_fields['chin']['info'] = "Particle Diffusivity"
    tglf_transport_fields['chin']['unit'] = None
    tglf_transport_fields['chin']['symb'] = "$\\chi_n$"

    tglf_transport_fields['chiv'] = {}
    tglf_transport_fields['chiv']['data'] = None
    tglf_transport_fields['chiv']['name'] = "Velocity Diffusivity"
    tglf_transport_fields['chiv']['info'] = "Velocity Diffusivity"
    tglf_transport_fields['chiv']['unit'] = None
    tglf_transport_fields['chiv']['symb'] = "$\\chi_v$"

    return tglf_transport_fields

def read_tglf_io_file(path_to_file):
    tglf_transport_fields = get_tglf_transport_fields()
    tglf_transport_fields_names = list(tglf_transport_fields.keys())

    if os.path.isdir(path_to_file):
       path_to_file = os.path.join(path_to_file,"tglf_io.dat")

    fhands = open(path_to_file, "r")
    contents = fhands.readlines()
    nlines = len(contents)
    fhands.close()

    tglf_transport_timetrace_fields = {}

    iline = 0
    while True:
        content = contents[iline].split()
        if 'step' in content:
           step = content[2]
           iter = content[4]
           nrec = int(content[5].split('=')[1])-1

           if step not in tglf_transport_timetrace_fields:       tglf_transport_timetrace_fields[step] = {}
           if iter not in tglf_transport_timetrace_fields[step]: tglf_transport_timetrace_fields[step][iter] = copy.deepcopy(tglf_transport_fields)

           iline += 1
           fields = contents[iline].split()
           for irec in range(nrec):
               iline += 1
               content = contents[iline].split()
               for fld_name in tglf_transport_fields_names:
                    fld_ind = tglf_transport_fields_names.index(fld_name)
                    if type(tglf_transport_timetrace_fields[step][iter][fld_name]['data']) == type_none: tglf_transport_timetrace_fields[step][iter][fld_name]['data'] =      [float(content[fld_ind])]
                    else:                                                                                tglf_transport_timetrace_fields[step][iter][fld_name]['data'].extend([float(content[fld_ind])])
        iline += 1
        if iline >= nlines: break

    return tglf_transport_timetrace_fields

def plot_tglf_io_file(path_to_file,**kwargs):
    if os.path.isdir(path_to_file):
       path_to_file = os.path.join(path_to_file,"tglf_io.dat")
    tglf_transport_timetrace_fields = read_tglf_io_file(path_to_file)

    steps = list(tglf_transport_timetrace_fields.keys())
    nsteps= len(steps)
    for step in steps:
        iters = list(tglf_transport_timetrace_fields[step].keys())
        niters= len(iters)
        fields = list(tglf_transport_timetrace_fields[step][iters[0]].keys())
        nfields = len(fields)

    if 'step_stride' in kwargs: step_stride = kwargs['step_stride']
    else:                       step_stride = 1
    if 'iter_stride' in kwargs: iter_stride = kwargs['iter_stride']
    else:                       iter_stride = 1

    fgs = []
    for field in fields[2:]:
        fg = plt.figure(field,dpi=100)
        ax = fg.add_subplot(111)
        for step in steps[::step_stride]:
            for iter in iters[::iter_stride]:
                ax.plot(tglf_transport_timetrace_fields[step][iter]['rho_n']['data'],tglf_transport_timetrace_fields[step][iter][field]['data'],label=iter,alpha=0.5)
	
        if tglf_transport_timetrace_fields[step][iter][field]['name']: ax.set_title(tglf_transport_timetrace_fields[step][iter][field]['name'],fontsize=15)
        ylabel_symb = tglf_transport_timetrace_fields[step][iter][field]['symb']
        ylabel_unit = tglf_transport_timetrace_fields[step][iter][field]['unit']
        ylabel_name = tglf_transport_timetrace_fields[step][iter][field]['name']
        ylabel = ""
        if   type(ylabel_symb) != type_none: ylabel = ylabel + ylabel_symb
        elif type(ylabel_name) != type_none: ylabel = ylabel + ylabel_name
        else:                                ylabel = ylabel + field
        if   type(ylabel_unit) != type_none: ylabel = ylabel + " [" + ylabel_unit + "]"
        ax.set_ylabel("%s" % ylabel,fontsize=12)
        ax.set_xlabel("$\\rho_n$")
        ax.legend(ncol=3,fontsize=8)
        fgs.append(fg)
        plt.close(fg)

    fname = 'tglf_io'
    if 'fname' in kwargs: fname = kwargs['fname'] + "_" + fname
    to_pdf(fgs,fname=fname)

    return tglf_transport_timetrace_fields

def plot_transport_conv_file(path_to_file,**kwargs):
    if os.path.isdir(path_to_file):
       path_to_file = os.path.join(path_to_file,"transport_conv.dat")
    transport_timetrace_errors,transport_timetrace_fields = read_transport_conv_file(path_to_file)

    steps = list(transport_timetrace_fields.keys())
    nsteps= len(steps)
    for step in steps:
        iters = list(transport_timetrace_fields[step].keys())
        niters= len(iters)
        fields = list(transport_timetrace_fields[step][iters[0]].keys())
        nfields = len(fields)

    if 'step_stride' in kwargs: step_stride = kwargs['step_stride']
    else:                       step_stride = 1
    if 'iter_stride' in kwargs: iter_stride = kwargs['iter_stride']
    else:                       iter_stride = 1

    fg_errors, ax_errors = plt.subplots(nrows=3,ncols=1,sharex=True,num='errors',dpi=100)
    for step in steps[::step_stride]:
        ax_errors[0].plot(transport_timetrace_errors[step]['res_e']['data'])
        ax_errors[1].plot(transport_timetrace_errors[step]['res_i']['data'])
        ax_errors[2].plot(transport_timetrace_errors[step]['res_n']['data'])

    fname = 'errors'
    if 'fname' in kwargs: fname = kwargs['fname'] + "_" + fname
    to_pdf(fg_errors,fname=fname)

    fgs_trans = []
    for field in fields[2:]:
        fg_trans = plt.figure(field,dpi=100)
        ax_trans = fg_trans.add_subplot(111)
        for step in steps[::step_stride]:
            for iter in iters[::iter_stride]:
                ax_trans.plot(transport_timetrace_fields[step][iter]['rho_n']['data'],transport_timetrace_fields[step][iter][field]['data'],label=iter,alpha=0.5)
        if transport_timetrace_fields[step][iter][field]['name']: ax_trans.set_title(transport_timetrace_fields[step][iter][field]['name'])
        if transport_timetrace_fields[step][iter][field]['unit']:
           ax_trans.set_ylabel("%s [%s]" % (field,transport_timetrace_fields[step][iter][field]['unit']))
        else:
           ax_trans.set_ylabel("%s" % field)
        ax_trans.set_xlabel("rho")
        ax_trans.legend(ncol=3,fontsize=8)
        fgs_trans.append(fg_trans)
        plt.close(fg_trans)
    
    fname = 'transport'
    if 'fname' in kwargs: fname = kwargs['fname'] + "_" + fname
    to_pdf(fgs_trans,fname=fname)

    return transport_timetrace_errors,transport_timetrace_fields


if __name__=="__main__": 
   path_to_files = sys.argv[1:]

   for path_to_file in path_to_files:
      #transport_errors,transport_fields = read_transport_conv_file(path_to_file)
      #tglf_transport_fields = read_tglf_io_file(path_to_file)
       transport_errors,transport_fields = plot_transport_conv_file(path_to_file,step_stride=10,iter_stride=20,fname="diiid_106740_15300")
       tglf_transport_fields = plot_tglf_io_file(path_to_file,step_stride=10,iter_stride=20,fname="diiid_106740_15300")
#      print(tglf_transport_fields['0']['99']['rho_n']['data'])
#      nlines = get_line_count(path_to_file)
#      print(nlines)

# step 0 iter 0  res_e=5.948e-03 res_i=6.124e-02 res_n=1.763e+04 res_v=0.000e+00  nrho_tr=50
