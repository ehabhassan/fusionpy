#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import re
#import os
import sys

import numpy       as npy
#import traceback   as traceback

from Namelist                     import Namelist
from iofiles.fastran.read_fastran import read_fastran
#from fastran.equilibrium import cheasetools
from maths.profile_fit import snyder_fit

#from scipy.optimize    import curve_fit
#from scipy.integrate   import trapz,simps
#from scipy.interpolate import interp1d,interp2d
#from scipy.interpolate import CubicSpline,RectBivariateSpline

#from fastran.plasmastate.plasmastate import plasmastate

if   sys.version_info.major == 3:
     PYTHON3 = True; PYTHON2 = False
elif sys.version_info.major == 2:
     PYTHON2 = True; PYTHON3 = False

mu0 = 4.0e-7*npy.pi

def get_plasmastate(instatefpath="",statefpath="",bcfpath="",eqfpath='',setParam={}):

    if 'mode' in setParam: mode = setParam['mode']
    else:                  mode = 'kinetic'

    if 'init_run' in setParam: init_run = setParam['init_run']
    else:                      init_run = True

    if 'betan_target' in setParam: betan_target = setparam['betan_target']
    else:                          betan_target = -1.0

    statedata = {}

    if bcfpath:
        inbc = Namelist(bcfpath)["inbc"]

        statedata['ip']     = abs(inbc['ip'][0])*1.0e6
        statedata['RCTR']   = abs(inbc["r0"][0])
        statedata['BCTR']   = abs(inbc["b0"][0])
        statedata['nlim']   = inbc["nlim"][0]
        statedata['rlim']   = inbc["rlim"][:]
        statedata['zlim']   = inbc["zlim"][:]
        statedata['nbound'] = inbc["nbdry"][0]
        statedata['rbound'] = inbc["rbdry"][:]
        statedata['zbound'] = inbc["zbdry"][:]
    elif eqfpath:
        eqdskdata = read_eqdsk(fpath=eqfpath)

        statedata['ip']     = abs(eqdskdata['CURNT'])
        statedata['RCTR']   = abs(eqdskdata['RCTR'])
        statedata['BCTR']   = abs(eqdskdata['BCTR'])
        statedata['RMAX']   = eqdskdata['RMAX']
        statedata['ZMAX']   = eqdskdata['ZMAX']
        statedata['nlim']   = eqdskdata['nlimit']
        statedata['rlim']   = eqdskdata["rlimit"]
        statedata['zlim']   = eqdskdata["zlimit"]
        statedata['nbound'] = eqdskdata["nbound"]
        statedata['rbound'] = eqdskdata["rbound"]
        statedata['zbound'] = eqdskdata["zbound"]

    if 'rbound' in statedata:
        Zmidl  = (max(statedata['zbound']) + min(statedata['zbound'])) / 2.0
        major  = (max(statedata['rbound']) + min(statedata['rbound'])) / 2.0
        minor  = (max(statedata['rbound']) - min(statedata['rbound'])) / 2.0
        kappa  = (max(statedata['zbound']) - min(statedata['zbound'])) / 2.0 / minor
        delta  = 2.0*major 
        delta -= statedata['rbound'][npy.argmax(statedata['zbound'])]
        delta -= statedata['rbound'][npy.argmin(statedata['zbound'])]
        delta /= (2.0*minor)

        statedata['ASPCT']  = minor/major
        statedata['ELONG']  = kappa
        statedata['TRIANG'] = delta

    if instatefpath:
        instate = Namelist(instatefpath)['instate']

        if not statedata['ip']:
            statedata['ip']     = instate["ip"][0]*1.0e6
        if not statedata['RCTR']:
            statedata['RCTR']   = instate["r0"][0]
        if not statedata['BCTR']:
            statedata['BCTR']   = abs(instate["b0"][0])
        if not statedata['nlim']:
            if instate["nlim" ]:
                statedata['nlim']   = instate["nlim" ][0]
                statedata['rlim']   = npy.array(instate["rlim" ])
                statedata['zlim']   = npy.array(instate["zlim" ])
        if not statedata['nbound']:
            if instate["nbdry"]:
                statedata['nbound'] = instate["nbdry"][0]
                statedata['rbound'] = npy.array(instate["rbdry"])
                statedata['zbound'] = npy.array(instate["zbdry"])

        statedata['nrho']   = instate['nrho'][0]
        if instate['rho']:
            statedata['rho'] = npy.array(instate['rho'])
        else:
           #statedata['rho'] = npy.array(npy.arange(statedata['nrho'])/(statedata['nrho']-1.0))
            statedata['rho'] = npy.linspace(0.0,1.0,statedata['nrho'])

        if instate['ne']:
            statedata['ne']     = npy.array(instate['ne'])
        elif instate['ne_axis']:
            statedata['ne']     = cheaseprofit.snyder_fit(rho        = statedata['rho'],
                                                           alpha      = instate['ne_alpha'][0],
                                                           ped_mid    = instate['ne_xmid'][0],
                                                           ped_width  = instate['ne_xwid'][0],
                                                           ped_height = instate['ne_ped'][0],
                                                           ped_sol    = instate['ne_sep'][0],
                                                           cor_exp    = instate['ne_beta'][0],
                                                           cor_height = instate['ne_axis'][0],
                                                           cor_width  = 0)
        if instate['Te']:
            statedata['Te']     = npy.array(instate['te'])*1.602e3
        elif instate['Te_axis']:
            statedata['Te']     = cheaseprofit.snyder_fit(rho        = statedata['rho'],
                                                           alpha      = instate['te_alpha'][0],
                                                           ped_mid    = instate['te_xmid'][0],
                                                           ped_width  = instate['te_xwid'][0],
                                                           ped_height = instate['te_ped'][0],
                                                           ped_sol    = instate['te_sep'][0],
                                                           cor_exp    = instate['te_beta'][0],
                                                           cor_height = instate['te_axis'][0],
                                                           cor_width  = 0)*1.602e3
        if instate['Ti']:
            statedata['Ti']     = npy.array(instate['ti'])*1.602e3
        elif instate['Ti_axis']:
            statedata['Ti']     = cheaseprofit.snyder_fit(rho        = statedata['rho'],
                                                           alpha      = instate['ti_alpha'][0],
                                                           ped_mid    = instate['ti_xmid'][0],
                                                           ped_width  = instate['ti_xwid'][0],
                                                           ped_height = instate['ti_ped'][0],
                                                           ped_sol    = instate['ti_sep'][0],
                                                           cor_exp    = instate['ti_beta'][0],
                                                           cor_height = instate['ti_axis'][0],
                                                           cor_width  = 0)*1.602e3
        if instate['zeff']:
            statedata['zeff']   = npy.array(instate['zeff'])
        elif instate['zeff_axis']:
            statedata['zeff']   = instate['zeff_axis'][0] * npy.ones(statedata['nrho'])

        if instate['ffprime']:
            statedata['ffprime']= npy.array(instate['ffprime'])

        if instate['j_tot']:
            statedata['jpar']   = npy.array(instate['j_tot'])
        elif instate['jpar_axis']:
            statedata['jpar']   = (instate['jpar_axis'][0] - instate['jpar_sep'][0])
            statedata['jpar']  *= (1.0 - statedata['rho']**instate['jpar_alpha'][0])**instate['jpar_beta'][0]
            statedata['jpar']  += instate['jpar_sep'][0]
        statedata['jpar'] *= 1.0e6
        if all(statedata['jpar'] < 0): statedata['jpar'] *= -1.0

        if instate['wbeam']:
            statedata['wbeam']  = npy.array(instate['wbeam'])
        else:
            statedata['wbeam']  = npy.zeros(statedata['nrho'])

        if instate['walpha']:
            statedata['walpha'] = npy.array(instate['walpha'])
        else:
            statedata['walpha'] = npy.zeros(statedata['nrho'])

        if instate['density_alpha']:
            statedata['nalpha'] = npy.array(instate['density_alpha'])
        else:
            statedata['nalpha'] = npy.zeros(statedata['nrho'])

        if instate['density_beam']: 
            statedata['nbfast'] = npy.array(instate['density_beam'])
        elif instate['nbeam_axis']:
            statedata['nbfast'] = (instate['nbeam_axis'][0]-instate['nbeam_sep'][0])
            statedata['nbfast']*= (1.0 - statedata['rho']**instate['nbeam_alpha'][0])**instate['nbeam_beta'][0]
            statedata['nbfast']+= instate['nbeam_sep'][0]
        else:
            statedata['nbfast'] = npy.zeros(statedata['nrho'])

        if instate['omega']:
            statedata['omega']  = npy.array(instate['omega'])
        elif instate['omega_axis']:
            statedata['omega']  = (instate['omega_axis'][0]-instate['omega_sep'][0])
            statedata['omega'] *= (1.0 - statedata['rho']**instate['omega_alpha'][0])**instate['omega_beta'][0]
            statedata['omega'] += instate['omega_sep'][0]
        else:
            statedata['omega']  = npy.zeros(statedata['nrho'])

        n_ion  =           instate['n_ion'][0]
        z_ion  = npy.array(instate['z_ion'])
        a_ion  = npy.array(instate['a_ion'])
        f_ion  = npy.array(instate['f_ion'])

        n_imp  =           instate['n_imp'][0]
        z_imp  = npy.array(instate['z_imp'])
        a_imp  = npy.array(instate['a_imp'])
        f_imp  = npy.array(instate['f_imp'])

        z_ion  = npy.dot(z_ion,f_ion) * npy.ones(statedata['nrho'])
        a_ion  = npy.dot(a_ion,f_ion)

        z_imp  = npy.dot(z_imp,f_imp) * npy.ones(statedata['nrho'])
        a_imp  = npy.dot(a_imp,f_imp)

        nhe    = npy.zeros(statedata['nrho'])

        if instate['ni']:
            statedata['ni']     = npy.array(instate['ni'])
        elif instate['ni_axis']:
            statedata['ni']     = cheaseprofit.snyder_fit(rho        = statedata['rho'],
                                                           alpha      = instate['ni_alpha'][0],
                                                           ped_mid    = instate['ni_xmid'][0],
                                                           ped_width  = instate['ni_xwid'][0],
                                                           ped_height = instate['ni_ped'][0],
                                                           ped_sol    = instate['ni_sep'][0],
                                                           cor_exp    = instate['ni_beta'][0],
                                                           cor_height = instate['ni_axis'][0],
                                                           cor_width  = 0)
        else:
            statedata['ni']  = z_imp**2 * (statedata['ne']                     - statedata['nbfast'] - 2.0*(statedata['nalpha'] + nhe))
            statedata['ni'] -= z_imp    * (statedata['ne'] * statedata['zeff'] - statedata['nbfast'] - 4.0*(statedata['nalpha'] + nhe))
            statedata['ni'] /= z_imp * z_ion * (z_imp - z_ion)

        if instate['nz']:
            statedata['nz']     = npy.array(instate['nz'])
        elif instate['nz_axis']:
            statedata['nz']     = cheaseprofit.snyder_fit(rho        = statedata['rho'],
                                                           alpha      = instate['nz_alpha'][0],
                                                           ped_mid    = instate['nz_xmid'][0],
                                                           ped_width  = instate['nz_xwid'][0],
                                                           ped_height = instate['nz_ped'][0],
                                                           ped_sol    = instate['nz_sep'][0],
                                                           cor_exp    = instate['nz_beta'][0],
                                                           cor_height = instate['nz_axis'][0],
                                                           cor_width  = 0)
        else:
            statedata['nz']  = statedata['ne'] * (statedata['zeff'] - 1.0) - 2.0*(statedata['nalpha'] + nhe)
            statedata['nz'] /= z_imp * z_ion * (z_imp - z_ion)

        if mode == 'kinetic':
           statedata['pressure']  = statedata['ne'] * statedata['Te'] + (statedata['ni'] + statedata['nz']) * statedata['Ti']
           statedata['pressure'] += (2.0/3.0) * 1.0e6*(statedata['wbeam'] + statedata['walpha'])
        else:
            if instate['p_eq'] and npy.all(npy.array(instate['p_eq'])):
               statedata['pressure'] = npy.array(instate['p_eq'])
            elif instate['pmhd'] and npy.all(npy.array(instate['pmhd'])):
               statedata['pressure'] = npy.array(instate['pmhd'])
            elif instate['ptot_axis']:
               statedata['pressure']  = (instate['ptot_axis'][0]-instate['ptot_sep'][0])
               statedata['pressure'] *= (1.0 - statedata['rho']**instate['ptot_alpha'][0])**instate['ptot_beta'][0]
               statedata['pressure'] += instate['ptot_sep'][0]
            else:
               statedata['pressure']  = npy.zeros(statedata['nrho'])
        if all(statedata['pressure'] < 0): statedata['pressure'] *= -1.0

        statedata['ne'] *= 1.0e19
        statedata['ni'] *= 1.0e19
        statedata['nz'] *= 1.0e19

    elif statefpath:
        if type(statefpath) == str:
            ps = plasmastate('ips',1)
            ps.read(statefpath)
        else:
            ps = self.statefpath

        if 'RMAX' not in statedata:
            statedata['RMAX']  = ps['R_axis']
        if 'ZMAX' not in statedata:
            statedata['ZMAX']  = ps['Z_axis']

        if 'rlim' not in statedata:
            statedata['rlim'] = ps['rlim']
        if 'zlim' not in statedata:
            statedata['zlim'] = ps['zlim']

        statedata['RLFT']  = min(statedata['rlim'])
        statedata['RLEN']  = max(statedata['rlim']) - min(statedata['rlim'])
        statedata['ZLEN']  = max(statedata['zlim']) - min(statedata['zlim'])
        statedata['ZMID']  =(max(statedata['zlim']) + min(statedata['zlim']))/2.0

        species_name = ps['S_name']
        species_type = ps['S_type']

        statedata['nrho'] = len(ps["rho"])
        statedata['rho']  =     ps['rho'][:]

        n_ion = 0
        n_imp = 0
        statedata['ni']   = npy.zeros(statedata['nrho'])
        statedata['nz']   = npy.zeros(statedata['nrho'])
        statedata['Ti']   = npy.zeros(statedata['nrho'])
        statedata['Tz']   = npy.zeros(statedata['nrho'])
        statedata['zeff'] = npy.zeros(statedata['nrho'])
        for s in range(npy.size(ps["q_s"])):
            if   species_name[s].strip().lower() in ['e']:
                 statedata['Te']    = ps.cell2node(ps["Ts"][s,:]*1.602e3)
                 statedata['ne']    = ps.cell2node(ps["ns"][s,:])
            elif species_name[s].strip().lower() in ['d','t']:
                 statedata['Ti']   += ps.cell2node(ps["Ts"][s,:]*1.602e3)
                 statedata['ni']   += ps.cell2node(ps["ns"][s,:])
                 statedata['zeff'] += ps.cell2node(ps["ns"][s,:])*(ps["q_s"][s]/abs(ps["q_s"][0]))**2
                 n_ion             += 1
            else:
                 statedata['Tz']   += ps.cell2node(ps["Ts"][s,:]*1.602e3)
                 statedata['nz']   += ps.cell2node(ps["ns"][s,:])
                 statedata['zeff'] += ps.cell2node(ps["ns"][s,:])*(ps["q_s"][s]/abs(ps["q_s"][0]))**2
                 n_imp             += 1
        statedata['Ti']   /= n_ion
        statedata['Tz']   /= n_imp
        statedata['zeff'] /= statedata['ne']
       #statedata['zeff']  = npy.append(ps["Zeff"][:],ps['Zeff'][-1])

        z_ion  = ps["q_s"][1]/abs(ps["q_s"][0])
        z_fus  = ps["q_sfus"][0]/abs(ps["q_s"][0])
        z_beam = ps["q_snbi"][0]/abs(ps["q_s"][0])
        if len(ps["q_rfmin"]) > 0: z_min = ps["q_rfmin"][0]/abs(ps["q_s"][0])
        else:                      z_min = 1.0

        statedata['nbfast'] = ps.dump_profile(statedata['rho'], "rho_nbi", "nbeami",      k=0)
        statedata['wbeam']  = ps.dump_profile(statedata['rho'], "rho_nbi", "eperp_beami", k=0) * 1.602e3
        statedata['wbeam'] += ps.dump_profile(statedata['rho'], "rho_nbi", "epll_beami",  k=0) * 1.602e3
        statedata['wbeam'] *= statedata['nbfast']

        statedata['nalpha']  = ps.dump_profile(statedata['rho'], "rho_fus", "nfusi",      k=0)
        statedata['walpha']  = ps.dump_profile(statedata['rho'], "rho_fus", "eperp_fusi", k=0) * 1.602e3
        statedata['walpha'] += ps.dump_profile(statedata['rho'], "rho_fus", "epll_fusi",  k=0) * 1.602e3
        statedata['walpha'] *= statedata['nalpha']

        statedata['q']       = ps['q_eq']
        statedata['Vrot']    = ps["omegat"][:]

        statedata['pkin']    = statedata['ne'] * statedata['Te']
        statedata['pkin']   += statedata['ni'] * statedata['Ti']
        statedata['pkin']   += statedata['nz'] * statedata['Tz']
        statedata['pkin']   += (2.0/3.0) * (statedata['wbeam'] + statedata['walpha'])
        statedata['pkin']   *= 1.0e-19

        statedata['pmhd']  = ps["P_eq"][:]

        if mode == 'kinetic':
            statedata['pressure'] = statedata['pkin']
        else:
            statedata['pressure'] = statedata['pmhd']

        statedata['jpar'] = ps.dump_j_parallel(statedata['rho'], "rho_eq", "curt", statedata['RCTR'], statedata['BCTR'], tot=True)
        if all(statedata['jpar'] < 0): statedata['jpar'] *= -1.0 

        if betan_target > 0:
            volume  = ps["vol"][:]
            rminor  = ps["rMinor_mean"][-1]

            wtot  = statedata['ne'] * statedata['Te']
            wtot += statedata['ni'] * statedata['Ti']
            wtot += statedata['nz'] * statedata['Tz']
            wtot *= (3.0/2.0)
            wtot += statedata['wbeam'] + statedata['walpha']
            wtot *= 1.0e6*1.0e-19

            betan  = npy.sum(npy.diff(volume) * wtot[:-1])
            betan /= (3.0/2.0) * volume[-1]
            betan *= 2.0 * (4.0*npy.pi*1.0e-7) / statedata['BCTR']**2
            betan /= abs(statedata['ip']/rminor/statedata['BCTR'])
            betan *= 1.0e2

            if betan > betan_target:
               statedata['pressure'] = statedata['pressure'] * betan_target / betan

    return statedata





