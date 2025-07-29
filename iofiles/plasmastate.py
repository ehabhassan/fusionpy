#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import re
import os
import sys

import numpy       as npy
#import iofiles.chease.cheaseprofit as cheaseprofit
#import traceback   as traceback

from maths.interp     import interp

from iofiles.eqdsk    import qtor,jtot
from iofiles.eqdsk    import read_eqdsk_file
from iofiles.eqdsk    import psigrids,phigrids

from iofiles.fastran  import read_fastran
from iofiles.Namelist import Namelist

#from maths.profile_fit import snyder_fit

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

def get_instate_vars():

    instate = {}
    instate['TOKAMAK_ID']    = [None]
    instate['MODEL_SHAPE']   = [None]
    instate['DENSITY_MODEL'] = [None]

    instate['R0']            = [None]
    instate['B0']            = [None]
    instate['IP']            = [None]
    instate['KAPPA']         = [None]
    instate['DELTA']         = [None]
    instate['ASPECT']        = [None]
    instate['RMAJOR']        = [None]
    instate['AMINOR']        = [None]

    instate['N_ION']         = [None]
    instate['Z_ION']         = [None]
    instate['A_ION']         = [None]
    instate['F_ION']         = [None]
    instate['N_IMP']         = [None]
    instate['Z_IMP']         = [None]
    instate['A_IMP']         = [None]
    instate['F_IMP']         = [None]
    instate['N_MIN']         = [None]
    instate['Z_MIN']         = [None]
    instate['A_MIN']         = [None]
    instate['N_BEAM']        = [None]
    instate['Z_BEAM']        = [None]
    instate['A_BEAM']        = [None]
    instate['N_FUSION']      = [None]
    instate['Z_FUSION']      = [None]
    instate['A_FUSION']      = [None]

    instate['RHO']           = [None]
    instate['NRHO']          = [None]
    instate['PSIPOL']        = [None]
    instate['RHOPSI']        = [None]

    instate['Q']             = [None]
    instate['NE']            = [None]
    instate['TE']            = [None]
    instate['TI']            = [None]
    instate['ZEFF']          = [None]
    instate['P_EQ']          = [None]
    instate['OMEGA']         = [None]
    instate['PPRIME']        = [None]
    instate['FFPRIME']       = [None]

    instate['J_OH']          = [None]
    instate['J_BS']          = [None]
    instate['J_NB']          = [None]
    instate['J_EC']          = [None]
    instate['J_IC']          = [None]
    instate['J_LH']          = [None]
    instate['J_HC']          = [None]
    instate['J_TOT']         = [None]

    instate['P_EI']          = [None]
    instate['SE_NB']         = [None]
    instate['PE_NB']         = [None]
    instate['PE_EC']         = [None]
    instate['PE_IC']         = [None]
    instate['PE_LH']         = [None]
    instate['PE_HC']         = [None]
    instate['SI_NB']         = [None]
    instate['PI_NB']         = [None]
    instate['PI_EC']         = [None]
    instate['PI_IC']         = [None]
    instate['PI_LH']         = [None]
    instate['PI_HC']         = [None]
    instate['PI_CX']         = [None]
    instate['PI_FUS']        = [None]
    instate['PE_FUS']        = [None]
    instate['P_RAD']         = [None]
    instate['P_OHM']         = [None]

    instate['TORQUE_NB']     = [None]
    instate['TORQUE_IN']     = [None]
    instate['SE_IONIZATION'] = [None]
    instate['SI_IONIZATION'] = [None]
    instate['PE_IONIZATION'] = [None]
    instate['PI_IONIZATION'] = [None]
    instate['WBEAM']         = [None]
    instate['WALPHA']        = [None]
    instate['DENSITY_BEAM']  = [None]
    instate['SCALE_DENSITY_BEAM']  = [None]
    instate['DENSITY_ALPHA'] = [None]
    instate['CHIE']          = [None]
    instate['CHII']          = [None]

    instate['NBDRY']         = [None]
    instate['RBDRY']         = [None]
    instate['ZBDRY']         = [None]
    instate['NLIM']          = [None]
    instate['RLIM']          = [None]
    instate['ZLIM']          = [None]

    return instate

