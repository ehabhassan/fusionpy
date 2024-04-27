import os
import sys
import numpy
import random
import netCDF4 as ncdf

from maths.interp        import interp
from iofiles.Namelist    import Namelist
from iofiles.eqdsk       import read_eqdsk_file
from iofiles.plasmastate import get_instate_vars

def get_iterdb_vars():
    onetwo = {}
    
    onetwo['file_type']               = None

    onetwo['shot']                    = {} 
    onetwo['shot']['data']            = None
    onetwo['shot']['unit']            = None
    onetwo['shot']['info']            = "Shot Number"

    onetwo['Ipsign']                   = {} 
    onetwo['Ipsign']['data']           = None
    onetwo['Ipsign']['unit']           = None
    onetwo['Ipsign']['info']           = "Sign of Total Current"

    onetwo['nj']                       = {} 
    onetwo['nj']['data']               = None
    onetwo['nj']['unit']               = None
    onetwo['nj']['info']               = "Size of rho Grid"
    
    onetwo['time']                     = {} 
    onetwo['time']['data']             = None
    onetwo['time']['unit']             = None
    onetwo['time']['info']             = "Time At Which Data is Printed"
    
    onetwo['tGCNMf']                   = {} 
    onetwo['tGCNMf']['data']           = None
    onetwo['tGCNMf']['unit']           = None
    onetwo['tGCNMf']['info']           = "GCNMP Evolve Solution from Time to tGCNMf"
    
    onetwo['time_bc']                  = {} 
    onetwo['time_bc']['data']          = None
    onetwo['time_bc']['unit']          = None
    onetwo['time_bc']['info']          = "Boundary Condition Time"
    
    onetwo['psiaxis']                  = {} 
    onetwo['psiaxis']['data']          = None
    onetwo['psiaxis']['unit']          = "V.s/rad"
    onetwo['psiaxis']['info']          = "psi Value on Magnetic Axis"
    
    onetwo['psibdry']                  = {} 
    onetwo['psibdry']['data']          = None
    onetwo['psibdry']['unit']          = "V.s/rad"
    onetwo['psibdry']['info']          = "psi Value on Plasma Edge (Separatrix)"
    
    onetwo['rgeom']                    = {} 
    onetwo['rgeom']['data']            = None
    onetwo['rgeom']['unit']            = "m"
    onetwo['rgeom']['info']            = "Major Radius of Geometric Center at Elevation of Magnetic Axis"
    
    onetwo['btgeom']                   = {} 
    onetwo['btgeom']['data']           = None
    onetwo['btgeom']['unit']           = "T"
    onetwo['btgeom']['info']           = "Toroidal B-Field at Geometric Center (Rgeom)"
    
    onetwo['rma']                      = {} 
    onetwo['rma']['data']              = None
    onetwo['rma']['unit']              = "m"
    onetwo['rma']['info']              = "Major Radius of Magnetic Axis (rmag)"
    
    onetwo['zma']                      = {} 
    onetwo['zma']['data']              = None
    onetwo['zma']['unit']              = "m"
    onetwo['zma']['info']              = "Z of Magnetic Axis"
    
    onetwo['rsep']                     = {} 
    onetwo['rsep']['data']             = None
    onetwo['rsep']['unit']             = "m"
    onetwo['rsep']['info']             = "R of Separatrix X-Point"
    
    onetwo['zsep']                     = {} 
    onetwo['zsep']['data']             = None
    onetwo['zsep']['unit']             = "m"
    onetwo['zsep']['info']             = "Z of Separatrix X-Point"
    
    onetwo['rmajor']                   = {} 
    onetwo['rmajor']['data']           = None
    onetwo['rmajor']['unit']           = "m"
    onetwo['rmajor']['info']           = "Major Radius of Vacuum BT0 (R0)"
    
    onetwo['rplasmin']                 = {} 
    onetwo['rplasmin']['data']         = None
    onetwo['rplasmin']['unit']         = "m"
    onetwo['rplasmin']['info']         = "Minimum R of Plasma"
    
    onetwo['rplasmax']                 = {} 
    onetwo['rplasmax']['data']         = None
    onetwo['rplasmax']['unit']         = "m"
    onetwo['rplasmax']['info']         = "Maximum R of Plasma"
    
    onetwo['zplasmin']                 = {} 
    onetwo['zplasmin']['data']         = None
    onetwo['zplasmin']['unit']         = "m"
    onetwo['zplasmin']['info']         = "Minimum Z of Plasma"
    
    onetwo['zplasmax']                 = {} 
    onetwo['zplasmax']['data']         = None
    onetwo['zplasmax']['unit']         = "m"
    onetwo['zplasmax']['info']         = "Maximum Z of Plasma"
    
    onetwo['kappa']                    = {} 
    onetwo['kappa']['data']            = None
    onetwo['kappa']['unit']            = None
    onetwo['kappa']['info']            = "Plasma Elongation"
    
    onetwo['deltao']                   = {} 
    onetwo['deltao']['data']           = None
    onetwo['deltao']['unit']           = None
    onetwo['deltao']['info']           = "Plasma (Upper) Triangularity on Axis"
    
    onetwo['pindento']                 = {} 
    onetwo['pindento']['data']         = None
    onetwo['pindento']['unit']         = None
    onetwo['pindento']['info']         = "On Axis Plasma Indentation (pindent)"
    
    onetwo['volume']                   = {} 
    onetwo['volume']['data']           = None
    onetwo['volume']['unit']           = "m^3"
    onetwo['volume']['info']           = "Plasma Volume (volo)"
    
    onetwo['circum']                   = {} 
    onetwo['circum']['data']           = None
    onetwo['circum']['unit']           = "m"
    onetwo['circum']['info']           = "Plasma Circumference"
    
    onetwo['areao']                    = {} 
    onetwo['areao']['data']            = None
    onetwo['areao']['unit']            = "m^2"
    onetwo['areao']['info']            = "Plasma Cross-Sectional Area"
    
    onetwo['nion']                     = {} 
    onetwo['nion']['data']             = None
    onetwo['nion']['unit']             = None
    onetwo['nion']['info']             = "The Number of Ion Species"
    
    onetwo['nprim']                    = {} 
    onetwo['nprim']['data']            = None
    onetwo['nprim']['unit']            = None
    onetwo['nprim']['info']            = "The Number of Primary Ion Species"
    
    onetwo['fd_thermal']               = {} 
    onetwo['fd_thermal']['data']       = None
    onetwo['fd_thermal']['unit']       = None
    onetwo['fd_thermal']['info']       = "Fraction of d in thermal dt mixture if input as one species"
    
    onetwo['nimp']                     = {} 
    onetwo['nimp']['data']             = None
    onetwo['nimp']['unit']             = None
    onetwo['nimp']['info']             = "The Number of Impurity Ion Species"
    
    onetwo['nneu']                     = {} 
    onetwo['nneu']['data']             = None
    onetwo['nneu']['unit']             = None
    onetwo['nneu']['info']             = "The Number of Neutral Species"
    
    onetwo['nbion']                    = {} 
    onetwo['nbion']['data']            = None
    onetwo['nbion']['unit']            = None
    onetwo['nbion']['info']            = "The Number of Fast Ion Species"
    
    onetwo['fd_beam']                  = {} 
    onetwo['fd_beam']['data']          = None
    onetwo['fd_beam']['unit']          = None
    onetwo['fd_beam']['info']          = "Fraction of d in dt fast ion mixture"
    
    onetwo['nbeams']                   = {}
    onetwo['nbeams']['data']           = None
    onetwo['nbeams']['unit']           = None
    onetwo['nbeams']['info']           = "Number of Neutral beam Injectors"

    onetwo['namep']                    = {} 
    onetwo['namep']['data']            = None
    onetwo['namep']['unit']            = None
    onetwo['namep']['info']            = "Name of Primary Ion Species"
    
    onetwo['namei']                    = {} 
    onetwo['namei']['data']            = None
    onetwo['namei']['unit']            = None
    onetwo['namei']['info']            = "Name of Impurity Ion Species"
    
    onetwo['namen']                    = {} 
    onetwo['namen']['data']            = None
    onetwo['namen']['unit']            = None
    onetwo['namen']['info']            = "Name of Neutral Species"
    
    onetwo['nameb']                    = {} 
    onetwo['nameb']['data']            = None
    onetwo['nameb']['unit']            = None
    onetwo['nameb']['info']            = "Name of Beam Species"
    
    onetwo['namepel']                  = {} 
    onetwo['namepel']['data']          = None
    onetwo['namepel']['unit']          = None
    onetwo['namepel']['info']          = "Name of Pellet Species"
    
    onetwo['btor']                     = {} 
    onetwo['btor']['data']             = None
    onetwo['btor']['unit']             = "T"
    onetwo['btor']['info']             = "Vacuum Toroidal Field at R0 (rmajor)"
    
    onetwo['tot_cur']                  = {} 
    onetwo['tot_cur']['data']          = None
    onetwo['tot_cur']['unit']          = "A"
    onetwo['tot_cur']['info']          = "Total Plasma Current (Itot)"
    
    onetwo['totohm_cur']               = {} 
    onetwo['totohm_cur']['data']       = None
    onetwo['totohm_cur']['unit']       = "A"
    onetwo['totohm_cur']['info']       = "Total Ohmic Plasma Current (Iohm)"
    
    onetwo['totboot_cur']              = {} 
    onetwo['totboot_cur']['data']      = None
    onetwo['totboot_cur']['unit']      = "A"
    onetwo['totboot_cur']['info']      = "Total Bootstrap Current (Ibs)"
    
    onetwo['totbeam_cur']              = {} 
    onetwo['totbeam_cur']['data']      = None
    onetwo['totbeam_cur']['unit']      = "A"
    onetwo['totbeam_cur']['info']      = "Total Beam Driven Current (Inb)"
    
    onetwo['totrf_cur']                = {} 
    onetwo['totrf_cur']['data']        = None
    onetwo['totrf_cur']['unit']        = "A"
    onetwo['totrf_cur']['info']        = "Total RF Driven Current (Irf)"
    
    onetwo['betap']                    = {} 
    onetwo['betap']['data']            = None
    onetwo['betap']['unit']            = None
    onetwo['betap']['info']            = "Poloidal Beta"
    
    onetwo['beta']                     = {} 
    onetwo['beta']['data']             = None
    onetwo['beta']['unit']             = None
    onetwo['beta']['info']             = "Toroidal Beta"
    
    onetwo['ali']                      = {} 
    onetwo['ali']['data']              = None
    onetwo['ali']['unit']              = None
    onetwo['ali']['info']              = "Plasma Inductance"
    
    onetwo['te0']                      = {} 
    onetwo['te0']['data']              = None
    onetwo['te0']['unit']              = "keV"
    onetwo['te0']['info']              = "Central Electron Temperature"
    
    onetwo['ti0']                      = {} 
    onetwo['ti0']['data']              = None
    onetwo['ti0']['unit']              = "keV"
    onetwo['ti0']['info']              = "Central Ion Temperature"
    
    onetwo['psi']                      = {}
    onetwo['psi']['data']              = None
    onetwo['psi']['unit']              = "V.s/rad"
    onetwo['psi']['info']              = "psi on (R,Z) grid"

    onetwo['psir_grid']                = {} 
    onetwo['psir_grid']['data']        = None
    onetwo['psir_grid']['unit']        = "V.s/rad"
    onetwo['psir_grid']['info']        = "psi on rho grid"
    
    onetwo['rho_mhd_gridnpsi']         = {} 
    onetwo['rho_mhd_gridnpsi']['data'] = None
    onetwo['rho_mhd_gridnpsi']['unit'] = "m"
    onetwo['rho_mhd_gridnpsi']['info'] = "rho grid correponding to MHD psival grid"
    
    onetwo['rmhdgrid']                 = {} 
    onetwo['rmhdgrid']['data']         = None
    onetwo['rmhdgrid']['unit']         = "m"
    onetwo['rmhdgrid']['info']         = "R Grid"
    
    onetwo['zmhdgrid']                 = {} 
    onetwo['zmhdgrid']['data']         = None
    onetwo['zmhdgrid']['unit']         = "m"
    onetwo['zmhdgrid']['info']         = "Z Grid"
    
    onetwo['rho_grid']                 = {}
    onetwo['rho_grid']['data']         = None
    onetwo['rho_grid']['unit']         = "m"
    onetwo['rho_grid']['info']         = "rho grid"

    onetwo['fcap']                     = {}
    onetwo['fcap']['data']             = None
    onetwo['fcap']['unit']             = None
    onetwo['fcap']['info']             = "f(psilim)/f(psi)"

    onetwo['gcap']                     = {}
    onetwo['gcap']['data']             = None
    onetwo['gcap']['unit']             = None
    onetwo['gcap']['info']             = "<(grad rho)**2*(R0/R)**2"

    onetwo['hcap']                     = {}
    onetwo['hcap']['data']             = None
    onetwo['hcap']['unit']             = None
    onetwo['hcap']['info']             = "(dvolume/drho)/(r*pi*pi*R0*rho)"

    onetwo['betan']                    = {} 
    onetwo['betan']['data']            = None
    onetwo['betan']['unit']            = None
    onetwo['betan']['info']            = "Normalized Beta (P/BTGEOM**2/2mu0/I/a/BTGEOM)"
    
    onetwo['Te']                       = {}
    onetwo['Te']['data']               = None
    onetwo['Te']['unit']               = "keV"
    onetwo['Te']['name']               = "Electron Temperature"
    onetwo['Te']['info']               = "Electron Temperature"

    onetwo['Ti']                       = {}
    onetwo['Ti']['data']               = None
    onetwo['Ti']['unit']               = "keV"
    onetwo['Ti']['name']               = "Ion Temperature"
    onetwo['Ti']['info']               = "Ion Temperature"

    onetwo['press']                    = {}
    onetwo['press']['data']            = None
    onetwo['press']['unit']            = "N/m^2"
    onetwo['press']['name']            = "Total Pressure"
    onetwo['press']['info']            = "Total Pressure on Transport rho grid"

    onetwo['pressb']                   = {}
    onetwo['pressb']['data']           = None
    onetwo['pressb']['unit']           = "N/m^2"
    onetwo['pressb']['name']           = "Beam Pressure"
    onetwo['pressb']['info']           = "Beam Pressure on Transport rho grid"

    onetwo['q_value']                  = {} 
    onetwo['q_value']['data']          = None
    onetwo['q_value']['unit']          = None
    onetwo['q_value']['name']          = "Safety Factor"
    onetwo['q_value']['info']          = "Safety Factor"
    
    onetwo['ene']                      = {}
    onetwo['ene']['data']              = None
    onetwo['ene']['unit']              = "/m^3"
    onetwo['ene']['name']              = "Electron Density"
    onetwo['ene']['info']              = "Electron Density"

    onetwo['p_flux_elct']              = {} 
    onetwo['p_flux_elct']['data']      = None
    onetwo['p_flux_elct']['unit']      = "1/m^2/s"
    onetwo['p_flux_elct']['name']      = "Electron Particle Flux"
    onetwo['p_flux_elct']['info']      = "Electron Particle Flux"
    
    onetwo['p_flux_ion']               = {} 
    onetwo['p_flux_ion']['data']       = None
    onetwo['p_flux_ion']['unit']       = "1/m^2/s"
    onetwo['p_flux_ion']['name']       = "Ion Total Particle Flux"
    onetwo['p_flux_ion']['info']       = "Ion Total Particle Flux"
    
    onetwo['enion']                    = {}
    onetwo['enion']['data']            = None
    onetwo['enion']['unit']            = "1/m^3"
    onetwo['enion']['name']            = "Ion Density"
    onetwo['enion']['info']            = "Thermal Ion Density"

    onetwo['p_flux']                   = {} 
    onetwo['p_flux']['data']           = None
    onetwo['p_flux']['unit']           = "1/m^2/s"
    onetwo['p_flux']['name']           = "Thermal Ion Particle Flux"
    onetwo['p_flux']['info']           = "Thermal Ion Particle Flux"
    
    onetwo['p_flux_conv']              = {} 
    onetwo['p_flux_conv']['data']      = None
    onetwo['p_flux_conv']['unit']      = "1/m^2/s"
    onetwo['p_flux_conv']['name']      = "Thermal Ion Convective Flux"
    onetwo['p_flux_conv']['info']      = "Thermal Ion Convective Flux"
    
    onetwo['e_fluxe']                  = {} 
    onetwo['e_fluxe']['data']          = None
    onetwo['e_fluxe']['unit']          = "J/m^2/s"
    onetwo['e_fluxe']['name']          = "Electron Energy Flux"
    onetwo['e_fluxe']['info']          = "Electron Energy Flux"
    
    onetwo['e_fluxe_conv']             = {} 
    onetwo['e_fluxe_conv']['data']     = None
    onetwo['e_fluxe_conv']['unit']     = "J/m^2/s"
    onetwo['e_fluxe_conv']['name']     = "Electron Convective Energy Flux"
    onetwo['e_fluxe_conv']['info']     = "Electron Convective Energy Flux"
    
    onetwo['e_fluxi']                  = {} 
    onetwo['e_fluxi']['data']          = None
    onetwo['e_fluxi']['unit']          = "J/m^2/s"
    onetwo['e_fluxi']['name']          = "Total Thermal Ion Energy Flux"
    onetwo['e_fluxi']['info']          = "Total Thermal Ion Energy Flux"
    
    onetwo['e_fluxi_conv']             = {} 
    onetwo['e_fluxi_conv']['data']     = None
    onetwo['e_fluxi_conv']['unit']     = "J/m^2/s"
    onetwo['e_fluxi_conv']['name']     = "Thermal Ion Convective Energy Flux"
    onetwo['e_fluxi_conv']['info']     = "Thermal Ion Convective Energy Flux"
    
    onetwo['fday_flux']                = {} 
    onetwo['fday_flux']['data']        = None
    onetwo['fday_flux']['unit']        = "T/s"
    onetwo['fday_flux']['info']        = "Faraday Law Associated Flux"
    
    onetwo['fday_flux_conv']           = {} 
    onetwo['fday_flux_conv']['data']   = None
    onetwo['fday_flux_conv']['unit']   = "T/s"
    onetwo['fday_flux_conv']['info']   = "Faraday Law Associated Convective Flux"
    
    onetwo['rot_flux']                 = {} 
    onetwo['rot_flux']['data']         = None
    onetwo['rot_flux']['unit']         = "kg/s^2"
    onetwo['rot_flux']['info']         = "Flux Associated with Toroidal Rotation"
    
    onetwo['rot_flux_conv']            = {} 
    onetwo['rot_flux_conv']['data']    = None
    onetwo['rot_flux_conv']['unit']    = "kg/s^2"
    onetwo['rot_flux_conv']['info']    = "Convective Flux Associated with Toroidal Rotation"
    
    onetwo['tglf_elct_p_flux']        = {} 
    onetwo['tglf_elct_p_flux']['data']= None
    onetwo['tglf_elct_p_flux']['unit']= "1/m^2/s"
    onetwo['tglf_elct_p_flux']['info']= "TGLF Turbulent Electron Particle Flux"
    
    onetwo['tglf_ion_p_flux']          = {} 
    onetwo['tglf_ion_p_flux']['data']  = None
    onetwo['tglf_ion_p_flux']['unit']  = "1/m^2/s"
    onetwo['tglf_ion_p_flux']['info']  = "TGLF Turbulent Effective Primary Particle Flux"
    
    onetwo['tglf_imp_p_flux']          = {} 
    onetwo['tglf_imp_p_flux']['data']  = None
    onetwo['tglf_imp_p_flux']['unit']  = "1/m^2/s"
    onetwo['tglf_imp_p_flux']['info']  = "TGLF Turbulent Effective Impurity Particle Flux"
    
    onetwo['tglf_elc_e_flux']        = {} 
    onetwo['tglf_elc_e_flux']['data']= None
    onetwo['tglf_elc_e_flux']['unit']= "J/m^2/s"
    onetwo['tglf_elc_e_flux']['info']= "TGLF Turbulent Electron Energy Flux"
    
    onetwo['tglf_ion_e_flux']          = {} 
    onetwo['tglf_ion_e_flux']['data']  = None
    onetwo['tglf_ion_e_flux']['unit']  = "J/m^2/s"
    onetwo['tglf_ion_e_flux']['info']  = "TGLF Turbulent Effective Primary Energy Flux"
    
    onetwo['tglf_imp_e_flux']          = {} 
    onetwo['tglf_imp_e_flux']['data']  = None
    onetwo['tglf_imp_e_flux']['unit']  = "J/m^2/s"
    onetwo['tglf_imp_e_flux']['info']  = "TGLF Turbulent Effective Impurity Energy Flux"
    
    onetwo['tglf_elc_m_flux']        = {} 
    onetwo['tglf_elc_m_flux']['data']= None
    onetwo['tglf_elc_m_flux']['unit']= "kg/s^2"
    onetwo['tglf_elc_m_flux']['info']= "TGLF Turbulent Electron Momentum Flux"
    
    onetwo['tglf_ion_m_flux']          = {} 
    onetwo['tglf_ion_m_flux']['data']  = None
    onetwo['tglf_ion_m_flux']['unit']  = "kg/s^2"
    onetwo['tglf_ion_m_flux']['info']  = "TGLF Turbulent Effective Primary Momentum Flux"
    
    onetwo['tglf_imp_m_flux']          = {} 
    onetwo['tglf_imp_m_flux']['data']  = None
    onetwo['tglf_imp_m_flux']['unit']  = "kg/s^2"
    onetwo['tglf_imp_m_flux']['info']  = "TGLF Turbulent Effective Impurity Momentum Flux"
    
    onetwo['dnedt']                    = {} 
    onetwo['dnedt']['data']            = None
    onetwo['dnedt']['unit']            = "1/m^3/s"
    onetwo['dnedt']['info']            = "Rate of Change of ene at time=0.0"
    
    onetwo['en_bc']                    = {} 
    onetwo['en_bc']['data']            = None
    onetwo['en_bc']['unit']            = "1/m^3"
    onetwo['en_bc']['info']            = "BC Density Profiles at t=Time, species: d c"
    
    onetwo['flux_bc']                  = {} 
    onetwo['flux_bc']['data']          = None
    onetwo['flux_bc']['unit']          = "keV/m^2/s"
    onetwo['flux_bc']['info']          = "BC Flux Profiles at time=Time, species: d c"
    
    onetwo['sion']                     = {}
    onetwo['sion']['data']             = None
    onetwo['sion']['unit']             = "#/m^3/s"
    onetwo['sion']['info']             = "Source of Ions Due to Electron Impact Ionozation of Neutrals"

    onetwo['srecom']                   = {}
    onetwo['srecom']['data']           = None
    onetwo['srecom']['unit']           = "#/m^3/s"
    onetwo['srecom']['info']           = "Source of Ions Due to Recombination"

    onetwo['scx']                      = {}
    onetwo['scx']['data']              = None
    onetwo['scx']['unit']              = "#/m^3/s"
    onetwo['scx']['info']              = "Source Due to Charge Exchange of Thermal Neutral, d c"

    onetwo['sbcx']                     = {}
    onetwo['sbcx']['data']             = None
    onetwo['sbcx']['unit']             = "#/m^3/s"
    onetwo['sbcx']['info']             = "Source of Fast Ions (and Theraml Neutrals) Due to Charge Exchange of Beam Neutrals with Thermal Ions"

    onetwo['stsource']                  = {} 
    onetwo['stsource']['data']          = None
    onetwo['stsource']['unit']          = "1/m^3/s"
    onetwo['stsource']['info']          = "Total Source Rate, d"
    
    onetwo['dudtsv']                = {} 
    onetwo['dudtsv']['data']        = None
    onetwo['dudtsv']['unit']        = "(1 or keV)/(m^3 sec)"
    onetwo['dudtsv']['info']        = "s dot"
    
    onetwo['enn']                = {} 
    onetwo['enn']['data']        = None
    onetwo['enn']['unit']        = "#/m^3"
    onetwo['enn']['info']        = "neutral density, #/meter^3, species: d"
    
    onetwo['ennw']                = {} 
    onetwo['ennw']['data']        = None
    onetwo['ennw']['unit']        = "#/m^3"
    onetwo['ennw']['info']        = "neutral density,due to wall source , species: d"
    
    onetwo['ennv']                = {} 
    onetwo['ennv']['data']        = None
    onetwo['ennv']['unit']        = "#/m^3"
    onetwo['ennv']['info']        = "neutral density,due to volume source , species: d"
    
    onetwo['volsn']                = {} 
    onetwo['volsn']['data']        = None
    onetwo['volsn']['unit']        = "#/m^3/s"
    onetwo['volsn']['info']        = "Source of neutrals"
    
    onetwo['z']                = {} 
    onetwo['z']['data']        = None
    onetwo['z']['unit']        = None
    onetwo['z']['info']        = "charge  z ,species : d c"
    
    onetwo['zsq']                = {} 
    onetwo['zsq']['data']        = None
    onetwo['zsq']['unit']        = None
    onetwo['zsq']['info']        = "charge  z ,species : d c"
    
    onetwo['stfuse']                = {} 
    onetwo['stfuse']['data']        = None
    onetwo['stfuse']['unit']        = "#/m^2/s"
    onetwo['stfuse']['info']        = "thermal fusion rate"
    
    onetwo['sbfuse']                = {} 
    onetwo['sbfuse']['data']        = None
    onetwo['sbfuse']['unit']        = "#/m^2/s"
    onetwo['sbfuse']['info']        = None
    
    onetwo['spellet']                = {} 
    onetwo['spellet']['data']        = None
    onetwo['spellet']['unit']        = "#/m^2/s"
    onetwo['spellet']['info']        = "THERMAL ion source due to pellets"
    
    onetwo['sbeame']                = {} 
    onetwo['sbeame']['data']        = None
    onetwo['sbeame']['unit']        = "#/m^2/s"
    onetwo['sbeame']['info']        = "beam electron source"
    
    onetwo['sbeam']                = {} 
    onetwo['sbeam']['data']        = None
    onetwo['sbeam']['unit']        = "#/m^2/s"
    onetwo['sbeam']['info']        = "beam ion source" 
    
    onetwo['enbeam']                = {} 
    onetwo['enbeam']['data']        = None
    onetwo['enbeam']['unit']        = "#/m^3"
    onetwo['enbeam']['info']        = "fast ion density"
    
    onetwo['curden']                = {} 
    onetwo['curden']['data']        = None
    onetwo['curden']['unit']        = "A/m^2"
    onetwo['curden']['info']        = "total toroidal current density, <Jtor R0/R>"
    
    onetwo['curpar']                = {} 
    onetwo['curpar']['data']        = None
    onetwo['curpar']['unit']        = "A/m^2"
    onetwo['curpar']['info']        = "total parallel current density, <J.B/Bt0>"
    
    onetwo['curohm']                = {} 
    onetwo['curohm']['data']        = None
    onetwo['curohm']['unit']        = "A/m^2"
    onetwo['curohm']['info']        = "ohmic current density"
    
    onetwo['curboot']                = {} 
    onetwo['curboot']['data']        = None
    onetwo['curboot']['unit']        = "A/m^2"
    onetwo['curboot']['info']        = "bootstrap current density"
    
    onetwo['curbeam']                = {} 
    onetwo['curbeam']['data']        = None
    onetwo['curbeam']['unit']        = "A/m^2"
    onetwo['curbeam']['info']        = "beam driven  current density"
    
    onetwo['currf']                = {} 
    onetwo['currf']['data']        = None
    onetwo['currf']['unit']        = "A/m^2"
    onetwo['currf']['info']        = "rf driven  current density"
    
    onetwo['etor']                = {} 
    onetwo['etor']['data']        = None
    onetwo['etor']['unit']        = "V/m"
    onetwo['etor']['info']        = "toroidal electric field profile"
    
    onetwo['rbp']                = {} 
    onetwo['rbp']['data']        = None
    onetwo['rbp']['unit']        = "T.m"
    onetwo['rbp']['info']        = "rho*bp0*fcap*gcap*hcap"
    
    onetwo['psivalnpsi']                = {} 
    onetwo['psivalnpsi']['data']        = None
    onetwo['psivalnpsi']['unit']        = "V.s/rad"
    onetwo['psivalnpsi']['info']        = "psivalnpsi(npsi) grid, edge to magnetic axis"
    
    onetwo['ravgnpsi']                = {} 
    onetwo['ravgnpsi']['data']        = None
    onetwo['ravgnpsi']['unit']        = "m"
    onetwo['ravgnpsi']['info']        = "ravg: <R> avg radius on mhd grid"
    
    onetwo['ravginpsi']                = {} 
    onetwo['ravginpsi']['data']        = None
    onetwo['ravginpsi']['unit']        = "1/m"
    onetwo['ravginpsi']['info']        = "ravgi:<1/R> on mhd grid"
    
    onetwo['fpsinpsi']                = {} 
    onetwo['fpsinpsi']['data']        = None
    onetwo['fpsinpsi']['unit']        = "T.m"
    onetwo['fpsinpsi']['info']        = "fpsi: f of psi (= R*Bt) on psivalnpsi(npsi) grid"
    
    onetwo['pprim']                = {} 
    onetwo['pprim']['data']        = None
    onetwo['pprim']['unit']        = "N/m^2/V/s"
    onetwo['pprim']['info']        = "dp/dpsi on transport grid (A/m^3)"
    
    onetwo['ffprim']                = {} 
    onetwo['ffprim']['data']        = None
    onetwo['ffprim']['unit']        = "kg/A/s^2"
    onetwo['ffprim']['info']        = "f*df/dpsi: on transport grid"
    
    onetwo['bp']                = {} 
    onetwo['bp']['data']        = None
    onetwo['bp']['unit']        = "T"
    onetwo['bp']['info']        = "<Bp> : flux avg B poloidal on transport grid"
    
    onetwo['bprmaj']                = {} 
    onetwo['bprmaj']['data']        = None
    onetwo['bprmaj']['unit']        = "T"
    onetwo['bprmaj']['info']        = "B poloidal on rmaj (and transport rho)  grid"
    
    onetwo['btotrmaj']                = {} 
    onetwo['btotrmaj']['data']        = None
    onetwo['btotrmaj']['unit']        = "T"
    onetwo['btotrmaj']['info']        = "Btotal on transport rho grid"
    
    onetwo['zeff']                = {} 
    onetwo['zeff']['data']        = None
    onetwo['zeff']['unit']        = None
    onetwo['zeff']['info']        = "Effective Charge"
    
    onetwo['vpol']                = {} 
    onetwo['vpol']['data']        = None
    onetwo['vpol']['unit']        = "m/s"
    onetwo['vpol']['info']        = "Poloidal Velocity Profile"
    
    onetwo['vpol_nclass']                = {} 
    onetwo['vpol_nclass']['data']        = None
    onetwo['vpol_nclass']['unit']        = "m/s"
    onetwo['vpol_nclass']['info']        = "poloidal velocity profile, forcebal Nclass model"
    
    onetwo['vpar']                = {} 
    onetwo['vpar']['data']        = None
    onetwo['vpar']['unit']        = "m/s"
    onetwo['vpar']['info']        = "parallel velocity profile"
    
    onetwo['vpar_nclass']                = {} 
    onetwo['vpar_nclass']['data']        = None
    onetwo['vpar_nclass']['unit']        = "m/s"
    onetwo['vpar_nclass']['info']        = "parallel velocity profile, forcebal Nclass model"
    
    onetwo['er_tot_nclass']                = {} 
    onetwo['er_tot_nclass']['data']        = None
    onetwo['er_tot_nclass']['unit']        = "V/m"
    onetwo['er_tot_nclass']['info']        = "Nclass total radial electric field"
    
    onetwo['angrot']                = {} 
    onetwo['angrot']['data']        = None
    onetwo['angrot']['unit']        = "rad/s"
    onetwo['angrot']['info']        = "angular rotation speed profile"
    
    onetwo['d']                = {} 
    onetwo['d']['data']        = None
    onetwo['d']['unit']        = None
    onetwo['d']['info']        = "diffusion matrix(ntot,ntot,nj) , on half grid"
    
    onetwo['chieinv']                = {} 
    onetwo['chieinv']['data']        = None
    onetwo['chieinv']['unit']        = "m^2/s"
    onetwo['chieinv']['info']        = "electron thermal diffusivity, on half grid"
    
    onetwo['chiinv']                = {} 
    onetwo['chiinv']['data']        = None
    onetwo['chiinv']['unit']        = "m^2/s"
    onetwo['chiinv']['info']        = "ion thermal diffusivity, on half grid"
    
    onetwo['xkineo']                = {} 
    onetwo['xkineo']['data']        = None
    onetwo['xkineo']['unit']        = "1/m/s"
    onetwo['xkineo']['info']        = "ion neoclassical thermal conductivity"
    
    onetwo['xkeneo']                = {} 
    onetwo['xkeneo']['data']        = None
    onetwo['xkeneo']['unit']        = "1/m/s"
    onetwo['xkeneo']['info']        = "Electron neoclassical thermal conductivity"
    
    onetwo['dpedt']                = {} 
    onetwo['dpedt']['data']        = None
    onetwo['dpedt']['unit']        = "W/m^3"
    onetwo['dpedt']['info']        = "1.5*dpedt, power density due to electron pressure"
    
    onetwo['dpidt']                = {} 
    onetwo['dpidt']['data']        = None
    onetwo['dpidt']['unit']        = "W/m^3"
    onetwo['dpidt']['info']        = "1.5*dpidt, power density due to ion pressure"
    
    onetwo['qconde']                = {} 
    onetwo['qconde']['data']        = None
    onetwo['qconde']['unit']        = "W/m^3"
    onetwo['qconde']['info']        = "Electron Conduction"
    
    onetwo['qcondi']                = {} 
    onetwo['qcondi']['data']        = None
    onetwo['qcondi']['unit']        = "W/m^3"
    onetwo['qcondi']['info']        = "Ion Conduction"
    
    onetwo['qconve']                = {} 
    onetwo['qconve']['data']        = None
    onetwo['qconve']['unit']        = "W/m^3"
    onetwo['qconve']['info']        = "Electron Convection"
    
    onetwo['qconvi']                = {} 
    onetwo['qconvi']['data']        = None
    onetwo['qconvi']['unit']        = "W/m^3"
    onetwo['qconvi']['info']        = "Ion Convection"
    
    onetwo['qbeame']                = {} 
    onetwo['qbeame']['data']        = None
    onetwo['qbeame']['unit']        = "W/m^3"
    onetwo['qbeame']['info']        = "power to electron from beam"
    
    onetwo['qbeami']                = {} 
    onetwo['qbeami']['data']        = None
    onetwo['qbeami']['unit']        = "W/m^3"
    onetwo['qbeami']['info']        = "power to ion from beam"
    
    onetwo['qdelt']                = {} 
    onetwo['qdelt']['data']        = None
    onetwo['qdelt']['unit']        = "W/m^3"
    onetwo['qdelt']['info']        = "Source of energy to electrons due to collisional energy exchange with thermal ions"
    
    onetwo['qexch']                = {} 
    onetwo['qexch']['data']        = None
    onetwo['qexch']['unit']        = "W/m^3"
    onetwo['qexch']['info']        = "nomalous electron-ion energy exchange term"
    
    onetwo['qrfe']                = {} 
    onetwo['qrfe']['data']        = None
    onetwo['qrfe']['unit']        = "W/m^3"
    onetwo['qrfe']['info']        = "RF Electron Heating"
    
    onetwo['qrfi']                = {} 
    onetwo['qrfi']['data']        = None
    onetwo['qrfi']['unit']        = "W/m^3"
    onetwo['qrfi']['info']        = "RF Ion Heating"
    
    onetwo['qione']                = {} 
    onetwo['qione']['data']        = None
    onetwo['qione']['unit']        = "W/m^3"
    onetwo['qione']['info']        = "electron power density due to recombination and impact ionization"
    
    onetwo['qioni']                = {} 
    onetwo['qioni']['data']        = None
    onetwo['qioni']['unit']        = "W/m^3"
    onetwo['qioni']['info']        = "Ion power density due to recombination and impact ionization"
    
    onetwo['qcx']                = {} 
    onetwo['qcx']['data']        = None
    onetwo['qcx']['unit']        = "W/m^3"
    onetwo['qcx']['info']        = "ion power density due to neutral-ion charge exchange"
    
    onetwo['qe2d']                = {} 
    onetwo['qe2d']['data']        = None
    onetwo['qe2d']['unit']        = "W/m^3"
    onetwo['qe2d']['info']        = "2D electron heating"
    
    onetwo['qi2d']                = {} 
    onetwo['qi2d']['data']        = None
    onetwo['qi2d']['unit']        = "W/m^3"
    onetwo['qi2d']['info']        = "2D Ion heating"
    
    onetwo['qfuse']                = {} 
    onetwo['qfuse']['data']        = None
    onetwo['qfuse']['unit']        = "W/m^3"
    onetwo['qfuse']['info']        = "total fusion electron heating"
    
    onetwo['qfusi']                = {} 
    onetwo['qfusi']['data']        = None
    onetwo['qfusi']['unit']        = "W/m^3"
    onetwo['qfusi']['info']        = "total fusion ion heating"
    
    onetwo['qbfuse']                = {} 
    onetwo['qbfuse']['data']        = None
    onetwo['qbfuse']['unit']        = "W/m^3"
    onetwo['qbfuse']['info']        = "beam fusion electron heating"
    
    onetwo['qbfusi']                = {} 
    onetwo['qbfusi']['data']        = None
    onetwo['qbfusi']['unit']        = "W/m^3"
    onetwo['qbfusi']['info']        = "beam fusion ion heating"
    
    onetwo['qmag']                = {} 
    onetwo['qmag']['data']        = None
    onetwo['qmag']['unit']        = "W/m^3"
    onetwo['qmag']['info']        = "qmag electron heating"
    
    onetwo['qsawe']                = {} 
    onetwo['qsawe']['data']        = None
    onetwo['qsawe']['unit']        = "W/m^3"
    onetwo['qsawe']['info']        = "sawtooth electron heating"
    
    onetwo['qsawi']                = {} 
    onetwo['qsawi']['data']        = None
    onetwo['qsawi']['unit']        = "W/m^3"
    onetwo['qsawi']['info']        = "sawtooth ion heating"
    
    onetwo['qrad']                = {} 
    onetwo['qrad']['data']        = None
    onetwo['qrad']['unit']        = "W/m^3"
    onetwo['qrad']['info']        = "radiated power density"
    
    onetwo['vpinch_nclass']                = {} 
    onetwo['vpinch_nclass']['data']        = None
    onetwo['vpinch_nclass']['unit']        = "m/s"
    onetwo['vpinch_nclass']['info']        = "nclass derived pinch velocity: e,plus ion species"
    
    onetwo['brems_nions']                = {} 
    onetwo['brems_nions']['data']        = None
    onetwo['brems_nions']['unit']        = "W/m^3"
    onetwo['brems_nions']['info']        = "radiative loss  species: d c"
    
    onetwo['cyclo_rad']                = {} 
    onetwo['cyclo_rad']['data']        = None
    onetwo['cyclo_rad']['unit']        = "W/m^3"
    onetwo['cyclo_rad']['info']        = "cyclotron radiation"
    
    onetwo['omegale']                = {} 
    onetwo['omegale']['data']        = None
    onetwo['omegale']['unit']        = "W/m^3"
    onetwo['omegale']['info']        = "beam electron energy correction due to rotation"
    
    onetwo['qomegapi']                = {} 
    onetwo['qomegapi']['data']        = None
    onetwo['qomegapi']['unit']        = "W/m^3"
    onetwo['qomegapi']['info']        = "beam ion energy correction due to rotation"
    
    onetwo['qangce']                = {} 
    onetwo['qangce']['data']        = None
    onetwo['qangce']['unit']        = "W/m^3"
    onetwo['qangce']['info']        = "beam ion energy correction due to rotation"
    
    onetwo['sprcxre']                = {} 
    onetwo['sprcxre']['data']        = None
    onetwo['sprcxre']['unit']        = "kg/m/s^2"
    onetwo['sprcxre']['info']        = "Torque on ions as thermal ions are lost to charge exchange with fast neutral or recombination"

    onetwo['sprcxree']                = {} 
    onetwo['sprcxree']['data']        = None
    onetwo['sprcxree']['unit']        = "W/m^3"
    onetwo['sprcxree']['info']        = "beam ion energy correction due to rotation"

    onetwo['spreimpe']                = {} 
    onetwo['spreimpe']['data']        = None
    onetwo['spreimpe']['unit']        = "W/m^3"
    onetwo['spreimpe']['info']        = "beam ion energy correction due to rotation"

    onetwo['pfuse_tot']                = {} 
    onetwo['pfuse_tot']['data']        = None
    onetwo['pfuse_tot']['unit']        = "W"
    onetwo['pfuse_tot']['info']        = "total electron plus ion thermal fusion heating power"

    onetwo['qrad_tot']                = {} 
    onetwo['qrad_tot']['data']        = None
    onetwo['qrad_tot']['unit']        = "W"
    onetwo['qrad_tot']['info']        = "total electron power radiated from plasma"

    onetwo['brems_tot']                = {} 
    onetwo['brems_tot']['data']        = None
    onetwo['brems_tot']['unit']        = "W"
    onetwo['brems_tot']['info']        = "total electron radiated power due to ion species"

    onetwo['qohm']                = {} 
    onetwo['qohm']['data']        = None
    onetwo['qohm']['unit']        = "W/m^3"
    onetwo['qohm']['info']        = "(electron) ohmic power density"

    onetwo['rmajavnpsi']                = {} 
    onetwo['rmajavnpsi']['data']        = None
    onetwo['rmajavnpsi']['unit']        = "m"
    onetwo['rmajavnpsi']['info']        = "average major radius of each flux surface, meter, evaluated at elevation of magnetic axis"

    onetwo['rminavnpsi']                = {} 
    onetwo['rminavnpsi']['data']        = None
    onetwo['rminavnpsi']['unit']        = "m"
    onetwo['rminavnpsi']['info']        = "average minor radius of each flux surface, meter, evaluated at elevation of magnetic axis"

    onetwo['psivolpnpsi']                = {} 
    onetwo['psivolpnpsi']['data']        = None
    onetwo['psivolpnpsi']['unit']        = "m^3"
    onetwo['psivolpnpsi']['info']        = "volume of each flux surface"

    onetwo['elongxnpsi']                = {} 
    onetwo['elongxnpsi']['data']        = None
    onetwo['elongxnpsi']['unit']        = None
    onetwo['elongxnpsi']['info']        = "elongation of each flux surface"

    onetwo['triangnpsi_u']                = {} 
    onetwo['triangnpsi_u']['data']        = None
    onetwo['triangnpsi_u']['unit']        = None
    onetwo['triangnpsi_u']['info']        = "upper triangularity of each flux surface"

    onetwo['triangnpsi_l']                = {} 
    onetwo['triangnpsi_l']['data']        = None
    onetwo['triangnpsi_l']['unit']        = None
    onetwo['triangnpsi_l']['info']        = "lower triangularity of each flux surface"

    onetwo['pindentnpsi']                = {} 
    onetwo['pindentnpsi']['data']        = None
    onetwo['pindentnpsi']['unit']        = None
    onetwo['pindentnpsi']['info']        = "indentation of each flux surface"

    onetwo['sfareanpsi']                = {} 
    onetwo['sfareanpsi']['data']        = None
    onetwo['sfareanpsi']['unit']        = "m^2"
    onetwo['sfareanpsi']['info']        = "surface area of each flux surface, this is 4*pi*pi*R0*hcap*rho*<ABS(grad rho)>"

    onetwo['cxareanpsi']                = {} 
    onetwo['cxareanpsi']['data']        = None
    onetwo['cxareanpsi']['unit']        = "m^2"
    onetwo['cxareanpsi']['info']        = "cross-sectional area of each flux"

    onetwo['cxareao']                   = {} 
    onetwo['cxareao']['data']           = None
    onetwo['cxareao']['unit']           = "m^2"
    onetwo['cxareao']['info']           = "plasma cross-sectional area"
    
    onetwo['grho1npsi']                = {} 
    onetwo['grho1npsi']['data']        = None
    onetwo['grho1npsi']['unit']        = None
    onetwo['grho1npsi']['info']        = "flux surface average absolute grad rho"

    onetwo['grho2npsi']                = {} 
    onetwo['grho2npsi']['data']        = None
    onetwo['grho2npsi']['unit']        = None
    onetwo['grho2npsi']['info']        = "flux surface average (grad rho)**2"

    onetwo['qpsinpsi']                = {} 
    onetwo['qpsinpsi']['data']        = None
    onetwo['qpsinpsi']['unit']        = None
    onetwo['qpsinpsi']['info']        = "q on eqdsk psigrid"

    onetwo['pressnpsi']                = {} 
    onetwo['pressnpsi']['data']        = None
    onetwo['pressnpsi']['unit']        = "N/m^2"
    onetwo['pressnpsi']['info']        = "pressure on eqdsk psigrid"

    onetwo['ffprimnpsi']                = {} 
    onetwo['ffprimnpsi']['data']        = None
    onetwo['ffprimnpsi']['unit']        = "kf/A/s^2"
    onetwo['ffprimnpsi']['info']        = "ffprime  on eqdsk psigrid"

    onetwo['pprimnpsi']                = {} 
    onetwo['pprimnpsi']['data']        = None
    onetwo['pprimnpsi']['unit']        = "A/m^3"
    onetwo['pprimnpsi']['info']        = "pprime  on eqdsk psigrid"

    onetwo['nplasbdry']                = {} 
    onetwo['nplasbdry']['data']        = None
    onetwo['nplasbdry']['unit']        = "m"
    onetwo['nplasbdry']['info']        = "number of points for plasma boundary"

    onetwo['rplasbdry']                = {} 
    onetwo['rplasbdry']['data']        = None
    onetwo['rplasbdry']['unit']        = "m"
    onetwo['rplasbdry']['info']        = "r points for plasma boundary"

    onetwo['zplasbdry']                = {} 
    onetwo['zplasbdry']['data']        = None
    onetwo['zplasbdry']['unit']        = "m"
    onetwo['zplasbdry']['info']        = "z points for plasma boundary"

    onetwo['rlimiter']                = {} 
    onetwo['rlimiter']['data']        = None
    onetwo['rlimiter']['unit']        = "m"
    onetwo['rlimiter']['info']        = "R points for limiter"

    onetwo['zlimiter']                = {} 
    onetwo['zlimiter']['data']        = None
    onetwo['zlimiter']['unit']        = "m"
    onetwo['zlimiter']['info']        = "Z points for limiter"

    onetwo['storqueb']                = {} 
    onetwo['storqueb']['data']        = None
    onetwo['storqueb']['unit']        = "kg/m/s^2"
    onetwo['storqueb']['info']        = "Torque due to beams (sprbeame+sprbeami+ssprcxl)"

    onetwo['totcur_bc']                = {} 
    onetwo['totcur_bc']['data']        = None
    onetwo['totcur_bc']['unit']        = "A"
    onetwo['totcur_bc']['info']        = "boundary condition total current at t = time"

    onetwo['vloop_bc']                = {} 
    onetwo['vloop_bc']['data']        = None
    onetwo['vloop_bc']['unit']        = "V"
    onetwo['vloop_bc']['info']        = "boundary condition loop voltage at t = time"

    onetwo['fix_edge_te_bc']                = {} 
    onetwo['fix_edge_te_bc']['data']        = None
    onetwo['fix_edge_te_bc']['unit']        = None
    onetwo['fix_edge_te_bc']['info']        = "te boundary condition rho flags at t = time"

    onetwo['fix_edge_ti_bc']                = {} 
    onetwo['fix_edge_ti_bc']['data']        = None
    onetwo['fix_edge_ti_bc']['unit']        = None
    onetwo['fix_edge_ti_bc']['info']        = "ti boundary condition rho flags at t = time"

    onetwo['fix_edge_rot_bc']                = {} 
    onetwo['fix_edge_rot_bc']['data']        = None
    onetwo['fix_edge_rot_bc']['unit']        = None
    onetwo['fix_edge_rot_bc']['info']        = "rot boundary condition rho flags at t = time"

    onetwo['fix_edge_ni_bc']                = {} 
    onetwo['fix_edge_ni_bc']['data']        = None
    onetwo['fix_edge_ni_bc']['unit']        = None
    onetwo['fix_edge_ni_bc']['info']        = " boundary condition rho flags at t = time"

    onetwo['te_bc']                = {} 
    onetwo['te_bc']['data']        = None
    onetwo['te_bc']['unit']        = "keV"
    onetwo['te_bc']['info']        = "boundary condition Te at t= time"

    onetwo['ti_bc']                = {} 
    onetwo['ti_bc']['data']        = None
    onetwo['ti_bc']['unit']        = "keV"
    onetwo['ti_bc']['info']        = "boundary condition Ti at t = time"

    onetwo['ene_bc']                = {} 
    onetwo['ene_bc']['data']        = None
    onetwo['ene_bc']['unit']        = "#/m^3"
    onetwo['ene_bc']['info']        = "bc profile: ene at t = time"

    onetwo['zeff_bc']                = {} 
    onetwo['zeff_bc']['data']        = None
    onetwo['zeff_bc']['unit']        = None
    onetwo['zeff_bc']['info']        = "bc profile: zeff at t = time"

    onetwo['angrot_bc']                = {} 
    onetwo['angrot_bc']['data']        = None
    onetwo['angrot_bc']['unit']        = "rad/s"
    onetwo['angrot_bc']['info']        = "angular rotation speed profile at t = time"

    onetwo['wbeam']                = {} 
    onetwo['wbeam']['data']        = None
    onetwo['wbeam']['unit']        = "keV/m^3"
    onetwo['wbeam']['info']        = "fast ion stored energy density"

    onetwo['walp']                = {} 
    onetwo['walp']['data']        = None
    onetwo['walp']['unit']        = "keV/m^3"
    onetwo['walp']['info']        = "fast alpha stored energy density"

    onetwo['enalp']                = {} 
    onetwo['enalp']['data']        = None
    onetwo['enalp']['unit']        = "#/m^3"
    onetwo['enalp']['info']        = "fast alpha density"

    onetwo['eps']                = {} 
    onetwo['eps']['data']        = None
    onetwo['eps']['unit']        = None
    onetwo['eps']['info']        = "horizontal inverse aspect ratio = (rmax-rmin)/(rmax+rmin)"

    onetwo['rcap']                = {} 
    onetwo['rcap']['data']        = None
    onetwo['rcap']['unit']        = "m"
    onetwo['rcap']['info']        = "<R>"

    onetwo['rcapi']                = {} 
    onetwo['rcapi']['data']        = None
    onetwo['rcapi']['unit']        = "1/m"
    onetwo['rcapi']['info']        = "<1/R>"

    onetwo['r2cap']                = {} 
    onetwo['r2cap']['data']        = None
    onetwo['r2cap']['unit']        = None
    onetwo['r2cap']['info']        = "<R0**2/R**2>"

    onetwo['r2capi']                = {} 
    onetwo['r2capi']['data']        = None
    onetwo['r2capi']['unit']        = "m^2"
    onetwo['r2capi']['info']        = "<R**2>"

    onetwo['xhm2']                = {} 
    onetwo['xhm2']['data']        = None
    onetwo['xhm2']['unit']        = None
    onetwo['xhm2']['info']        = "< (B total/ B axis)**2 > (=1 for circular plasmas)"

    onetwo['xi11']                = {} 
    onetwo['xi11']['data']        = None
    onetwo['xi11']['unit']        = None
    onetwo['xi11']['info']        = "( = 1.95 sqrt(eps)for circular plasmas)"

    onetwo['xi33']                = {} 
    onetwo['xi33']['data']        = None
    onetwo['xi33']['unit']        = None
    onetwo['xi33']['info']        = "( = 1.95 sqrt(eps)for circular plasmas)"

    onetwo['xips']                = {} 
    onetwo['xips']['data']        = None
    onetwo['xips']['unit']        = None
    onetwo['xips']['info']        = "<(Baxis/B)**2)> - 1./(<(B/Baxis)**2> )( = 2 eps**2 for circular plasmas)"

    onetwo['dfdt']                = {} 
    onetwo['dfdt']['data']        = None
    onetwo['dfdt']['unit']        = "1/s"
    onetwo['dfdt']['info']        = "(d/dt)Fcap"

    onetwo['dgdt']                = {} 
    onetwo['dgdt']['data']        = None
    onetwo['dgdt']['unit']        = "1/s"
    onetwo['dgdt']['info']        = "(d/dt)Gcap"

    onetwo['dhdt']                = {} 
    onetwo['dhdt']['data']        = None
    onetwo['dhdt']['unit']        = "1/s"
    onetwo['dhdt']['info']        = "(d/dt)Hcap"

    onetwo['xnus']                = {} 
    onetwo['xnus']['data']        = None
    onetwo['xnus']['unit']        = None
    onetwo['xnus']['info']        = "nu* ion collison/bounce freq, species: d c"

    onetwo['xnuse']                = {} 
    onetwo['xnuse']['data']        = None
    onetwo['xnuse']['unit']        = None
    onetwo['xnuse']['info']        = "nu*e  electron collison/bounce freq"

    onetwo['ftrap']                = {} 
    onetwo['ftrap']['data']        = None
    onetwo['ftrap']['unit']        = None
    onetwo['ftrap']['info']        = "electron trapped particle fraction"

    onetwo['eta']                = {} 
    onetwo['eta']['data']        = None
    onetwo['eta']['unit']        = "Ohm.m"
    onetwo['eta']['info']        = "resistivity"

    onetwo['chiepc']                = {} 
    onetwo['chiepc']['data']        = None
    onetwo['chiepc']['unit']        = "m^2/s"
    onetwo['chiepc']['info']        = "Electron Paleoclassical Diffusivity"

    onetwo['neutr_ddn_th']                = {} 
    onetwo['neutr_ddn_th']['data']        = None
    onetwo['neutr_ddn_th']['unit']        = "#/m^3/s"
    onetwo['neutr_ddn_th']['info']        = "thermal -thermal neutron rate"

    onetwo['neutr_ddn_beam_thermal']                = {} 
    onetwo['neutr_ddn_beam_thermal']['data']        = None
    onetwo['neutr_ddn_beam_thermal']['unit']        = "#/m^3/s"
    onetwo['neutr_ddn_beam_thermal']['info']        = "beam -thermal neutron rate"

    onetwo['neutr_ddn_beam_beam']                = {} 
    onetwo['neutr_ddn_beam_beam']['data']        = None
    onetwo['neutr_ddn_beam_beam']['unit']        = "#/m^3/s"
    onetwo['neutr_ddn_beam_beam']['info']        = "beam - beam neutron rate"

    onetwo['neutr_ddn_knock']                = {} 
    onetwo['neutr_ddn_knock']['data']        = None
    onetwo['neutr_ddn_knock']['unit']        = "#/m^3/s"
    onetwo['neutr_ddn_knock']['info']        = "knock on neutron rate"

    onetwo['neutr_ddn_tot']                = {} 
    onetwo['neutr_ddn_tot']['data']        = None
    onetwo['neutr_ddn_tot']['unit']        = "#/m^3/s"
    onetwo['neutr_ddn_tot']['info']        = "total neutron rate"

    onetwo['total_neutr_ddn_th']                = {} 
    onetwo['total_neutr_ddn_th']['data']        = None
    onetwo['total_neutr_ddn_th']['unit']        = "1/s"
    onetwo['total_neutr_ddn_th']['info']        = "total thermal-thermal neutron rate"

    onetwo['total_neutr_ddn_beam_beam']                = {} 
    onetwo['total_neutr_ddn_beam_beam']['data']        = None
    onetwo['total_neutr_ddn_beam_beam']['unit']        = "1/s"
    onetwo['total_neutr_ddn_beam_beam']['info']        = "total beam - beam neutron rate"

    onetwo['total_neutr_ddn_beam_thermal']                = {} 
    onetwo['total_neutr_ddn_beam_thermal']['data']        = None
    onetwo['total_neutr_ddn_beam_thermal']['unit']        = "1/s"
    onetwo['total_neutr_ddn_beam_thermal']['info']        = "total beam - thermal neutron rate"

    onetwo['total_neutr_ddn_knock']                = {} 
    onetwo['total_neutr_ddn_knock']['data']        = None
    onetwo['total_neutr_ddn_knock']['unit']        = "1/s"
    onetwo['total_neutr_ddn_knock']['info']        = "total knock on  neutron rate"

    onetwo['total_neutr_ddn']                = {} 
    onetwo['total_neutr_ddn']['data']        = None
    onetwo['total_neutr_ddn']['unit']        = "1/s"
    onetwo['total_neutr_ddn']['info']        = "total neutron rate"

    onetwo['ddpt']                = {} 
    onetwo['ddpt']['data']        = None
    onetwo['ddpt']['unit']        = "#/m^3/s"
    onetwo['ddpt']['info']        = "d(d,p)t rate"

    onetwo['ddpt_tot']                = {} 
    onetwo['ddpt_tot']['data']        = None
    onetwo['ddpt_tot']['unit']        = "1/s"
    onetwo['ddpt_tot']['info']        = "total d(d,p)t reaction rate"

    onetwo['he3dp_th']                = {} 
    onetwo['he3dp_th']['data']        = None
    onetwo['he3dp_th']['unit']        = "#/m^3/s"
    onetwo['he3dp_th']['info']        = "he3(d,p)he4 thermal rate"

    onetwo['he3dp_th_tot']                = {} 
    onetwo['he3dp_th_tot']['data']        = None
    onetwo['he3dp_th_tot']['unit']        = "1/s"
    onetwo['he3dp_th_tot']['info']        = "total thermal He3(d,p)He4 reaction rate"

    onetwo['he3dp_beam_th']                = {} 
    onetwo['he3dp_beam_th']['data']        = None
    onetwo['he3dp_beam_th']['unit']        = "#/m^3/s"
    onetwo['he3dp_beam_th']['info']        = "he3(d,p)he4 beam-thermal rate"

    onetwo['he3dp_beam_th_tot']                = {} 
    onetwo['he3dp_beam_th_tot']['data']        = None
    onetwo['he3dp_beam_th_tot']['unit']        = "1/s"
    onetwo['he3dp_beam_th_tot']['info']        = "total beam thermal He3(d,p)He4 reaction rate"

    onetwo['he3dp_tot']                = {} 
    onetwo['he3dp_tot']['data']        = None
    onetwo['he3dp_tot']['unit']        = "1/s"
    onetwo['he3dp_tot']['info']        = "total beam plus thermal He3(d,p)He4 reaction rat"

    onetwo['he3_frac']                = {} 
    onetwo['he3_frac']['data']        = None
    onetwo['he3_frac']['unit']        = None
    onetwo['he3_frac']['info']        = "fraction of He that is He3"

    onetwo['he3_thermal_spin_pol']                = {} 
    onetwo['he3_thermal_spin_pol']['data']        = None
    onetwo['he3_thermal_spin_pol']['unit']        = None
    onetwo['he3_thermal_spin_pol']['info']        = "thermal He3 spin polarization relative to magnetic field direction"

    onetwo['he3_thermal_spin_pol']                = {} 
    onetwo['he3_thermal_spin_pol']['data']        = None
    onetwo['he3_thermal_spin_pol']['unit']        = None
    onetwo['he3_thermal_spin_pol']['info']        = "thermal He3 spin polarization relative to magnetic field direction"

    onetwo['d_beam_spin_pol']                = {} 
    onetwo['d_beam_spin_pol']['data']        = None
    onetwo['d_beam_spin_pol']['unit']        = None
    onetwo['d_beam_spin_pol']['info']        = "spin polarization of injected d beam"

    onetwo['omega_pi_d']                = {} 
    onetwo['omega_pi_d']['data']        = None
    onetwo['omega_pi_d']['unit']        = "rad/s"
    onetwo['omega_pi_d']['info']        = "plasma frequency species :d"

    onetwo['omega_ci_d']                = {} 
    onetwo['omega_ci_d']['data']        = None
    onetwo['omega_ci_d']['unit']        = "rad/s"
    onetwo['omega_ci_d']['info']        = "ion cyclotron  frequency species :d"

    onetwo['omega_lh_d']                = {} 
    onetwo['omega_lh_d']['data']        = None
    onetwo['omega_lh_d']['unit']        = "rad/s"
    onetwo['omega_lh_d']['info']        = "lower hybrid  frequency species :d"

    onetwo['omega_uh_d']                = {} 
    onetwo['omega_uh_d']['data']        = None
    onetwo['omega_uh_d']['unit']        = "rad/s"
    onetwo['omega_uh_d']['info']        = "upper hybrid  frequency species :d"

    onetwo['omega_ce']                = {} 
    onetwo['omega_ce']['data']        = None
    onetwo['omega_ce']['unit']        = "rad/s"
    onetwo['omega_ce']['info']        = "electron cyclotron  frequency"

    onetwo['omega_pe']                = {} 
    onetwo['omega_pe']['data']        = None
    onetwo['omega_pe']['unit']        = "rad/s"
    onetwo['omega_pe']['info']        = "electron plasma frequency"

    onetwo['stotal_ion']                = {} 
    onetwo['stotal_ion']['data']        = None
    onetwo['stotal_ion']['unit']        = "#/m^3/s"
    onetwo['stotal_ion']['info']        = "Total Sources of Ions"

    onetwo['sion_thermal_e']                = {} 
    onetwo['sion_thermal_e']['data']        = None
    onetwo['sion_thermal_e']['unit']        = "#/m^3/s"
    onetwo['sion_thermal_e']['info']        = "Source of electrons due to electron impact ionization of thermal neutrals"

    onetwo['srecom_e']                = {} 
    onetwo['srecom_e']['data']        = None
    onetwo['srecom_e']['unit']        = "#/m^3/s"
    onetwo['srecom_e']['info']        = "Source of electrons due to recombination"

    onetwo['sbeam_e']                = {} 
    onetwo['sbeam_e']['data']        = None
    onetwo['sbeam_e']['unit']        = "#/m^3/s"
    onetwo['sbeam_e']['info']        = "Source of electrons due to electron impact ionization of beam neutrals"

    onetwo['stotal_e']                = {} 
    onetwo['stotal_e']['data']        = None
    onetwo['stotal_e']['unit']        = "#/m^3/s"
    onetwo['stotal_e']['info']        = "Total sources of electrons"

    onetwo['qcond_e']                = {} 
    onetwo['qcond_e']['data']        = None
    onetwo['qcond_e']['unit']        = "W/m^3"
    onetwo['qcond_e']['info']        = "Conductive electron energy flow (total - convective)"

    onetwo['qconv_e']                = {} 
    onetwo['qconv_e']['data']        = None
    onetwo['qconv_e']['unit']        = "W/m^3"
    onetwo['qconv_e']['info']        = "Convective electron energy flow (five_halfs_te * (electron particle flux>0) * Te)"

    onetwo['qohm_e']                = {} 
    onetwo['qohm_e']['data']        = None
    onetwo['qohm_e']['unit']        = "W/m^3"
    onetwo['qohm_e']['info']        = "Source of energy to electrons due to ohmic heating"

    onetwo['qion_e']                = {} 
    onetwo['qion_e']['data']        = None
    onetwo['qion_e']['unit']        = "W/m^3"
    onetwo['qion_e']['info']        = "Source of energy to electrons due to recombination and ionization (sign?)"

    onetwo['qrad_e']                = {} 
    onetwo['qrad_e']['data']        = None
    onetwo['qrad_e']['unit']        = "W/m^3"
    onetwo['qrad_e']['info']        = "Source of energy from electrons due to radiation"

    onetwo['qomegal_e']                = {} 
    onetwo['qomegal_e']['data']        = None
    onetwo['qomegal_e']['unit']        = "W/m^3"
    onetwo['qomegal_e']['info']        = "Source of energy from electrons due to delayed beam ion momentum transfer"

    onetwo['qbeam_e']                = {} 
    onetwo['qbeam_e']['data']        = None
    onetwo['qbeam_e']['unit']        = "W/m^3"
    onetwo['qbeam_e']['info']        = "Source of energy to electrons due to beam heating"

    onetwo['qcond_i']                = {} 
    onetwo['qcond_i']['data']        = None
    onetwo['qcond_i']['unit']        = "W/m^3"
    onetwo['qcond_i']['info']        = "Conductive ion energy flow (total - convective)"

    onetwo['qconv_i']                = {} 
    onetwo['qconv_i']['data']        = None
    onetwo['qconv_i']['unit']        = "W/m^3"
    onetwo['qconv_i']['info']        = "Convective ion energy flow (five_halfs_ti * (total ion particle flux > 0) * ti)"

    onetwo['qdelt_i']                = {} 
    onetwo['qdelt_i']['data']        = None
    onetwo['qdelt_i']['unit']        = "W/m^3"
    onetwo['qdelt_i']['info']        = "Source of energy to ions due to collisional energy exchange with electrons"

    onetwo['qion_i']                = {} 
    onetwo['qion_i']['data']        = None
    onetwo['qion_i']['unit']        = "W/m^3"
    onetwo['qion_i']['info']        = "Source of energy from ions  due to recombination (3/2 T_i sum_i (srecom_i)) and ionization (3/2 sum_i sion_i tn_i)"

    onetwo['qcx_i']                = {} 
    onetwo['qcx_i']['data']        = None
    onetwo['qcx_i']['unit']        = "W/m^3"
    onetwo['qcx_i']['info']        = "Source of energy to ions due to charge exchange (with beam ions, thermal neutrals)"

    onetwo['qomegale_i']                = {} 
    onetwo['qomegale_i']['data']        = None
    onetwo['qomegale_i']['unit']        = "W/m^3"
    onetwo['qomegale_i']['info']        = "Source of energy subtracted from ions because it was added into the momentum sources (qomegap)"

    onetwo['qomegap_i']                = {} 
    onetwo['qomegap_i']['data']        = None
    onetwo['qomegap_i']['unit']        = "W/m^3"
    onetwo['qomegap_i']['info']        = "Source of energy to ions due to rotation * momentum flux"

    onetwo['qbeam_i']                = {} 
    onetwo['qbeam_i']['data']        = None
    onetwo['qbeam_i']['unit']        = "W/m^3"
    onetwo['qbeam_i']['info']        = "Source of energy to ions due to beam heating"

    onetwo['qbcx_i']                = {} 
    onetwo['qbcx_i']['data']        = None
    onetwo['qbcx_i']['unit']        = "W/m^3"
    onetwo['qbcx_i']['info']        = "Source of energy to thermal neutrals due to neutral beam charge exchange to ions"

    onetwo['qomegdgam']                = {} 
    onetwo['qomegdgam']['data']        = None
    onetwo['qomegdgam']['unit']        = "W/m^3"
    onetwo['qomegdgam']['info']        = "Source of energy to ions (qomegapi + vischeat)"

    onetwo['qvisc_i']                = {} 
    onetwo['qvisc_i']['data']        = None
    onetwo['qvisc_i']['unit']        = "W/m^3"
    onetwo['qvisc_i']['info']        = "Source of energy to ions due to viscous heating (-Pi*d omega/d rho)"

    onetwo['qangce_i']                = {} 
    onetwo['qangce_i']['data']        = None
    onetwo['qangce_i']['unit']        = "W/m^3"
    onetwo['qangce_i']['info']        = "Source of energy to ions due to convective momentum flux"

    onetwo['qthcx_i']                = {} 
    onetwo['qthcx_i']['data']        = None
    onetwo['qthcx_i']['unit']        = "W/m^3"
    onetwo['qthcx_i']['info']        = "Source of energy to ions (rotational kinetic) due to thermal charge exchange"

    onetwo['qrecfcx_i']                = {} 
    onetwo['qrecfcx_i']['data']        = None
    onetwo['qrecfcx_i']['unit']        = "W/m^3"
    onetwo['qrecfcx_i']['info']        = "Source of energy to ions (rotational kinetic) due to recombination and fast ion charge exchange"

    onetwo['qeimpact_i']                = {} 
    onetwo['qeimpact_i']['data']        = None
    onetwo['qeimpact_i']['unit']        = "W/m^3"
    onetwo['qeimpact_i']['info']        = "Source of energy to ions (rotational kinetic) due to electron impact ionization of thermal neutrals"

    onetwo['hibr']                = {} 
    onetwo['hibr']['data']        = None
    onetwo['hibr']['unit']        = None
    onetwo['hibr']['info']        = "hot ion birth rate"

    onetwo['hdep']                = {} 
    onetwo['hdep']['data']        = None
    onetwo['hdep']['unit']        = None
    onetwo['hdep']['info']        = "hot ion deposition"

    onetwo['zeta']                = {} 
    onetwo['zeta']['data']        = None
    onetwo['zeta']['unit']        = None
    onetwo['zeta']['info']        = "hot ion average pitch angle (cos)"

    onetwo['qbsav']                = {} 
    onetwo['qbsav']['data']        = None
    onetwo['qbsav']['unit']        = "W/m^3"
    onetwo['qbsav']['info']        = "total beam heating"

    onetwo['qb']                = {} 
    onetwo['qb']['data']        = None
    onetwo['qb']['unit']        = "W/m^3"
    onetwo['qb']['info']        = "delayed beam heating"

    onetwo['fb_e']                = {} 
    onetwo['fb_e']['data']        = None
    onetwo['fb_e']['unit']        = None
    onetwo['fb_e']['info']        = "fraction of energy to electrons"

    onetwo['fb_i']                = {} 
    onetwo['fb_i']['data']        = None
    onetwo['fb_i']['unit']        = None
    onetwo['fb_i']['info']        = "fraction of energy to ions"

    onetwo['taupb']                = {} 
    onetwo['taupb']['data']        = None
    onetwo['taupb']['unit']        = "s"
    onetwo['taupb']['info']        = "beam particle slowing down time"

    onetwo['taueb']                = {} 
    onetwo['taueb']['data']        = None
    onetwo['taueb']['unit']        = "s"
    onetwo['taueb']['info']        = "beam energy slowing down time"

    onetwo['ebeam']                = {} 
    onetwo['ebeam']['data']        = None
    onetwo['ebeam']['unit']        = "keV"
    onetwo['ebeam']['info']        = "beam particle energy"

    onetwo['bion']                = {} 
    onetwo['bion']['data']        = None
    onetwo['bion']['unit']        = "#/s"
    onetwo['bion']['info']        = "ion beam intensity"

    onetwo['bneut']                = {} 
    onetwo['bneut']['data']        = None
    onetwo['bneut']['unit']        = "#/s"
    onetwo['bneut']['info']        = "neutral beam intensity"

    onetwo['pbeam']                = {} 
    onetwo['pbeam']['data']        = None
    onetwo['pbeam']['unit']        = "W"
    onetwo['pbeam']['info']        = "beam power"

    onetwo['fap']                = {} 
    onetwo['fap']['data']        = None
    onetwo['fap']['unit']        = None
    onetwo['fap']['info']        = "Fraction of beam stopped by aperature"

    onetwo['fwall']                = {} 
    onetwo['fwall']['data']        = None
    onetwo['fwall']['unit']        = None
    onetwo['fwall']['info']        = "Fraction of beam incident on wall (shinethrough)"

    onetwo['forb']                = {} 
    onetwo['forb']['data']        = None
    onetwo['forb']['unit']        = None
    onetwo['forb']['info']        = "Fraction of beam lost on orbits"

    onetwo['fp_e']                = {} 
    onetwo['fp_e']['data']        = None
    onetwo['fp_e']['unit']        = None
    onetwo['fp_e']['info']        = "Fraction of beam deposited in electrons"

    onetwo['fp_i']                = {} 
    onetwo['fp_i']['data']        = None
    onetwo['fp_i']['unit']        = None
    onetwo['fp_i']['info']        = "Fraction of beam deposited in ions"

    onetwo['fpcx']                = {} 
    onetwo['fpcx']['data']        = None
    onetwo['fpcx']['unit']        = None
    onetwo['fpcx']['info']        = "Fraction of beam lost to fast ion charge exchange"

    onetwo['pbap']                = {} 
    onetwo['pbap']['data']        = None
    onetwo['pbap']['unit']        = "W"
    onetwo['pbap']['info']        = "Total beam power through the aperature"

    onetwo['fsap']                = {} 
    onetwo['fsap']['data']        = None
    onetwo['fsap']['unit']        = None
    onetwo['fsap']['info']        = "Total fraction of beams lost to the aperature"

    onetwo['fw']                = {} 
    onetwo['fw']['data']        = None
    onetwo['fw']['unit']        = None
    onetwo['fw']['info']        = "Total fraction of beams lost to shinethrough"

    onetwo['florb']                = {} 
    onetwo['florb']['data']        = None
    onetwo['florb']['unit']        = None
    onetwo['florb']['info']        = "Total fraction of beams lost to orbit losses"

    onetwo['pblaf']                = {} 
    onetwo['pblaf']['data']        = None
    onetwo['pblaf']['unit']        = "W"
    onetwo['pblaf']['info']        = "Total neutral beam power in plasma"

    onetwo['pblas']                = {} 
    onetwo['pblas']['data']        = None
    onetwo['pblas']['unit']        = "W"
    onetwo['pblas']['info']        = "Total slowed neutral beam power in plasma"

    onetwo['fpbe']                = {} 
    onetwo['fpbe']['data']        = None
    onetwo['fpbe']['unit']        = None
    onetwo['fpbe']['info']        = "Total fraction of neutral beam deposited in electrons"

    onetwo['fpbi']                = {} 
    onetwo['fpbi']['data']        = None
    onetwo['fpbi']['unit']        = None
    onetwo['fpbi']['info']        = "Total fraction of neutral beam deposited in ions"

    onetwo['fpbcx']                = {} 
    onetwo['fpbcx']['data']        = None
    onetwo['fpbcx']['unit']        = None
    onetwo['fpbcx']['info']        = "Total fraction of neutral beam lost to charge exchange (fast ion to thermal neutral)"

    onetwo['storque']                = {} 
    onetwo['storque']['data']        = None
    onetwo['storque']['unit']        = "kg/m/s^2"
    onetwo['storque']['info']        = "Total torque"

    onetwo['smagtorque']                = {} 
    onetwo['smagtorque']['data']        = None
    onetwo['smagtorque']['unit']        = "kg/m/s^2"
    onetwo['smagtorque']['info']        = "Torque due to magnetic breaking (see cb_mgbr)"

    onetwo['sprbeam_e']                = {} 
    onetwo['sprbeam_e']['data']        = None
    onetwo['sprbeam_e']['unit']        = "kg/m/s^2"
    onetwo['sprbeam_e']['info']        = "Torque directly to electrons from beams, but counted to ions, due to a delayed momentum transfer from the neutral beams"

    onetwo['sprbeam_i']                = {} 
    onetwo['sprbeam_i']['data']        = None
    onetwo['sprbeam_i']['unit']        = "kg/m/s^2"
    onetwo['sprbeam_i']['info']        = "Torque to ions from beams, due to a delayed momentum transfer from the beams"

    onetwo['ssprcxl']                = {} 
    onetwo['ssprcxl']['data']        = None
    onetwo['ssprcxl']['unit']        = "kg/m/s^2"
    onetwo['ssprcxl']['info']        = "Torque directly to thermal neutrals, but counted to ions, due to beam fast ion transfer of momentum during charge exchange with thermal neutrals"

    onetwo['sprcx']                = {} 
    onetwo['sprcx']['data']        = None
    onetwo['sprcx']['unit']        = "kg/m/s^2"
    onetwo['sprcx']['info']        = "Torque on ions as thermal neutrals charge exchange with thermal ions"

    onetwo['stotal']                = {} 
    onetwo['stotal']['data']        = None
    onetwo['stotal']['unit']        = "kg/m/s^2"
    onetwo['stotal']['info']        = "Total torque on ions (storqueb + spbolt + sntvtorque + smagtorque + sprcxre + spreimpt + sprcx)"

    onetwo['angmtm_density']                = {} 
    onetwo['angmtm_density']['data']        = None
    onetwo['angmtm_density']['unit']        = "kg/m/s"
    onetwo['angmtm_density']['info']        = "Angular momentum density"

    onetwo['vionz']                = {} 
    onetwo['vionz']['data']        = None
    onetwo['vionz']['unit']        = "m/s"
    onetwo['vionz']['info']        = "Ion speed"

    onetwo['angmtm_flux']                = {} 
    onetwo['angmtm_flux']['data']        = None
    onetwo['angmtm_flux']['unit']        = "kg/s^2"
    onetwo['angmtm_flux']['info']        = "Angular momentum flux" 

    onetwo['chi_angmtm']                = {} 
    onetwo['chi_angmtm']['data']        = None
    onetwo['chi_angmtm']['unit']        = "m^2/s"
    onetwo['chi_angmtm']['info']        = "Angular momentum diffusivity"

    onetwo['moment_inertia_density']                = {} 
    onetwo['moment_inertia_density']['data']        = None
    onetwo['moment_inertia_density']['unit']        = "kg/m"
    onetwo['moment_inertia_density']['info']        = "Moment of inertia density"

    onetwo['tn']                = {} 
    onetwo['tn']['data']        = None
    onetwo['tn']['unit']        = "keV"
    onetwo['tn']['info']        = "Temperature of neutral species"

    # EXTRA FIELDS MIGHT NO BE USED

    onetwo['sscxl']              = {}
    onetwo['sscxl']['data']      = None
    onetwo['sscxl']['unit']      = None
    onetwo['sscxl']['info']        = None

    onetwo['qsync']              = {}
    onetwo['qsync']['data']      = None
    onetwo['qsync']['unit']      = None
    onetwo['qsync']['info']        = None

    return onetwo


