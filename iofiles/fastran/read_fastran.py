#!/usr/bin/python

import os
import re
import sys
import json
import random
import argparse
import efit_eqdsk
import subprocess

from glob                            import glob
from netCDF4                         import Dataset
#from scipy.signal                    import find_peaks
#from scipy.optimize                  import curve_fit
#from scipy.interpolate               import CubicSpline

#from Namelist import Namelist

def read_fastran(fastranfpath):
    cdffh = Dataset(fastranfpath, mode='r')

    fastran = {}
    for name, variable in cdffh.variables.items():
        fastran[name]                  = {}
        fastran[name]['data']          = cdffh.variables[name][:]
        fastran[name]['units']         = ""
        fastran[name]['symbol']        = ""
        fastran[name]['long_name']     = ""

        if hasattr(variable, "unit"):      fastran[name]['units']     = getattr(variable, "units")
        elif name == 'time':               fastran[name]['units']     = "s"
        elif name == 'r0':                 fastran[name]['units']     = "m"
        elif name == 'a0':                 fastran[name]['units']     = "m"
        elif name == 'b0':                 fastran[name]['units']     = "T"
        elif name == 'wi':                 fastran[name]['units']     = "MJ"
        elif name == 'we':                 fastran[name]['units']     = "MJ"
        elif name == 'wb':                 fastran[name]['units']     = "MJ"
        elif name == 'pei':                fastran[name]['units']     = "MW"
        elif name == 'poh':                fastran[name]['units']     = "MW"
        elif name == 'taue':               fastran[name]['units']     = "s"
        elif name == 'taui':               fastran[name]['units']     = "s"
        elif name == 'tauth':              fastran[name]['units']     = "s"
        elif name == 'tau98':              fastran[name]['units']     = "s"
        elif name == 'tau89':              fastran[name]['units']     = "s"
        elif name == 'taunc':              fastran[name]['units']     = "s"
        elif name == 'tautot':             fastran[name]['units']     = "s"
        elif name == 'pnbe':               fastran[name]['units']     = "MW"
        elif name == 'pnbi':               fastran[name]['units']     = "MW"
        elif name == 'prfe':               fastran[name]['units']     = "MW"
        elif name == 'prfi':               fastran[name]['units']     = "MW"
        elif name == 'prad':               fastran[name]['units']     = "MW"
        elif name == 'pfuse':              fastran[name]['units']     = "MW"
        elif name == 'pfusi':              fastran[name]['units']     = "MW"
        elif name == 'pfuse_equiv':        fastran[name]['units']     = "MW"
        elif name == 'pfusi_equiv':        fastran[name]['units']     = "MW"
        else:                              fastran[name]['units']     = ""

        if hasattr(variable, "long_name"): fastran[name]['long_name'] = getattr(variable, "long_name")
        elif name == 'time':               fastran[name]['long_name'] = "Time"
        elif name == 'r0':                 fastran[name]['long_name'] = "Major Radius"
        elif name == 'a0':                 fastran[name]['long_name'] = "Minor Radius"
        elif name == 'b0':                 fastran[name]['long_name'] = "Toroidal Magnetic Field at r0"
        elif name == 'wi':                 fastran[name]['long_name'] = "Ion Thermal Stored Energy"
        elif name == 'we':                 fastran[name]['long_name'] = "Electron Thermal Stored Energy"
        elif name == 'wb':                 fastran[name]['long_name'] = "Fast Ion Thermal Stored Energy"
        elif name == 'pei':                fastran[name]['long_name'] = "Total e-i Exchange"
        elif name == 'poh':                fastran[name]['long_name'] = "Ohmic Heating"
        elif name == 'taue':               fastran[name]['long_name'] = "Electron Energy Confinement Time"
        elif name == 'taui':               fastran[name]['long_name'] = "Ion Energy Confinement Time"
        elif name == 'tauth':              fastran[name]['long_name'] = "Thermal Energy Confinement Time"
        elif name == 'tau98':              fastran[name]['long_name'] = "H-mode Confinement Time Scaling"
        elif name == 'tau89':              fastran[name]['long_name'] = "L-mode Confinement Time Scaling"
        elif name == 'taunc':              fastran[name]['long_name'] = "Neoclassical Confinement Time Scaling"
        elif name == 'tautot':             fastran[name]['long_name'] = "Total Energy Confinement Time"
        elif name == 'pnbe':               fastran[name]['long_name'] = "NB Electron Heating"
        elif name == 'pnbi':               fastran[name]['long_name'] = "NB Ion Heating"
        elif name == 'prfe':               fastran[name]['long_name'] = "RF Electron Heating"
        elif name == 'prfi':               fastran[name]['long_name'] = "RF Ion Heating"
        elif name == 'prad':               fastran[name]['long_name'] = "Total Radiation"
        elif name == 'pfuse':              fastran[name]['long_name'] = "Electron Alpha Heating"
        elif name == 'pfusi':              fastran[name]['long_name'] = "Ion Alpha Heating"
        elif name == 'betan':              fastran[name]['long_name'] = "Normalized Beta"
        elif name == 'amain':              fastran[name]['long_name'] = "Atomic Number of Main Ion"
        elif name == 'zmain':              fastran[name]['long_name'] = "Charge Number of Main Ion"
        elif name == 'pfuse_equiv':        fastran[name]['long_name'] = "Equilvalent Electron Alpha Heating for Deutron Plasma"
        elif name == 'pfusi_equiv':        fastran[name]['long_name'] = "Equilvalent Ion Alpha Heating for Deutron Plasma"
        else:                              fastran[name]['long_name'] = ""

        if   name == 'q':                  fastran[name]['symbol']    = "$q$"
        elif name == 'a':                  fastran[name]['symbol']    = "$a$"
        elif name == 'R':                  fastran[name]['symbol']    = "$R$"
        elif name == 'b0':                 fastran[name]['symbol']    = "$B_0$"
        elif name == 'te':                 fastran[name]['symbol']    = "$T_e$"           # DONE
        elif name == 'ti':                 fastran[name]['symbol']    = "$T_i$"           # DONE
        elif name == 'ne':                 fastran[name]['symbol']    = "$n_e$"           # DONE
        elif name == 'ni':                 fastran[name]['symbol']    = "$n_i$"           # DONE
        elif name == 'pe':                 fastran[name]['symbol']    = "$P_e$"           # DONE
        elif name == 'pi':                 fastran[name]['symbol']    = "$P_i$"           # DONE
        elif name == 'nz0':                fastran[name]['symbol']    = "$n_z$"
        elif name == 'rho':                fastran[name]['symbol']    = "$\\rho$"
        elif name == 'fpol':               fastran[name]['symbol']    = "$f$"
        elif name == 'j_bs':               fastran[name]['symbol']    = "$J_{BS}$"        # DONE
        elif name == 'j_nb':               fastran[name]['symbol']    = "$J_{NB}$"        # DONE
        elif name == 'j_rf':               fastran[name]['symbol']    = "$J_{RF}$"        # DONE
        elif name == 'j_oh':               fastran[name]['symbol']    = "$J_{OH}$"        # DONE
        elif name == 'qmhd':               fastran[name]['symbol']    = "$q_{mhd}$"
        elif name == 'shat':               fastran[name]['symbol']    = "$\\hat{s}$"
        elif name == 'chii':               fastran[name]['symbol']    = "$D_i$"
        elif name == 'chie':               fastran[name]['symbol']    = "$D_e$"
        elif name == 'pnbe':               fastran[name]['symbol']    = "$P_{NB_e}$"
        elif name == 'pnbi':               fastran[name]['symbol']    = "$P_{NB_i}$"
        elif name == 'prfe':               fastran[name]['symbol']    = "$P_{RF_e}$"
        elif name == 'prfi':               fastran[name]['symbol']    = "$P_{RF_i}$"
        elif name == 'pe_nb':              fastran[name]['symbol']    = "$P_{NB_e}$"
        elif name == 'pi_nb':              fastran[name]['symbol']    = "$P_{NB_i}$"
        elif name == 'pe_rf':              fastran[name]['symbol']    = "$P_{RF_e}$"
        elif name == 'pi_rf':              fastran[name]['symbol']    = "$P_{RF_i}$"
        elif name == 'fluxe':              fastran[name]['symbol']    = "$Q_e$"
        elif name == 'fluxi':              fastran[name]['symbol']    = "$Q_i$"
        elif name == 'j_tot':              fastran[name]['symbol']    = "$J_{TOT}$"       # DONE
        elif name == 'omega':              fastran[name]['symbol']    = "$\\Omega$"
        elif name == 'delta':              fastran[name]['symbol']    = "$\\delta$"
        elif name == 'kappa':              fastran[name]['symbol']    = "$\\kappa$"
        elif name == 'betan':              fastran[name]['symbol']    = "$\\beta_n$"
        elif name == 'shift':              fastran[name]['symbol']    = "$\\delta_r$"
        elif name == 'pfuse':              fastran[name]['symbol']    = "$P_{FUS_e}$"
        elif name == 'pfusi':              fastran[name]['symbol']    = "$P_{FUS_i}$"
        elif name == 'pe_fus':             fastran[name]['symbol']    = "$P_{FUS_e}$"
        elif name == 'pi_fus':             fastran[name]['symbol']    = "$P_{FUS_i}$"
        elif name == 'j_bs_0':             fastran[name]['symbol']    = "$J_{BS_0}$"
        elif name == 'chieneo':            fastran[name]['symbol']    = "$D_{e_{neo}}$"
        elif name == 'chiineo':            fastran[name]['symbol']    = "$D_{i_{neo}}$"
        elif name == 'chie_exp':           fastran[name]['symbol']    = "$D_{e,{balance}}$"
        elif name == 'chii_exp':           fastran[name]['symbol']    = "$D_{i,{balance}}}$"
        elif name == 'fluxe_exp':          fastran[name]['symbol']    = "$Q_{e,{balance}}$"
        elif name == 'fluxi_exp':          fastran[name]['symbol']    = "$Q_{i,{balance}}$"
    return fastran