def get_plasmastate(ifpath="",sfpath="",bfpath="",gfpath='',setParam={}):
    if   ifpath:
         if os.path.isfile(ifpath):
            statedata = read_instate_file(fpath=ifpath,setParam={})
         else:
            print('FILE DOES NOT EXISTS IN DESTINATION PATH:')
            print(ifpath)
            sys.exit()
    elif statefpath:
         statedata = read_state_file(fpath=sfpath,setParam={})

    if bfpath and os.path.isfile(bfpath):
        inbc = Namelist(bfpath)["inbc"]

        statedata['ip']     = abs(inbc['ip'][0])*1.0e6
        statedata['rctr']   = abs(inbc["r0"][0])
        statedata['bctr']   = abs(inbc["b0"][0])
        statedata['nlim']   = inbc["nlim"][0]
        statedata['rlim']   = inbc["rlim"][:]
        statedata['zlim']   = inbc["zlim"][:]
        statedata['nbound'] = inbc["nbdry"][0]
        statedata['rbound'] = inbc["rbdry"][:]
        statedata['zbound'] = inbc["zbdry"][:]

    elif gfpath and os.path.isfile(gfpath):
        eqdskdata = read_eqdsk_file(fpath=gfpath)
        calc_psigrids = psigrids()
        calc_phigrids = phigrids()
        calc_psigrids(eqdskdata,ps_update=True)
        calc_phigrids(eqdskdata,ps_update=True)

        calc_iterp = interp()
        eqdskdata['qtor']     = calc_iterp(eqdskdata['rhopsi'],eqdskdata['qpsi'],    statedata['rho'])
        eqdskdata['pprime']   = calc_iterp(eqdskdata['rhopsi'],eqdskdata['pprime'],  statedata['rho'])
        eqdskdata['ffprime']  = calc_iterp(eqdskdata['rhopsi'],eqdskdata['ffprime'], statedata['rho'])
        eqdskdata['pressure'] = calc_iterp(eqdskdata['rhopsi'],eqdskdata['pressure'],statedata['rho'])

        statedata['q']        =     eqdskdata['qtor']
        statedata['ip']       = abs(eqdskdata['CURNT'])
        statedata['rctr']     = abs(eqdskdata['RCTR'])
        statedata['bctr']     = abs(eqdskdata['BCTR'])
        statedata['rmax']     =     eqdskdata['RMAX']
        statedata['zmax']     =     eqdskdata['ZMAX']
        statedata['nlim']     =     eqdskdata['nlimit']
        statedata['rlim']     =     eqdskdata["rlimit"]
        statedata['zlim']     =     eqdskdata["zlimit"]
        statedata['nbound']   =     eqdskdata["nbound"]
        statedata['rbound']   =     eqdskdata["rbound"]
        statedata['zbound']   =     eqdskdata["zbound"]
        statedata['pprime']   =     eqdskdata["pprime"]
        statedata['ffprime']  =     eqdskdata["ffprime"]
        statedata['pressure'] =     eqdskdata["pressure"]

    if 'rbound' in statedata:
        Zmidl  = (max(statedata['zbound']) + min(statedata['zbound'])) / 2.0
        major  = (max(statedata['rbound']) + min(statedata['rbound'])) / 2.0
        minor  = (max(statedata['rbound']) - min(statedata['rbound'])) / 2.0
        kappa  = (max(statedata['zbound']) - min(statedata['zbound'])) / 2.0 / minor
        delta  = 2.0*major 
        delta -= statedata['rbound'][npy.argmax(statedata['zbound'])]
        delta -= statedata['rbound'][npy.argmin(statedata['zbound'])]
        delta /= (2.0*minor)

        statedata['ELONG']  = kappa
        statedata['TRIANG'] = delta
        statedata['ASPECT'] = minor/major

    return statedata