def read_iterdb_file(fname):
    if os.path.isfile(fname):
        fid = open(fname,'r')
    else:
        raise IOError("FILE %s DOES NOT EXIST!" % fname); sys.exit()

    onetwo = get_iterdb_vars()
    onetwo['file_type'] = 'iterdb'

    onetwo_varnames = list(onetwo.keys())

    fid.readline()
    fid.readline()
    line = fid.readline()
    onetwo["shot"]['data'] = line.strip()

    fid.readline()
    line = fid.readline()
    onetwo["nj"]['data'] = int(line.strip())
    nrho = int(line.strip())
    nlines = int((onetwo["nj"]['data'] / 5) + (onetwo["nj"]['data'] % 5))

    fid.readline()
    line = fid.readline()
    onetwo["nion"]['data'] = int(line.strip())
    nion = int(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["nprim"]['data'] = int(line.strip())
    nprim = int(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["nimp"]['data'] = int(line.strip())
    nimp = int(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["nneu"]['data'] = int(line.strip())
    nneu = int(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["bion"]['data'] = int(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["namep"]['data'] = line.strip()

    fid.readline()
    line = fid.readline()
    onetwo["namei"]['data'] = line.strip()

    fid.readline()
    line = fid.readline()
    onetwo["namen"]['data'] = line.strip()

    fid.readline()
    line = fid.readline()
    onetwo["time"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["rgeom"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["rma"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["rmajor"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["kappa"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["deltao"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["pindento"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["volume"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["cxareao"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["btor"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    linecontent = line.split()
    onetwo['tot_cur']['data'] = float(linecontent[0])
    onetwo['totohm_cur']['data'] = float(linecontent[1])
    onetwo['totboot_cur']['data']  = float(linecontent[2])
    onetwo['totbeam_cur']['data']  = float(linecontent[3])
    onetwo['totrf_cur']['data']  = float(linecontent[4])

    fid.readline()
    line = fid.readline()
    onetwo["betap"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["beta"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["ali"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["te0"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["ti0"]['data'] = float(line.strip())

   #onetwo["psi"]['data'] = numpy.zeros(nrho,dtype=float)
    onetwo["psir_grid"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["psir_grid"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["psir_grid"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["psir_grid"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["psir_grid"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["psir_grid"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["rho_grid"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["rho_grid"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["rho_grid"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["rho_grid"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["rho_grid"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["rho_grid"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["fcap"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["fcap"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["fcap"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["fcap"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["fcap"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["fcap"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["gcap"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["gcap"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["gcap"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["gcap"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["gcap"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["gcap"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["hcap"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["hcap"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["hcap"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["hcap"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["hcap"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["hcap"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["Te"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["Te"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["Te"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["Te"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["Te"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["Te"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["Ti"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["Ti"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["Ti"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["Ti"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["Ti"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["Ti"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["q_value"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["q_value"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["q_value"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["q_value"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["q_value"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["q_value"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["ene"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["ene"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["ene"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["ene"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["ene"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["ene"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["enion"]['data'] = numpy.zeros((nion,nrho),dtype=float)
    for i in range(nion):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["enion"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["enion"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["enion"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["enion"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["enion"]['data'][i,iline*5+4] = float(linecontent[4])
            except:
                error = 'empty records'

    onetwo["sion"]['data'] = numpy.zeros((nprim,nrho),dtype=float)
    for i in range(nprim):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["sion"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["sion"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["sion"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["sion"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["sion"]['data'][i,iline*5+4] = float(linecontent[4])
            except:
                error = 'empty records'
    onetwo["sion"]["data"] = numpy.sum(onetwo["sion"]["data"],axis=0)

    onetwo["srecom"]['data'] = numpy.zeros((nprim,nrho),dtype=float)
    for i in range(nprim):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["srecom"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["srecom"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["srecom"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["srecom"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["srecom"]['data'][i,iline*5+4] = float(linecontent[4])
            except:
                error = 'empty records'


    onetwo["scx"]['data'] = numpy.zeros((nprim,nrho),dtype=float)
    for i in range(nprim):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["scx"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["scx"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["scx"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["scx"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["scx"]['data'][i,iline*5+4] = float(linecontent[4])
            except:
                error = 'empty records'


    onetwo["sbcx"]['data'] = numpy.zeros((nprim,nrho),dtype=float)
    for i in range(nprim):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["sbcx"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["sbcx"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["sbcx"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["sbcx"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["sbcx"]['data'][i,iline*5+4] = float(linecontent[4])
            except:
                error = 'empty records'
    onetwo["sbcx"]["data"] = numpy.sum(onetwo["sbcx"]["data"],axis=0)


    onetwo["stsource"]['data'] = numpy.zeros((nprim,nrho),dtype=float)
    for i in range(nprim):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["stsource"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["stsource"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["stsource"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["stsource"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["stsource"]['data'][i,iline*5+4] = float(linecontent[4])
            except:
                error = 'empty records'


    onetwo["dudtsv"]['data'] = numpy.zeros((nprim,nrho),dtype=float)
    for i in range(nprim):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["dudtsv"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["dudtsv"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["dudtsv"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["dudtsv"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["dudtsv"]['data'][i,iline*5+4] = float(linecontent[4])
            except:
                error = 'empty records'

    onetwo["enbeam"]['data'] = numpy.zeros((1,nrho),dtype=float)
    for i in range(1):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["enbeam"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["enbeam"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["enbeam"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["enbeam"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["enbeam"]['data'][i,iline*5+4] = float(linecontent[4])
            except:
                error = 'empty records'

    onetwo["enn"]['data'] = numpy.zeros((nprim,nrho),dtype=float)
    for i in range(nprim):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["enn"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["enn"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["enn"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["enn"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["enn"]['data'][i,iline*5+4] = float(linecontent[4])
            except:
                error = 'empty records'

    onetwo["ennw"]['data'] = numpy.zeros((nprim,nrho),dtype=float)
    for i in range(nprim):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["ennw"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["ennw"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["ennw"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["ennw"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["ennw"]['data'][i,iline*5+4] = float(linecontent[4])
            except:
                error = 'empty records'

    onetwo["ennv"]['data'] = numpy.zeros((nprim,nrho),dtype=float)
    for i in range(nprim):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["ennv"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["ennv"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["ennv"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["ennv"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["ennv"]['data'][i,iline*5+4] = float(linecontent[4])
            except:
                error = 'empty records'

    onetwo["volsn"]['data'] = numpy.zeros((nprim,nrho),dtype=float)
    for i in range(nprim):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["volsn"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["volsn"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["volsn"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["volsn"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["volsn"]['data'][i,iline*5+4] = float(linecontent[4])
            except:
                error = 'empty records'

    onetwo["sbeame"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["sbeame"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["sbeame"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["sbeame"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["sbeame"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["sbeame"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["sbeam"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["sbeam"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["sbeam"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["sbeam"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["sbeam"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["sbeam"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["curden"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["curden"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["curden"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["curden"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["curden"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["curden"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["curohm"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["curohm"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["curohm"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["curohm"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["curohm"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["curohm"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["curboot"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["curboot"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["curboot"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["curboot"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["curboot"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["curboot"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["curbeam"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["curbeam"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["curbeam"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["curbeam"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["curbeam"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["curbeam"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["currf"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["currf"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["currf"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["currf"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["currf"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["currf"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["rbp"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["rbp"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["rbp"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["rbp"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["rbp"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["rbp"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["zeff"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["zeff"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["zeff"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["zeff"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["zeff"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["zeff"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["angrot"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["angrot"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["angrot"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["angrot"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["angrot"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["angrot"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["chieinv"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["chieinv"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["chieinv"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["chieinv"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["chieinv"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["chieinv"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["chiinv"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["chiinv"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["chiinv"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["chiinv"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["chiinv"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["chiinv"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["xkineo"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["xkineo"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["xkineo"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["xkineo"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["xkineo"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["xkineo"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["dpedt"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["dpedt"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["dpedt"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["dpedt"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["dpedt"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["dpedt"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["dpidt"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["dpidt"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["dpidt"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["dpidt"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["dpidt"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["dpidt"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qconde"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qconde"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qconde"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qconde"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qconde"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qconde"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qcondi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qcondi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qcondi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qcondi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qcondi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qcondi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qconve"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qconve"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qconve"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qconve"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qconve"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qconve"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qconvi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qconvi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qconvi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qconvi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qconvi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qconvi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qbeame"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qbeame"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qbeame"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qbeame"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qbeame"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qbeame"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qdelt"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qdelt"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qdelt"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qdelt"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qdelt"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qdelt"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qbeami"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qbeami"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qbeami"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qbeami"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qbeami"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qbeami"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qrfe"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qrfe"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qrfe"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qrfe"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qrfe"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qrfe"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qrfi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qrfi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qrfi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qrfi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qrfi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qrfi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qione"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qione"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qione"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qione"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qione"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qione"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qioni"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qioni"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qioni"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qioni"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qioni"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qioni"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qcx"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qcx"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qcx"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qcx"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qcx"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qcx"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qe2d"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qe2d"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qe2d"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qe2d"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qe2d"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qe2d"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qi2d"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qi2d"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qi2d"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qi2d"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qi2d"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qi2d"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qfuse"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qfuse"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qfuse"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qfuse"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qfuse"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qfuse"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qfusi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qfusi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qfusi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qfusi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qfusi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qfusi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qbfuse"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qbfuse"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qbfuse"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qbfuse"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qbfuse"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qbfuse"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qbfusi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qbfusi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qbfusi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qbfusi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qbfusi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qbfusi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qmag"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qmag"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qmag"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qmag"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qmag"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qmag"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qsawe"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qsawe"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qsawe"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qsawe"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qsawe"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qsawe"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qsawi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qsawi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qsawi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qsawi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qsawi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qsawi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qrad"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qrad"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qrad"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qrad"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qrad"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qrad"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qohm"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qohm"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qohm"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qohm"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qohm"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qohm"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["rmajavnpsi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["rmajavnpsi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["rmajavnpsi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["rmajavnpsi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["rmajavnpsi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["rmajavnpsi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["rminavnpsi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["rminavnpsi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["rminavnpsi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["rminavnpsi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["rminavnpsi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["rminavnpsi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["psivolpnpsi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["psivolpnpsi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["psivolpnpsi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["psivolpnpsi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["psivolpnpsi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["psivolpnpsi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["elongxnpsi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["elongxnpsi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["elongxnpsi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["elongxnpsi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["elongxnpsi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["elongxnpsi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["triangnpsi_u"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["triangnpsi_u"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["triangnpsi_u"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["triangnpsi_u"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["triangnpsi_u"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["triangnpsi_u"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["pindentnpsi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["pindentnpsi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["pindentnpsi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["pindentnpsi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["pindentnpsi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["pindentnpsi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    fid.readline()

    onetwo["sfareanpsi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["sfareanpsi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["sfareanpsi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["sfareanpsi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["sfareanpsi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["sfareanpsi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["cxareanpsi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["cxareanpsi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["cxareanpsi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["cxareanpsi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["cxareanpsi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["cxareanpsi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["grho1npsi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["grho1npsi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["grho1npsi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["grho1npsi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["grho1npsi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["grho1npsi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["grho2npsi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["grho2npsi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["grho2npsi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["grho2npsi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["grho2npsi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["grho2npsi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    fid.readline()
    line = fid.readline()
    onetwo["nplasbdry"]['data'] = int(line.strip())
    nplasbdry = int(line.strip())
    nblines = int(numpy.ceil((onetwo["nplasbdry"]['data'] / 5)))

    onetwo["rplasbdry"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nblines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["rplasbdry"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["rplasbdry"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["rplasbdry"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["rplasbdry"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["rplasbdry"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["zplasbdry"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nblines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["zplasbdry"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["zplasbdry"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["zplasbdry"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["zplasbdry"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["zplasbdry"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["storqueb"]['data'] = numpy.zeros(nrho,dtype=float)
    infoline = fid.readline()
    if "beam   torque" in infoline:
       for iline in range(nlines):
           line = fid.readline()
           linecontent = line.split()
           try:
               onetwo["storqueb"]['data'][iline*5+0] = float(linecontent[0])
               onetwo["storqueb"]['data'][iline*5+1] = float(linecontent[1])
               onetwo["storqueb"]['data'][iline*5+2] = float(linecontent[2])
               onetwo["storqueb"]['data'][iline*5+3] = float(linecontent[3])
               onetwo["storqueb"]['data'][iline*5+4] = float(linecontent[4])
           except:
               error = 'empty records'

    onetwo["pressb"]['data'] = numpy.zeros(nrho,dtype=float)
    infoline = fid.readline()
    if "beam  pressure" in infoline:
       for iline in range(nlines):
           line = fid.readline()
           linecontent = line.split()
           try:
               onetwo["pressb"]['data'][iline*5+0] = float(linecontent[0])
               onetwo["pressb"]['data'][iline*5+1] = float(linecontent[1])
               onetwo["pressb"]['data'][iline*5+2] = float(linecontent[2])
               onetwo["pressb"]['data'][iline*5+3] = float(linecontent[3])
               onetwo["pressb"]['data'][iline*5+4] = float(linecontent[4])
           except:
               error = 'empty records'

    onetwo["press"]['data'] = numpy.zeros(nrho,dtype=float)
    infoline = fid.readline()
    if "total  pressure" in infoline:
       for iline in range(nlines):
           line = fid.readline()
           linecontent = line.split()
           try:
               onetwo["press"]['data'][iline*5+0] = float(linecontent[0])
               onetwo["press"]['data'][iline*5+1] = float(linecontent[1])
               onetwo["press"]['data'][iline*5+2] = float(linecontent[2])
               onetwo["press"]['data'][iline*5+3] = float(linecontent[3])
               onetwo["press"]['data'][iline*5+4] = float(linecontent[4])
           except:
               error = 'empty records'

    onetwo["sscxl"]['data'] = numpy.zeros(nrho,dtype=float)
    infoline = fid.readline()
    if "sscxl" in infoline:
       for iline in range(nlines):
           line = fid.readline()
           linecontent = line.split()
           try:
               onetwo["sscxl"]['data'][iline*5+0] = float(linecontent[0])
               onetwo["sscxl"]['data'][iline*5+1] = float(linecontent[1])
               onetwo["sscxl"]['data'][iline*5+2] = float(linecontent[2])
               onetwo["sscxl"]['data'][iline*5+3] = float(linecontent[3])
               onetwo["sscxl"]['data'][iline*5+4] = float(linecontent[4])
           except:
               error = 'empty records'

    onetwo["qsync"]['data'] = numpy.zeros(nrho,dtype=float)
    infoline = fid.readline()
    if "qsync" in infoline:
       for iline in range(nlines):
           line = fid.readline()
           linecontent = line.split()
           try:
               onetwo["qsync"]['data'][iline*5+0] = float(linecontent[0])
               onetwo["qsync"]['data'][iline*5+1] = float(linecontent[1])
               onetwo["qsync"]['data'][iline*5+2] = float(linecontent[2])
               onetwo["qsync"]['data'][iline*5+3] = float(linecontent[3])
               onetwo["qsync"]['data'][iline*5+4] = float(linecontent[4])
           except:
               error = 'empty records'

    return onetwo


def read_state_file(fpath):
    onetwo = get_iterdb_vars()
    onetwo['file_type'] = 'state'

    if os.path.isfile(fpath):
       fid = ncdf.Dataset(fpath)
    else:
       raise IOError("ONETWO STATE FILE DOES NOT EXIST!" % fpath)
    fvars = fid.variables.keys()
    for fvar in fvars:
        onetwo[fvar]['data'] = fid.variables[fvar][:]
        try:
           onetwo[fvar]['data'] = fid.variables[fvar][:]
        except KeyError:
            print(fvar)
            pass

    if all(onetwo['qcx']['data']) > 0.0:   onetwo['qcx']['data'] *= -1.0
    if all(onetwo['qrad']['data']) > 0.0:  onetwo['qrad']['data'] *= -1.0
    if all(onetwo['qione']['data']) > 0.0: onetwo['qione']['data'] *= -1.0
    onetwo['qdelt']['data']     = numpy.abs(onetwo['qdelt']['data'])
    onetwo['q_value']['data']   = numpy.abs(onetwo['q_value']['data'])
    onetwo['dudtsv']['data']    = numpy.transpose(onetwo['dudtsv']['data'])
    onetwo['stsource']['data']  = numpy.transpose(onetwo['stsource']['data'])

    return onetwo

def test_binary_file(fname):
    textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
    is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
    return is_binary_string(open(fname,'rb').read(1024))

def read_onetwo_file(fpath):
    if test_binary_file(fpath):
        onetwo = read_state_file(fpath)
    else:
        onetwo = read_iterdb_file(fpath)
    return onetwo


def to_instate(fpath,gfpath={},setParam={}):
    onetwo = read_onetwo_file(fpath)
    if onetwo['file_type'] == 'state':
        fpstate_flag = True
        fiterdb_flag = False
    elif onetwo['file_type'] == 'iterdb':
        fpstate_flag = False
        fiterdb_flag = True
        
    if gfpath:
        geqdskdata = read_eqdsk_file(gfpath)
    instate = get_instate_vars()

    if   'SHOT_ID' in setParam:
          SHOT_ID = setParam['SHOT_ID']
    elif 'shot_id' in setParam:
          SHOT_ID = setParam['shot_id']
    else:
          SHOT_ID = "%06d" % (int(onetwo['shot']['data']))
          
    if   'TIME_ID' in setParam:
          TIME_ID = setParam['TIME_ID']
    elif 'time_id' in setParam:
          TIME_ID = setParam['time_id']
    else:
          TIME_ID = "%05d" % (int(onetwo['time']['data']*1.0e4))
          
    if   'TOKAMAK_ID' in setParam:
          TOKAMAK_ID = setParam['TOKAMAK_ID']
    elif 'tokamak_id' in setParam:
          TOKAMAK_ID = setParam['tokamak_id']
    else:
          TOKAMAK_ID = "TOKAMAK"
          
    if   'LIMITER_MODEL' in setParam:
          LIMITER_MODEL = setParam['LIMITER_MODEL']
    elif 'limiter_model' in setParam:
          LIMITER_MODEL = setParam['limiter_model']
    else:
          LIMITER_MODEL = 1
          
    instate['SHOT_ID']       = [SHOT_ID]
    instate['TIME_ID']       = [TIME_ID]
    instate['TOKAMAK_ID']    = [TOKAMAK_ID]
    instate['MODEL_SHAPE']   = [0]
    instate['DENSITY_MODEL'] = [0]

    if fiterdb_flag and type(onetwo['psiaxis']['data']) == type(None):
        onetwo['eps']['data'] = onetwo['rminavnpsi']['data']/onetwo['rmajavnpsi']['data']

    instate['R0']     = [round(float(onetwo['rmajor']['data']),                             7)]
    instate['B0']     = [round(float(abs(onetwo['btor']['data'])),                          7)]
    instate['IP']     = [round(float(onetwo['tot_cur']['data']) * 1.0e-6,                   7)]
    instate['KAPPA']  = [round(float(onetwo['kappa']['data']),                              7)]
    instate['DELTA']  = [round(float(onetwo['deltao']['data']),                             7)]
    instate['RMAJOR'] = [round(float(onetwo['rmajor']['data']),                             7)]
    instate['ASPECT'] = [round(float(onetwo['eps']['data'][-1]),                            7)]
    instate['AMINOR'] = [round(float(onetwo['rmajor']['data'] * onetwo['eps']['data'][-1]), 7)]

    instate['N_ION']    = [1]
    instate['Z_ION']    = [1]
    instate['A_ION']    = [2]
    instate['F_ION']    = [1]
    instate['N_IMP']    = [1]
    instate['Z_IMP']    = [6]
    instate['A_IMP']    = [12]
    instate['F_IMP']    = [1]
    instate['N_MIN']    = [0]
    instate['Z_MIN']    = [1]
    instate['A_MIN']    = [1]
    instate['N_BEAM']   = [1]
    instate['Z_BEAM']   = [1]
    instate['A_BEAM']   = [2]
    instate['N_FUSION'] = [1]
    instate['Z_FUSION'] = [2]
    instate['A_FUSION'] = [4]

    RHO  = (onetwo['rho_grid']['data']     - onetwo['rho_grid']['data'][0])
    RHO /= (onetwo['rho_grid']['data'][-1] - onetwo['rho_grid']['data'][0])
    instate['RHO']    = [round(i,2) for i in RHO                        ]
    instate['NRHO']   = [numpy.size(instate['RHO'])                     ]
    instate['PSIPOL'] = [round(i,7) for i in onetwo['psir_grid']['data']]

    instate['NE']      = [round(i,7) for i in (onetwo['ene']['data']*1.0e-19)]
    instate['TE']      = [round(i,7) for i in onetwo['Te']['data']           ]
    instate['TI']      = [round(i,7) for i in onetwo['Ti']['data']           ]
    instate['ZEFF']    = [round(i,7) for i in onetwo['zeff']['data']         ]
    instate['OMEGA']   = [round(i,7) for i in onetwo['angrot']['data']       ]

    if type(onetwo['psiaxis']['data']) == type(None):
        onetwo['psiaxis']['data'] = onetwo['psir_grid']['data'][0]
        onetwo['psibdry']['data'] = onetwo['psir_grid']['data'][-1]

    PSI    = (onetwo['psibdry']['data']-onetwo['psiaxis']['data'])
    PSI   *= numpy.arange(onetwo['nj']['data'])/(onetwo['nj']['data']-1.0)
    PSIN   = (PSI-PSI[0])/(PSI[-1]-PSI[0])
    RHOPSI = numpy.sqrt(PSIN)
    instate['RHOPSI']  = [round(i,7) for i in RHOPSI]

    instate['Q']       = [round(i,7) for i in onetwo['q_value']['data']]
    instate['P_EQ']    = [round(i,7) for i in onetwo['press']['data']]
    if type(onetwo['pprim']['data']) != type(None):
        instate['PPRIME']  = [round(i,7) for i in onetwo['pprim']['data']]
    if type(onetwo['ffprim']['data']) != type(None):
        instate['FFPRIME'] = [round(i,7) for i in onetwo['ffprim']['data']]

    instate['J_RF']  = [round(i,7) for i in (onetwo['currf']['data']   * 1.0e-6)]
    instate['J_OH']  = [round(i,7) for i in (onetwo['curohm']['data']  * 1.0e-6)]
    instate['J_NB']  = [round(i,7) for i in (onetwo['curbeam']['data'] * 1.0e-6)]
    instate['J_BS']  = [round(i,7) for i in (onetwo['curboot']['data'] * 1.0e-6)]
    instate['J_EC']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['J_IC']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['J_LH']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['J_HC']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['J_TOT'] = [round(i,7) for i in (onetwo['curden']['data']  * 1.0e-6)]

    instate['PE_RF']  = [round(i,7) for i in (onetwo['qrfe']['data']   * 1.0e-6)]
    instate['PI_RF']  = [round(i,7) for i in (onetwo['qrfi']['data']   * 1.0e-6)]
    instate['PE_NB']  = [round(i,7) for i in (onetwo['qbeame']['data'] * 1.0e-6)]
    instate['PI_NB']  = [round(i,7) for i in (onetwo['qbeami']['data'] * 1.0e-6)]
    instate['SE_NB']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['SI_NB']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['PE_EC']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['PI_EC']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['PE_IC']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['PI_IC']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['PE_LH']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['PI_LH']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['PE_HC']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['PI_HC']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]

    if fpstate_flag:
        instate['P_EI']   = [round(i,7) for i in (onetwo['qdelt']['data'] * 1.0e-6)]
    elif fiterdb_flag:
        instate['P_EI']   = [-round(i,7) for i in (onetwo['qdelt']['data'] * 1.0e-6)]
    instate['P_RAD']  = [round(i,7) for i in (onetwo['qrad']['data']    * 1.0e-6)]
    instate['P_OHM']  = [round(i,7) for i in (onetwo['qohm']['data']    * 1.0e-6)]
    instate['PI_CX']  = [round(i,7) for i in (onetwo['qcx']['data']     * 1.0e-6)]
    instate['PI_FUS'] = [round(i,7) for i in (onetwo['qfusi']['data']   * 1.0e-6)]
    instate['PE_FUS'] = [round(i,7) for i in (onetwo['qfuse']['data']   * 1.0e-6)]

    instate['CHIE']          = [round(i,7) for i in onetwo['chieinv']['data']            ]
    instate['CHII']          = [round(i,7) for i in onetwo['chiinv']['data']             ]
    if type(onetwo['wbeam']['data']) != type(None):
        instate['WBEAM']         = [round(i,7) for i in (onetwo['wbeam']['data']  *1.603e-22)]
    if type(onetwo['walp']['data']) != type(None):
        instate['WALPHA']        = [round(i,7) for i in (onetwo['walp']['data']   *1.603e-22)]
    instate['TORQUE_NB']     = [round(i,7) for i in onetwo['storqueb']['data']           ]
    instate['TORQUE_IN']     = [round(0.0,7) for i in range(instate['NRHO'][0])          ]
    instate['DENSITY_BEAM']  = [round(i,7) for i in (onetwo['enbeam']['data'][0]*1.0e-19)]
    if type(onetwo['enalp']['data']) != type(None):
        instate['DENSITY_ALPHA'] = [round(i,7) for i in onetwo['enalp']['data']              ]
    instate['SE_IONIZATION'] = [round(0.0,7) for i in range(instate['NRHO'][0])          ]
    instate['SI_IONIZATION'] = [round(0.0,7) for i in range(instate['NRHO'][0])          ]
    instate['PE_IONIZATION'] = [round(0.0,7) for i in range(instate['NRHO'][0])          ]
    instate['PI_IONIZATION'] = [round(0.0,7) for i in range(instate['NRHO'][0])          ]


    if gfpath:
        instate['NBDRY'] = [geqdskdata['nbound']]
        instate['RBDRY'] =  list(geqdskdata['rbound'])
        instate['ZBDRY'] =  list(geqdskdata['zbound'])

        instate['NLIM'] = [geqdskdata['nlimit']]
        instate['RLIM'] =  list(geqdskdata['rlimit'])
        instate['ZLIM'] =  list(geqdskdata['zlimit'])
        
        if instate['NLIM'][0] % 2 == 0:
            if instate['RLIM'][0] != instate['RLIM'][-1] or instate['ZLIM'][0] != instate['ZLIM'][-1]:
                instate['RLIM'].append(instate['RLIM'][0])
                instate['ZLIM'].append(instate['ZLIM'][0])
                instate['NLIM'] = [instate['NLIM'][0] + 1]
            else:
                instate['RLIM'].pop(-2)
                instate['ZLIM'].pop(-2)
                instate['NLIM'] = [instate['NLIM'][0] - 1]
    else:
        NBDRYmax = 85
        NBDRY = numpy.size(onetwo['rplasbdry']['data'])
        if NBDRY > NBDRYmax:
           RBDRY = onetwo['rplasbdry']['data']
           ZBDRY = onetwo['zplasbdry']['data']
           BDRY = zip(RBDRY,ZBDRY)
           BDRYINDS = random.sample(range(NBDRY),NBDRYmax)
           instate['NBDRY'] = [NBDRYmax]
           instate['RBDRY'] = [round(i,7) for i in RBDRY[BDRYINDS]]
           instate['ZBDRY'] = [round(i,7) for i in ZBDRY[BDRYINDS]]
        else:
           instate['NBDRY'] = [numpy.size(onetwo['rplasbdry']['data'])]
           instate['RBDRY'] = [round(i,7) for i in onetwo['rplasbdry']['data']]
           instate['ZBDRY'] = [round(i,7) for i in onetwo['zplasbdry']['data']]


        if type(onetwo['rlimiter']['data']) != type(None):
            if LIMITER_MODEL == 1:
               NLIMTmax = 86
               NLIMT = numpy.size(onetwo['rlimiter']['data'])
               if NLIMT > NLIMTmax:
                  RLIMT = onetwo['rlimiter']['data']
                  ZLIMT = onetwo['zlimiter']['data']
                  stride = int(NLIMT / (NLIMTmax+1))
                  indexes = list(range(2,NLIMTmax-2,stride))
                  indexes.insert(0,0)
                  indexes.append(NLIMTmax)
                  instate['NLIM'] = [len(indexes)]
                  instate['RLIM'] = [round(RLIMT[i],7) for i in indexes]
                  instate['ZLIM'] = [round(ZLIMT[i],7) for i in indexes]
                 #LIMT = zip(RLIMT,ZLIMT)
                 #LIMTINDS = random.sample(range(NLIMT),NLIMTmax)
                 #instate['NLIM'] = [NLIMTmax]
                 #instate['RLIM'] = [round(i,7) for i in RLIMT[LIMTINDS]]
                 #instate['ZLIM'] = [round(i,7) for i in ZLIMT[LIMTINDS]]
               else:
                  instate['NLIM']  = [numpy.size(onetwo['rlimiter']['data'])]
                  instate['RLIM']  = [round(i,7) for i in onetwo['rlimiter']['data'] ]
                  instate['ZLIM']  = [round(i,7) for i in onetwo['zlimiter']['data'] ]

            elif LIMITER_MODEL == 2:
               RLIM_MAX = max(onetwo['rlimiter']['data'])
               RLIM_MIN = min(onetwo['rlimiter']['data'])
               ZLIM_MAX = max(onetwo['zlimiter']['data'])
               ZLIM_MIN = min(onetwo['zlimiter']['data'])
               instate['RLIM'] = [RLIM_MAX, RLIM_MIN, RLIM_MIN, RLIM_MAX, RLIM_MAX]
               instate['ZLIM'] = [ZLIM_MAX, ZLIM_MAX, ZLIM_MIN, ZLIM_MIN, ZLIM_MAX]
               instate['NLIM'] = [len(instate['RLIM'])]
        else:
            RLIM_MAX = max(onetwo['rplasbdry']['data']) + 0.5
            RLIM_MIN = min(onetwo['rplasbdry']['data']) - 0.5
            ZLIM_MAX = max(onetwo['zplasbdry']['data']) + 0.5
            ZLIM_MIN = min(onetwo['zplasbdry']['data']) - 0.5
            instate['RLIM'] = [RLIM_MAX, RLIM_MIN, RLIM_MIN, RLIM_MAX, RLIM_MAX]
            instate['ZLIM'] = [ZLIM_MAX, ZLIM_MAX, ZLIM_MIN, ZLIM_MIN, ZLIM_MAX]
            instate['NLIM'] = [len(instate['RLIM'])]

   #for i in range(instate['NLIM'][0]):
   #    print(instate['RLIM'][i], instate['ZLIM'][i])

  # for fvar in list(instate.keys()):
  # for fvar in list(instate.keys()):
  #     if type(instate[fvar]) in [numpy.ma.core.MaskedArray]:
  #        print(fvar," = ",instate[fvar])
  #     elif type(instate[fvar]) in [list,tuple]:
  #        print(fvar," = ",instate[fvar])

    INSTATE = Namelist()
    INSTATE['instate'] = {}
    INSTATE['instate'].update(instate)
    INSTATE.write("instate_%s_%s.%s" % (TOKAMAK_ID,SHOT_ID,TIME_ID))

    return instate


if __name__ == "__main__":
    onetwofname = "statefile_2.026000E+00.nc"
    instate_from_pstate = to_instate(fpath=onetwofname,setParam={"TOKAMAK_ID":"d3d","LIMITER_MODEL":2})
    onetwofname = "iterdb.150139"
    instate_from_iterdb = to_instate(fpath=onetwofname,setParam={"TOKAMAK_ID":"d3d","LIMITER_MODEL":2})

    sys.exit()



   #geqdskfname = "../../Discharges/DIIID/DIIID150139/g150139.02026"
   #onetwofname = "../../Discharges/DIIID/DIIID150139/statefile_2.026000E+00.nc"
   #onetwo = to_instate(fpath=onetwofname,gfpath=geqdskfname,setParam={"TOKAMAK_ID":"d3d"})

    onetwofname = "../../Discharges/DIIID/DIIID150139/statefile_2.026000E+00.nc"
   #onetwo = to_instate(fpath=onetwofname,setParam={"TOKAMAK_ID":"d3d"})
    onetwo = to_instate(fpath=onetwofname,setParam={"TOKAMAK_ID":"d3d","LIMITER_MODEL":2})

   #fname = "../testsuite/onetwo/onetwo_statefile_101381.02630.nc"
   #onetwo = read_state_file(fname)

   #import matplotlib.pyplot as plt
   #plt.plot(onetwo['rho_grid']['data'],onetwo['Te']['data'])
   #plt.plot(onetwo['rho_grid']['data'],onetwo['Ti']['data'])
   #plt.show()



