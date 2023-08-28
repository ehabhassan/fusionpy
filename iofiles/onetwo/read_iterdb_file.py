import os
import sys
import numpy

def get_iterdb_vars():
    onetwo = {}
    
    onetwo['ishot']                    = {} 
    onetwo['ishot']['data']            = None
    onetwo['ishot']['unit']            = None
    onetwo['ishot']['info']            = "Shot Number"

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
    
    onetwo['tGCNMF']                   = {} 
    onetwo['tGCNMF']['data']           = None
    onetwo['tGCNMF']['unit']           = None
    onetwo['tGCNMF']['info']           = "GCNMP Evolve Solution from Time to tGCNMF"
    
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
    onetwo['Te']['info']               = "Electron Temperature"

    onetwo['Ti']                       = {}
    onetwo['Ti']['data']               = None
    onetwo['Ti']['unit']               = "keV"
    onetwo['Ti']['info']               = "Ion Temperature"

    onetwo['press']                    = {}
    onetwo['press']['data']            = None
    onetwo['press']['unit']            = "N/m^2"
    onetwo['press']['info']            = "Total Pressure on Transport rho grid"

    onetwo['pressb']                   = {}
    onetwo['pressb']['data']           = None
    onetwo['pressb']['unit']           = "N/m^2"
    onetwo['pressb']['info']           = "Beam Pressure on Transport rho grid"

    onetwo['q_value']                  = {} 
    onetwo['q_value']['data']          = None
    onetwo['q_value']['unit']          = None
    onetwo['q_value']['info']          = "Safety Factor"
    
    onetwo['ene']                      = {}
    onetwo['ene']['data']              = None
    onetwo['ene']['unit']              = "/m^3"
    onetwo['ene']['info']              = "Electron Density"

    onetwo['p_flux_elec']              = {} 
    onetwo['p_flux_elec']['data']      = None
    onetwo['p_flux_elec']['unit']      = "1/m^2/s"
    onetwo['p_flux_elec']['info']      = "Electron Particle Flux"
    
    onetwo['p_flux_ion']               = {} 
    onetwo['p_flux_ion']['data']       = None
    onetwo['p_flux_ion']['unit']       = "1/m^2/s"
    onetwo['p_flux_ion']['info']       = "Ion Total Particle Flux"
    
    onetwo['enion']                    = {}
    onetwo['enion']['data']            = None
    onetwo['enion']['unit']            = "1/m^3"
    onetwo['enion']['info']            = "Thermal Ion Density"

    onetwo['p_flux']                   = {} 
    onetwo['p_flux']['data']           = None
    onetwo['p_flux']['unit']           = 
    onetwo['p_flux']['info']           = "TThermal Ion Particle Flux"
    
    onetwo['p_flux_conv']              = {} 
    onetwo['p_flux_conv']['data']      = None
    onetwo['p_flux_conv']['unit']      = "1/m^2/s"
    onetwo['p_flux_conv']['info']      = "Thermal Ion Convectiove Flux"
    
    onetwo['e_fluxe']                  = {} 
    onetwo['e_fluxe']['data']          = None
    onetwo['e_fluxe']['unit']          = "J/m^2/s"
    onetwo['e_fluxe']['info']          = "Electron Energy Flux"
    
    onetwo['e_fluxe_conv']             = {} 
    onetwo['e_fluxe_conv']['data']     = None
    onetwo['e_fluxe_conv']['unit']     = "J/m^2/s"
    onetwo['e_fluxe_conv']['info']     = "Electron Convective Energy Flux"
    
    onetwo['e_fluxi']                  = {} 
    onetwo['e_fluxi']['data']          = None
    onetwo['e_fluxi']['unit']          = "J/m^2/s"
    onetwo['e_fluxi']['info']          = "Total Thermal Ion Energy Flux"
    
    onetwo['e_fluxi_conv']             = {} 
    onetwo['e_fluxi_conv']['data']     = None
    onetwo['e_fluxi_conv']['unit']     = "J/m^2/s"
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
    
    onetwo['tglf_elect_p_flux']        = {} 
    onetwo['tglf_elect_p_flux']['data']= None
    onetwo['tglf_elect_p_flux']['unit']= "1/m^2/s"
    onetwo['tglf_elect_p_flux']['info']= "TGLF Turbulent Electron Particle Flux"
    
    onetwo['tglf_ion_p_flux']          = {} 
    onetwo['tglf_ion_p_flux']['data']  = None
    onetwo['tglf_ion_p_flux']['unit']  = "1/m^2/s"
    onetwo['tglf_ion_p_flux']['info']  = "TGLF Turbulent Effective Primary Particle Flux"
    
    onetwo['tglf_imp_p_flux']          = {} 
    onetwo['tglf_imp_p_flux']['data']  = None
    onetwo['tglf_imp_p_flux']['unit']  = "1/m^2/s"
    onetwo['tglf_imp_p_flux']['info']  = "TGLF Turbulent Effective Impurity Particle Flux"
    
    onetwo['tglf_elect_e_flux']        = {} 
    onetwo['tglf_elect_e_flux']['data']= None
    onetwo['tglf_elect_e_flux']['unit']= "J/m^2/s"
    onetwo['tglf_elect_e_flux']['info']= "TGLF Turbulent Electron Energy Flux"
    
    onetwo['tglf_ion_e_flux']          = {} 
    onetwo['tglf_ion_e_flux']['data']  = None
    onetwo['tglf_ion_e_flux']['unit']  = "J/m^2/s"
    onetwo['tglf_ion_e_flux']['info']  = "TGLF Turbulent Effective Primary Energy Flux"
    
    onetwo['tglf_imp_e_flux']          = {} 
    onetwo['tglf_imp_e_flux']['data']  = None
    onetwo['tglf_imp_e_flux']['unit']  = "J/m^2/s"
    onetwo['tglf_imp_e_flux']['info']  = "TGLF Turbulent Effective Impurity Energy Flux"
    
    onetwo['tglf_elect_m_flux']        = {} 
    onetwo['tglf_elect_m_flux']['data']= None
    onetwo['tglf_elect_m_flux']['unit']= "kg/s^2"
    onetwo['tglf_elect_m_flux']['info']= "TGLF Turbulent Electron Momentum Flux"
    
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

    onetwo['stource']                  = {} 
    onetwo['stource']['data']          = None
    onetwo['stource']['unit']          = "1/m^3/s"
    onetwo['stource']['info']          = "Total Source Rate, d"
    
    onetwo['']                = {} 
    onetwo['']['data']        = None
    onetwo['']['unit']        = None
    onetwo['']['info']        = None
    
    onetwo['']                = {} 
    onetwo['']['data']        = None
    onetwo['']['unit']        = None
    onetwo['']['info']        = None
    
    onetwo['']                = {} 
    onetwo['']['data']        = None
    onetwo['']['unit']        = None
    onetwo['']['info']        = None
    
    onetwo['']                = {} 
    onetwo['']['data']        = None
    onetwo['']['unit']        = None
    onetwo['']['info']        = None
    
    onetwo['']                = {} 
    onetwo['']['data']        = None
    onetwo['']['unit']        = None
    onetwo['']['info']        = None
    
    onetwo['']                = {} 
    onetwo['']['data']        = None
    onetwo['']['unit']        = None
    onetwo['']['info']        = None
    
    onetwo['']                = {} 
    onetwo['']['data']        = None
    onetwo['']['unit']        = None
    onetwo['']['info']        = None
    
    onetwo['']                = {} 
    onetwo['']['data']        = None
    onetwo['']['unit']        = None
    onetwo['']['info']        = None
    
    onetwo['']                = {} 
    onetwo['']['data']        = None
    onetwo['']['unit']        = None
    onetwo['']['info']        = None
    
    onetwo['']                = {} 
    onetwo['']['data']        = None
    onetwo['']['unit']        = None
    onetwo['']['info']        = None
    
    onetwo['']                = {} 
    onetwo['']['data']        = None
    onetwo['']['unit']        = None
    onetwo['']['info']        = None
    
    onetwo['']                = {} 
    onetwo['']['data']        = None
    onetwo['']['unit']        = None
    onetwo['']['info']        = None
    
    onetwo['jbs']                = {} 
    onetwo['jbs']['data']        = None
    onetwo['jbs']['unit']        = None
    onetwo['jbs']['info']        = None
    
    onetwo['jnb']                = {} 
    onetwo['jnb']['data']        = None
    onetwo['jnb']['unit']        = None
    onetwo['jnb']['info']        = None
    
    onetwo['jrf']                = {} 
    onetwo['jrf']['data']        = None
    onetwo['jrf']['unit']        = None
    onetwo['jrf']['info']        = None
    
    onetwo['johm']               = {} 
    onetwo['johm']['data']       = None
    onetwo['johm']['unit']        = None
    onetwo['johm']['info']        = None
    
    onetwo['jtot']               = {} 
    onetwo['jtot']['data']       = None
    onetwo['jtot']['unit']        = None
    onetwo['jtot']['info']        = None
    
    onetwo['Rmag']               = {} 
    onetwo['Rmag']['data']       = None
    onetwo['Rmag']['unit']        = None
    onetwo['Rmag']['info']        = None
    
    onetwo['ibion']              = {} 
    onetwo['ibion']['data']      = None
    onetwo['ibion']['unit']        = None
    onetwo['ibion']['info']        = None
    
    onetwo['kappa']              = {} 
    onetwo['kappa']['data']      = None
    onetwo['kappa']['unit']        = None
    onetwo['kappa']['info']        = None
    
    onetwo['delta']              = {} 
    onetwo['delta']['data']      = None
    onetwo['delta']['unit']        = None
    onetwo['delta']['info']        = None
    
    onetwo['cxareao']            = {} 
    onetwo['cxareao']['data']    = None
    onetwo['cxareao']['unit']        = None
    onetwo['cxareao']['info']        = None
    
    onetwo['rho']                = {}
    onetwo['rho']['data']        = None
    onetwo['rho']['unit']        = None
    onetwo['rho']['info']        = None

    onetwo['s']                  = {}
    onetwo['s']['data']          = None
    onetwo['s']['unit']        = None
    onetwo['s']['info']        = None

    onetwo['dudt']               = {}
    onetwo['dudt']['data']       = None
    onetwo['dudt']['unit']        = None
    onetwo['dudt']['info']        = None

    onetwo['sbcx_d']             = {}
    onetwo['sbcx_d']['data']     = None
    onetwo['sbcx_d']['unit']        = None
    onetwo['sbcx_d']['info']        = None

    onetwo['sion_d']             = {}
    onetwo['sion_d']['data']     = None
    onetwo['sion_d']['unit']        = None
    onetwo['sion_d']['info']        = None

    onetwo['enbeam']             = {}
    onetwo['enbeam']['data']     = None
    onetwo['enbeam']['unit']        = None
    onetwo['enbeam']['info']        = None

    onetwo['enn']                = {}
    onetwo['enn']['data']        = None
    onetwo['enn']['unit']        = None
    onetwo['enn']['info']        = None

    onetwo['ennw']               = {}
    onetwo['ennw']['data']       = None
    onetwo['ennw']['unit']        = None
    onetwo['ennw']['info']        = None

    onetwo['ennv']               = {}
    onetwo['ennv']['data']       = None
    onetwo['ennv']['unit']        = None
    onetwo['ennv']['info']        = None

    onetwo['ennvol']             = {}
    onetwo['ennvol']['data']     = None
    onetwo['ennvol']['unit']        = None
    onetwo['ennvol']['info']        = None

    onetwo['sbeame']             = {}
    onetwo['sbeame']['data']     = None
    onetwo['sbeame']['unit']        = None
    onetwo['sbeame']['info']        = None

    onetwo['sbeam']              = {}
    onetwo['sbeam']['data']      = None
    onetwo['sbeam']['unit']        = None
    onetwo['sbeam']['info']        = None

    onetwo['Tm']                 = {}
    onetwo['Tm']['data']         = None
    onetwo['Tm']['unit']        = None
    onetwo['Tm']['info']        = None

    onetwo['zeff']               = {}
    onetwo['zeff']['data']       = None
    onetwo['zeff']['unit']        = None
    onetwo['zeff']['info']        = None

    onetwo['angrot']             = {}
    onetwo['angrot']['data']     = None
    onetwo['angrot']['unit']        = None
    onetwo['angrot']['info']        = None

    onetwo['edifth']             = {}
    onetwo['edifth']['data']     = None
    onetwo['edifth']['unit']        = None
    onetwo['edifth']['info']        = None

    onetwo['idifth']             = {}
    onetwo['idifth']['data']     = None
    onetwo['idifth']['unit']        = None
    onetwo['idifth']['info']        = None

    onetwo['ineoth']             = {}
    onetwo['ineoth']['data']     = None
    onetwo['ineoth']['unit']        = None
    onetwo['ineoth']['info']        = None

    onetwo['dpedt']              = {}
    onetwo['dpedt']['data']      = None
    onetwo['dpedt']['unit']        = None
    onetwo['dpedt']['info']        = None

    onetwo['dpidt']              = {}
    onetwo['dpidt']['data']      = None
    onetwo['dpidt']['unit']        = None
    onetwo['dpidt']['info']        = None

    onetwo['econduct']           = {}
    onetwo['econduct']['data']   = None
    onetwo['econduct']['unit']        = None
    onetwo['econduct']['info']        = None

    onetwo['iconduct']           = {}
    onetwo['iconduct']['data']   = None
    onetwo['iconduct']['unit']        = None
    onetwo['iconduct']['info']        = None

    onetwo['econvect']           = {}
    onetwo['econvect']['data']   = None
    onetwo['econvect']['unit']        = None
    onetwo['econvect']['info']        = None

    onetwo['iconvect']           = {}
    onetwo['iconvect']['data']   = None
    onetwo['iconvect']['unit']        = None
    onetwo['iconvect']['info']        = None

    onetwo['qbeame']             = {}
    onetwo['qbeame']['data']     = None
    onetwo['qbeame']['unit']        = None
    onetwo['qbeame']['info']        = None

    onetwo['qdelt']              = {}
    onetwo['qdelt']['data']      = None
    onetwo['qdelt']['unit']        = None
    onetwo['qdelt']['info']        = None

    onetwo['qbeami']             = {}
    onetwo['qbeami']['data']     = None
    onetwo['qbeami']['unit']        = None
    onetwo['qbeami']['info']        = None

    onetwo['qrfe']               = {}
    onetwo['qrfe']['data']       = None
    onetwo['qrfe']['unit']        = None
    onetwo['qrfe']['info']        = None

    onetwo['qrfi']               = {}
    onetwo['qrfi']['data']       = None
    onetwo['qrfi']['unit']        = None
    onetwo['qrfi']['info']        = None

    onetwo['qione']              = {}
    onetwo['qione']['data']      = None
    onetwo['qione']['unit']        = None
    onetwo['qione']['info']        = None

    onetwo['qioni']              = {}
    onetwo['qioni']['data']      = None
    onetwo['qioni']['unit']        = None
    onetwo['qioni']['info']        = None

    onetwo['qcx']                = {}
    onetwo['qcx']['data']        = None
    onetwo['qcx']['unit']        = None
    onetwo['qcx']['info']        = None

    onetwo['qe2d']               = {}
    onetwo['qe2d']['data']       = None
    onetwo['qe2d']['unit']        = None
    onetwo['qe2d']['info']        = None

    onetwo['qi2d']               = {}
    onetwo['qi2d']['data']       = None
    onetwo['qi2d']['unit']        = None
    onetwo['qi2d']['info']        = None

    onetwo['qfuse']              = {}
    onetwo['qfuse']['data']      = None
    onetwo['qfuse']['unit']        = None
    onetwo['qfuse']['info']        = None

    onetwo['qfusi']              = {}
    onetwo['qfusi']['data']      = None
    onetwo['qfusi']['unit']        = None
    onetwo['qfusi']['info']        = None

    onetwo['qfuseb']             = {}
    onetwo['qfuseb']['data']     = None
    onetwo['qfuseb']['unit']        = None
    onetwo['qfuseb']['info']        = None

    onetwo['qfusib']             = {}
    onetwo['qfusib']['data']     = None
    onetwo['qfusib']['unit']        = None
    onetwo['qfusib']['info']        = None

    onetwo['qmage']              = {}
    onetwo['qmage']['data']      = None
    onetwo['qmage']['unit']        = None
    onetwo['qmage']['info']        = None

    onetwo['qswte']              = {}
    onetwo['qswte']['data']      = None
    onetwo['qswte']['unit']        = None
    onetwo['qswte']['info']        = None

    onetwo['qswti']              = {}
    onetwo['qswti']['data']      = None
    onetwo['qswti']['unit']        = None
    onetwo['qswti']['info']        = None

    onetwo['qrad']               = {}
    onetwo['qrad']['data']       = None
    onetwo['qrad']['unit']        = None
    onetwo['qrad']['info']        = None

    onetwo['qohm']               = {}
    onetwo['qohm']['data']       = None
    onetwo['qohm']['unit']        = None
    onetwo['qohm']['info']        = None

    onetwo['rmajfs']             = {}
    onetwo['rmajfs']['data']     = None
    onetwo['rmajfs']['unit']        = None
    onetwo['rmajfs']['info']        = None

    onetwo['rminfs']             = {}
    onetwo['rminfs']['data']     = None
    onetwo['rminfs']['unit']        = None
    onetwo['rminfs']['info']        = None

    onetwo['volfs']              = {}
    onetwo['volfs']['data']      = None
    onetwo['volfs']['unit']        = None
    onetwo['volfs']['info']        = None

    onetwo['kappafs']            = {}
    onetwo['kappafs']['data']    = None
    onetwo['kappafs']['unit']        = None
    onetwo['kappafs']['info']        = None

    onetwo['deltafs']            = {}
    onetwo['deltafs']['data']    = None
    onetwo['deltafs']['unit']        = None
    onetwo['deltafs']['info']        = None

    onetwo['indfs']              = {}
    onetwo['indfs']['data']      = None
    onetwo['indfs']['unit']        = None
    onetwo['indfs']['info']        = None

    onetwo['areafs']             = {}
    onetwo['areafs']['data']     = None
    onetwo['areafs']['unit']        = None
    onetwo['areafs']['info']        = None

    onetwo['xareafs']            = {}
    onetwo['xareafs']['data']    = None
    onetwo['xareafs']['unit']        = None
    onetwo['xareafs']['info']        = None

    onetwo['gradrhofs']          = {}
    onetwo['gradrhofs']['data']  = None
    onetwo['gradrhofs']['unit']        = None
    onetwo['gradrhofs']['info']        = None

    onetwo['gradrho2fs']         = {}
    onetwo['gradrho2fs']['data'] = None
    onetwo['gradrho2fs']['unit']        = None
    onetwo['gradrho2fs']['info']        = None

    onetwo['nplasbdry']          = {}
    onetwo['nplasbdry']['data']  = None
    onetwo['nplasbdry']['unit']        = None
    onetwo['nplasbdry']['info']        = None

    onetwo['rbdry']              = {}
    onetwo['rbdry']['data']      = None
    onetwo['rbdry']['unit']        = None
    onetwo['rbdry']['info']        = None

    onetwo['zbdry']              = {}
    onetwo['zbdry']['data']      = None
    onetwo['zbdry']['unit']        = None
    onetwo['zbdry']['info']        = None

    onetwo['storqueb']           = {}
    onetwo['storqueb']['data']   = None
    onetwo['storqueb']['unit']        = None
    onetwo['storqueb']['info']        = None

    onetwo['p_tot']              = {}
    onetwo['p_tot']['data']      = None
    onetwo['p_tot']['unit']      = None
    onetwo['p_tot']['info']        = None

    onetwo['sscxl']              = {}
    onetwo['sscxl']['data']      = None
    onetwo['sscxl']['unit']      = None
    onetwo['sscxl']['info']        = None

    onetwo['qsync']              = {}
    onetwo['qsync']['data']      = None
    onetwo['qsync']['unit']      = None
    onetwo['qsync']['info']        = None

  # onetwo['']                 = {}
  # onetwo['']['data']         = {}

    return onetwo