def read_instate_file(fpath="",setParam={}):
    if os.path.isfile(fpath):
       instate = Namelist(fpath)['instate']
    else:
       raise IOError("INSTATE FILE (%s) DOES NOT EXIST!" % fpath)

    if 'mode' in setParam: mode = setParam['mode']
    else:                  mode = 'kinetic'

    statedata = {}

    if instate['SHOT_ID']: 
        statedata['SHOT_ID'] = instate['SHOT_ID']

    if instate['TIME_ID' ]:
        statedata['TIME_ID'] = instate['TIME_ID']

    if instate['TOKAMAK_ID']:
        statedata['TOKAMAK_ID'] = instate['TOKAMAK_ID']

    if 'ip' not in statedata:
        statedata['ip']     = instate["ip"][0]*1.0e6
    if 'RCTR' not in statedata:
        statedata['RCTR']   = instate["r0"][0]
    if 'BCTR' not in statedata:
        statedata['BCTR']   = abs(instate["b0"][0])
    if 'RMAJOR' not in statedata:
        statedata['rmajor']   = abs(instate["rmajor"][0])
    if 'AMINOR' not in statedata:
        statedata['aminor']   = abs(instate["aminor"][0])
    if 'nlim' not in statedata:
        if instate["nlim" ]:
            statedata['nlim']   = instate["nlim" ][0]
            statedata['rlim']   = npy.array(instate["rlim" ])
            statedata['zlim']   = npy.array(instate["zlim" ])
    if 'nbdry' not in statedata:
        if instate["nbdry"]:
            statedata['nbound'] = instate["nbdry"][0]
            statedata['rbound'] = npy.array(instate["rbdry"])
            statedata['zbound'] = npy.array(instate["zbdry"])

    statedata['nrho']   = instate['nrho'][0]
    if instate['rho']:
        statedata['rho'] = npy.array(instate['rho'])
    else:
        statedata['rho'] = npy.linspace(0.0,1.0,statedata['nrho'])

    if instate['rhopsi']:
        statedata['rhopsi']= npy.array(instate['rhopsi'])
    else:
        statedata['rhopsi'] = npy.zeros(statedata['nrho'])

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
       #statedata['Te']     = npy.array(instate['te'])*1.602e3
        statedata['Te']     = npy.array(instate['te'])*1.0e3
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
       #statedata['Ti']     = npy.array(instate['ti'])*1.602e3
        statedata['Ti']     = npy.array(instate['ti'])*1.0e3
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
    else:
        statedata['ffprime'] = npy.zeros(statedata['nrho'])

    if instate['pprime']:
        statedata['pprime']= npy.array(instate['pprime'])
    else:
        statedata['pprime'] = npy.zeros(statedata['nrho'])

    if instate['rminor']:
        statedata['rminor']= instate['rminor'][0]
    else:
        statedata['rminor'] = npy.nan

    if instate['aminor']:
        statedata['aminor']= instate['aminor'][0]
    else:
        statedata['aminor'] = npy.nan

    if instate['j_tot']:
        statedata['jpar']   = npy.array(instate['j_tot'])
    elif instate['jpar_axis']:
        statedata['jpar']   = (instate['jpar_axis'][0] - instate['jpar_sep'][0])
        statedata['jpar']  *= (1.0 - statedata['rho']**instate['jpar_alpha'][0])**instate['jpar_beta'][0]
        statedata['jpar']  += instate['jpar_sep'][0]
    else:
        statedata['jpar'] = npy.zeros(statedata['nrho'])
    statedata['jpar'] *= 1.0e6
    if all(statedata['jpar'] < 0): statedata['jpar'] *= -1.0

    if instate['j_oh']:
        statedata['joh']= npy.array(instate['j_oh'])
    else:
        statedata['joh'] = npy.zeros(statedata['nrho'])
    statedata['joh'] *= 1.0e6

    if instate['j_bs']:
        statedata['jbs']= npy.array(instate['j_bs'])
    else:
        statedata['jbs'] = npy.zeros(statedata['nrho'])
    statedata['jbs'] *= 1.0e6

    if instate['j_nb']:
        statedata['jnb']= npy.array(instate['j_nb'])
    else:
        statedata['jnb'] = npy.zeros(statedata['nrho'])
    statedata['jnb'] *= 1.0e6

    if instate['j_rf']:
        statedata['jrf']= npy.array(instate['j_rf'])
    else:
        statedata['jrf'] = npy.zeros(statedata['nrho'])
    statedata['jrf'] *= 1.0e6

    if instate['j_ec']:
        statedata['jec']= npy.array(instate['j_ec'])
    else:
        statedata['jec'] = npy.zeros(statedata['nrho'])
    statedata['jec'] *= 1.0e6

    if instate['j_ic']:
        statedata['jic']= npy.array(instate['j_ic'])
    else:
        statedata['jic'] = npy.zeros(statedata['nrho'])
    statedata['jic'] *= 1.0e6

    if instate['j_lh']:
        statedata['jlh']= npy.array(instate['j_lh'])
    else:
        statedata['jlh'] = npy.zeros(statedata['nrho'])
    statedata['jlh'] *= 1.0e6

    if instate['j_hc']:
        statedata['jhc']= npy.array(instate['j_hc'])
    else:
        statedata['jhc'] = npy.zeros(statedata['nrho'])
    statedata['jhc'] *= 1.0e6

    if instate['p_ei']:
        statedata['pei']= npy.array(instate['p_ei'])
    else:
        statedata['pei'] = npy.zeros(statedata['nrho'])
    statedata['pei'] *= 1.0e6

    if instate['p_rad']:
        statedata['prad']= npy.array(instate['p_rad'])
    else:
        statedata['prad'] = npy.zeros(statedata['nrho'])
    statedata['prad'] *= 1.0e6

    if instate['p_ohm']:
        statedata['pohm']= npy.array(instate['p_ohm'])
    else:
        statedata['pohm'] = npy.zeros(statedata['nrho'])
    statedata['pohm'] *= 1.0e6

    if instate['pi_cx']:
        statedata['picx']= npy.array(instate['pi_cx'])
    else:
        statedata['picx'] = npy.zeros(statedata['nrho'])
    statedata['picx'] *= 1.0e6

    if instate['pe_fus']:
        statedata['pefus']= npy.array(instate['pe_fus'])
    else:
        statedata['pefus'] = npy.zeros(statedata['nrho'])
    statedata['pefus'] *= 1.0e6

    if instate['pi_fus']:
        statedata['pifus']= npy.array(instate['pi_fus'])
    else:
        statedata['pifus'] = npy.zeros(statedata['nrho'])
    statedata['pifus'] *= 1.0e6

    if instate['pe_nb']:
        statedata['penb']= npy.array(instate['pe_nb'])
    else:
        statedata['penb'] = npy.zeros(statedata['nrho'])
    statedata['penb'] *= 1.0e6

    if instate['pi_nb']:
        statedata['pinb']= npy.array(instate['pi_nb'])
    else:
        statedata['pinb'] = npy.zeros(statedata['nrho'])
    statedata['pinb'] *= 1.0e6

    if instate['pe_rf']:
        statedata['perf']= npy.array(instate['pe_rf'])
    else:
        statedata['perf'] = npy.zeros(statedata['nrho'])
    statedata['perf'] *= 1.0e6

    if instate['pi_rf']:
        statedata['pirf']= npy.array(instate['pi_rf'])
    else:
        statedata['pirf'] = npy.zeros(statedata['nrho'])
    statedata['pirf'] *= 1.0e6

    if instate['wbeam']:
        statedata['wbeam']  = npy.array(instate['wbeam'])
    else:
        statedata['wbeam']  = npy.zeros(statedata['nrho'])

    if instate['scale_sion']: 
        statedata['scale_sion'] = instate['scale_sion']
    else:
        statedata['scale_sion'] = [0.0]

    if instate['scale_ne']: 
        statedata['scale_ne'] = instate['scale_ne']
    else:
        statedata['scale_ne'] = [0.0]

    if instate['sion']:
        statedata['sion']  = npy.array(instate['sion'])
    else:
        statedata['sion']  = npy.zeros(statedata['nrho'])

    if instate['q']:
        statedata['q']  = npy.array(instate['q'])
    else:
        statedata['q']  = npy.zeros(statedata['nrho'])
    if all(statedata['q'] < 0): statedata['q'] *= -1.0

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

    if instate['scale_density_beam']:
       statedata['scale_density_beam'] = instate['scale_density_beam']
    else:
       statedata['scale_density_beam'] = [1.0]

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

    return statedata