#tea(time) : volume average electron temperature [keV]
#tia(time) : volume average ion temperature [keV]
#nebar(time) : line-average density [10^19/m^3]
#ip(time) : plasma current [MA]
#ibs(time) : bootstrap current [MA]
#inb(time) : NB current [MA]
#irf(time) : RF current [MA]
#sn(time) : particle source [10^19#]
#rhob(time, rho) : sqrt(toroidal_flux/B0) [m]
#te(time, rho) : electron temperature [keV]
#ti(time, rho) : ion temperature [keV]
#ne(time, rho) : electron density [10^19/m^3]
#ni(time, rho) : ion density [10^19/m^3]
#nz0(time, rho) : impurity 1 density [10^19/m^3]
#omega(time, rho) : rotation [rad/sec]
#zeff(time, rho) : zeff []
#aimp(imp) : mass number of impurities []
#zimp(imp) : charge number of impurities []
#tep(time, rho) : radial derivative of electron temperature with respect to rho [keV]
#tip(time, rho) : radial derivative of ion temperature with respect to rho [keV]
#nep(time, rho) : radial derivative of electron density with respect to rho [10^19/m^3]
#nip(time, rho) : radial derivative of electron density with respect to rho [10^19/m^3]
#j_tot(time, rho) : plasma current [MA/m^2]
#j_bs(time, rho) : bootstrap current [MA/m^2]
#j_bs_0(time, rho) : bootstrap current w/o smooth [MA/m^2]
#j_nb(time, rho) : NB current [MA/m^2]
#j_rf(time, rho) : RF current [MA/m^2]
#j_oh(time, rho) : Ohmic current [MA/m^2]
#pe_nb(time, rho) : NB electron heating [MW/m^3]
#pe_rf(time, rho) : RF electron heating [MW/m^3]
#p_rad(time, rho) : radiation [MW/m^3]
#p_ohm(time, rho) : Ohmic heating [MW/m^3]
#p_ei(time, rho) : electron-ion collisional heating [MW/m^3]
#pe_fus(time, rho) : electron alpha heating [MW/m^3]
#pe_ionization(time, rho) : electron ionization loss [MW/m^3]
#pi_nb(time, rho) : NB ion heating [MW/m^3]
#pi_rf(time, rho) : RF ion heating [MW/m^3]
#pi_fus(time, rho) : ion alpha heating [MW/m^3]
#pi_cx(time, rho) : charge exchange loss [MW/m^3]
#pi_ionization(time, rho) : ion ionization loss [MW/m^3]
#pe(time, rho) : total electron heating [MW/m^3]
#pi(time, rho) : total ion heating [MW/m^3]
#torque_nb(time, rho) : NB torque [Nm]
#q(time, rho) : safety factor []
#shat(time, rho) : magnetic shear []
#fpol(time, rho) : poloidal magentic flux [Wb]
#sigma(time, rho) : parallel electric conductivity [MS/m]
#vloop(time, rho) : loop voltage [V]
#pmhd(time, rho) : pressure from MHD equilibrium [Pa]
#qmhd(time, rho) : safety factor from MhD equilibrium []
#ermhd(time, rho) : radial electric field [V/m]
#wbeam(time, rho) : beam stored energy [MJ/m^3]
#nbeam(time, rho) : beam density [10^19/m^3]
#sion(time, rho) : particle source [10^19/m^3/s]
#walp(time, rho) : alpha stored energy [MJ]
#betan_loc(time, rho) : local normalized beta
#nhe(time, rho) : He ash density [10^19/m^3]
#chie(time, rho) : electron heat duffusivity [m^2/s]
#chie_etg(time, rho) : high-k electron heat duffusivity [m^2/s]
#chii(time, rho) : ion heat duffusivity [m^2/s]
#chiv(time, rho) : momentum duffusivity [m^2/s]
#chin(time, rho) : particle duffusivity [m^2/s]
#chieneo(time, rho) : neoclassical electron heat duffusivity [m^2/s]
#chiineo(time, rho) : neoclassical ion heat duffusivity [m^2/s]
#fluxe(time, rho) : electron energy flux [MW/m^2]
#fluxi(time, rho) : ion energy flux [MW/m^2]
#fluxe_exp(time, rho) : power balance electron energy flux [MW/m^2]
#fluxi_exp(time, rho) : power balance ion energy flux [MW/m^2]
#chie_exp(time, rho) : power balance electron heat duffusivity [m^2/s]
#chii_exp(time, rho) : power balance ion heat duffusivity [m^2/s]
#chiv_exp(time, rho) : power balance momentum duffusivity [m^2/s]
#volp(time, rho) : dV/drhob (m^2)
#ipol(time, rho) : rbt/(r0b0) []
#g11(time, rho) : volp < (grad rhob)^2 > [m^2]
#g22(time, rho) : volp / (4*pi**2) < (grad rhob/r)^2 > * r0/ipol [m]
#g33(time, rho) : < (r0/r)**2 > []
#gradrho(time, rho) : < grad rhob > []
#area(time, rho) : surface area [m^2]
#aminor(time, rho) : minor radius [m]
#rmajor(time, rho) : major radius [m]
#shift(time, rho) : shafranov shift [m]
#delta(time, rho) : triangularity []
#kappa(time, rho) : elongation []
#chin_exp(time, rho) : power balance electron heat duffusivity [m^2/s]
#chie_paleo(time, rho) : paleo-classical electron heat duffusivity [m^2/s]
#nue_s(time, rho) : normalized electron collision frequency []