def read_iterdb_file(fname):
    if os.path.isfile(fname):
        fid = open(fname,'r')
    else:
        raise IOError("FILE %s DOES NOT EXIST!" % fname); sys.exit()

    onetwo = get_iterdb_vars()
    onetwo_varnames = list(onetwo.keys())

    fid.readline()
    fid.readline()
    line = fid.readline()
    onetwo["ishot"]['data'] = line.strip()

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
    onetwo["ibion"]['data'] = int(line.strip())

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
    onetwo["Rmag"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["R0"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["kappa"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["delta"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["pindent"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["volo"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["cxareao"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    onetwo["Btor"]['data'] = float(line.strip())

    fid.readline()
    line = fid.readline()
    linecontent = line.split()
    onetwo['itot']['data'] = float(linecontent[0])
    onetwo['iohm']['data'] = float(linecontent[1])
    onetwo['ibs']['data']  = float(linecontent[2])
    onetwo['inb']['data']  = float(linecontent[3])
    onetwo['irf']['data']  = float(linecontent[4])

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

    onetwo["psi"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["psi"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["psi"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["psi"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["psi"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["psi"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["rhogrid"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["rhogrid"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["rhogrid"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["rhogrid"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["rhogrid"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["rhogrid"]['data'][iline*5+4] = float(linecontent[4])
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

    onetwo["te"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["te"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["te"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["te"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["te"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["te"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["ti"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["ti"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["ti"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["ti"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["ti"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["ti"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["q"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["q"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["q"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["q"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["q"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["q"]['data'][iline*5+4] = float(linecontent[4])
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
    onetwo["sion_d"]["data"] = numpy.sum(onetwo["sion"]["data"],axis=0)

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
    onetwo["sbcx_d"]["data"] = numpy.sum(onetwo["sbcx"]["data"],axis=0)


    onetwo["s"]['data'] = numpy.zeros((nprim,nrho),dtype=float)
    for i in range(nprim):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["s"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["s"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["s"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["s"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["s"]['data'][i,iline*5+4] = float(linecontent[4])
            except:
                error = 'empty records'


    onetwo["dudt"]['data'] = numpy.zeros((nprim,nrho),dtype=float)
    for i in range(nprim):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["dudt"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["dudt"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["dudt"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["dudt"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["dudt"]['data'][i,iline*5+4] = float(linecontent[4])
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

    onetwo["ennvol"]['data'] = numpy.zeros((nprim,nrho),dtype=float)
    for i in range(nprim):
        fid.readline()
        for iline in range(nlines):
            line = fid.readline()
            linecontent = line.split()
            try:
                onetwo["ennvol"]['data'][i,iline*5+0] = float(linecontent[0])
                onetwo["ennvol"]['data'][i,iline*5+1] = float(linecontent[1])
                onetwo["ennvol"]['data'][i,iline*5+2] = float(linecontent[2])
                onetwo["ennvol"]['data'][i,iline*5+3] = float(linecontent[3])
                onetwo["ennvol"]['data'][i,iline*5+4] = float(linecontent[4])
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

    onetwo["jtot"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["jtot"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["jtot"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["jtot"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["jtot"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["jtot"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["johm"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["johm"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["johm"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["johm"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["johm"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["johm"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["jbs"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["jbs"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["jbs"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["jbs"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["jbs"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["jbs"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["jnb"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["jnb"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["jnb"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["jnb"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["jnb"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["jnb"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["jrf"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["jrf"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["jrf"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["jrf"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["jrf"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["jrf"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["Tm"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["Tm"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["Tm"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["Tm"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["Tm"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["Tm"]['data'][iline*5+4] = float(linecontent[4])
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

    onetwo["edifth"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["edifth"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["edifth"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["edifth"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["edifth"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["edifth"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["idifth"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["idifth"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["idifth"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["idifth"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["idifth"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["idifth"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["ineoth"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["ineoth"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["ineoth"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["ineoth"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["ineoth"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["ineoth"]['data'][iline*5+4] = float(linecontent[4])
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

    onetwo["econduct"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["econduct"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["econduct"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["econduct"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["econduct"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["econduct"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["iconduct"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["iconduct"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["iconduct"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["iconduct"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["iconduct"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["iconduct"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["econvect"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["econvect"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["econvect"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["econvect"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["econvect"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["econvect"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["iconvect"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["iconvect"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["iconvect"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["iconvect"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["iconvect"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["iconvect"]['data'][iline*5+4] = float(linecontent[4])
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

    onetwo["qfuseb"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qfuseb"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qfuseb"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qfuseb"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qfuseb"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qfuseb"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qfusib"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qfusib"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qfusib"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qfusib"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qfusib"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qfusib"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qmage"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qmage"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qmage"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qmage"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qmage"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qmage"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qswte"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qswte"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qswte"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qswte"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qswte"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qswte"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["qswti"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["qswti"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["qswti"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["qswti"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["qswti"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["qswti"]['data'][iline*5+4] = float(linecontent[4])
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

    onetwo["rmajfs"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["rmajfs"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["rmajfs"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["rmajfs"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["rmajfs"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["rmajfs"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["rminfs"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["rminfs"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["rminfs"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["rminfs"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["rminfs"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["rminfs"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["volfs"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["volfs"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["volfs"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["volfs"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["volfs"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["volfs"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["kappafs"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["kappafs"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["kappafs"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["kappafs"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["kappafs"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["kappafs"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["deltafs"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["deltafs"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["deltafs"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["deltafs"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["deltafs"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["deltafs"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["indfs"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["indfs"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["indfs"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["indfs"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["indfs"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["indfs"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    fid.readline()

    onetwo["areafs"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["areafs"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["areafs"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["areafs"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["areafs"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["areafs"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["xareafs"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["xareafs"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["xareafs"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["xareafs"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["xareafs"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["xareafs"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["gradrhofs"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["gradrhofs"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["gradrhofs"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["gradrhofs"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["gradrhofs"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["gradrhofs"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["gradrho2fs"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nlines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["gradrho2fs"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["gradrho2fs"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["gradrho2fs"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["gradrho2fs"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["gradrho2fs"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    fid.readline()
    line = fid.readline()
    onetwo["nplasbdry"]['data'] = int(line.strip())
    nplasbdry = int(line.strip())
    nblines = int((onetwo["nj"]['data'] / 5) + (onetwo["nj"]['data'] % 5))

    onetwo["rbdry"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nblines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["rbdry"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["rbdry"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["rbdry"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["rbdry"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["rbdry"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["zbdry"]['data'] = numpy.zeros(nrho,dtype=float)
    fid.readline()
    for iline in range(nblines):
        line = fid.readline()
        linecontent = line.split()
        try:
            onetwo["zbdry"]['data'][iline*5+0] = float(linecontent[0])
            onetwo["zbdry"]['data'][iline*5+1] = float(linecontent[1])
            onetwo["zbdry"]['data'][iline*5+2] = float(linecontent[2])
            onetwo["zbdry"]['data'][iline*5+3] = float(linecontent[3])
            onetwo["zbdry"]['data'][iline*5+4] = float(linecontent[4])
        except:
            error = 'empty records'

    onetwo["storqueb"]['data'] = numpy.zeros(nrho,dtype=float)
    infoline = fid.readline()
    if "beam  torque" in infoline:
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

    onetwo["p_tot"]['data'] = numpy.zeros(nrho,dtype=float)
    infoline = fid.readline()
    if "total  pressure" in infoline:
       for iline in range(nlines):
           line = fid.readline()
           linecontent = line.split()
           try:
               onetwo["p_tot"]['data'][iline*5+0] = float(linecontent[0])
               onetwo["p_tot"]['data'][iline*5+1] = float(linecontent[1])
               onetwo["p_tot"]['data'][iline*5+2] = float(linecontent[2])
               onetwo["p_tot"]['data'][iline*5+3] = float(linecontent[3])
               onetwo["p_tot"]['data'][iline*5+4] = float(linecontent[4])
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



if __name__ == "__main__":
    fname = "iterdb.101381"
    read_iterdb_file(fname)