def read_state_file(fpath="",setParam={}):
    if 'mode' in setParam: mode = setParam['mode']
    else:                  mode = 'kinetic'

    if 'init_run' in setParam: init_run = setParam['init_run']
    else:                      init_run = True

    if 'betan_target' in setParam: betan_target = setparam['betan_target']
    else:                          betan_target = -1.0

    statedata = {}

    if type(fpath) == str:
        ps = plasmastate('ips',1)
        ps.read(fpath)
    else:
        ps = self.fpath

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
    statedata['ni']     = npy.zeros(statedata['nrho'])
    statedata['nz']     = npy.zeros(statedata['nrho'])
    statedata['Ti']     = npy.zeros(statedata['nrho'])
    statedata['Tz']     = npy.zeros(statedata['nrho'])
    statedata['zeff']   = npy.zeros(statedata['nrho'])
    statedata['aminor'] = npy.zeros(statedata['nrho'])
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

    statedata['aminor']  = ps['rminor']
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

def update_instate_file(ifpath,gfpath="",bfpath=""):
    instate   = Namelist(ifpath)['instate']
    statedata = get_plasmastate(ifpath=ifpath,gfpath=gfpath,bfpath=bfpath)

    SHOT_ID    = instate['SHOT_ID'][0]
    TIME_ID    = instate['TIME_ID'][0]
    TOKAMAK_ID = instate['TOKAMAK_ID'][0]