#def read_fastran(WORK_DIR):
#    fastrandata = {}
#
#    if type(WORK_DIR) == str: WORK_DIR = [WORK_DIR]
#
#    CASE_ID = 0
#    shotref = ""
#
#    for iWORK_DIR in WORK_DIR:
#       #if os.path.isfile(iWORK_DIR):
#       #    iWORK_DIR_PATH = 
#       #    WORK_FILES = 
#        iWORK_DIR_PATH = '%s' % os.path.abspath(iWORK_DIR)
#        WORK_FILES = sorted(glob('%s/fastran.nc' % (iWORK_DIR_PATH)))
#        if not WORK_FILES:
#            iWORK_DIR_PATH = '%s/work/plasma_state' % os.path.abspath(iWORK_DIR)
#            WORK_FILES = glob('%s/f*' % (iWORK_DIR_PATH))
#            if not WORK_FILES:
#                iWORK_DIR_PATH = '%s' % os.path.abspath(iWORK_DIR)
#                WORK_FILES = glob('%s/f*' % (iWORK_DIR_PATH))
#        if WORK_FILES:
#            for i in range(len(WORK_FILES)):
#                FASTRAN_FILEPATH = WORK_FILES[i]
#                print(FASTRAN_FILEPATH)
#                FASTRAN_FILENAME = FASTRAN_FILEPATH.replace(iWORK_DIR_PATH+'/','')
#                SHOT_NUMBER, TIME_ID = FASTRAN_FILENAME[1:].split('.')
#                shot = SHOT_NUMBER + '.' + TIME_ID
#                if shot == shotref:
#                    CASE_ID += 1
#                elif shotref == "":
#                    shotref = shot
#                    CASE_ID += 1
#                elif shotref != "" and shot != shotref:
#                    shotref = shot
#                    CASE_ID = 1
#                shot = SHOT_NUMBER + '.' + TIME_ID + '.%02d' % CASE_ID
#
#                fastrandata[shot] = read_fastran_outputs(FASTRAN_FILEPATH)
#                if len(fastrandata[shot]['j_rf']['data']) == 0:
#                    del fastrandata[shot]
#                    print(CRED   + 'READING %s ... FAILED' % FASTRAN_FILEPATH + CEND)
#                else:
#                    print(CGREEN + 'READING %s ... PASSED' % FASTRAN_FILEPATH + CEND)
#        else:
#           print(CRED   + 'READING %s ... FAILED' % iWORK_DIR_PATH + CEND)
#
#    return fastrandata