#   instate['IP']        = [round(statedata['ip']*1.0e-6,7)]
#   instate['R0']        = [round(statedata['rctr'],     7)]
#   instate['B0']        = [round(statedata['bctr'],     7)]
#   instate['RMAX']      = [round(statedata['rmax'],     7)]
#   instate['ZMAX']      = [round(statedata['zmax'],     7)]

    instate['NLIM']      = [round(statedata['nlim'],     7)]
    instate['RLIM']      = [round(i,7) for i in statedata['rlim']  ]
    instate['ZLIM']      = [round(i,7) for i in statedata['zlim']  ]

    instate['NBDRY']     = [round(statedata['nbound'],   7)]
    instate['RBDRY']     = [round(i,7) for i in statedata['rbound']]
    instate['ZBDRY']     = [round(i,7) for i in statedata['zbound']]

#   instate['Q']         = [round(i,7) for i in statedata['q']     ]
#   instate['P_EQ']      = [round(i,7) for i in statedata['pressure']]
#   instate['RHOPSI']    = [round(i,7) for i in statedata['rhopsi']  ]
#   instate['PPRIME']    = [round(i,7) for i in statedata['pprime']  ]
#   instate['FFPRIME']   = [round(i,7) for i in statedata['ffprime'] ]

    INSTATE = Namelist()
    INSTATE['instate'] = {}
    INSTATE['instate'].update(instate)
    INSTATE.write("instate_%s_%s.%s" % (TOKAMAK_ID,SHOT_ID,TIME_ID))

    return statedata

if __name__ == "__main__":
    geqdsk_fname  = "../../Discharges/DIIID/DIIID150139/g150139.02026"
    instate_fname = "../testsuite/state_files/instate_d3d_150139.20259"
    update_instate_file(ifpath=instate_fname,gfpath=geqdsk_fname)
   #get_plasmastate(ifpath=instate_fname,gfpath=geqdsk_fname,setParam={})





