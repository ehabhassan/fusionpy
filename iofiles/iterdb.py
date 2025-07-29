import os
import sys
import numpy
import random
import netCDF4 as ncdf

from maths.interp        import interp
from iofiles.Namelist    import Namelist
from iofiles.eqdsk       import read_eqdsk_file
from iofiles.plasmastate import get_instate_vars

type_none = type(None)

def get_iterdb_vars():
    iterdb = {}
    
    iterdb['hash_codes'] = {}
    iterdb['hash_codes']['data'] = None
    iterdb['hash_codes']['units'] = None
    
    iterdb['version_id'] = {}
    iterdb['version_id']['data'] = None
    iterdb['version_id']['units'] = None
    
    iterdb['alla_index'] = {}
    iterdb['alla_index']['data'] = None
    iterdb['alla_index']['units'] = None
    iterdb['alla_index']['section'] = 'SIMULATION_INIT'
    iterdb['alla_index']['long_name'] = 'species index in original lists'
    iterdb['alla_index']['component'] = 'PLASMA'
    iterdb['alla_index']['specification'] = 'I alla_index(0:nspec_alla)'
    
    iterdb['ALLA_name'] = {}
    iterdb['ALLA_name']['data'] = None
    iterdb['ALLA_name']['units'] = None
    iterdb['ALLA_name']['section'] = 'SIMULATION_INIT'
    iterdb['ALLA_name']['long_name'] = 'all species abridged'
    iterdb['ALLA_name']['component'] = 'PLASMA'
    iterdb['ALLA_name']['specification'] = 'S|specie  ALLA(0:nspec_alla)'
    
    iterdb['ALLA_type'] = {}
    iterdb['ALLA_type']['data'] = None
    iterdb['ALLA_type']['units'] = None
    iterdb['ALLA_type']['section'] = 'SIMULATION_INIT'
    iterdb['ALLA_type']['long_name'] = 'ALLA specie types'
    iterdb['ALLA_type']['component'] = 'PLASMA'
    iterdb['ALLA_type']['specification'] = 'S|specie  ALLA(0:nspec_alla)'
    
    iterdb['all_index'] = {}
    iterdb['all_index']['data'] = None
    iterdb['all_index']['units'] = None
    iterdb['all_index']['section'] = 'SIMULATION_INIT'
    iterdb['all_index']['long_name'] = 'species index in original lists'
    iterdb['all_index']['component'] = 'PLASMA'
    iterdb['all_index']['specification'] = 'I all_index(0:nspec_all)'
    
    iterdb['ALL_name'] = {}
    iterdb['ALL_name']['data'] = None
    iterdb['ALL_name']['units'] = None
    iterdb['ALL_name']['section'] = 'SIMULATION_INIT'
    iterdb['ALL_name']['long_name'] = 'all species'
    iterdb['ALL_name']['component'] = 'PLASMA'
    iterdb['ALL_name']['specification'] = 'S|specie  ALL(0:nspec_all)'
    
    iterdb['ALL_type'] = {}
    iterdb['ALL_type']['data'] = None
    iterdb['ALL_type']['units'] = None
    iterdb['ALL_type']['section'] = 'SIMULATION_INIT'
    iterdb['ALL_type']['long_name'] = 'ALL specie types'
    iterdb['ALL_type']['component'] = 'PLASMA'
    iterdb['ALL_type']['specification'] = 'S|specie  ALL(0:nspec_all)'
    
    iterdb['ANOM_Code_Info'] = {}
    iterdb['ANOM_Code_Info']['data'] = None
    iterdb['ANOM_Code_Info']['units'] = None
    iterdb['ANOM_Code_Info']['section'] = 'SIMULATION_INIT'
    iterdb['ANOM_Code_Info']['long_name'] = 'Information: code implementing ANOM component'
    iterdb['ANOM_Code_Info']['component'] = 'ANOM'
    iterdb['ANOM_Code_Info']['specification'] = 'C*80   ANOM_Code_Info'
    
    iterdb['ap2_halfheight'] = {}
    iterdb['ap2_halfheight']['data'] = None
    iterdb['ap2_halfheight']['units'] = 'm'
    iterdb['ap2_halfheight']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['ap2_halfheight']['long_name'] = 'aperture half-height'
    iterdb['ap2_halfheight']['component'] = 'NBI'
    iterdb['ap2_halfheight']['specification'] = 'R|units=m         ap2_halfheight(nbeam)'
    
    iterdb['ap2_halfwidth'] = {}
    iterdb['ap2_halfwidth']['data'] = None
    iterdb['ap2_halfwidth']['units'] = 'm'
    iterdb['ap2_halfwidth']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['ap2_halfwidth']['long_name'] = '2nd aperture half-width'
    iterdb['ap2_halfwidth']['component'] = 'NBI'
    iterdb['ap2_halfwidth']['specification'] = 'R|units=m         ap2_halfwidth(nbeam)'
    
    iterdb['ap2_horiz_offset'] = {}
    iterdb['ap2_horiz_offset']['data'] = None
    iterdb['ap2_horiz_offset']['units'] = 'm'
    iterdb['ap2_horiz_offset']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['ap2_horiz_offset']['long_name'] = 'horizontal offset, 2nd aperture'
    iterdb['ap2_horiz_offset']['component'] = 'NBI'
    iterdb['ap2_horiz_offset']['specification'] = 'R|units=m         ap2_horiz_offset(nbeam)'
    
    iterdb['ap2_vert_offset'] = {}
    iterdb['ap2_vert_offset']['data'] = None
    iterdb['ap2_vert_offset']['units'] = 'm'
    iterdb['ap2_vert_offset']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['ap2_vert_offset']['long_name'] = 'vertical offset, 2nd aperture'
    iterdb['ap2_vert_offset']['component'] = 'NBI'
    iterdb['ap2_vert_offset']['specification'] = 'R|units=m         ap2_vert_offset(nbeam)'
    
    iterdb['ap_halfheight'] = {}
    iterdb['ap_halfheight']['data'] = None
    iterdb['ap_halfheight']['units'] = 'm'
    iterdb['ap_halfheight']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['ap_halfheight']['long_name'] = 'aperture half-height'
    iterdb['ap_halfheight']['component'] = 'NBI'
    iterdb['ap_halfheight']['specification'] = 'R|units=m         ap_halfheight(nbeam)'
    
    iterdb['ap_halfwidth'] = {}
    iterdb['ap_halfwidth']['data'] = None
    iterdb['ap_halfwidth']['units'] = 'm'
    iterdb['ap_halfwidth']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['ap_halfwidth']['long_name'] = 'aperture half-width'
    iterdb['ap_halfwidth']['component'] = 'NBI'
    iterdb['ap_halfwidth']['specification'] = 'R|units=m         ap_halfwidth(nbeam)'
    
    iterdb['ap_horiz_offset'] = {}
    iterdb['ap_horiz_offset']['data'] = None
    iterdb['ap_horiz_offset']['units'] = 'm'
    iterdb['ap_horiz_offset']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['ap_horiz_offset']['long_name'] = 'horizontal offset of aperture'
    iterdb['ap_horiz_offset']['component'] = 'NBI'
    iterdb['ap_horiz_offset']['specification'] = 'R|units=m         ap_horiz_offset(nbeam)'
    
    iterdb['ap_vert_offset'] = {}
    iterdb['ap_vert_offset']['data'] = None
    iterdb['ap_vert_offset']['units'] = 'm'
    iterdb['ap_vert_offset']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['ap_vert_offset']['long_name'] = 'vertical offset of aperture'
    iterdb['ap_vert_offset']['component'] = 'NBI'
    iterdb['ap_vert_offset']['specification'] = 'R|units=m         ap_vert_offset(nbeam)'
    
    iterdb['area'] = {}
    iterdb['area']['data'] = None
    iterdb['area']['units'] = 'm^2'
    iterdb['area']['section'] = 'STATE_PROFILES'
    iterdb['area']['long_name'] = 'enclosed area'
    iterdb['area']['component'] = 'EQ'
    iterdb['area']['specification'] = 'R|units=m^2|Spline_00 area(nrho_eq)'
    
    iterdb['beam_type'] = {}
    iterdb['beam_type']['data'] = None
    iterdb['beam_type']['units'] = None
    iterdb['beam_type']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['beam_type']['long_name'] = 'beam type:'
    iterdb['beam_type']['component'] = 'NBI'
    iterdb['beam_type']['specification'] = 'N     beam_type(nbeam)'
    
    iterdb['BphiRZ'] = {}
    iterdb['BphiRZ']['data'] = None
    iterdb['BphiRZ']['units'] = 'T'
    iterdb['BphiRZ']['section'] = 'STATE_PROFILES'
    iterdb['BphiRZ']['long_name'] = 'Toroidal field'
    iterdb['BphiRZ']['component'] = 'EQ'
    iterdb['BphiRZ']['specification'] = 'R|units=T|Hermite      BphiRZ(nR,nZ)'
    
    iterdb['BRRZ'] = {}
    iterdb['BRRZ']['data'] = None
    iterdb['BRRZ']['units'] = 'T'
    iterdb['BRRZ']['section'] = 'STATE_PROFILES'
    iterdb['BRRZ']['long_name'] = 'R component of poloidal field'
    iterdb['BRRZ']['component'] = 'EQ'
    iterdb['BRRZ']['specification'] = 'R|units=T|Hermite      BRRZ(nR,nZ)'
    
    iterdb['BZRZ'] = {}
    iterdb['BZRZ']['data'] = None
    iterdb['BZRZ']['units'] = 'T'
    iterdb['BZRZ']['section'] = 'STATE_PROFILES'
    iterdb['BZRZ']['long_name'] = 'Z component of poloidal field'
    iterdb['BZRZ']['component'] = 'EQ'
    iterdb['BZRZ']['specification'] = 'R|units=T|Hermite      BZRZ(nR,nZ)'
    
    iterdb['B_axis'] = {}
    iterdb['B_axis']['data'] = None
    iterdb['B_axis']['units'] = 'T'
    iterdb['B_axis']['section'] = 'STATE_DATA'
    iterdb['B_axis']['long_name'] = '|B| at magnetic axis'
    iterdb['B_axis']['component'] = 'EQ'
    iterdb['B_axis']['specification'] = 'R  B_axis'
    
    iterdb['B_axis_vac'] = {}
    iterdb['B_axis_vac']['data'] = None
    iterdb['B_axis_vac']['units'] = 'T'
    iterdb['B_axis_vac']['section'] = 'STATE_DATA'
    iterdb['B_axis_vac']['long_name'] = 'vacuum B field at axis'
    iterdb['B_axis_vac']['component'] = 'EQ'
    iterdb['B_axis_vac']['specification'] = 'R  B_axis_vac'
    
    iterdb['b_halfHeight'] = {}
    iterdb['b_halfHeight']['data'] = None
    iterdb['b_halfHeight']['units'] = 'm'
    iterdb['b_halfHeight']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['b_halfHeight']['long_name'] = 'beam half-height at source'
    iterdb['b_halfHeight']['component'] = 'NBI'
    iterdb['b_halfHeight']['specification'] = 'R|units=m       b_halfHeight(nbeam)'
    
    iterdb['b_halfwidth'] = {}
    iterdb['b_halfwidth']['data'] = None
    iterdb['b_halfwidth']['units'] = 'm'
    iterdb['b_halfwidth']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['b_halfwidth']['long_name'] = 'beam half-width at source'
    iterdb['b_halfwidth']['component'] = 'NBI'
    iterdb['b_halfwidth']['specification'] = 'R|units=m       b_halfwidth(nbeam)'
    
    iterdb['b_Hdivergence'] = {}
    iterdb['b_Hdivergence']['data'] = None
    iterdb['b_Hdivergence']['units'] = 'degrees'
    iterdb['b_Hdivergence']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['b_Hdivergence']['long_name'] = 'horizontal divergence (D) of beam'
    iterdb['b_Hdivergence']['component'] = 'NBI'
    iterdb['b_Hdivergence']['specification'] = 'R|units=degrees   b_Hdivergence(nbeam)'
    
    iterdb['b_Hfocal_length'] = {}
    iterdb['b_Hfocal_length']['data'] = None
    iterdb['b_Hfocal_length']['units'] = 'm'
    iterdb['b_Hfocal_length']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['b_Hfocal_length']['long_name'] = 'horizontal focal length'
    iterdb['b_Hfocal_length']['component'] = 'NBI'
    iterdb['b_Hfocal_length']['specification'] = 'R|units=m       b_Hfocal_length(nbeam)'
    
    iterdb['B_max_lcfs'] = {}
    iterdb['B_max_lcfs']['data'] = None
    iterdb['B_max_lcfs']['units'] = 'T'
    iterdb['B_max_lcfs']['section'] = 'STATE_DATA'
    iterdb['B_max_lcfs']['long_name'] = '|B|_max of last closed flux surface'
    iterdb['B_max_lcfs']['component'] = 'EQ'
    iterdb['B_max_lcfs']['specification'] = 'R  B_max_lcfs'
    
    iterdb['B_min_lcfs'] = {}
    iterdb['B_min_lcfs']['data'] = None
    iterdb['B_min_lcfs']['units'] = 'T'
    iterdb['B_min_lcfs']['section'] = 'STATE_DATA'
    iterdb['B_min_lcfs']['long_name'] = '|B|_min of last closed flux surface'
    iterdb['B_min_lcfs']['component'] = 'EQ'
    iterdb['B_min_lcfs']['specification'] = 'R  B_min_lcfs'
    
    iterdb['B_surfMax'] = {}
    iterdb['B_surfMax']['data'] = None
    iterdb['B_surfMax']['units'] = 'T'
    iterdb['B_surfMax']['section'] = 'STATE_PROFILES'
    iterdb['B_surfMax']['long_name'] = 'max mod(B) on flux surface'
    iterdb['B_surfMax']['component'] = 'EQ'
    iterdb['B_surfMax']['specification'] = 'R|pclin  B_surfMax(nrho_eq_geo)'
    
    iterdb['B_surfMin'] = {}
    iterdb['B_surfMin']['data'] = None
    iterdb['B_surfMin']['units'] = 'T'
    iterdb['B_surfMin']['section'] = 'STATE_PROFILES'
    iterdb['B_surfMin']['long_name'] = 'min mod(B) on flux surface'
    iterdb['B_surfMin']['component'] = 'EQ'
    iterdb['B_surfMin']['specification'] = 'R|pclin  B_surfMin(nrho_eq_geo)'
    
    iterdb['b_Vdivergence'] = {}
    iterdb['b_Vdivergence']['data'] = None
    iterdb['b_Vdivergence']['units'] = 'degrees'
    iterdb['b_Vdivergence']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['b_Vdivergence']['long_name'] = 'vertical divergence (D) of beam'
    iterdb['b_Vdivergence']['component'] = 'NBI'
    iterdb['b_Vdivergence']['specification'] = 'R|units=degrees   b_Vdivergence(nbeam)'
    
    iterdb['b_Vfocal_length'] = {}
    iterdb['b_Vfocal_length']['data'] = None
    iterdb['b_Vfocal_length']['units'] = 'm'
    iterdb['b_Vfocal_length']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['b_Vfocal_length']['long_name'] = 'vertical focal length'
    iterdb['b_Vfocal_length']['component'] = 'NBI'
    iterdb['b_Vfocal_length']['specification'] = 'R|units=m       b_Vfocal_length(nbeam)'
    
    iterdb['chie_trans'] = {}
    iterdb['chie_trans']['data'] = None
    iterdb['chie_trans']['units'] = 'm^2/sec'
    iterdb['chie_trans']['section'] = 'STATE_PROFILES'
    iterdb['chie_trans']['long_name'] = 'electron thermal diffusivity'
    iterdb['chie_trans']['component'] = 'PLASMA'
    iterdb['chie_trans']['specification'] = 'R|pclin chie_trans(nrho)'
    
    iterdb['chii_trans'] = {}
    iterdb['chii_trans']['data'] = None
    iterdb['chii_trans']['units'] = 'm^2/sec'
    iterdb['chii_trans']['section'] = 'STATE_PROFILES'
    iterdb['chii_trans']['long_name'] = 'ion thermal diffusivity'
    iterdb['chii_trans']['component'] = 'PLASMA'
    iterdb['chii_trans']['specification'] = 'R|pclin chii_trans(nrho)'
    
    iterdb['chimo_trans'] = {}
    iterdb['chimo_trans']['data'] = None
    iterdb['chimo_trans']['units'] = 'm^2/sec'
    iterdb['chimo_trans']['section'] = 'STATE_PROFILES'
    iterdb['chimo_trans']['long_name'] = 'angular momentum diffusivity'
    iterdb['chimo_trans']['component'] = 'PLASMA'
    iterdb['chimo_trans']['specification'] = 'R|pclin chimo_trans(nrho)'
    
    iterdb['curbeam'] = {}
    iterdb['curbeam']['data'] = None
    iterdb['curbeam']['units'] = 'A'
    iterdb['curbeam']['section'] = 'STATE_PROFILES'
    iterdb['curbeam']['long_name'] = 'beam ion driven current (shielded)'
    iterdb['curbeam']['component'] = 'NBI'
    iterdb['curbeam']['specification'] = 'R|step*dA|units=A   curbeam(~nrho_nbi)'
    
    iterdb['curech'] = {}
    iterdb['curech']['data'] = None
    iterdb['curech']['units'] = 'A'
    iterdb['curech']['section'] = 'STATE_PROFILES'
    iterdb['curech']['long_name'] = 'ECH current drive'
    iterdb['curech']['component'] = 'EC'
    iterdb['curech']['specification'] = 'R|step*dA|units=A   curech(~nrho_ecrf)'
    
    iterdb['curech_src'] = {}
    iterdb['curech_src']['data'] = None
    iterdb['curech_src']['units'] = 'A'
    iterdb['curech_src']['section'] = 'STATE_PROFILES'
    iterdb['curech_src']['long_name'] = 'ECH current drive (by antenna)'
    iterdb['curech_src']['component'] = 'EC'
    iterdb['curech_src']['specification'] = 'R|step*dA|units=A   curech_src(~nrho_ecrf,necrf_src)'
    
    iterdb['curfusn'] = {}
    iterdb['curfusn']['data'] = None
    iterdb['curfusn']['units'] = 'A'
    iterdb['curfusn']['section'] = 'STATE_PROFILES'
    iterdb['curfusn']['long_name'] = 'fusion ion driven current (shielded)'
    iterdb['curfusn']['component'] = 'FUS'
    iterdb['curfusn']['specification'] = 'R|step*dA|units=A   curfusn(~nrho_fus)'
    
    iterdb['curr_bootstrap'] = {}
    iterdb['curr_bootstrap']['data'] = None
    iterdb['curr_bootstrap']['units'] = 'A'
    iterdb['curr_bootstrap']['section'] = 'STATE_PROFILES'
    iterdb['curr_bootstrap']['long_name'] = 'Neoclassical bootstrap current'
    iterdb['curr_bootstrap']['component'] = 'PLASMA'
    iterdb['curr_bootstrap']['specification'] = 'R|units=A|step*dA   curr_bootstrap(~nrho)'
    
    iterdb['curr_ohmic'] = {}
    iterdb['curr_ohmic']['data'] = None
    iterdb['curr_ohmic']['units'] = 'A'
    iterdb['curr_ohmic']['section'] = 'STATE_PROFILES'
    iterdb['curr_ohmic']['long_name'] = 'Ohmic current'
    iterdb['curr_ohmic']['component'] = 'PLASMA'
    iterdb['curr_ohmic']['specification'] = 'R|units=A|step*dA   curr_ohmic(~nrho)'
    
    iterdb['curt'] = {}
    iterdb['curt']['data'] = None
    iterdb['curt']['units'] = 'A'
    iterdb['curt']['section'] = 'STATE_PROFILES'
    iterdb['curt']['long_name'] = 'total enclosed toroidal current'
    iterdb['curt']['component'] = 'EQ'
    iterdb['curt']['specification'] = 'R|units=A|Spline_00   curt(nrho_eq)'
    
    iterdb['CUR_Data_Info'] = {}
    iterdb['CUR_Data_Info']['data'] = None
    iterdb['CUR_Data_Info']['units'] = None
    iterdb['CUR_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['CUR_Data_Info']['long_name'] = 'information on source of plasma current data'
    iterdb['CUR_Data_Info']['component'] = 'PLASMA'
    iterdb['CUR_Data_Info']['specification'] = 'C*80   CUR_Data_Info'
    
    iterdb['d2R_geo_dRHOdTH'] = {}
    iterdb['d2R_geo_dRHOdTH']['data'] = None
    iterdb['d2R_geo_dRHOdTH']['units'] = 'm/-/rad'
    iterdb['d2R_geo_dRHOdTH']['section'] = 'STATE_PROFILES'
    iterdb['d2R_geo_dRHOdTH']['long_name'] = 'flux surfaces R(rho,theta)'
    iterdb['d2R_geo_dRHOdTH']['component'] = 'EQ'
    iterdb['d2R_geo_dRHOdTH']['specification'] = 'R|units=m|Hermite_explicit R_geo(nrho_eq,nth_eq)'
    
    iterdb['d2Z_geo_dRHOdTH'] = {}
    iterdb['d2Z_geo_dRHOdTH']['data'] = None
    iterdb['d2Z_geo_dRHOdTH']['units'] = 'm/-/rad'
    iterdb['d2Z_geo_dRHOdTH']['section'] = 'STATE_PROFILES'
    iterdb['d2Z_geo_dRHOdTH']['long_name'] = 'flux surfaces Z(rho,theta)'
    iterdb['d2Z_geo_dRHOdTH']['component'] = 'EQ'
    iterdb['d2Z_geo_dRHOdTH']['specification'] = 'R|units=m|Hermite_explicit Z_geo(nrho_eq,nth_eq)'
    
    iterdb['difb_fusi'] = {}
    iterdb['difb_fusi']['data'] = None
    iterdb['difb_fusi']['units'] = 'm^2/sec'
    iterdb['difb_fusi']['section'] = 'STATE_PROFILES'
    iterdb['difb_fusi']['long_name'] = 'fusion ion anomalous diffusivity'
    iterdb['difb_fusi']['component'] = 'ANOM'
    iterdb['difb_fusi']['specification'] = 'R|pclin  difb_fusi(nrho_anom)'
    
    iterdb['difb_nbi'] = {}
    iterdb['difb_nbi']['data'] = None
    iterdb['difb_nbi']['units'] = 'm^2/sec'
    iterdb['difb_nbi']['section'] = 'STATE_PROFILES'
    iterdb['difb_nbi']['long_name'] = 'beam ion anomalous diffusivity'
    iterdb['difb_nbi']['component'] = 'ANOM'
    iterdb['difb_nbi']['specification'] = 'R|pclin  difb_nbi(nrho_anom)'
    
    iterdb['difb_rfmi'] = {}
    iterdb['difb_rfmi']['data'] = None
    iterdb['difb_rfmi']['units'] = 'm^2/sec'
    iterdb['difb_rfmi']['section'] = 'STATE_PROFILES'
    iterdb['difb_rfmi']['long_name'] = 'RF minority ion anomalous diffusivity'
    iterdb['difb_rfmi']['component'] = 'ANOM'
    iterdb['difb_rfmi']['specification'] = 'R|pclin  difb_rfmi(nrho_anom)'
    
    iterdb['diff_trans'] = {}
    iterdb['diff_trans']['data'] = None
    iterdb['diff_trans']['units'] = 'm^2/sec'
    iterdb['diff_trans']['section'] = 'STATE_PROFILES'
    iterdb['diff_trans']['long_name'] = 'specie ptcl diffusivity'
    iterdb['diff_trans']['component'] = 'PLASMA'
    iterdb['diff_trans']['specification'] = 'R|units=m^2/sec|pclin diff_trans(nrho,0:nspec_th)'
    
    iterdb['dist_fun'] = {}
    iterdb['dist_fun']['data'] = None
    iterdb['dist_fun']['units'] = None
    iterdb['dist_fun']['section'] = 'STATE_DATA'
    iterdb['dist_fun']['long_name'] = 'distribution function filenames'
    iterdb['dist_fun']['component'] = 'IC'
    iterdb['dist_fun']['specification'] = 'F  dist_fun(0:nspec_alla)'
    
    iterdb['dn0out'] = {}
    iterdb['dn0out']['data'] = None
    iterdb['dn0out']['units'] = 'm^-3'
    iterdb['dn0out']['section'] = 'STATE_DATA'
    iterdb['dn0out']['long_name'] = 'Hydrogenic neutral density in scrape off region'
    iterdb['dn0out']['component'] = 'GAS'
    iterdb['dn0out']['specification'] = 'R|units=m^-3  dn0out'
    
    iterdb['dR0_momeq_dRHO'] = {}
    iterdb['dR0_momeq_dRHO']['data'] = None
    iterdb['dR0_momeq_dRHO']['units'] = 'm/-'
    iterdb['dR0_momeq_dRHO']['section'] = 'STATE_PROFILES'
    iterdb['dR0_momeq_dRHO']['long_name'] = 'R0 of flux surface'
    iterdb['dR0_momeq_dRHO']['component'] = 'EQ'
    iterdb['dR0_momeq_dRHO']['specification'] = 'R|units=m|Hermite_explicit  R0_momeq(nrho_eq)'
    
    iterdb['dR_geo_dRHO'] = {}
    iterdb['dR_geo_dRHO']['data'] = None
    iterdb['dR_geo_dRHO']['units'] = 'm/-'
    iterdb['dR_geo_dRHO']['section'] = 'STATE_PROFILES'
    iterdb['dR_geo_dRHO']['long_name'] = 'flux surfaces R(rho,theta)'
    iterdb['dR_geo_dRHO']['component'] = 'EQ'
    iterdb['dR_geo_dRHO']['specification'] = 'R|units=m|Hermite_explicit R_geo(nrho_eq,nth_eq)'
    
    iterdb['dR_geo_dTH'] = {}
    iterdb['dR_geo_dTH']['data'] = None
    iterdb['dR_geo_dTH']['units'] = 'm/rad'
    iterdb['dR_geo_dTH']['section'] = 'STATE_PROFILES'
    iterdb['dR_geo_dTH']['long_name'] = 'flux surfaces R(rho,theta)'
    iterdb['dR_geo_dTH']['component'] = 'EQ'
    iterdb['dR_geo_dTH']['specification'] = 'R|units=m|Hermite_explicit R_geo(nrho_eq,nth_eq)'
    
    iterdb['dxRjcos_momeq_dRHO'] = {}
    iterdb['dxRjcos_momeq_dRHO']['data'] = None
    iterdb['dxRjcos_momeq_dRHO']['units'] = 'm/-'
    iterdb['dxRjcos_momeq_dRHO']['section'] = 'STATE_PROFILES'
    iterdb['dxRjcos_momeq_dRHO']['long_name'] = 'scaled R cos moments'
    iterdb['dxRjcos_momeq_dRHO']['component'] = 'EQ'
    iterdb['dxRjcos_momeq_dRHO']['specification'] = 'R|units=m|Hermite_explicit  xRjcos_momeq(nrho_eq,neqmom)'
    
    iterdb['dxRjsin_momeq_dRHO'] = {}
    iterdb['dxRjsin_momeq_dRHO']['data'] = None
    iterdb['dxRjsin_momeq_dRHO']['units'] = 'm/-'
    iterdb['dxRjsin_momeq_dRHO']['section'] = 'STATE_PROFILES'
    iterdb['dxRjsin_momeq_dRHO']['long_name'] = 'scaled R sin moments'
    iterdb['dxRjsin_momeq_dRHO']['component'] = 'EQ'
    iterdb['dxRjsin_momeq_dRHO']['specification'] = 'R|units=m|Hermite_explicit  xRjsin_momeq(nrho_eq,neqmom)'
    
    iterdb['dxZjcos_momeq_dRHO'] = {}
    iterdb['dxZjcos_momeq_dRHO']['data'] = None
    iterdb['dxZjcos_momeq_dRHO']['units'] = 'm/-'
    iterdb['dxZjcos_momeq_dRHO']['section'] = 'STATE_PROFILES'
    iterdb['dxZjcos_momeq_dRHO']['long_name'] = 'scaled Z cos moments'
    iterdb['dxZjcos_momeq_dRHO']['component'] = 'EQ'
    iterdb['dxZjcos_momeq_dRHO']['specification'] = 'R|units=m|Hermite_explicit  xZjcos_momeq(nrho_eq,neqmom)'
    
    iterdb['dxZjsin_momeq_dRHO'] = {}
    iterdb['dxZjsin_momeq_dRHO']['data'] = None
    iterdb['dxZjsin_momeq_dRHO']['units'] = 'm/-'
    iterdb['dxZjsin_momeq_dRHO']['section'] = 'STATE_PROFILES'
    iterdb['dxZjsin_momeq_dRHO']['long_name'] = 'scaled Z sin moments'
    iterdb['dxZjsin_momeq_dRHO']['component'] = 'EQ'
    iterdb['dxZjsin_momeq_dRHO']['specification'] = 'R|units=m|Hermite_explicit  xZjsin_momeq(nrho_eq,neqmom)'
    
    iterdb['dZ0_momeq_dRHO'] = {}
    iterdb['dZ0_momeq_dRHO']['data'] = None
    iterdb['dZ0_momeq_dRHO']['units'] = 'm/-'
    iterdb['dZ0_momeq_dRHO']['section'] = 'STATE_PROFILES'
    iterdb['dZ0_momeq_dRHO']['long_name'] = 'Z0 of flux surface'
    iterdb['dZ0_momeq_dRHO']['component'] = 'EQ'
    iterdb['dZ0_momeq_dRHO']['specification'] = 'R|units=m|Hermite_explicit  Z0_momeq(nrho_eq)'
    
    iterdb['dZ_geo_dRHO'] = {}
    iterdb['dZ_geo_dRHO']['data'] = None
    iterdb['dZ_geo_dRHO']['units'] = 'm/-'
    iterdb['dZ_geo_dRHO']['section'] = 'STATE_PROFILES'
    iterdb['dZ_geo_dRHO']['long_name'] = 'flux surfaces Z(rho,theta)'
    iterdb['dZ_geo_dRHO']['component'] = 'EQ'
    iterdb['dZ_geo_dRHO']['specification'] = 'R|units=m|Hermite_explicit Z_geo(nrho_eq,nth_eq)'
    
    iterdb['dZ_geo_dTH'] = {}
    iterdb['dZ_geo_dTH']['data'] = None
    iterdb['dZ_geo_dTH']['units'] = 'm/rad'
    iterdb['dZ_geo_dTH']['section'] = 'STATE_PROFILES'
    iterdb['dZ_geo_dTH']['long_name'] = 'flux surfaces Z(rho,theta)'
    iterdb['dZ_geo_dTH']['component'] = 'EQ'
    iterdb['dZ_geo_dTH']['specification'] = 'R|units=m|Hermite_explicit Z_geo(nrho_eq,nth_eq)'
    
    iterdb['e0_av'] = {}
    iterdb['e0_av']['data'] = None
    iterdb['e0_av']['units'] = 'KeV'
    iterdb['e0_av']['section'] = 'STATE_DATA'
    iterdb['e0_av']['long_name'] = 'average energy of neutral sources, "(3/2)*T0"'
    iterdb['e0_av']['component'] = 'GAS'
    iterdb['e0_av']['specification'] = 'R|units=KeV   e0_av(ngsc0)'
    
    iterdb['ecrf_src_name'] = {}
    iterdb['ecrf_src_name']['data'] = None
    iterdb['ecrf_src_name']['units'] = None
    iterdb['ecrf_src_name']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['ecrf_src_name']['long_name'] = 'number & name of ECRF sources'
    iterdb['ecrf_src_name']['component'] = 'EC'
    iterdb['ecrf_src_name']['specification'] = 'L|ecrf_source   ecrf_src_name(necrf_src)'
    
    iterdb['EC_Beam_Elongation'] = {}
    iterdb['EC_Beam_Elongation']['data'] = None
    iterdb['EC_Beam_Elongation']['units'] = None
    iterdb['EC_Beam_Elongation']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['EC_Beam_Elongation']['long_name'] = 'EC beam ellipticity'
    iterdb['EC_Beam_Elongation']['component'] = 'EC'
    iterdb['EC_Beam_Elongation']['specification'] = 'R|units=-   EC_Beam_Elongation(necrf_src)'
    
    iterdb['EC_Code_Info'] = {}
    iterdb['EC_Code_Info']['data'] = None
    iterdb['EC_Code_Info']['units'] = None
    iterdb['EC_Code_Info']['section'] = 'SIMULATION_INIT'
    iterdb['EC_Code_Info']['long_name'] = 'Information: code implementing EC component'
    iterdb['EC_Code_Info']['component'] = 'EC'
    iterdb['EC_Code_Info']['specification'] = 'C*80   EC_Code_Info'
    
    iterdb['EC_Data_Info'] = {}
    iterdb['EC_Data_Info']['data'] = None
    iterdb['EC_Data_Info']['units'] = None
    iterdb['EC_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['EC_Data_Info']['long_name'] = 'information on source of ECRF power data'
    iterdb['EC_Data_Info']['component'] = 'EC'
    iterdb['EC_Data_Info']['specification'] = 'C*80   EC_Data_Info'
    
    iterdb['EC_Half_Power_Angle'] = {}
    iterdb['EC_Half_Power_Angle']['data'] = None
    iterdb['EC_Half_Power_Angle']['units'] = 'degrees'
    iterdb['EC_Half_Power_Angle']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['EC_Half_Power_Angle']['long_name'] = 'Divergence of EC beam'
    iterdb['EC_Half_Power_Angle']['component'] = 'EC'
    iterdb['EC_Half_Power_Angle']['specification'] = 'R|units=degrees  EC_Half_Power_Angle(necrf_src)'
    
    iterdb['EC_Omode_Fraction'] = {}
    iterdb['EC_Omode_Fraction']['data'] = None
    iterdb['EC_Omode_Fraction']['units'] = None
    iterdb['EC_Omode_Fraction']['section'] = 'SHOT_CONFIGURATION'
    iterdb['EC_Omode_Fraction']['long_name'] = 'O-mode fraction of EC source'
    iterdb['EC_Omode_Fraction']['component'] = 'EC'
    iterdb['EC_Omode_Fraction']['specification'] = 'R|units=-   EC_Omode_Fraction(necrf_src)'
    
    iterdb['EC_phi_aim'] = {}
    iterdb['EC_phi_aim']['data'] = None
    iterdb['EC_phi_aim']['units'] = 'degrees'
    iterdb['EC_phi_aim']['section'] = 'SHOT_CONFIGURATION'
    iterdb['EC_phi_aim']['long_name'] = 'toroidal aiming angle'
    iterdb['EC_phi_aim']['component'] = 'EC'
    iterdb['EC_phi_aim']['specification'] = 'R|units=degrees  EC_phi_aim(necrf_src)'
    
    iterdb['EC_theta_aim'] = {}
    iterdb['EC_theta_aim']['data'] = None
    iterdb['EC_theta_aim']['units'] = 'degrees'
    iterdb['EC_theta_aim']['section'] = 'SHOT_CONFIGURATION'
    iterdb['EC_theta_aim']['long_name'] = 'poloidal aiming angle'
    iterdb['EC_theta_aim']['component'] = 'EC'
    iterdb['EC_theta_aim']['specification'] = 'R|units=degrees  EC_theta_aim(necrf_src)'
    
    iterdb['Einj_max'] = {}
    iterdb['Einj_max']['data'] = None
    iterdb['Einj_max']['units'] = 'keV'
    iterdb['Einj_max']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['Einj_max']['long_name'] = 'maximum injection energy'
    iterdb['Einj_max']['component'] = 'NBI'
    iterdb['Einj_max']['specification'] = 'R|units=keV       Einj_max(nbeam)'
    
    iterdb['Einj_min'] = {}
    iterdb['Einj_min']['data'] = None
    iterdb['Einj_min']['units'] = 'keV'
    iterdb['Einj_min']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['Einj_min']['long_name'] = 'minimum injection energy'
    iterdb['Einj_min']['component'] = 'NBI'
    iterdb['Einj_min']['specification'] = 'R|units=keV       Einj_min(nbeam)'
    
    iterdb['eldot'] = {}
    iterdb['eldot']['data'] = None
    iterdb['eldot']['units'] = '1/sec'
    iterdb['eldot']['section'] = 'STATE_DATA'
    iterdb['eldot']['long_name'] = '[d(Philim)/dt]/[2*Philim]'
    iterdb['eldot']['component'] = 'PLASMA'
    iterdb['eldot']['specification'] = 'R|units=1/sec  eldot'
    
    iterdb['elong'] = {}
    iterdb['elong']['data'] = None
    iterdb['elong']['units'] = None
    iterdb['elong']['section'] = 'STATE_PROFILES'
    iterdb['elong']['long_name'] = 'elongation (b/a)'
    iterdb['elong']['component'] = 'EQ'
    iterdb['elong']['specification'] = 'R|pclin  elong(nrho_eq_geo)'
    
    iterdb['eperp_beami'] = {}
    iterdb['eperp_beami']['data'] = None
    iterdb['eperp_beami']['units'] = 'keV'
    iterdb['eperp_beami']['section'] = 'STATE_PROFILES'
    iterdb['eperp_beami']['long_name'] = 'beam species <Eperp>, lab frame'
    iterdb['eperp_beami']['component'] = 'NBI'
    iterdb['eperp_beami']['specification'] = 'R|units=keV|alias=eperp_|step*nbeami eperp_beami(~nrho_nbi,nspec_beam)'
    
    iterdb['eperp_fusi'] = {}
    iterdb['eperp_fusi']['data'] = None
    iterdb['eperp_fusi']['units'] = 'keV'
    iterdb['eperp_fusi']['section'] = 'STATE_PROFILES'
    iterdb['eperp_fusi']['long_name'] = 'fusion ion <Eperp>, lab frame'
    iterdb['eperp_fusi']['component'] = 'FUS'
    iterdb['eperp_fusi']['specification'] = 'R|units=keV|alias=eperp_|step*nfusi eperp_fusi(~nrho_fus,nspec_fusion)'
    
    iterdb['epll_beami'] = {}
    iterdb['epll_beami']['data'] = None
    iterdb['epll_beami']['units'] = 'keV'
    iterdb['epll_beami']['section'] = 'STATE_PROFILES'
    iterdb['epll_beami']['long_name'] = 'beam species <Epll>, lab frame'
    iterdb['epll_beami']['component'] = 'NBI'
    iterdb['epll_beami']['specification'] = 'R|units=keV|alias=epll_|step*nbeami  epll_beami(~nrho_nbi,nspec_beam)'
    
    iterdb['epll_fusi'] = {}
    iterdb['epll_fusi']['data'] = None
    iterdb['epll_fusi']['units'] = 'keV'
    iterdb['epll_fusi']['section'] = 'STATE_PROFILES'
    iterdb['epll_fusi']['long_name'] = 'fusion ion <Epll>, lab frame'
    iterdb['epll_fusi']['component'] = 'FUS'
    iterdb['epll_fusi']['specification'] = 'R|units=keV|alias=epll_|step*nfusi  epll_fusi(~nrho_fus,nspec_fusion)'
    
    iterdb['Epot'] = {}
    iterdb['Epot']['data'] = None
    iterdb['Epot']['units'] = 'keV'
    iterdb['Epot']['section'] = 'STATE_PROFILES'
    iterdb['Epot']['long_name'] = 'radial electrostatic potential'
    iterdb['Epot']['component'] = 'PLASMA'
    iterdb['Epot']['specification'] = 'R|units=keV|pclin  Epot(nrho)'
    
    iterdb['eqdsk_file'] = {}
    iterdb['eqdsk_file']['data'] = None
    iterdb['eqdsk_file']['units'] = None
    iterdb['eqdsk_file']['section'] = 'STATE_DATA'
    iterdb['eqdsk_file']['long_name'] = 'EFIT G-eqdsk file: psi(R,Z), g(psi), etc.'
    iterdb['eqdsk_file']['component'] = 'EQ'
    iterdb['eqdsk_file']['specification'] = 'F  eqdsk_file'
    
    iterdb['eqmom_num'] = {}
    iterdb['eqmom_num']['data'] = None
    iterdb['eqmom_num']['units'] = None
    iterdb['eqmom_num']['section'] = 'SIMULATION_INIT'
    iterdb['eqmom_num']['long_name'] = 'Equilibrium moments'
    iterdb['eqmom_num']['component'] = 'EQ'
    iterdb['eqmom_num']['specification'] = 'L|EQ_moments  eqmom_num(neqmom)'
    
    iterdb['EQ_Code_Info'] = {}
    iterdb['EQ_Code_Info']['data'] = None
    iterdb['EQ_Code_Info']['units'] = None
    iterdb['EQ_Code_Info']['section'] = 'SIMULATION_INIT'
    iterdb['EQ_Code_Info']['long_name'] = 'Information: code implementing EQ component'
    iterdb['EQ_Code_Info']['component'] = 'EQ'
    iterdb['EQ_Code_Info']['specification'] = 'C*80   EQ_Code_Info'
    
    iterdb['EQ_Data_Info'] = {}
    iterdb['EQ_Data_Info']['data'] = None
    iterdb['EQ_Data_Info']['units'] = None
    iterdb['EQ_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['EQ_Data_Info']['long_name'] = 'Information: source of EQ input data'
    iterdb['EQ_Data_Info']['component'] = 'EQ'
    iterdb['EQ_Data_Info']['specification'] = 'C*80   EQ_Data_Info'
    
    iterdb['eta_parallel'] = {}
    iterdb['eta_parallel']['data'] = None
    iterdb['eta_parallel']['units'] = 'ohm*m'
    iterdb['eta_parallel']['section'] = 'STATE_PROFILES'
    iterdb['eta_parallel']['long_name'] = 'parallel electrical resistivity'
    iterdb['eta_parallel']['component'] = 'PLASMA'
    iterdb['eta_parallel']['specification'] = 'R|units=ohm*m|Hermite eta_parallel(nrho)'
    
    iterdb['Fi_depletion'] = {}
    iterdb['Fi_depletion']['data'] = None
    iterdb['Fi_depletion']['units'] = None
    iterdb['Fi_depletion']['section'] = 'STATE_PROFILES'
    iterdb['Fi_depletion']['long_name'] = 'fast ion depletion: sum[nj*Zj/ne]'
    iterdb['Fi_depletion']['component'] = 'PLASMA'
    iterdb['Fi_depletion']['specification'] = 'R|units=-|step*ns(:,ps_elec_index) Fi_depletion(~nrho)'
    
    iterdb['frac_full'] = {}
    iterdb['frac_full']['data'] = None
    iterdb['frac_full']['units'] = None
    iterdb['frac_full']['section'] = 'STATE_DATA'
    iterdb['frac_full']['long_name'] = 'fraction of beam current at full voltage'
    iterdb['frac_full']['component'] = 'NBI'
    iterdb['frac_full']['specification'] = 'R|units=-  frac_full(nbeam)'
    
    iterdb['frac_half'] = {}
    iterdb['frac_half']['data'] = None
    iterdb['frac_half']['units'] = None
    iterdb['frac_half']['section'] = 'STATE_DATA'
    iterdb['frac_half']['long_name'] = 'fraction of beam current at half voltage'
    iterdb['frac_half']['component'] = 'NBI'
    iterdb['frac_half']['specification'] = 'R|units=-  frac_half(nbeam)'
    
    iterdb['freq_ec'] = {}
    iterdb['freq_ec']['data'] = None
    iterdb['freq_ec']['units'] = 'Hz'
    iterdb['freq_ec']['section'] = 'SHOT_CONFIGURATION'
    iterdb['freq_ec']['long_name'] = 'frequency of EC source'
    iterdb['freq_ec']['component'] = 'EC'
    iterdb['freq_ec']['specification'] = 'R|units=Hz freq_ec(necrf_src)'
    
    iterdb['FUS_Code_Info'] = {}
    iterdb['FUS_Code_Info']['data'] = None
    iterdb['FUS_Code_Info']['units'] = None
    iterdb['FUS_Code_Info']['section'] = 'SIMULATION_INIT'
    iterdb['FUS_Code_Info']['long_name'] = 'Information: code implementing FUS component'
    iterdb['FUS_Code_Info']['component'] = 'FUS'
    iterdb['FUS_Code_Info']['specification'] = 'C*80   FUS_Code_Info'
    
    iterdb['gamma_nc'] = {}
    iterdb['gamma_nc']['data'] = None
    iterdb['gamma_nc']['units'] = 'm^-1'
    iterdb['gamma_nc']['section'] = 'STATE_PROFILES'
    iterdb['gamma_nc']['long_name'] = 'NC gamma'
    iterdb['gamma_nc']['component'] = 'EQ'
    iterdb['gamma_nc']['specification'] = 'R|units=m^-1|pclin   gamma_nc(nrho_eq_geo)'
    
    iterdb['gas_atom'] = {}
    iterdb['gas_atom']['data'] = None
    iterdb['gas_atom']['units'] = None
    iterdb['gas_atom']['section'] = 'SHOT_CONFIGURATION'
    iterdb['gas_atom']['long_name'] = 'name of species introduced by each gas source'
    iterdb['gas_atom']['component'] = 'GAS'
    iterdb['gas_atom']['specification'] = 'N  gas_atom(ngsc0)'
    
    iterdb['GAS_Code_Info'] = {}
    iterdb['GAS_Code_Info']['data'] = None
    iterdb['GAS_Code_Info']['units'] = None
    iterdb['GAS_Code_Info']['section'] = 'SIMULATION_INIT'
    iterdb['GAS_Code_Info']['long_name'] = 'Information: code implementing GAS component'
    iterdb['GAS_Code_Info']['component'] = 'GAS'
    iterdb['GAS_Code_Info']['specification'] = 'C*80   GAS_Code_Info'
    
    iterdb['gb1'] = {}
    iterdb['gb1']['data'] = None
    iterdb['gb1']['units'] = 'T'
    iterdb['gb1']['section'] = 'STATE_PROFILES'
    iterdb['gb1']['long_name'] = '<|B|>'
    iterdb['gb1']['component'] = 'EQ'
    iterdb['gb1']['specification'] = 'R|units=T|pclin      gb1(nrho_eq_geo)'
    
    iterdb['gb2'] = {}
    iterdb['gb2']['data'] = None
    iterdb['gb2']['units'] = 'T^2'
    iterdb['gb2']['section'] = 'STATE_PROFILES'
    iterdb['gb2']['long_name'] = '<B^2>'
    iterdb['gb2']['component'] = 'EQ'
    iterdb['gb2']['specification'] = 'R|units=T^2|pclin    gb2(nrho_eq_geo)'
    
    iterdb['gb2i'] = {}
    iterdb['gb2i']['data'] = None
    iterdb['gb2i']['units'] = 'T^-2'
    iterdb['gb2i']['section'] = 'STATE_PROFILES'
    iterdb['gb2i']['long_name'] = '<1/B^2>'
    iterdb['gb2i']['component'] = 'EQ'
    iterdb['gb2i']['specification'] = 'R|units=T^-2|pclin   gb2i(nrho_eq_geo)'
    
    iterdb['gbr2'] = {}
    iterdb['gbr2']['data'] = None
    iterdb['gbr2']['units'] = 'T*m^2'
    iterdb['gbr2']['section'] = 'STATE_PROFILES'
    iterdb['gbr2']['long_name'] = '<|B|*R^2>'
    iterdb['gbr2']['component'] = 'EQ'
    iterdb['gbr2']['specification'] = 'R|units=T*m^2|pclin  gbr2(nrho_eq_geo)'
    
    iterdb['geometry'] = {}
    iterdb['geometry']['data'] = None
    iterdb['geometry']['units'] = None
    iterdb['geometry']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['geometry']['long_name'] = 'path to file(s) vac. vessel & coil descr.'
    iterdb['geometry']['component'] = 'EQ'
    iterdb['geometry']['specification'] = 'F  geometry'
    
    iterdb['Global_label'] = {}
    iterdb['Global_label']['data'] = None
    iterdb['Global_label']['units'] = None
    iterdb['Global_label']['section'] = 'SIMULATION_INIT'
    iterdb['Global_label']['long_name'] = 'Run Label'
    iterdb['Global_label']['component'] = 'PLASMA'
    iterdb['Global_label']['specification'] = 'C*80   Global_label'
    
    iterdb['gncfb2h'] = {}
    iterdb['gncfb2h']['data'] = None
    iterdb['gncfb2h']['units'] = 'T^-2'
    iterdb['gncfb2h']['section'] = 'STATE_PROFILES'
    iterdb['gncfb2h']['long_name'] = '<(B^-2)*((1-H)^0.5-(1/3)*(1-H)^1.5)>; H=B/Bmax'
    iterdb['gncfb2h']['component'] = 'EQ'
    iterdb['gncfb2h']['specification'] = 'R|units=T^-2|pclin  gncfb2h(nrho_eq_geo)'
    
    iterdb['gncfh'] = {}
    iterdb['gncfh']['data'] = None
    iterdb['gncfh']['units'] = None
    iterdb['gncfh']['section'] = 'STATE_PROFILES'
    iterdb['gncfh']['long_name'] = '<H^-2*(1-SQRT(1-H)*(1+H/2))>; H=B/Bmax'
    iterdb['gncfh']['component'] = 'EQ'
    iterdb['gncfh']['specification'] = 'R|units=-|pclin  gncfh(nrho_eq_geo)'
    
    iterdb['gr1'] = {}
    iterdb['gr1']['data'] = None
    iterdb['gr1']['units'] = 'm'
    iterdb['gr1']['section'] = 'STATE_PROFILES'
    iterdb['gr1']['long_name'] = '<R>'
    iterdb['gr1']['component'] = 'EQ'
    iterdb['gr1']['specification'] = 'R|units=m|pclin   gr1(nrho_eq_geo)'
    
    iterdb['gr2'] = {}
    iterdb['gr2']['data'] = None
    iterdb['gr2']['units'] = 'm^2'
    iterdb['gr2']['section'] = 'STATE_PROFILES'
    iterdb['gr2']['long_name'] = '<R^2>'
    iterdb['gr2']['component'] = 'EQ'
    iterdb['gr2']['specification'] = 'R|units=m^2|pclin gr2(nrho_eq_geo)'
    
    iterdb['gr2i'] = {}
    iterdb['gr2i']['data'] = None
    iterdb['gr2i']['units'] = 'm^-2'
    iterdb['gr2i']['section'] = 'STATE_PROFILES'
    iterdb['gr2i']['long_name'] = '<R^-2>'
    iterdb['gr2i']['component'] = 'EQ'
    iterdb['gr2i']['specification'] = 'R|units=m^-2|pclin gr2i(nrho_eq_geo)'
    
    iterdb['gr2rho2'] = {}
    iterdb['gr2rho2']['data'] = None
    iterdb['gr2rho2']['units'] = None
    iterdb['gr2rho2']['section'] = 'STATE_PROFILES'
    iterdb['gr2rho2']['long_name'] = '<R^2*|grad(rho)|^2>'
    iterdb['gr2rho2']['component'] = 'EQ'
    iterdb['gr2rho2']['specification'] = 'R|units=-|pclin gr2rho2(nrho_eq_geo)'
    
    iterdb['gr3i'] = {}
    iterdb['gr3i']['data'] = None
    iterdb['gr3i']['units'] = 'm^-3'
    iterdb['gr3i']['section'] = 'STATE_PROFILES'
    iterdb['gr3i']['long_name'] = '<R^-3>'
    iterdb['gr3i']['component'] = 'EQ'
    iterdb['gr3i']['specification'] = 'R|units=m^-3|pclin gr3i(nrho_eq_geo)'
    
    iterdb['grho1'] = {}
    iterdb['grho1']['data'] = None
    iterdb['grho1']['units'] = 'm^-1'
    iterdb['grho1']['section'] = 'STATE_PROFILES'
    iterdb['grho1']['long_name'] = '<|grad(rho)|>'
    iterdb['grho1']['component'] = 'EQ'
    iterdb['grho1']['specification'] = 'R|units=m^-1|pclin grho1(nrho_eq_geo)'
    
    iterdb['grho2'] = {}
    iterdb['grho2']['data'] = None
    iterdb['grho2']['units'] = 'm^-2'
    iterdb['grho2']['section'] = 'STATE_PROFILES'
    iterdb['grho2']['long_name'] = '<|grad(rho)|^2>'
    iterdb['grho2']['component'] = 'EQ'
    iterdb['grho2']['specification'] = 'R|units=m^-2|pclin grho2(nrho_eq_geo)'
    
    iterdb['grho2b2i'] = {}
    iterdb['grho2b2i']['data'] = None
    iterdb['grho2b2i']['units'] = 'T^-2*m^-2'
    iterdb['grho2b2i']['section'] = 'STATE_PROFILES'
    iterdb['grho2b2i']['long_name'] = '<|grad(rho)|^2/B^2>'
    iterdb['grho2b2i']['component'] = 'EQ'
    iterdb['grho2b2i']['specification'] = 'R|units=T^-2*m^-2|pclin grho2b2i(nrho_eq_geo)'
    
    iterdb['grho2r2i'] = {}
    iterdb['grho2r2i']['data'] = None
    iterdb['grho2r2i']['units'] = 'm^-4'
    iterdb['grho2r2i']['section'] = 'STATE_PROFILES'
    iterdb['grho2r2i']['long_name'] = '<|grad(rho)|^2/R^2>'
    iterdb['grho2r2i']['component'] = 'EQ'
    iterdb['grho2r2i']['specification'] = 'R|units=m^-4|pclin grho2r2i(nrho_eq_geo)'
    
    iterdb['grho2r3i'] = {}
    iterdb['grho2r3i']['data'] = None
    iterdb['grho2r3i']['units'] = 'm^-5'
    iterdb['grho2r3i']['section'] = 'STATE_PROFILES'
    iterdb['grho2r3i']['long_name'] = '<|grad(rho)|^2/R^3>'
    iterdb['grho2r3i']['component'] = 'EQ'
    iterdb['grho2r3i']['specification'] = 'R|units=m^-5|pclin grho2r3i(nrho_eq_geo)'
    
    iterdb['gri'] = {}
    iterdb['gri']['data'] = None
    iterdb['gri']['units'] = 'm^-2'
    iterdb['gri']['section'] = 'STATE_PROFILES'
    iterdb['gri']['long_name'] = '<1/R>'
    iterdb['gri']['component'] = 'EQ'
    iterdb['gri']['specification'] = 'R|units=m^-2|pclin gri(nrho_eq_geo)'
    
    iterdb['grirhoi'] = {}
    iterdb['grirhoi']['data'] = None
    iterdb['grirhoi']['units'] = None
    iterdb['grirhoi']['section'] = 'STATE_PROFILES'
    iterdb['grirhoi']['long_name'] = '<1/(R*|grad(rho)|)>'
    iterdb['grirhoi']['component'] = 'EQ'
    iterdb['grirhoi']['specification'] = 'R|units=-|pclin grirhoi(nrho_eq_geo)'
    
    iterdb['gs_name'] = {}
    iterdb['gs_name']['data'] = None
    iterdb['gs_name']['units'] = None
    iterdb['gs_name']['section'] = 'SHOT_CONFIGURATION'
    iterdb['gs_name']['long_name'] = 'number & name of edge neutral gas sources'
    iterdb['gs_name']['component'] = 'GAS'
    iterdb['gs_name']['specification'] = 'L|gas_source    gs_name(ngsc0)'
    
    iterdb['g_eq'] = {}
    iterdb['g_eq']['data'] = None
    iterdb['g_eq']['units'] = 'T*m'
    iterdb['g_eq']['section'] = 'STATE_PROFILES'
    iterdb['g_eq']['long_name'] = 'equilibrium R*|B_phi|'
    iterdb['g_eq']['component'] = 'EQ'
    iterdb['g_eq']['specification'] = 'R|units=T*m|Spline_00      g_eq(nrho_eq)'
    
    iterdb['IC_Code_Info'] = {}
    iterdb['IC_Code_Info']['data'] = None
    iterdb['IC_Code_Info']['units'] = None
    iterdb['IC_Code_Info']['section'] = 'SIMULATION_INIT'
    iterdb['IC_Code_Info']['long_name'] = 'Information: code implementing IC component'
    iterdb['IC_Code_Info']['component'] = 'IC'
    iterdb['IC_Code_Info']['specification'] = 'C*80   IC_Code_Info'
    
    iterdb['IC_Data_Info'] = {}
    iterdb['IC_Data_Info']['data'] = None
    iterdb['IC_Data_Info']['units'] = None
    iterdb['IC_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['IC_Data_Info']['long_name'] = 'information on source of ICRF power data'
    iterdb['IC_Data_Info']['component'] = 'IC'
    iterdb['IC_Data_Info']['specification'] = 'C*80   IC_Data_Info'
    
    iterdb['iota'] = {}
    iterdb['iota']['data'] = None
    iterdb['iota']['units'] = None
    iterdb['iota']['section'] = 'STATE_PROFILES'
    iterdb['iota']['long_name'] = 'iota profile (1/q)'
    iterdb['iota']['component'] = 'PLASMA'
    iterdb['iota']['specification'] = 'R|units=-|Spline_00  iota(nrho)'
    
    iterdb['is_recycling'] = {}
    iterdb['is_recycling']['data'] = None
    iterdb['is_recycling']['units'] = None
    iterdb['is_recycling']['section'] = 'SHOT_CONFIGURATION'
    iterdb['is_recycling']['long_name'] = '0/1; =1 to for recycling sources'
    iterdb['is_recycling']['component'] = 'GAS'
    iterdb['is_recycling']['specification'] = 'I  is_recycling(ngsc0)'
    
    iterdb['jdotb'] = {}
    iterdb['jdotb']['data'] = None
    iterdb['jdotb']['units'] = 'A*T/m^2'
    iterdb['jdotb']['section'] = 'STATE_PROFILES'
    iterdb['jdotb']['long_name'] = '<J.B>'
    iterdb['jdotb']['component'] = 'EQ'
    iterdb['jdotb']['specification'] = 'R|units=A*T/m^2|Hermite_00     jdotb(nrho_eq)'
    
    iterdb['kccw_Bphi'] = {}
    iterdb['kccw_Bphi']['data'] = None
    iterdb['kccw_Bphi']['units'] = None
    iterdb['kccw_Bphi']['section'] = 'SHOT_CONFIGURATION'
    iterdb['kccw_Bphi']['long_name'] = 'B_phi orientation: +1 means CCW viewed from above'
    iterdb['kccw_Bphi']['component'] = 'EQ'
    iterdb['kccw_Bphi']['specification'] = 'I  kccw_Bphi = 0'
    
    iterdb['kccw_Jphi'] = {}
    iterdb['kccw_Jphi']['data'] = None
    iterdb['kccw_Jphi']['units'] = None
    iterdb['kccw_Jphi']['section'] = 'SHOT_CONFIGURATION'
    iterdb['kccw_Jphi']['long_name'] = 'J_phi orientation: +1 means CCW viewed from above'
    iterdb['kccw_Jphi']['component'] = 'EQ'
    iterdb['kccw_Jphi']['specification'] = 'I  kccw_Jphi = 0'
    
    iterdb['kdens_rfmin'] = {}
    iterdb['kdens_rfmin']['data'] = None
    iterdb['kdens_rfmin']['units'] = None
    iterdb['kdens_rfmin']['section'] = 'SIMULATION_INIT'
    iterdb['kdens_rfmin']['long_name'] = '= "fraction" => nmini(i) = fracmin(i)*ne'
    iterdb['kdens_rfmin']['component'] = 'IC'
    iterdb['kdens_rfmin']['specification'] = 'N  kdens_rfmin = "data"'
    
    iterdb['kvolt_nbi'] = {}
    iterdb['kvolt_nbi']['data'] = None
    iterdb['kvolt_nbi']['units'] = 'keV'
    iterdb['kvolt_nbi']['section'] = 'STATE_DATA'
    iterdb['kvolt_nbi']['long_name'] = 'energy of each beam source **keV**'
    iterdb['kvolt_nbi']['component'] = 'NBI'
    iterdb['kvolt_nbi']['specification'] = 'R|units=keV kvolt_nbi(nbeam)'
    
    iterdb['Lbscap'] = {}
    iterdb['Lbscap']['data'] = None
    iterdb['Lbscap']['units'] = 'm'
    iterdb['Lbscap']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['Lbscap']['long_name'] = 'distance, source to aperture'
    iterdb['Lbscap']['component'] = 'NBI'
    iterdb['Lbscap']['specification'] = 'R|units=m       Lbscap(nbeam)'
    
    iterdb['Lbscap2'] = {}
    iterdb['Lbscap2']['data'] = None
    iterdb['Lbscap2']['units'] = 'm'
    iterdb['Lbscap2']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['Lbscap2']['long_name'] = 'distance, source to 2nd aperture'
    iterdb['Lbscap2']['component'] = 'NBI'
    iterdb['Lbscap2']['specification'] = 'R|units=m       Lbscap2(nbeam)'
    
    iterdb['Lbsctan'] = {}
    iterdb['Lbsctan']['data'] = None
    iterdb['Lbsctan']['units'] = 'm'
    iterdb['Lbsctan']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['Lbsctan']['long_name'] = 'distance, source to tangency point'
    iterdb['Lbsctan']['component'] = 'NBI'
    iterdb['Lbsctan']['specification'] = 'R|units=m       Lbsctan(nbeam)'
    
    iterdb['LH_Code_Info'] = {}
    iterdb['LH_Code_Info']['data'] = None
    iterdb['LH_Code_Info']['units'] = None
    iterdb['LH_Code_Info']['section'] = 'SIMULATION_INIT'
    iterdb['LH_Code_Info']['long_name'] = 'Information: code implementing LH component'
    iterdb['LH_Code_Info']['component'] = 'LH'
    iterdb['LH_Code_Info']['specification'] = 'C*80   LH_Code_Info'
    
    iterdb['LH_Data_Info'] = {}
    iterdb['LH_Data_Info']['data'] = None
    iterdb['LH_Data_Info']['units'] = None
    iterdb['LH_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['LH_Data_Info']['long_name'] = 'Information on source of LHRF power data'
    iterdb['LH_Data_Info']['component'] = 'LH'
    iterdb['LH_Data_Info']['specification'] = 'C*80   LH_Data_Info'
    
    iterdb['LMHD_eq_code'] = {}
    iterdb['LMHD_eq_code']['data'] = None
    iterdb['LMHD_eq_code']['units'] = None
    iterdb['LMHD_eq_code']['section'] = 'SIMULATION_INIT'
    iterdb['LMHD_eq_code']['long_name'] = 'name of MHD equilibrium refinement code used'
    iterdb['LMHD_eq_code']['component'] = 'LMHD'
    iterdb['LMHD_eq_code']['specification'] = 'N  LMHD_eq_code'
    
    iterdb['LMHD_status'] = {}
    iterdb['LMHD_status']['data'] = None
    iterdb['LMHD_status']['units'] = None
    iterdb['LMHD_status']['section'] = 'STATE_DATA'
    iterdb['LMHD_status']['long_name'] = '0: OK; =1: at least one code error occurred.'
    iterdb['LMHD_status']['component'] = 'LMHD'
    iterdb['LMHD_status']['specification'] = 'I   LMHD_status'
    
    iterdb['lock_machine_descr'] = {}
    iterdb['lock_machine_descr']['data'] = None
    iterdb['lock_machine_descr']['units'] = None
    iterdb['lock_machine_descr']['section'] = 'STATE_DATA'
    iterdb['lock_machine_descr']['long_name'] = 'Machine_Description section lock'
    iterdb['lock_machine_descr']['component'] = 'PLASMA'
    iterdb['lock_machine_descr']['specification'] = 'I  lock_machine_descr = 0'
    
    iterdb['lock_shot_config'] = {}
    iterdb['lock_shot_config']['data'] = None
    iterdb['lock_shot_config']['units'] = None
    iterdb['lock_shot_config']['section'] = 'STATE_DATA'
    iterdb['lock_shot_config']['long_name'] = 'Shot_Configuration section lock'
    iterdb['lock_shot_config']['component'] = 'PLASMA'
    iterdb['lock_shot_config']['specification'] = 'I  lock_shot_config = 0'
    
    iterdb['lock_sim_init'] = {}
    iterdb['lock_sim_init']['data'] = None
    iterdb['lock_sim_init']['units'] = None
    iterdb['lock_sim_init']['section'] = 'STATE_DATA'
    iterdb['lock_sim_init']['long_name'] = 'Simulation_Init section lock'
    iterdb['lock_sim_init']['component'] = 'PLASMA'
    iterdb['lock_sim_init']['specification'] = 'I  lock_sim_init = 0'
    
    iterdb['Lpol'] = {}
    iterdb['Lpol']['data'] = None
    iterdb['Lpol']['units'] = 'm'
    iterdb['Lpol']['section'] = 'STATE_PROFILES'
    iterdb['Lpol']['long_name'] = 'poloidal path length'
    iterdb['Lpol']['component'] = 'EQ'
    iterdb['Lpol']['specification'] = 'R|units=m|Spline Lpol(nrho_eq)'
    
    iterdb['MHD_eq_status'] = {}
    iterdb['MHD_eq_status']['data'] = None
    iterdb['MHD_eq_status']['units'] = None
    iterdb['MHD_eq_status']['section'] = 'STATE_DATA'
    iterdb['MHD_eq_status']['long_name'] = '0: OK; =1: MHD equilibrium refinement failed'
    iterdb['MHD_eq_status']['component'] = 'LMHD'
    iterdb['MHD_eq_status']['specification'] = 'I   MHD_eq_status'
    
    iterdb['m_ALL'] = {}
    iterdb['m_ALL']['data'] = None
    iterdb['m_ALL']['units'] = 'kg'
    iterdb['m_ALL']['section'] = 'SIMULATION_INIT'
    iterdb['m_ALL']['long_name'] = 'ALL specie mass'
    iterdb['m_ALL']['component'] = 'PLASMA'
    iterdb['m_ALL']['specification'] = 'S|specie  ALL(0:nspec_all)'
    
    iterdb['m_ALLA'] = {}
    iterdb['m_ALLA']['data'] = None
    iterdb['m_ALLA']['units'] = 'kg'
    iterdb['m_ALLA']['section'] = 'SIMULATION_INIT'
    iterdb['m_ALLA']['long_name'] = 'ALLA specie mass'
    iterdb['m_ALLA']['component'] = 'PLASMA'
    iterdb['m_ALLA']['specification'] = 'S|specie  ALLA(0:nspec_alla)'
    
    iterdb['m_S'] = {}
    iterdb['m_S']['data'] = None
    iterdb['m_S']['units'] = 'kg'
    iterdb['m_S']['section'] = 'SHOT_CONFIGURATION'
    iterdb['m_S']['long_name'] = 'S specie mass'
    iterdb['m_S']['component'] = 'PLASMA'
    iterdb['m_S']['specification'] = 'S|thermal_specie  S(0:nspec_th)'
    
    iterdb['m_SA'] = {}
    iterdb['m_SA']['data'] = None
    iterdb['m_SA']['units'] = 'kg'
    iterdb['m_SA']['section'] = 'SIMULATION_INIT'
    iterdb['m_SA']['long_name'] = 'SA specie mass'
    iterdb['m_SA']['component'] = 'PLASMA'
    iterdb['m_SA']['specification'] = 'S|thermal_specie  SA(0:nspec_tha)'
    
    iterdb['m_SFUS'] = {}
    iterdb['m_SFUS']['data'] = None
    iterdb['m_SFUS']['units'] = 'kg'
    iterdb['m_SFUS']['section'] = 'SHOT_CONFIGURATION'
    iterdb['m_SFUS']['long_name'] = 'SFUS specie mass'
    iterdb['m_SFUS']['component'] = 'FUS'
    iterdb['m_SFUS']['specification'] = 'S|fusion_ion   SFUS(nspec_fusion)'
    
    iterdb['m_SGAS'] = {}
    iterdb['m_SGAS']['data'] = None
    iterdb['m_SGAS']['units'] = 'kg'
    iterdb['m_SGAS']['section'] = 'SIMULATION_INIT'
    iterdb['m_SGAS']['long_name'] = 'SGAS specie mass'
    iterdb['m_SGAS']['component'] = 'GAS'
    iterdb['m_SGAS']['specification'] = 'S|neutral_gas  SGAS(nspec_gas)'
    
    iterdb['m_SIMP0'] = {}
    iterdb['m_SIMP0']['data'] = None
    iterdb['m_SIMP0']['units'] = 'kg'
    iterdb['m_SIMP0']['section'] = 'SIMULATION_INIT'
    iterdb['m_SIMP0']['long_name'] = 'SIMP0 specie mass'
    iterdb['m_SIMP0']['component'] = 'GAS'
    iterdb['m_SIMP0']['specification'] = 'S|impurity_atoms SIMP0(nspec_imp0)'
    
    iterdb['m_SIMPI'] = {}
    iterdb['m_SIMPI']['data'] = None
    iterdb['m_SIMPI']['units'] = 'kg'
    iterdb['m_SIMPI']['section'] = 'SIMULATION_INIT'
    iterdb['m_SIMPI']['long_name'] = 'SIMPI specie mass'
    iterdb['m_SIMPI']['component'] = 'PLASMA'
    iterdb['m_SIMPI']['specification'] = 'S|impurity_atoms SIMPI(nspec_impi)'
    
    iterdb['m_SNBI'] = {}
    iterdb['m_SNBI']['data'] = None
    iterdb['m_SNBI']['units'] = 'kg'
    iterdb['m_SNBI']['section'] = 'SIMULATION_INIT'
    iterdb['m_SNBI']['long_name'] = 'SNBI specie mass'
    iterdb['m_SNBI']['component'] = 'NBI'
    iterdb['m_SNBI']['specification'] = 'S|beam_ion     SNBI(nspec_beam)'
    
    iterdb['n0norm'] = {}
    iterdb['n0norm']['data'] = None
    iterdb['n0norm']['units'] = '(m^-3)/(#/sec)'
    iterdb['n0norm']['section'] = 'STATE_PROFILES'
    iterdb['n0norm']['long_name'] = 'neutral density per unit gas influx (sc0)'
    iterdb['n0norm']['component'] = 'GAS'
    iterdb['n0norm']['specification'] = 'R|step|units=(m^-3)/(#/sec)    n0norm(~nrho_gas,nspec_gas,ngsc0)'
    
    iterdb['n0_halo'] = {}
    iterdb['n0_halo']['data'] = None
    iterdb['n0_halo']['units'] = 'm^-3'
    iterdb['n0_halo']['section'] = 'STATE_PROFILES'
    iterdb['n0_halo']['long_name'] = 'halo thermal neutral density'
    iterdb['n0_halo']['component'] = 'NBI'
    iterdb['n0_halo']['specification'] = 'R|units=m^-3|step         n0_halo(~nrho_nbi,nspec_gas)'
    
    iterdb['n0_reco'] = {}
    iterdb['n0_reco']['data'] = None
    iterdb['n0_reco']['units'] = 'm^-3'
    iterdb['n0_reco']['section'] = 'STATE_PROFILES'
    iterdb['n0_reco']['long_name'] = 'reco thermal neutral density'
    iterdb['n0_reco']['component'] = 'GAS'
    iterdb['n0_reco']['specification'] = 'R|units=m^-3|step         n0_reco(~nrho_gas,nspec_gas)'
    
    iterdb['nbap2_shape'] = {}
    iterdb['nbap2_shape']['data'] = None
    iterdb['nbap2_shape']['units'] = None
    iterdb['nbap2_shape']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['nbap2_shape']['long_name'] = 'keyword for optional 2nd aperture'
    iterdb['nbap2_shape']['component'] = 'NBI'
    iterdb['nbap2_shape']['specification'] = 'N     nbap2_shape(nbeam)'
    
    iterdb['nbap_shape'] = {}
    iterdb['nbap_shape']['data'] = None
    iterdb['nbap_shape']['units'] = None
    iterdb['nbap_shape']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['nbap_shape']['long_name'] = 'shape keyword for beam aperture'
    iterdb['nbap_shape']['component'] = 'NBI'
    iterdb['nbap_shape']['specification'] = 'N     nbap_shape(nbeam)'
    
    iterdb['nbeami'] = {}
    iterdb['nbeami']['data'] = None
    iterdb['nbeami']['units'] = 'm^-3'
    iterdb['nbeami']['section'] = 'STATE_PROFILES'
    iterdb['nbeami']['long_name'] = 'beam species density'
    iterdb['nbeami']['component'] = 'NBI'
    iterdb['nbeami']['specification'] = 'R|units=m^-3|alias=n|step  nbeami(~nrho_nbi,nspec_beam)'
    
    iterdb['nbeami_bdy'] = {}
    iterdb['nbeami_bdy']['data'] = None
    iterdb['nbeami_bdy']['units'] = 'm^-3'
    iterdb['nbeami_bdy']['section'] = 'STATE_DATA'
    iterdb['nbeami_bdy']['long_name'] = 'beam ion densities at/beyond boundary'
    iterdb['nbeami_bdy']['component'] = 'NBI'
    iterdb['nbeami_bdy']['specification'] = 'R|units=m^-3  nbeami_bdy(nspec_beam)'
    
    iterdb['nbion'] = {}
    iterdb['nbion']['data'] = None
    iterdb['nbion']['units'] = None
    iterdb['nbion']['section'] = 'SHOT_CONFIGURATION'
    iterdb['nbion']['long_name'] = 'name of species injected by each beam.'
    iterdb['nbion']['component'] = 'NBI'
    iterdb['nbion']['specification'] = 'N  nbion(nbeam)'
    
    iterdb['nbion_trace'] = {}
    iterdb['nbion_trace']['data'] = None
    iterdb['nbion_trace']['units'] = None
    iterdb['nbion_trace']['section'] = 'SHOT_CONFIGURATION'
    iterdb['nbion_trace']['long_name'] = '(if non-blank) beam trace element'
    iterdb['nbion_trace']['component'] = 'NBI'
    iterdb['nbion_trace']['specification'] = 'N  nbion_trace(nbeam)'
    
    iterdb['NBI_Code_Info'] = {}
    iterdb['NBI_Code_Info']['data'] = None
    iterdb['NBI_Code_Info']['units'] = None
    iterdb['NBI_Code_Info']['section'] = 'SIMULATION_INIT'
    iterdb['NBI_Code_Info']['long_name'] = 'Information: code implementing NBI component'
    iterdb['NBI_Code_Info']['component'] = 'NBI'
    iterdb['NBI_Code_Info']['specification'] = 'C*80   NBI_Code_Info'
    
    iterdb['NBI_Data_Info'] = {}
    iterdb['NBI_Data_Info']['data'] = None
    iterdb['NBI_Data_Info']['units'] = None
    iterdb['NBI_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['NBI_Data_Info']['long_name'] = 'information on source of beam power & voltage data'
    iterdb['NBI_Data_Info']['component'] = 'NBI'
    iterdb['NBI_Data_Info']['specification'] = 'C*80   NBI_Data_Info'
    
    iterdb['nbi_src_name'] = {}
    iterdb['nbi_src_name']['data'] = None
    iterdb['nbi_src_name']['units'] = None
    iterdb['nbi_src_name']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['nbi_src_name']['long_name'] = 'number & name of neutral beams'
    iterdb['nbi_src_name']['component'] = 'NBI'
    iterdb['nbi_src_name']['specification'] = 'L|neutral_beams nbi_src_name(nbeam)'
    
    iterdb['nbshape'] = {}
    iterdb['nbshape']['data'] = None
    iterdb['nbshape']['units'] = None
    iterdb['nbshape']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['nbshape']['long_name'] = 'shape keyword for beam source grid'
    iterdb['nbshape']['component'] = 'NBI'
    iterdb['nbshape']['specification'] = 'N     nbshape(nbeam)'
    
    iterdb['nebar'] = {}
    iterdb['nebar']['data'] = None
    iterdb['nebar']['units'] = '#/m^2'
    iterdb['nebar']['section'] = 'STATE_DATA'
    iterdb['nebar']['long_name'] = 'line-averaged electron density'
    iterdb['nebar']['component'] = 'PLASMA'
    iterdb['nebar']['specification'] = 'R|units=#/m^2 nebar'
    
    iterdb['nfusi'] = {}
    iterdb['nfusi']['data'] = None
    iterdb['nfusi']['units'] = 'm^-3'
    iterdb['nfusi']['section'] = 'STATE_PROFILES'
    iterdb['nfusi']['long_name'] = 'fusion ion density'
    iterdb['nfusi']['component'] = 'FUS'
    iterdb['nfusi']['specification'] = 'R|units=m^-3|alias=n|step  nfusi(~nrho_fus,nspec_fusion)'
    
    iterdb['nfusi_bdy'] = {}
    iterdb['nfusi_bdy']['data'] = None
    iterdb['nfusi_bdy']['units'] = 'm^-3'
    iterdb['nfusi_bdy']['section'] = 'STATE_DATA'
    iterdb['nfusi_bdy']['long_name'] = 'fusion ion densities at/beyond boundary'
    iterdb['nfusi_bdy']['component'] = 'IC'
    iterdb['nfusi_bdy']['specification'] = 'R|units=m^-3  nfusi_bdy(nspec_beam)'
    
    iterdb['ngradb2_av'] = {}
    iterdb['ngradb2_av']['data'] = None
    iterdb['ngradb2_av']['units'] = 'T^2*m^-2'
    iterdb['ngradb2_av']['section'] = 'STATE_PROFILES'
    iterdb['ngradb2_av']['long_name'] = '<(B.grad(B)/|B|)^2>'
    iterdb['ngradb2_av']['component'] = 'EQ'
    iterdb['ngradb2_av']['specification'] = 'R|units=T^2*m^-2|pclin   ngradb2_av(nrho_eq_geo)'
    
    iterdb['ni'] = {}
    iterdb['ni']['data'] = None
    iterdb['ni']['units'] = 'm^-3'
    iterdb['ni']['section'] = 'STATE_PROFILES'
    iterdb['ni']['long_name'] = 'total thermal ion density'
    iterdb['ni']['component'] = 'PLASMA'
    iterdb['ni']['specification'] = 'R|units=m^-3|step  ni(~nrho)'
    
    iterdb['nmdifb'] = {}
    iterdb['nmdifb']['data'] = None
    iterdb['nmdifb']['units'] = None
    iterdb['nmdifb']['section'] = 'STATE_DATA'
    iterdb['nmdifb']['long_name'] = 'type of fast ion diffusivity'
    iterdb['nmdifb']['component'] = 'ANOM'
    iterdb['nmdifb']['specification'] = 'I   nmdifb = 0'
    
    iterdb['nmini_bdy'] = {}
    iterdb['nmini_bdy']['data'] = None
    iterdb['nmini_bdy']['units'] = 'm^-3'
    iterdb['nmini_bdy']['section'] = 'STATE_DATA'
    iterdb['nmini_bdy']['long_name'] = 'RF minority ion densities at/beyond boundary'
    iterdb['nmini_bdy']['component'] = 'FUS'
    iterdb['nmini_bdy']['specification'] = 'R|units=m^-3  nmini_bdy(nspec_beam)'
    
    iterdb['nmodel_bdy'] = {}
    iterdb['nmodel_bdy']['data'] = None
    iterdb['nmodel_bdy']['units'] = 'm^-3'
    iterdb['nmodel_bdy']['section'] = 'STATE_DATA'
    iterdb['nmodel_bdy']['long_name'] = 'model density, boundary value'
    iterdb['nmodel_bdy']['component'] = 'ANOM'
    iterdb['nmodel_bdy']['specification'] = 'R|units=m^-3   nmodel_bdy'
    
    iterdb['nmom'] = {}
    iterdb['nmom']['data'] = None
    iterdb['nmom']['units'] = None
    iterdb['nmom']['section'] = 'SIMULATION_INIT'
    iterdb['nmom']['long_name'] = 'number of Fourier (R,Z) moments'
    iterdb['nmom']['component'] = 'EQ'
    iterdb['nmom']['specification'] = 'I  nmom = 16'
    
    iterdb['ns'] = {}
    iterdb['ns']['data'] = None
    iterdb['ns']['units'] = 'm^-3'
    iterdb['ns']['section'] = 'STATE_PROFILES'
    iterdb['ns']['long_name'] = 'thermal specie density'
    iterdb['ns']['component'] = 'PLASMA'
    iterdb['ns']['specification'] = 'R|units=m^-3|alias=n|step  ns(~nrho,0:nspec_th)'
    
    iterdb['ns_bdy'] = {}
    iterdb['ns_bdy']['data'] = None
    iterdb['ns_bdy']['units'] = 'm^-3'
    iterdb['ns_bdy']['section'] = 'STATE_DATA'
    iterdb['ns_bdy']['long_name'] = 'specie densities at/beyond boundary'
    iterdb['ns_bdy']['component'] = 'PLASMA'
    iterdb['ns_bdy']['specification'] = 'R|units=m^-3 ns_bdy(0:nspec_th)'
    
    iterdb['ns_Data_Info'] = {}
    iterdb['ns_Data_Info']['data'] = None
    iterdb['ns_Data_Info']['units'] = None
    iterdb['ns_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['ns_Data_Info']['long_name'] = 'information on source of Density data'
    iterdb['ns_Data_Info']['component'] = 'PLASMA'
    iterdb['ns_Data_Info']['specification'] = 'C*80   ns_Data_Info'
    
    iterdb['ns_is_input'] = {}
    iterdb['ns_is_input']['data'] = None
    iterdb['ns_is_input']['units'] = None
    iterdb['ns_is_input']['section'] = 'STATE_DATA'
    iterdb['ns_is_input']['long_name'] = 'specie density measurement flag'
    iterdb['ns_is_input']['component'] = 'PLASMA'
    iterdb['ns_is_input']['specification'] = 'I ns_is_input(0:nspec_th)'
    
    iterdb['ntf_coil2'] = {}
    iterdb['ntf_coil2']['data'] = None
    iterdb['ntf_coil2']['units'] = None
    iterdb['ntf_coil2']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['ntf_coil2']['long_name'] = 'number of TF coils involved in inducing 2nd component'
    iterdb['ntf_coil2']['component'] = 'RIPPLE'
    iterdb['ntf_coil2']['specification'] = 'I ntf_coil2'
    
    iterdb['ntf_coils'] = {}
    iterdb['ntf_coils']['data'] = None
    iterdb['ntf_coils']['units'] = None
    iterdb['ntf_coils']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['ntf_coils']['long_name'] = 'number of TF coils'
    iterdb['ntf_coils']['component'] = 'RIPPLE'
    iterdb['ntf_coils']['specification'] = 'I ntf_coils'
    
    iterdb['omeg0cx'] = {}
    iterdb['omeg0cx']['data'] = None
    iterdb['omeg0cx']['units'] = 'rad/sec'
    iterdb['omeg0cx']['section'] = 'STATE_PROFILES'
    iterdb['omeg0cx']['long_name'] = 'effective neutral angular velocity for CX torque'
    iterdb['omeg0cx']['component'] = 'GAS'
    iterdb['omeg0cx']['specification'] = 'R|step*tqqcx|units=rad/sec  omeg0cx(~nrho_gas,ngsc0)'
    
    iterdb['omeg0sc0'] = {}
    iterdb['omeg0sc0']['data'] = None
    iterdb['omeg0sc0']['units'] = '(rad/sec)'
    iterdb['omeg0sc0']['section'] = 'STATE_PROFILES'
    iterdb['omeg0sc0']['long_name'] = 'toroidal angular velocity'
    iterdb['omeg0sc0']['component'] = 'GAS'
    iterdb['omeg0sc0']['specification'] = 'R|step*n0norm|units=(rad/sec)  omeg0sc0(~nrho_gas,nspec_gas,ngsc0)'
    
    iterdb['omeg0_halo'] = {}
    iterdb['omeg0_halo']['data'] = None
    iterdb['omeg0_halo']['units'] = 'rad/sec'
    iterdb['omeg0_halo']['section'] = 'STATE_PROFILES'
    iterdb['omeg0_halo']['long_name'] = 'halo neutral toroidal angular velocity'
    iterdb['omeg0_halo']['component'] = 'NBI'
    iterdb['omeg0_halo']['specification'] = 'R|units=rad/sec|step*n0_halo  omeg0_halo(~nrho_nbi,nspec_gas)'
    
    iterdb['omeg0_reco'] = {}
    iterdb['omeg0_reco']['data'] = None
    iterdb['omeg0_reco']['units'] = 'rad/sec'
    iterdb['omeg0_reco']['section'] = 'STATE_PROFILES'
    iterdb['omeg0_reco']['long_name'] = 'reco neutral toroidal angular velocity'
    iterdb['omeg0_reco']['component'] = 'GAS'
    iterdb['omeg0_reco']['specification'] = 'R|units=rad/sec|step*n0_reco  omeg0_reco(~nrho_gas,nspec_gas)'
    
    iterdb['omegat'] = {}
    iterdb['omegat']['data'] = None
    iterdb['omegat']['units'] = 'rad/sec'
    iterdb['omegat']['section'] = 'STATE_PROFILES'
    iterdb['omegat']['long_name'] = 'ion toroidal angular velocity'
    iterdb['omegat']['component'] = 'PLASMA'
    iterdb['omegat']['specification'] = 'R|units=rad/sec|step*ni  omegat(~nrho)'
    
    iterdb['omegat_bdy'] = {}
    iterdb['omegat_bdy']['data'] = None
    iterdb['omegat_bdy']['units'] = 'rad/sec'
    iterdb['omegat_bdy']['section'] = 'STATE_DATA'
    iterdb['omegat_bdy']['long_name'] = 'toroidal angular velocity at/beyond boundary'
    iterdb['omegat_bdy']['component'] = 'PLASMA'
    iterdb['omegat_bdy']['specification'] = 'R|units=rad/sec  omegat_bdy'
    
    iterdb['p0_reco'] = {}
    iterdb['p0_reco']['data'] = None
    iterdb['p0_reco']['units'] = 'W'
    iterdb['p0_reco']['section'] = 'STATE_PROFILES'
    iterdb['p0_reco']['long_name'] = 'power in recombination neutral source'
    iterdb['p0_reco']['component'] = 'GAS'
    iterdb['p0_reco']['specification'] = 'R|step*dV   p0_reco(~nrho_gas)'
    
    iterdb['pb0_halo'] = {}
    iterdb['pb0_halo']['data'] = None
    iterdb['pb0_halo']['units'] = 'W'
    iterdb['pb0_halo']['section'] = 'STATE_PROFILES'
    iterdb['pb0_halo']['long_name'] = 'power in halo neutral source'
    iterdb['pb0_halo']['component'] = 'NBI'
    iterdb['pb0_halo']['specification'] = 'R|step*dV   pb0_halo(~nrho_nbi)'
    
    iterdb['pbe'] = {}
    iterdb['pbe']['data'] = None
    iterdb['pbe']['units'] = 'W'
    iterdb['pbe']['section'] = 'STATE_PROFILES'
    iterdb['pbe']['long_name'] = 'electron heating by all beam ions'
    iterdb['pbe']['component'] = 'NBI'
    iterdb['pbe']['specification'] = 'R|step*dV   pbe(~nrho_nbi)'
    
    iterdb['pbi'] = {}
    iterdb['pbi']['data'] = None
    iterdb['pbi']['units'] = 'W'
    iterdb['pbi']['section'] = 'STATE_PROFILES'
    iterdb['pbi']['long_name'] = 'thermal ion heating by all beam ions'
    iterdb['pbi']['component'] = 'NBI'
    iterdb['pbi']['specification'] = 'R|step*dV   pbi(~nrho_nbi)'
    
    iterdb['pbth'] = {}
    iterdb['pbth']['data'] = None
    iterdb['pbth']['units'] = 'W'
    iterdb['pbth']['section'] = 'STATE_PROFILES'
    iterdb['pbth']['long_name'] = 'thermalization of beam ions'
    iterdb['pbth']['component'] = 'NBI'
    iterdb['pbth']['specification'] = 'R|step*dV   pbth(~nrho_nbi)'
    
    iterdb['pcx_halo'] = {}
    iterdb['pcx_halo']['data'] = None
    iterdb['pcx_halo']['units'] = 'W'
    iterdb['pcx_halo']['section'] = 'STATE_PROFILES'
    iterdb['pcx_halo']['long_name'] = 'beam halo driven CX power'
    iterdb['pcx_halo']['component'] = 'NBI'
    iterdb['pcx_halo']['specification'] = 'R|step*dV   pcx_halo(~nrho_nbi)'
    
    iterdb['pcx_reco'] = {}
    iterdb['pcx_reco']['data'] = None
    iterdb['pcx_reco']['units'] = 'W'
    iterdb['pcx_reco']['section'] = 'STATE_PROFILES'
    iterdb['pcx_reco']['long_name'] = 'reco driven CX power'
    iterdb['pcx_reco']['component'] = 'GAS'
    iterdb['pcx_reco']['specification'] = 'R|step*dV   pcx_reco(~nrho_gas)'
    
    iterdb['peech'] = {}
    iterdb['peech']['data'] = None
    iterdb['peech']['units'] = 'W'
    iterdb['peech']['section'] = 'STATE_PROFILES'
    iterdb['peech']['long_name'] = 'electron heating by ECH'
    iterdb['peech']['component'] = 'EC'
    iterdb['peech']['specification'] = 'R|step*dV|units=W   peech(~nrho_ecrf)'
    
    iterdb['peech_src'] = {}
    iterdb['peech_src']['data'] = None
    iterdb['peech_src']['units'] = 'W'
    iterdb['peech_src']['section'] = 'STATE_PROFILES'
    iterdb['peech_src']['long_name'] = 'ECH heating (by antenna)'
    iterdb['peech_src']['component'] = 'EC'
    iterdb['peech_src']['specification'] = 'R|step*dV|units=W   peech_src(~nrho_ecrf,necrf_src)'
    
    iterdb['pe_trans'] = {}
    iterdb['pe_trans']['data'] = None
    iterdb['pe_trans']['units'] = 'W'
    iterdb['pe_trans']['section'] = 'STATE_PROFILES'
    iterdb['pe_trans']['long_name'] = 'electron transport (loss) power'
    iterdb['pe_trans']['component'] = 'PLASMA'
    iterdb['pe_trans']['specification'] = 'R|step*dV   pe_trans(~nrho)'
    
    iterdb['pfuse'] = {}
    iterdb['pfuse']['data'] = None
    iterdb['pfuse']['units'] = 'W'
    iterdb['pfuse']['section'] = 'STATE_PROFILES'
    iterdb['pfuse']['long_name'] = 'electron heating by all fusion ions'
    iterdb['pfuse']['component'] = 'FUS'
    iterdb['pfuse']['specification'] = 'R|step*dV   pfuse(~nrho_fus)'
    
    iterdb['pfusi'] = {}
    iterdb['pfusi']['data'] = None
    iterdb['pfusi']['units'] = 'W'
    iterdb['pfusi']['section'] = 'STATE_PROFILES'
    iterdb['pfusi']['long_name'] = 'thermal ion heating by all fusion ions'
    iterdb['pfusi']['component'] = 'FUS'
    iterdb['pfusi']['specification'] = 'R|step*dV   pfusi(~nrho_fus)'
    
    iterdb['pfusth'] = {}
    iterdb['pfusth']['data'] = None
    iterdb['pfusth']['units'] = 'W'
    iterdb['pfusth']['section'] = 'STATE_PROFILES'
    iterdb['pfusth']['long_name'] = 'thermalization of fusion ions'
    iterdb['pfusth']['component'] = 'FUS'
    iterdb['pfusth']['specification'] = 'R|step*dV   pfusth(~nrho_fus)'
    
    iterdb['Phibsc'] = {}
    iterdb['Phibsc']['data'] = None
    iterdb['Phibsc']['units'] = 'degrees'
    iterdb['Phibsc']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['Phibsc']['long_name'] = 'toroidal location of beam source'
    iterdb['Phibsc']['component'] = 'NBI'
    iterdb['Phibsc']['specification'] = 'R|units=degrees       Phibsc(nbeam)'
    
    iterdb['phit'] = {}
    iterdb['phit']['data'] = None
    iterdb['phit']['units'] = 'Wb'
    iterdb['phit']['section'] = 'STATE_PROFILES'
    iterdb['phit']['long_name'] = 'toroidal flux vs. rho'
    iterdb['phit']['component'] = 'EQ'
    iterdb['phit']['specification'] = 'R|units=Wb|Spline_00       phit(nrho_eq)'
    
    iterdb['Phi_EC_launch'] = {}
    iterdb['Phi_EC_launch']['data'] = None
    iterdb['Phi_EC_launch']['units'] = 'degrees'
    iterdb['Phi_EC_launch']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['Phi_EC_launch']['long_name'] = 'Phi of center of launcher'
    iterdb['Phi_EC_launch']['component'] = 'EC'
    iterdb['Phi_EC_launch']['specification'] = 'R|units=degrees  Phi_EC_launch(necrf_src)'
    
    iterdb['pi_trans'] = {}
    iterdb['pi_trans']['data'] = None
    iterdb['pi_trans']['units'] = 'W'
    iterdb['pi_trans']['section'] = 'STATE_PROFILES'
    iterdb['pi_trans']['long_name'] = 'ion transport (loss) power'
    iterdb['pi_trans']['component'] = 'PLASMA'
    iterdb['pi_trans']['specification'] = 'R|step*dV   pi_trans(~nrho)'
    
    iterdb['PLASMA_Code_Info'] = {}
    iterdb['PLASMA_Code_Info']['data'] = None
    iterdb['PLASMA_Code_Info']['units'] = None
    iterdb['PLASMA_Code_Info']['section'] = 'SIMULATION_INIT'
    iterdb['PLASMA_Code_Info']['long_name'] = 'Information: code managing PLASMA component'
    iterdb['PLASMA_Code_Info']['component'] = 'PLASMA'
    iterdb['PLASMA_Code_Info']['specification'] = 'C*80   PLASMA_Code_Info'
    
    iterdb['pohme'] = {}
    iterdb['pohme']['data'] = None
    iterdb['pohme']['units'] = 'W'
    iterdb['pohme']['section'] = 'STATE_PROFILES'
    iterdb['pohme']['long_name'] = 'Ohmic heating of electrons'
    iterdb['pohme']['component'] = 'PLASMA'
    iterdb['pohme']['specification'] = 'R|units=W|step*dV   pohme(~nrho)'
    
    iterdb['power_ec'] = {}
    iterdb['power_ec']['data'] = None
    iterdb['power_ec']['units'] = 'W'
    iterdb['power_ec']['section'] = 'STATE_DATA'
    iterdb['power_ec']['long_name'] = 'power on each ECRF source'
    iterdb['power_ec']['component'] = 'EC'
    iterdb['power_ec']['specification'] = 'R|units=W  power_ec(necrf_src)'
    
    iterdb['power_nbi'] = {}
    iterdb['power_nbi']['data'] = None
    iterdb['power_nbi']['units'] = 'W'
    iterdb['power_nbi']['section'] = 'STATE_DATA'
    iterdb['power_nbi']['long_name'] = 'power on each beam source'
    iterdb['power_nbi']['component'] = 'NBI'
    iterdb['power_nbi']['specification'] = 'R|units=W  power_nbi(nbeam)'
    
    iterdb['power_nbi_trace'] = {}
    iterdb['power_nbi_trace']['data'] = None
    iterdb['power_nbi_trace']['units'] = 'W'
    iterdb['power_nbi_trace']['section'] = 'STATE_DATA'
    iterdb['power_nbi_trace']['long_name'] = 'power injected as trace element (if any)'
    iterdb['power_nbi_trace']['component'] = 'NBI'
    iterdb['power_nbi_trace']['specification'] = 'R|units=W  power_nbi_trace(nbeam)'
    
    iterdb['prad'] = {}
    iterdb['prad']['data'] = None
    iterdb['prad']['units'] = 'W'
    iterdb['prad']['section'] = 'STATE_PROFILES'
    iterdb['prad']['long_name'] = 'total radiated power'
    iterdb['prad']['component'] = 'RAD'
    iterdb['prad']['specification'] = 'R|step*dV  prad(~nrho_rad)'
    
    iterdb['prad_br'] = {}
    iterdb['prad_br']['data'] = None
    iterdb['prad_br']['units'] = 'W'
    iterdb['prad_br']['section'] = 'STATE_PROFILES'
    iterdb['prad_br']['long_name'] = 'bremsstrahlung contribution'
    iterdb['prad_br']['component'] = 'RAD'
    iterdb['prad_br']['specification'] = 'R|step*dV  prad_br(~nrho_rad)'
    
    iterdb['prad_cy'] = {}
    iterdb['prad_cy']['data'] = None
    iterdb['prad_cy']['units'] = 'W'
    iterdb['prad_cy']['section'] = 'STATE_PROFILES'
    iterdb['prad_cy']['long_name'] = 'cyclotron radiation contribution'
    iterdb['prad_cy']['component'] = 'RAD'
    iterdb['prad_cy']['specification'] = 'R|step*dV  prad_cy(~nrho_rad)'
    
    iterdb['prad_li'] = {}
    iterdb['prad_li']['data'] = None
    iterdb['prad_li']['units'] = 'W'
    iterdb['prad_li']['section'] = 'STATE_PROFILES'
    iterdb['prad_li']['long_name'] = 'line radiation contribution'
    iterdb['prad_li']['component'] = 'RAD'
    iterdb['prad_li']['specification'] = 'R|step*dV  prad_li(~nrho_rad)'
    
    iterdb['psc_halo'] = {}
    iterdb['psc_halo']['data'] = None
    iterdb['psc_halo']['units'] = 'W'
    iterdb['psc_halo']['section'] = 'STATE_PROFILES'
    iterdb['psc_halo']['long_name'] = 'beam halo power: recapture - pb0_halo'
    iterdb['psc_halo']['component'] = 'NBI'
    iterdb['psc_halo']['specification'] = 'R|step*dV   psc_halo(~nrho_nbi)'
    
    iterdb['psc_reco'] = {}
    iterdb['psc_reco']['data'] = None
    iterdb['psc_reco']['units'] = 'W'
    iterdb['psc_reco']['section'] = 'STATE_PROFILES'
    iterdb['psc_reco']['long_name'] = 'reco power: recapture - p0_reco'
    iterdb['psc_reco']['component'] = 'GAS'
    iterdb['psc_reco']['specification'] = 'R|step*dV   psc_reco(~nrho_gas)'
    
    iterdb['psipol'] = {}
    iterdb['psipol']['data'] = None
    iterdb['psipol']['units'] = 'Wb/rad'
    iterdb['psipol']['section'] = 'STATE_PROFILES'
    iterdb['psipol']['long_name'] = 'poloidal flux vs. rho'
    iterdb['psipol']['component'] = 'EQ'
    iterdb['psipol']['specification'] = 'R|units=Wb/rad|Spline_00   psipol(nrho_eq)'
    
    iterdb['PsiRZ'] = {}
    iterdb['PsiRZ']['data'] = None
    iterdb['PsiRZ']['units'] = 'Wb/rad'
    iterdb['PsiRZ']['section'] = 'STATE_PROFILES'
    iterdb['PsiRZ']['long_name'] = 'Psi(R,Z)'
    iterdb['PsiRZ']['component'] = 'EQ'
    iterdb['PsiRZ']['specification'] = 'R|units=Wb/rad|Spline  PsiRZ(nR,nZ)'
    
    iterdb['Psi_to_machine_axis'] = {}
    iterdb['Psi_to_machine_axis']['data'] = None
    iterdb['Psi_to_machine_axis']['units'] = 'Wb/rad'
    iterdb['Psi_to_machine_axis']['section'] = 'STATE_DATA'
    iterdb['Psi_to_machine_axis']['long_name'] = 'delta(Psi) from magnetic axis to machine axis'
    iterdb['Psi_to_machine_axis']['component'] = 'EQ'
    iterdb['Psi_to_machine_axis']['specification'] = 'R|units=Wb/rad   Psi_to_machine_axis'
    
    iterdb['psmom_errck'] = {}
    iterdb['psmom_errck']['data'] = None
    iterdb['psmom_errck']['units'] = None
    iterdb['psmom_errck']['section'] = 'STATE_PROFILES'
    iterdb['psmom_errck']['long_name'] = 'PS moments sum convergence'
    iterdb['psmom_errck']['component'] = 'EQ'
    iterdb['psmom_errck']['specification'] = 'R|units=-|pclin       psmom_errck(nrho_eq_geo)'
    
    iterdb['psmom_nc'] = {}
    iterdb['psmom_nc']['data'] = None
    iterdb['psmom_nc']['units'] = 'm^-2'
    iterdb['psmom_nc']['section'] = 'STATE_PROFILES'
    iterdb['psmom_nc']['long_name'] = 'PS moments'
    iterdb['psmom_nc']['component'] = 'EQ'
    iterdb['psmom_nc']['specification'] = 'R|units=m^-2|pclin    psmom_nc(nrho_eq_geo,npsmom)'
    
    iterdb['psmom_num'] = {}
    iterdb['psmom_num']['data'] = None
    iterdb['psmom_num']['units'] = None
    iterdb['psmom_num']['section'] = 'SIMULATION_INIT'
    iterdb['psmom_num']['long_name'] = 'Pfirsch-Schlutter moments'
    iterdb['psmom_num']['component'] = 'EQ'
    iterdb['psmom_num']['specification'] = 'L|PS_moments  psmom_num(npsmom)'
    
    iterdb['P_eq'] = {}
    iterdb['P_eq']['data'] = None
    iterdb['P_eq']['units'] = 'Pa'
    iterdb['P_eq']['section'] = 'STATE_PROFILES'
    iterdb['P_eq']['long_name'] = 'equilibrium scalar pressure'
    iterdb['P_eq']['component'] = 'EQ'
    iterdb['P_eq']['specification'] = 'R|units=Pa|Spline_00       P_eq(nrho_eq)'
    
    iterdb['qatom_ALL'] = {}
    iterdb['qatom_ALL']['data'] = None
    iterdb['qatom_ALL']['units'] = 'C'
    iterdb['qatom_ALL']['section'] = 'SIMULATION_INIT'
    iterdb['qatom_ALL']['long_name'] = 'ALL atomic number'
    iterdb['qatom_ALL']['component'] = 'PLASMA'
    iterdb['qatom_ALL']['specification'] = 'S|specie  ALL(0:nspec_all)'
    
    iterdb['qatom_ALLA'] = {}
    iterdb['qatom_ALLA']['data'] = None
    iterdb['qatom_ALLA']['units'] = 'C'
    iterdb['qatom_ALLA']['section'] = 'SIMULATION_INIT'
    iterdb['qatom_ALLA']['long_name'] = 'ALLA atomic number'
    iterdb['qatom_ALLA']['component'] = 'PLASMA'
    iterdb['qatom_ALLA']['specification'] = 'S|specie  ALLA(0:nspec_alla)'
    
    iterdb['qatom_S'] = {}
    iterdb['qatom_S']['data'] = None
    iterdb['qatom_S']['units'] = 'C'
    iterdb['qatom_S']['section'] = 'SHOT_CONFIGURATION'
    iterdb['qatom_S']['long_name'] = 'S atomic number'
    iterdb['qatom_S']['component'] = 'PLASMA'
    iterdb['qatom_S']['specification'] = 'S|thermal_specie  S(0:nspec_th)'
    
    iterdb['qatom_SA'] = {}
    iterdb['qatom_SA']['data'] = None
    iterdb['qatom_SA']['units'] = 'C'
    iterdb['qatom_SA']['section'] = 'SIMULATION_INIT'
    iterdb['qatom_SA']['long_name'] = 'SA atomic number'
    iterdb['qatom_SA']['component'] = 'PLASMA'
    iterdb['qatom_SA']['specification'] = 'S|thermal_specie  SA(0:nspec_tha)'
    
    iterdb['qatom_SFUS'] = {}
    iterdb['qatom_SFUS']['data'] = None
    iterdb['qatom_SFUS']['units'] = 'C'
    iterdb['qatom_SFUS']['section'] = 'SHOT_CONFIGURATION'
    iterdb['qatom_SFUS']['long_name'] = 'SFUS atomic number'
    iterdb['qatom_SFUS']['component'] = 'FUS'
    iterdb['qatom_SFUS']['specification'] = 'S|fusion_ion   SFUS(nspec_fusion)'
    
    iterdb['qatom_SGAS'] = {}
    iterdb['qatom_SGAS']['data'] = None
    iterdb['qatom_SGAS']['units'] = 'C'
    iterdb['qatom_SGAS']['section'] = 'SIMULATION_INIT'
    iterdb['qatom_SGAS']['long_name'] = 'SGAS atomic number'
    iterdb['qatom_SGAS']['component'] = 'GAS'
    iterdb['qatom_SGAS']['specification'] = 'S|neutral_gas  SGAS(nspec_gas)'
    
    iterdb['qatom_SIMP0'] = {}
    iterdb['qatom_SIMP0']['data'] = None
    iterdb['qatom_SIMP0']['units'] = 'C'
    iterdb['qatom_SIMP0']['section'] = 'SIMULATION_INIT'
    iterdb['qatom_SIMP0']['long_name'] = 'SIMP0 atomic number'
    iterdb['qatom_SIMP0']['component'] = 'GAS'
    iterdb['qatom_SIMP0']['specification'] = 'S|impurity_atoms SIMP0(nspec_imp0)'
    
    iterdb['qatom_SIMPI'] = {}
    iterdb['qatom_SIMPI']['data'] = None
    iterdb['qatom_SIMPI']['units'] = 'C'
    iterdb['qatom_SIMPI']['section'] = 'SIMULATION_INIT'
    iterdb['qatom_SIMPI']['long_name'] = 'SIMPI atomic number'
    iterdb['qatom_SIMPI']['component'] = 'PLASMA'
    iterdb['qatom_SIMPI']['specification'] = 'S|impurity_atoms SIMPI(nspec_impi)'
    
    iterdb['qatom_SNBI'] = {}
    iterdb['qatom_SNBI']['data'] = None
    iterdb['qatom_SNBI']['units'] = 'C'
    iterdb['qatom_SNBI']['section'] = 'SIMULATION_INIT'
    iterdb['qatom_SNBI']['long_name'] = 'SNBI atomic number'
    iterdb['qatom_SNBI']['component'] = 'NBI'
    iterdb['qatom_SNBI']['specification'] = 'S|beam_ion     SNBI(nspec_beam)'
    
    iterdb['qbeami'] = {}
    iterdb['qbeami']['data'] = None
    iterdb['qbeami']['units'] = 'C'
    iterdb['qbeami']['section'] = 'STATE_PROFILES'
    iterdb['qbeami']['long_name'] = 'average beam ion charge'
    iterdb['qbeami']['component'] = 'NBI'
    iterdb['qbeami']['specification'] = 'R|units=C|step*nbeami qbeami(~nrho_nbi,nspec_beam)'
    
    iterdb['qcomp_e'] = {}
    iterdb['qcomp_e']['data'] = None
    iterdb['qcomp_e']['units'] = 'W'
    iterdb['qcomp_e']['section'] = 'STATE_PROFILES'
    iterdb['qcomp_e']['long_name'] = 'Compressional electron heating'
    iterdb['qcomp_e']['component'] = 'PLASMA'
    iterdb['qcomp_e']['specification'] = 'R|step*dV   qcomp_e(~nrho)'
    
    iterdb['qcomp_i'] = {}
    iterdb['qcomp_i']['data'] = None
    iterdb['qcomp_i']['units'] = 'W'
    iterdb['qcomp_i']['section'] = 'STATE_PROFILES'
    iterdb['qcomp_i']['long_name'] = 'Compressional ion heating'
    iterdb['qcomp_i']['component'] = 'PLASMA'
    iterdb['qcomp_i']['specification'] = 'R|step*dV   qcomp_i(~nrho)'
    
    iterdb['qie'] = {}
    iterdb['qie']['data'] = None
    iterdb['qie']['units'] = 'W'
    iterdb['qie']['section'] = 'STATE_PROFILES'
    iterdb['qie']['long_name'] = 'Ion->Electron heat coupling'
    iterdb['qie']['component'] = 'PLASMA'
    iterdb['qie']['specification'] = 'R|units=W|step*dV   qie(~nrho)'
    
    iterdb['qioniz'] = {}
    iterdb['qioniz']['data'] = None
    iterdb['qioniz']['units'] = 'W/(#/sec)'
    iterdb['qioniz']['section'] = 'STATE_PROFILES'
    iterdb['qioniz']['long_name'] = 'ionization power per unit influx (sc0)'
    iterdb['qioniz']['component'] = 'GAS'
    iterdb['qioniz']['specification'] = 'R|step*dV|units=W/(#/sec)     qioniz(~nrho_gas,ngsc0)'
    
    iterdb['ql_operator'] = {}
    iterdb['ql_operator']['data'] = None
    iterdb['ql_operator']['units'] = None
    iterdb['ql_operator']['section'] = 'STATE_DATA'
    iterdb['ql_operator']['long_name'] = 'quasilinear operator filenames'
    iterdb['ql_operator']['component'] = 'IC'
    iterdb['ql_operator']['specification'] = 'F  ql_operator(0:nspec_alla)'
    
    iterdb['qqcx'] = {}
    iterdb['qqcx']['data'] = None
    iterdb['qqcx']['units'] = 'W/(#/sec)/keV'
    iterdb['qqcx']['section'] = 'STATE_PROFILES'
    iterdb['qqcx']['long_name'] = 'cx power per unit influx per (T0-Ti)'
    iterdb['qqcx']['component'] = 'GAS'
    iterdb['qqcx']['specification'] = 'R|step*dV|units=W/(#/sec)/keV  qqcx(~nrho_gas,ngsc0)'
    
    iterdb['qrot_conv'] = {}
    iterdb['qrot_conv']['data'] = None
    iterdb['qrot_conv']['units'] = 'W'
    iterdb['qrot_conv']['section'] = 'STATE_PROFILES'
    iterdb['qrot_conv']['long_name'] = 'rotational energy dissipation (convective)'
    iterdb['qrot_conv']['component'] = 'PLASMA'
    iterdb['qrot_conv']['specification'] = 'R|step*dV   qrot_conv(~nrho)'
    
    iterdb['qrot_diff'] = {}
    iterdb['qrot_diff']['data'] = None
    iterdb['qrot_diff']['units'] = 'W'
    iterdb['qrot_diff']['section'] = 'STATE_PROFILES'
    iterdb['qrot_diff']['long_name'] = 'rotational energy dissipation (diffusive)'
    iterdb['qrot_diff']['component'] = 'PLASMA'
    iterdb['qrot_diff']['specification'] = 'R|step*dV   qrot_diff(~nrho)'
    
    iterdb['q_ALL'] = {}
    iterdb['q_ALL']['data'] = None
    iterdb['q_ALL']['units'] = 'C'
    iterdb['q_ALL']['section'] = 'SIMULATION_INIT'
    iterdb['q_ALL']['long_name'] = 'ALL specie charge'
    iterdb['q_ALL']['component'] = 'PLASMA'
    iterdb['q_ALL']['specification'] = 'S|specie  ALL(0:nspec_all)'
    
    iterdb['q_ALLA'] = {}
    iterdb['q_ALLA']['data'] = None
    iterdb['q_ALLA']['units'] = 'C'
    iterdb['q_ALLA']['section'] = 'SIMULATION_INIT'
    iterdb['q_ALLA']['long_name'] = 'ALLA specie charge'
    iterdb['q_ALLA']['component'] = 'PLASMA'
    iterdb['q_ALLA']['specification'] = 'S|specie  ALLA(0:nspec_alla)'
    
    iterdb['q_eq'] = {}
    iterdb['q_eq']['data'] = None
    iterdb['q_eq']['units'] = None
    iterdb['q_eq']['section'] = 'STATE_PROFILES'
    iterdb['q_eq']['long_name'] = 'equilibrium q profile'
    iterdb['q_eq']['component'] = 'EQ'
    iterdb['q_eq']['specification'] = 'R|units=-|Spline           q_eq(nrho_eq)'
    
    iterdb['q_S'] = {}
    iterdb['q_S']['data'] = None
    iterdb['q_S']['units'] = 'C'
    iterdb['q_S']['section'] = 'SHOT_CONFIGURATION'
    iterdb['q_S']['long_name'] = 'S specie charge'
    iterdb['q_S']['component'] = 'PLASMA'
    iterdb['q_S']['specification'] = 'S|thermal_specie  S(0:nspec_th)'
    
    iterdb['q_SA'] = {}
    iterdb['q_SA']['data'] = None
    iterdb['q_SA']['units'] = 'C'
    iterdb['q_SA']['section'] = 'SIMULATION_INIT'
    iterdb['q_SA']['long_name'] = 'SA specie charge'
    iterdb['q_SA']['component'] = 'PLASMA'
    iterdb['q_SA']['specification'] = 'S|thermal_specie  SA(0:nspec_tha)'
    
    iterdb['q_SFUS'] = {}
    iterdb['q_SFUS']['data'] = None
    iterdb['q_SFUS']['units'] = 'C'
    iterdb['q_SFUS']['section'] = 'SHOT_CONFIGURATION'
    iterdb['q_SFUS']['long_name'] = 'SFUS specie charge'
    iterdb['q_SFUS']['component'] = 'FUS'
    iterdb['q_SFUS']['specification'] = 'S|fusion_ion   SFUS(nspec_fusion)'
    
    iterdb['q_SGAS'] = {}
    iterdb['q_SGAS']['data'] = None
    iterdb['q_SGAS']['units'] = 'C'
    iterdb['q_SGAS']['section'] = 'SIMULATION_INIT'
    iterdb['q_SGAS']['long_name'] = 'SGAS specie charge'
    iterdb['q_SGAS']['component'] = 'GAS'
    iterdb['q_SGAS']['specification'] = 'S|neutral_gas  SGAS(nspec_gas)'
    
    iterdb['q_SIMP0'] = {}
    iterdb['q_SIMP0']['data'] = None
    iterdb['q_SIMP0']['units'] = 'C'
    iterdb['q_SIMP0']['section'] = 'SIMULATION_INIT'
    iterdb['q_SIMP0']['long_name'] = 'SIMP0 specie charge'
    iterdb['q_SIMP0']['component'] = 'GAS'
    iterdb['q_SIMP0']['specification'] = 'S|impurity_atoms SIMP0(nspec_imp0)'
    
    iterdb['q_SIMPI'] = {}
    iterdb['q_SIMPI']['data'] = None
    iterdb['q_SIMPI']['units'] = 'C'
    iterdb['q_SIMPI']['section'] = 'SIMULATION_INIT'
    iterdb['q_SIMPI']['long_name'] = 'SIMPI specie charge'
    iterdb['q_SIMPI']['component'] = 'PLASMA'
    iterdb['q_SIMPI']['specification'] = 'S|impurity_atoms SIMPI(nspec_impi)'
    
    iterdb['q_SNBI'] = {}
    iterdb['q_SNBI']['data'] = None
    iterdb['q_SNBI']['units'] = 'C'
    iterdb['q_SNBI']['section'] = 'SIMULATION_INIT'
    iterdb['q_SNBI']['long_name'] = 'SNBI specie charge'
    iterdb['q_SNBI']['component'] = 'NBI'
    iterdb['q_SNBI']['specification'] = 'S|beam_ion     SNBI(nspec_beam)'
    
    iterdb['R0_momeq'] = {}
    iterdb['R0_momeq']['data'] = None
    iterdb['R0_momeq']['units'] = 'm'
    iterdb['R0_momeq']['section'] = 'STATE_PROFILES'
    iterdb['R0_momeq']['long_name'] = 'R0 of flux surface'
    iterdb['R0_momeq']['component'] = 'EQ'
    iterdb['R0_momeq']['specification'] = 'R|units=m|Hermite_explicit  R0_momeq(nrho_eq)'
    
    iterdb['RAD_Code_Info'] = {}
    iterdb['RAD_Code_Info']['data'] = None
    iterdb['RAD_Code_Info']['units'] = None
    iterdb['RAD_Code_Info']['section'] = 'SIMULATION_INIT'
    iterdb['RAD_Code_Info']['long_name'] = 'Information: code implementing RAD component'
    iterdb['RAD_Code_Info']['component'] = 'RAD'
    iterdb['RAD_Code_Info']['specification'] = 'C*80   RAD_Code_Info'
    
    iterdb['RAD_Data_Info'] = {}
    iterdb['RAD_Data_Info']['data'] = None
    iterdb['RAD_Data_Info']['units'] = None
    iterdb['RAD_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['RAD_Data_Info']['long_name'] = 'Information on source of radiated power data'
    iterdb['RAD_Data_Info']['component'] = 'RAD'
    iterdb['RAD_Data_Info']['specification'] = 'C*80   RAD_Data_Info'
    
    iterdb['rate_sinb0i'] = {}
    iterdb['rate_sinb0i']['data'] = None
    iterdb['rate_sinb0i']['units'] = '1/sec'
    iterdb['rate_sinb0i']['section'] = 'STATE_PROFILES'
    iterdb['rate_sinb0i']['long_name'] = 'sink rate due to ionization by beam ions'
    iterdb['rate_sinb0i']['component'] = 'NBI'
    iterdb['rate_sinb0i']['specification'] = 'R|step|units=1/sec       rate_sinb0i(~nrho_nbi,nspec_gas)'
    
    iterdb['rate_sinb0x'] = {}
    iterdb['rate_sinb0x']['data'] = None
    iterdb['rate_sinb0x']['units'] = '1/sec'
    iterdb['rate_sinb0x']['section'] = 'STATE_PROFILES'
    iterdb['rate_sinb0x']['long_name'] = 'sink rate due to CX with beam ions (total)'
    iterdb['rate_sinb0x']['component'] = 'NBI'
    iterdb['rate_sinb0x']['specification'] = 'R|step|units=1/sec       rate_sinb0x(~nrho_nbi,nspec_gas)'
    
    iterdb['rate_sinb0xs'] = {}
    iterdb['rate_sinb0xs']['data'] = None
    iterdb['rate_sinb0xs']['units'] = '1/sec'
    iterdb['rate_sinb0xs']['section'] = 'STATE_PROFILES'
    iterdb['rate_sinb0xs']['long_name'] = 'sink rate due to CX with beam ions'
    iterdb['rate_sinb0xs']['component'] = 'NBI'
    iterdb['rate_sinb0xs']['specification'] = 'R|step|units=1/sec       rate_sinb0xs(~nrho_nbi,nspec_gas,nspec_beam)'
    
    iterdb['rate_sinf0i'] = {}
    iterdb['rate_sinf0i']['data'] = None
    iterdb['rate_sinf0i']['units'] = '1/sec'
    iterdb['rate_sinf0i']['section'] = 'STATE_PROFILES'
    iterdb['rate_sinf0i']['long_name'] = 'sink rate due to ionization by fusion ions'
    iterdb['rate_sinf0i']['component'] = 'FUS'
    iterdb['rate_sinf0i']['specification'] = 'R|step|units=1/sec       rate_sinf0i(~nrho_fus,nspec_gas)'
    
    iterdb['rate_sinf0x'] = {}
    iterdb['rate_sinf0x']['data'] = None
    iterdb['rate_sinf0x']['units'] = '1/sec'
    iterdb['rate_sinf0x']['section'] = 'STATE_PROFILES'
    iterdb['rate_sinf0x']['long_name'] = 'sink rate due to CX with fusion ions (total)'
    iterdb['rate_sinf0x']['component'] = 'FUS'
    iterdb['rate_sinf0x']['specification'] = 'R|step|units=1/sec       rate_sinf0x(~nrho_fus,nspec_gas)'
    
    iterdb['rate_sinf0xs'] = {}
    iterdb['rate_sinf0xs']['data'] = None
    iterdb['rate_sinf0xs']['units'] = '1/sec'
    iterdb['rate_sinf0xs']['section'] = 'STATE_PROFILES'
    iterdb['rate_sinf0xs']['long_name'] = 'sink rate due to CX with fusion ions'
    iterdb['rate_sinf0xs']['component'] = 'FUS'
    iterdb['rate_sinf0xs']['specification'] = 'R|step|units=1/sec       rate_sinf0xs(~nrho_fus,nspec_gas,nspec_fusion)'
    
    iterdb['res_sn'] = {}
    iterdb['res_sn']['data'] = None
    iterdb['res_sn']['units'] = 'Norm'
    iterdb['res_sn']['section'] = 'STATE_PROFILES'
    iterdb['res_sn']['long_name'] = 'residuals for particle transport eqn'
    iterdb['res_sn']['component'] = 'PLASMA'
    iterdb['res_sn']['specification'] = 'R|units=Norm|step*dV res_sn(~nrho,0:nspec_th)'
    
    iterdb['res_te'] = {}
    iterdb['res_te']['data'] = None
    iterdb['res_te']['units'] = 'Norm'
    iterdb['res_te']['section'] = 'STATE_PROFILES'
    iterdb['res_te']['long_name'] = 'residuals for electron transport eqn'
    iterdb['res_te']['component'] = 'PLASMA'
    iterdb['res_te']['specification'] = 'R|step*dV res_te(~nrho)'
    
    iterdb['res_ti'] = {}
    iterdb['res_ti']['data'] = None
    iterdb['res_ti']['units'] = 'Norm'
    iterdb['res_ti']['section'] = 'STATE_PROFILES'
    iterdb['res_ti']['long_name'] = 'residuals for ion transport eqn'
    iterdb['res_ti']['component'] = 'PLASMA'
    iterdb['res_ti']['specification'] = 'R|step*dV res_ti(~nrho)'
    
    iterdb['res_tq'] = {}
    iterdb['res_tq']['data'] = None
    iterdb['res_tq']['units'] = 'Norm'
    iterdb['res_tq']['section'] = 'STATE_PROFILES'
    iterdb['res_tq']['long_name'] = 'rediduals for angular momentum transport eqn'
    iterdb['res_tq']['component'] = 'PLASMA'
    iterdb['res_tq']['specification'] = 'R|units=Norm|step*dV res_tq(~nrho)'
    
    iterdb['rho'] = {}
    iterdb['rho']['data'] = None
    iterdb['rho']['units'] = None
    iterdb['rho']['section'] = 'SIMULATION_INIT'
    iterdb['rho']['long_name'] = 'rho grid (PLASMA)'
    iterdb['rho']['component'] = 'PLASMA'
    iterdb['rho']['specification'] = 'G   rho(nrho)'
    
    iterdb['rho_anom'] = {}
    iterdb['rho_anom']['data'] = None
    iterdb['rho_anom']['units'] = None
    iterdb['rho_anom']['section'] = 'SIMULATION_INIT'
    iterdb['rho_anom']['long_name'] = 'rho grid (1d anomalous transport profiles)'
    iterdb['rho_anom']['component'] = 'ANOM'
    iterdb['rho_anom']['specification'] = 'G  rho_anom(nrho_anom)'
    
    iterdb['rho_bdy_ns'] = {}
    iterdb['rho_bdy_ns']['data'] = None
    iterdb['rho_bdy_ns']['units'] = None
    iterdb['rho_bdy_ns']['section'] = 'STATE_DATA'
    iterdb['rho_bdy_ns']['long_name'] = 'locations beyond which densities are known'
    iterdb['rho_bdy_ns']['component'] = 'PLASMA'
    iterdb['rho_bdy_ns']['specification'] = 'R|units=- rho_bdy_ns(0:nspec_th)'
    
    iterdb['rho_bdy_omegat'] = {}
    iterdb['rho_bdy_omegat']['data'] = None
    iterdb['rho_bdy_omegat']['units'] = None
    iterdb['rho_bdy_omegat']['section'] = 'STATE_DATA'
    iterdb['rho_bdy_omegat']['long_name'] = 'location beyond which angular velocity is known'
    iterdb['rho_bdy_omegat']['component'] = 'PLASMA'
    iterdb['rho_bdy_omegat']['specification'] = 'R rho_bdy_omegat'
    
    iterdb['rho_bdy_Te'] = {}
    iterdb['rho_bdy_Te']['data'] = None
    iterdb['rho_bdy_Te']['units'] = None
    iterdb['rho_bdy_Te']['section'] = 'STATE_DATA'
    iterdb['rho_bdy_Te']['long_name'] = 'location beyond which Te is known'
    iterdb['rho_bdy_Te']['component'] = 'PLASMA'
    iterdb['rho_bdy_Te']['specification'] = 'R rho_bdy_Te'
    
    iterdb['rho_bdy_Ti'] = {}
    iterdb['rho_bdy_Ti']['data'] = None
    iterdb['rho_bdy_Ti']['units'] = None
    iterdb['rho_bdy_Ti']['section'] = 'STATE_DATA'
    iterdb['rho_bdy_Ti']['long_name'] = 'location beyond which Ti is known'
    iterdb['rho_bdy_Ti']['component'] = 'PLASMA'
    iterdb['rho_bdy_Ti']['specification'] = 'R rho_bdy_Ti'
    
    iterdb['rho_ecrf'] = {}
    iterdb['rho_ecrf']['data'] = None
    iterdb['rho_ecrf']['units'] = None
    iterdb['rho_ecrf']['section'] = 'SIMULATION_INIT'
    iterdb['rho_ecrf']['long_name'] = 'rho grid -- ECRF'
    iterdb['rho_ecrf']['component'] = 'EC'
    iterdb['rho_ecrf']['specification'] = 'G  rho_ecrf(nrho_ecrf)'
    
    iterdb['rho_eq'] = {}
    iterdb['rho_eq']['data'] = None
    iterdb['rho_eq']['units'] = None
    iterdb['rho_eq']['section'] = 'SIMULATION_INIT'
    iterdb['rho_eq']['long_name'] = 'rho grid (EQ)'
    iterdb['rho_eq']['component'] = 'EQ'
    iterdb['rho_eq']['specification'] = 'G   rho_eq(nrho_eq)'
    
    iterdb['rho_eq_geo'] = {}
    iterdb['rho_eq_geo']['data'] = None
    iterdb['rho_eq_geo']['units'] = None
    iterdb['rho_eq_geo']['section'] = 'SIMULATION_INIT'
    iterdb['rho_eq_geo']['long_name'] = 'rho grid (EQ flux surface averages)'
    iterdb['rho_eq_geo']['component'] = 'EQ'
    iterdb['rho_eq_geo']['specification'] = 'G   rho_eq_geo(nrho_eq_geo)'
    
    iterdb['rho_fus'] = {}
    iterdb['rho_fus']['data'] = None
    iterdb['rho_fus']['units'] = None
    iterdb['rho_fus']['section'] = 'SIMULATION_INIT'
    iterdb['rho_fus']['long_name'] = 'rho grid -- Fusion products model'
    iterdb['rho_fus']['component'] = 'FUS'
    iterdb['rho_fus']['specification'] = 'G  rho_fus(nrho_fus)'
    
    iterdb['rho_gas'] = {}
    iterdb['rho_gas']['data'] = None
    iterdb['rho_gas']['units'] = None
    iterdb['rho_gas']['section'] = 'SIMULATION_INIT'
    iterdb['rho_gas']['long_name'] = 'rho grid (GAS -- neutral gas model)'
    iterdb['rho_gas']['component'] = 'GAS'
    iterdb['rho_gas']['specification'] = 'G  rho_gas(nrho_gas)'
    
    iterdb['rho_nbi'] = {}
    iterdb['rho_nbi']['data'] = None
    iterdb['rho_nbi']['units'] = None
    iterdb['rho_nbi']['section'] = 'SIMULATION_INIT'
    iterdb['rho_nbi']['long_name'] = 'rho grid -- NBI'
    iterdb['rho_nbi']['component'] = 'NBI'
    iterdb['rho_nbi']['specification'] = 'G  rho_nbi(nrho_nbi)'
    
    iterdb['rho_rad'] = {}
    iterdb['rho_rad']['data'] = None
    iterdb['rho_rad']['units'] = None
    iterdb['rho_rad']['section'] = 'SIMULATION_INIT'
    iterdb['rho_rad']['long_name'] = 'rho grid (RAD)'
    iterdb['rho_rad']['component'] = 'RAD'
    iterdb['rho_rad']['specification'] = 'G  rho_rad(nrho_rad)'
    
    iterdb['rlim'] = {}
    iterdb['rlim']['data'] = None
    iterdb['rlim']['units'] = 'm'
    iterdb['rlim']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['rlim']['long_name'] = 'R points in closed (R,Z) contour sequence'
    iterdb['rlim']['component'] = 'EQ'
    iterdb['rlim']['specification'] = 'R|units=m  rlim(num_rzlim)'
    
    iterdb['Rmajor_mean'] = {}
    iterdb['Rmajor_mean']['data'] = None
    iterdb['Rmajor_mean']['units'] = 'm'
    iterdb['Rmajor_mean']['section'] = 'STATE_PROFILES'
    iterdb['Rmajor_mean']['long_name'] = 'Rmajor_mean = (R_Surfmax+R_surfmin)/2'
    iterdb['Rmajor_mean']['component'] = 'EQ'
    iterdb['Rmajor_mean']['specification'] = 'R|pclin  Rmajor_mean(nrho_eq_geo)'
    
    iterdb['rMinor_mean'] = {}
    iterdb['rMinor_mean']['data'] = None
    iterdb['rMinor_mean']['units'] = 'm'
    iterdb['rMinor_mean']['section'] = 'STATE_PROFILES'
    iterdb['rMinor_mean']['long_name'] = 'rMinor_mean = (R_Surfmax-R_surfmin)/2'
    iterdb['rMinor_mean']['component'] = 'EQ'
    iterdb['rMinor_mean']['specification'] = 'R|pclin  rMinor_mean(nrho_eq_geo)'
    
    iterdb['RUNAWAY_Code_Info'] = {}
    iterdb['RUNAWAY_Code_Info']['data'] = None
    iterdb['RUNAWAY_Code_Info']['units'] = None
    iterdb['RUNAWAY_Code_Info']['section'] = 'SIMULATION_INIT'
    iterdb['RUNAWAY_Code_Info']['long_name'] = 'Information: code implementing RUNAWAY component'
    iterdb['RUNAWAY_Code_Info']['component'] = 'RUNAWAY'
    iterdb['RUNAWAY_Code_Info']['specification'] = 'C*80   RUNAWAY_Code_Info'
    
    iterdb['RunID'] = {}
    iterdb['RunID']['data'] = None
    iterdb['RunID']['units'] = None
    iterdb['RunID']['section'] = 'SIMULATION_INIT'
    iterdb['RunID']['long_name'] = 'Run ID'
    iterdb['RunID']['component'] = 'PLASMA'
    iterdb['RunID']['specification'] = 'N      RunID'
    
    iterdb['R_axis'] = {}
    iterdb['R_axis']['data'] = None
    iterdb['R_axis']['units'] = 'm'
    iterdb['R_axis']['section'] = 'STATE_DATA'
    iterdb['R_axis']['long_name'] = 'R of magnetic axis'
    iterdb['R_axis']['component'] = 'EQ'
    iterdb['R_axis']['specification'] = 'R  R_axis'
    
    iterdb['R_EC_launch'] = {}
    iterdb['R_EC_launch']['data'] = None
    iterdb['R_EC_launch']['units'] = 'm'
    iterdb['R_EC_launch']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['R_EC_launch']['long_name'] = 'R of center of launcher'
    iterdb['R_EC_launch']['component'] = 'EC'
    iterdb['R_EC_launch']['specification'] = 'R|units=m   R_EC_launch(necrf_src)'
    
    iterdb['R_geo'] = {}
    iterdb['R_geo']['data'] = None
    iterdb['R_geo']['units'] = 'm'
    iterdb['R_geo']['section'] = 'STATE_PROFILES'
    iterdb['R_geo']['long_name'] = 'flux surfaces R(rho,theta)'
    iterdb['R_geo']['component'] = 'EQ'
    iterdb['R_geo']['specification'] = 'R|units=m|Hermite_explicit R_geo(nrho_eq,nth_eq)'
    
    iterdb['R_grid'] = {}
    iterdb['R_grid']['data'] = None
    iterdb['R_grid']['units'] = 'm'
    iterdb['R_grid']['section'] = 'SIMULATION_INIT'
    iterdb['R_grid']['long_name'] = 'R grid'
    iterdb['R_grid']['component'] = 'EQ'
    iterdb['R_grid']['specification'] = 'G   R_grid(nR)'
    
    iterdb['R_max_box'] = {}
    iterdb['R_max_box']['data'] = None
    iterdb['R_max_box']['units'] = 'm'
    iterdb['R_max_box']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['R_max_box']['long_name'] = 'R_max of bounding box'
    iterdb['R_max_box']['component'] = 'EQ'
    iterdb['R_max_box']['specification'] = 'R  R_max_box'
    
    iterdb['R_max_lcfs'] = {}
    iterdb['R_max_lcfs']['data'] = None
    iterdb['R_max_lcfs']['units'] = 'm'
    iterdb['R_max_lcfs']['section'] = 'STATE_DATA'
    iterdb['R_max_lcfs']['long_name'] = 'R_max of last closed flux surface'
    iterdb['R_max_lcfs']['component'] = 'EQ'
    iterdb['R_max_lcfs']['specification'] = 'R  R_max_lcfs'
    
    iterdb['R_midp_in'] = {}
    iterdb['R_midp_in']['data'] = None
    iterdb['R_midp_in']['units'] = 'm'
    iterdb['R_midp_in']['section'] = 'STATE_PROFILES'
    iterdb['R_midp_in']['long_name'] = 'R (high field side) midplane intercept'
    iterdb['R_midp_in']['component'] = 'EQ'
    iterdb['R_midp_in']['specification'] = 'R|pclin  R_midp_in(nrho_eq_geo)'
    
    iterdb['R_midp_out'] = {}
    iterdb['R_midp_out']['data'] = None
    iterdb['R_midp_out']['units'] = 'm'
    iterdb['R_midp_out']['section'] = 'STATE_PROFILES'
    iterdb['R_midp_out']['long_name'] = 'R (low field side) midplane intercept'
    iterdb['R_midp_out']['component'] = 'EQ'
    iterdb['R_midp_out']['specification'] = 'R|pclin  R_midp_out(nrho_eq_geo)'
    
    iterdb['R_min_box'] = {}
    iterdb['R_min_box']['data'] = None
    iterdb['R_min_box']['units'] = 'm'
    iterdb['R_min_box']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['R_min_box']['long_name'] = 'R_min of bounding box'
    iterdb['R_min_box']['component'] = 'EQ'
    iterdb['R_min_box']['specification'] = 'R  R_min_box'
    
    iterdb['R_min_lcfs'] = {}
    iterdb['R_min_lcfs']['data'] = None
    iterdb['R_min_lcfs']['units'] = 'm'
    iterdb['R_min_lcfs']['section'] = 'STATE_DATA'
    iterdb['R_min_lcfs']['long_name'] = 'R_min of last closed flux surface'
    iterdb['R_min_lcfs']['component'] = 'EQ'
    iterdb['R_min_lcfs']['specification'] = 'R  R_min_lcfs'
    
    iterdb['R_surfMax'] = {}
    iterdb['R_surfMax']['data'] = None
    iterdb['R_surfMax']['units'] = 'm'
    iterdb['R_surfMax']['section'] = 'STATE_PROFILES'
    iterdb['R_surfMax']['long_name'] = 'max R on flux surface'
    iterdb['R_surfMax']['component'] = 'EQ'
    iterdb['R_surfMax']['specification'] = 'R|pclin  R_surfMax(nrho_eq_geo)'
    
    iterdb['R_surfMin'] = {}
    iterdb['R_surfMin']['data'] = None
    iterdb['R_surfMin']['units'] = 'm'
    iterdb['R_surfMin']['section'] = 'STATE_PROFILES'
    iterdb['R_surfMin']['long_name'] = 'min R on flux surface'
    iterdb['R_surfMin']['component'] = 'EQ'
    iterdb['R_surfMin']['specification'] = 'R|pclin  R_surfMin(nrho_eq_geo)'
    
    iterdb['s0reco'] = {}
    iterdb['s0reco']['data'] = None
    iterdb['s0reco']['units'] = '#/sec'
    iterdb['s0reco']['section'] = 'STATE_PROFILES'
    iterdb['s0reco']['long_name'] = 'recombination neutral sce'
    iterdb['s0reco']['component'] = 'GAS'
    iterdb['s0reco']['specification'] = 'R|step*dV|units=#/sec s0reco(~nrho_gas,nspec_gas)'
    
    iterdb['s0reco_e'] = {}
    iterdb['s0reco_e']['data'] = None
    iterdb['s0reco_e']['units'] = '#/sec'
    iterdb['s0reco_e']['section'] = 'STATE_PROFILES'
    iterdb['s0reco_e']['long_name'] = 'net electron source associated with recombination:'
    iterdb['s0reco_e']['component'] = 'GAS'
    iterdb['s0reco_e']['specification'] = 'R|step*dV|units=#/sec s0reco_e(~nrho_gas)'
    
    iterdb['s0reco_recap'] = {}
    iterdb['s0reco_recap']['data'] = None
    iterdb['s0reco_recap']['units'] = '#/sec'
    iterdb['s0reco_recap']['section'] = 'STATE_PROFILES'
    iterdb['s0reco_recap']['long_name'] = 'recombination neutrals recapture'
    iterdb['s0reco_recap']['component'] = 'GAS'
    iterdb['s0reco_recap']['specification'] = 'R|step*dV|units=#/sec s0reco_recap(~nrho_gas,nspec_gas)'
    
    iterdb['sa_index'] = {}
    iterdb['sa_index']['data'] = None
    iterdb['sa_index']['units'] = None
    iterdb['sa_index']['section'] = 'SIMULATION_INIT'
    iterdb['sa_index']['long_name'] = 'species index in original lists'
    iterdb['sa_index']['component'] = 'PLASMA'
    iterdb['sa_index']['specification'] = 'I sa_index(0:nspec_all)'
    
    iterdb['SA_name'] = {}
    iterdb['SA_name']['data'] = None
    iterdb['SA_name']['units'] = None
    iterdb['SA_name']['section'] = 'SIMULATION_INIT'
    iterdb['SA_name']['long_name'] = 'thermal species abridged'
    iterdb['SA_name']['component'] = 'PLASMA'
    iterdb['SA_name']['specification'] = 'S|thermal_specie  SA(0:nspec_tha)'
    
    iterdb['SA_type'] = {}
    iterdb['SA_type']['data'] = None
    iterdb['SA_type']['units'] = None
    iterdb['SA_type']['section'] = 'SIMULATION_INIT'
    iterdb['SA_type']['long_name'] = 'SA specie types'
    iterdb['SA_type']['component'] = 'PLASMA'
    iterdb['SA_type']['specification'] = 'S|thermal_specie  SA(0:nspec_tha)'
    
    iterdb['sb0halo'] = {}
    iterdb['sb0halo']['data'] = None
    iterdb['sb0halo']['units'] = '#/sec'
    iterdb['sb0halo']['section'] = 'STATE_PROFILES'
    iterdb['sb0halo']['long_name'] = 'beam dep cx sink'
    iterdb['sb0halo']['component'] = 'NBI'
    iterdb['sb0halo']['specification'] = 'R|step*dV|units=#/sec sb0halo(~nrho_nbi,nspec_gas)'
    
    iterdb['sb0halo_recap'] = {}
    iterdb['sb0halo_recap']['data'] = None
    iterdb['sb0halo_recap']['units'] = '#/sec'
    iterdb['sb0halo_recap']['section'] = 'STATE_PROFILES'
    iterdb['sb0halo_recap']['long_name'] = 'cx neutral recapture'
    iterdb['sb0halo_recap']['component'] = 'NBI'
    iterdb['sb0halo_recap']['specification'] = 'R|step*dV|units=#/sec sb0halo_recap(~nrho_nbi,nspec_gas)'
    
    iterdb['sbedep'] = {}
    iterdb['sbedep']['data'] = None
    iterdb['sbedep']['units'] = '#/sec'
    iterdb['sbedep']['section'] = 'STATE_PROFILES'
    iterdb['sbedep']['long_name'] = 'beam deposition cold electron sce'
    iterdb['sbedep']['component'] = 'NBI'
    iterdb['sbedep']['specification'] = 'R|step*dV|units=#/sec sbedep(~nrho_nbi)'
    
    iterdb['sbehalo'] = {}
    iterdb['sbehalo']['data'] = None
    iterdb['sbehalo']['units'] = '#/sec'
    iterdb['sbehalo']['section'] = 'STATE_PROFILES'
    iterdb['sbehalo']['long_name'] = 'cold electron sce due to'
    iterdb['sbehalo']['component'] = 'NBI'
    iterdb['sbehalo']['specification'] = 'R|step*dV|units=#/sec sbehalo(~nrho_nbi)'
    
    iterdb['sbsce'] = {}
    iterdb['sbsce']['data'] = None
    iterdb['sbsce']['units'] = '#/sec'
    iterdb['sbsce']['section'] = 'STATE_PROFILES'
    iterdb['sbsce']['long_name'] = 'net source, thermal ions & electrons'
    iterdb['sbsce']['component'] = 'NBI'
    iterdb['sbsce']['specification'] = 'R|step*dV|units=#/sec   sbsce(~nrho_nbi,0:nspec_tha)'
    
    iterdb['sbtherm'] = {}
    iterdb['sbtherm']['data'] = None
    iterdb['sbtherm']['units'] = '#/sec'
    iterdb['sbtherm']['section'] = 'STATE_PROFILES'
    iterdb['sbtherm']['long_name'] = 'beam ion thermalization'
    iterdb['sbtherm']['component'] = 'NBI'
    iterdb['sbtherm']['specification'] = 'R|step*dV|units=#/sec sbtherm(~nrho_nbi,nspec_beam)'
    
    iterdb['sc0'] = {}
    iterdb['sc0']['data'] = None
    iterdb['sc0']['units'] = '#/sec'
    iterdb['sc0']['section'] = 'STATE_DATA'
    iterdb['sc0']['long_name'] = 'edge neutral sources (atoms/sec)'
    iterdb['sc0']['component'] = 'GAS'
    iterdb['sc0']['specification'] = 'R|units=#/sec  sc0(ngsc0)'
    
    iterdb['sc0_to_sgas'] = {}
    iterdb['sc0_to_sgas']['data'] = None
    iterdb['sc0_to_sgas']['units'] = None
    iterdb['sc0_to_sgas']['section'] = 'SIMULATION_INIT'
    iterdb['sc0_to_sgas']['long_name'] = 'index map from neutral source to neutral species'
    iterdb['sc0_to_sgas']['component'] = 'GAS'
    iterdb['sc0_to_sgas']['specification'] = 'I  sc0_to_sgas(ngsc0)'
    
    iterdb['sfsce'] = {}
    iterdb['sfsce']['data'] = None
    iterdb['sfsce']['units'] = '#/sec'
    iterdb['sfsce']['section'] = 'STATE_PROFILES'
    iterdb['sfsce']['long_name'] = 'net thermalization source of fusion ions'
    iterdb['sfsce']['component'] = 'FUS'
    iterdb['sfsce']['specification'] = 'R|step*dV|units=#/sec   sfsce(~nrho_fus,0:nspec_tha)'
    
    iterdb['sftherm'] = {}
    iterdb['sftherm']['data'] = None
    iterdb['sftherm']['units'] = '#/sec'
    iterdb['sftherm']['section'] = 'STATE_PROFILES'
    iterdb['sftherm']['long_name'] = 'fusion ion thermalization'
    iterdb['sftherm']['component'] = 'FUS'
    iterdb['sftherm']['specification'] = 'R|step*dV|units=#/sec   sftherm(~nrho_fus,nspec_fusion)'
    
    iterdb['SFUS_name'] = {}
    iterdb['SFUS_name']['data'] = None
    iterdb['SFUS_name']['units'] = None
    iterdb['SFUS_name']['section'] = 'SHOT_CONFIGURATION'
    iterdb['SFUS_name']['long_name'] = 'fusion product ion species'
    iterdb['SFUS_name']['component'] = 'FUS'
    iterdb['SFUS_name']['specification'] = 'S|fusion_ion   SFUS(nspec_fusion)'
    
    iterdb['sfus_to_all'] = {}
    iterdb['sfus_to_all']['data'] = None
    iterdb['sfus_to_all']['units'] = None
    iterdb['sfus_to_all']['section'] = 'SIMULATION_INIT'
    iterdb['sfus_to_all']['long_name'] = 'map sfus index to "all" list'
    iterdb['sfus_to_all']['component'] = 'PLASMA'
    iterdb['sfus_to_all']['specification'] = 'I  sfus_to_all(nspec_fusion)'
    
    iterdb['sfus_to_alla'] = {}
    iterdb['sfus_to_alla']['data'] = None
    iterdb['sfus_to_alla']['units'] = None
    iterdb['sfus_to_alla']['section'] = 'SIMULATION_INIT'
    iterdb['sfus_to_alla']['long_name'] = 'map sfus index to "alla" list'
    iterdb['sfus_to_alla']['component'] = 'PLASMA'
    iterdb['sfus_to_alla']['specification'] = 'I  sfus_to_alla(nspec_fusion)'
    
    iterdb['SFUS_type'] = {}
    iterdb['SFUS_type']['data'] = None
    iterdb['SFUS_type']['units'] = None
    iterdb['SFUS_type']['section'] = 'SHOT_CONFIGURATION'
    iterdb['SFUS_type']['long_name'] = 'SFUS specie types'
    iterdb['SFUS_type']['component'] = 'FUS'
    iterdb['SFUS_type']['specification'] = 'S|fusion_ion   SFUS(nspec_fusion)'
    
    iterdb['SGAS_name'] = {}
    iterdb['SGAS_name']['data'] = None
    iterdb['SGAS_name']['units'] = None
    iterdb['SGAS_name']['section'] = 'SIMULATION_INIT'
    iterdb['SGAS_name']['long_name'] = 'atomic neutral species in plasma core'
    iterdb['SGAS_name']['component'] = 'GAS'
    iterdb['SGAS_name']['specification'] = 'S|neutral_gas  SGAS(nspec_gas)'
    
    iterdb['sgas_to_s'] = {}
    iterdb['sgas_to_s']['data'] = None
    iterdb['sgas_to_s']['units'] = None
    iterdb['sgas_to_s']['section'] = 'SIMULATION_INIT'
    iterdb['sgas_to_s']['long_name'] = 'map sgas index to "s" list'
    iterdb['sgas_to_s']['component'] = 'GAS'
    iterdb['sgas_to_s']['specification'] = 'I  sgas_to_s(nspec_gas)'
    
    iterdb['SGAS_type'] = {}
    iterdb['SGAS_type']['data'] = None
    iterdb['SGAS_type']['units'] = None
    iterdb['SGAS_type']['section'] = 'SIMULATION_INIT'
    iterdb['SGAS_type']['long_name'] = 'SGAS specie types'
    iterdb['SGAS_type']['component'] = 'GAS'
    iterdb['SGAS_type']['specification'] = 'S|neutral_gas  SGAS(nspec_gas)'
    
    iterdb['shot_number'] = {}
    iterdb['shot_number']['data'] = None
    iterdb['shot_number']['units'] = None
    iterdb['shot_number']['section'] = 'SHOT_CONFIGURATION'
    iterdb['shot_number']['long_name'] = 'integer shot number'
    iterdb['shot_number']['component'] = 'PLASMA'
    iterdb['shot_number']['specification'] = 'I shot_number'
    
    iterdb['SIMP0_name'] = {}
    iterdb['SIMP0_name']['data'] = None
    iterdb['SIMP0_name']['units'] = None
    iterdb['SIMP0_name']['section'] = 'SIMULATION_INIT'
    iterdb['SIMP0_name']['long_name'] = 'atomic impurity species in simulation'
    iterdb['SIMP0_name']['component'] = 'GAS'
    iterdb['SIMP0_name']['specification'] = 'S|impurity_atoms SIMP0(nspec_imp0)'
    
    iterdb['simp0_to_s'] = {}
    iterdb['simp0_to_s']['data'] = None
    iterdb['simp0_to_s']['units'] = None
    iterdb['simp0_to_s']['section'] = 'SIMULATION_INIT'
    iterdb['simp0_to_s']['long_name'] = 'map simp0 index to "s" list'
    iterdb['simp0_to_s']['component'] = 'GAS'
    iterdb['simp0_to_s']['specification'] = 'I  simp0_to_s(nspec_imp0)'
    
    iterdb['SIMP0_type'] = {}
    iterdb['SIMP0_type']['data'] = None
    iterdb['SIMP0_type']['units'] = None
    iterdb['SIMP0_type']['section'] = 'SIMULATION_INIT'
    iterdb['SIMP0_type']['long_name'] = 'SIMP0 specie types'
    iterdb['SIMP0_type']['component'] = 'GAS'
    iterdb['SIMP0_type']['specification'] = 'S|impurity_atoms SIMP0(nspec_imp0)'
    
    iterdb['SIMPI_name'] = {}
    iterdb['SIMPI_name']['data'] = None
    iterdb['SIMPI_name']['units'] = None
    iterdb['SIMPI_name']['section'] = 'SIMULATION_INIT'
    iterdb['SIMPI_name']['long_name'] = 'impurity ion species in simulation'
    iterdb['SIMPI_name']['component'] = 'PLASMA'
    iterdb['SIMPI_name']['specification'] = 'S|impurity_atoms SIMPI(nspec_impi)'
    
    iterdb['simpi_to_s'] = {}
    iterdb['simpi_to_s']['data'] = None
    iterdb['simpi_to_s']['units'] = None
    iterdb['simpi_to_s']['section'] = 'SIMULATION_INIT'
    iterdb['simpi_to_s']['long_name'] = 'map simpi index to "s" list'
    iterdb['simpi_to_s']['component'] = 'PLASMA'
    iterdb['simpi_to_s']['specification'] = 'I  simpi_to_s(nspec_impi)'
    
    iterdb['SIMPI_type'] = {}
    iterdb['SIMPI_type']['data'] = None
    iterdb['SIMPI_type']['units'] = None
    iterdb['SIMPI_type']['section'] = 'SIMULATION_INIT'
    iterdb['SIMPI_type']['long_name'] = 'SIMPI specie types'
    iterdb['SIMPI_type']['component'] = 'PLASMA'
    iterdb['SIMPI_type']['specification'] = 'S|impurity_atoms SIMPI(nspec_impi)'
    
    iterdb['SNBI_name'] = {}
    iterdb['SNBI_name']['data'] = None
    iterdb['SNBI_name']['units'] = None
    iterdb['SNBI_name']['section'] = 'SIMULATION_INIT'
    iterdb['SNBI_name']['long_name'] = 'beam ion species'
    iterdb['SNBI_name']['component'] = 'NBI'
    iterdb['SNBI_name']['specification'] = 'S|beam_ion     SNBI(nspec_beam)'
    
    iterdb['snbi_to_all'] = {}
    iterdb['snbi_to_all']['data'] = None
    iterdb['snbi_to_all']['units'] = None
    iterdb['snbi_to_all']['section'] = 'SIMULATION_INIT'
    iterdb['snbi_to_all']['long_name'] = 'map snbi index to "all" list'
    iterdb['snbi_to_all']['component'] = 'PLASMA'
    iterdb['snbi_to_all']['specification'] = 'I  snbi_to_all(nspec_beam)'
    
    iterdb['snbi_to_alla'] = {}
    iterdb['snbi_to_alla']['data'] = None
    iterdb['snbi_to_alla']['units'] = None
    iterdb['snbi_to_alla']['section'] = 'SIMULATION_INIT'
    iterdb['snbi_to_alla']['long_name'] = 'map snbi index to "alla" list'
    iterdb['snbi_to_alla']['component'] = 'PLASMA'
    iterdb['snbi_to_alla']['specification'] = 'I  snbi_to_alla(nspec_beam)'
    
    iterdb['SNBI_type'] = {}
    iterdb['SNBI_type']['data'] = None
    iterdb['SNBI_type']['units'] = None
    iterdb['SNBI_type']['section'] = 'SIMULATION_INIT'
    iterdb['SNBI_type']['long_name'] = 'SNBI specie types'
    iterdb['SNBI_type']['component'] = 'NBI'
    iterdb['SNBI_type']['specification'] = 'S|beam_ion     SNBI(nspec_beam)'
    
    iterdb['sn_trans'] = {}
    iterdb['sn_trans']['data'] = None
    iterdb['sn_trans']['units'] = '#/sec'
    iterdb['sn_trans']['section'] = 'STATE_PROFILES'
    iterdb['sn_trans']['long_name'] = 'particle transport (loss)'
    iterdb['sn_trans']['component'] = 'PLASMA'
    iterdb['sn_trans']['specification'] = 'R|units=#/sec|step*dV sn_trans(~nrho,0:nspec_th)'
    
    iterdb['sprof0'] = {}
    iterdb['sprof0']['data'] = None
    iterdb['sprof0']['units'] = '(#/sec)/(#/sec)'
    iterdb['sprof0']['section'] = 'STATE_PROFILES'
    iterdb['sprof0']['long_name'] = 'gas species source/sinks per unit species influx'
    iterdb['sprof0']['component'] = 'GAS'
    iterdb['sprof0']['specification'] = 'R|step*dV|units=(#/sec)/(#/sec)  sprof0(~nrho_gas,nspec_gas,ngsc0)'
    
    iterdb['sprof0e'] = {}
    iterdb['sprof0e']['data'] = None
    iterdb['sprof0e']['units'] = '(#/sec)/(#/sec)'
    iterdb['sprof0e']['section'] = 'STATE_PROFILES'
    iterdb['sprof0e']['long_name'] = 'electron source per unit neutral species influx'
    iterdb['sprof0e']['component'] = 'GAS'
    iterdb['sprof0e']['specification'] = 'R|step*dV|units=(#/sec)/(#/sec)  sprof0e(~nrho_gas,ngsc0)'
    
    iterdb['squareLO'] = {}
    iterdb['squareLO']['data'] = None
    iterdb['squareLO']['units'] = None
    iterdb['squareLO']['section'] = 'STATE_PROFILES'
    iterdb['squareLO']['long_name'] = 'lower outer squareness'
    iterdb['squareLO']['component'] = 'EQ'
    iterdb['squareLO']['specification'] = 'R|pclin  squareLO(nrho_eq_geo)'
    
    iterdb['squareUO'] = {}
    iterdb['squareUO']['data'] = None
    iterdb['squareUO']['units'] = None
    iterdb['squareUO']['section'] = 'STATE_PROFILES'
    iterdb['squareUO']['long_name'] = 'upper outer squareness'
    iterdb['squareUO']['component'] = 'EQ'
    iterdb['squareUO']['specification'] = 'R|pclin  squareUO(nrho_eq_geo)'
    
    iterdb['sRtcen'] = {}
    iterdb['sRtcen']['data'] = None
    iterdb['sRtcen']['units'] = 'm'
    iterdb['sRtcen']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['sRtcen']['long_name'] = 'signed tangency radius'
    iterdb['sRtcen']['component'] = 'NBI'
    iterdb['sRtcen']['specification'] = 'R|units=m       sRtcen(nbeam)'
    
    iterdb['surf'] = {}
    iterdb['surf']['data'] = None
    iterdb['surf']['units'] = 'm^2'
    iterdb['surf']['section'] = 'STATE_PROFILES'
    iterdb['surf']['long_name'] = 'area of flux surfaces'
    iterdb['surf']['component'] = 'EQ'
    iterdb['surf']['specification'] = 'R|units=m^2|Spline surf(nrho_eq)'
    
    iterdb['S_name'] = {}
    iterdb['S_name']['data'] = None
    iterdb['S_name']['units'] = None
    iterdb['S_name']['section'] = 'SHOT_CONFIGURATION'
    iterdb['S_name']['long_name'] = 'thermal species list'
    iterdb['S_name']['component'] = 'PLASMA'
    iterdb['S_name']['specification'] = 'S|thermal_specie  S(0:nspec_th)'
    
    iterdb['s_to_sa'] = {}
    iterdb['s_to_sa']['data'] = None
    iterdb['s_to_sa']['units'] = None
    iterdb['s_to_sa']['section'] = 'SIMULATION_INIT'
    iterdb['s_to_sa']['long_name'] = 'address in sa species list'
    iterdb['s_to_sa']['component'] = 'PLASMA'
    iterdb['s_to_sa']['specification'] = 'I s_to_sa(0:nspec_th)'
    
    iterdb['S_type'] = {}
    iterdb['S_type']['data'] = None
    iterdb['S_type']['units'] = None
    iterdb['S_type']['section'] = 'SHOT_CONFIGURATION'
    iterdb['S_type']['long_name'] = 'S specie types'
    iterdb['S_type']['component'] = 'PLASMA'
    iterdb['S_type']['specification'] = 'S|thermal_specie  S(0:nspec_th)'
    
    iterdb['t0'] = {}
    iterdb['t0']['data'] = None
    iterdb['t0']['units'] = 'sec'
    iterdb['t0']['section'] = 'STATE_DATA'
    iterdb['t0']['long_name'] = 'time at beginning of IPS macro timestep'
    iterdb['t0']['component'] = 'PLASMA'
    iterdb['t0']['specification'] = 'R  t0'
    
    iterdb['T0cx'] = {}
    iterdb['T0cx']['data'] = None
    iterdb['T0cx']['units'] = 'keV'
    iterdb['T0cx']['section'] = 'STATE_PROFILES'
    iterdb['T0cx']['long_name'] = 'effective neutral temperature for CX power'
    iterdb['T0cx']['component'] = 'GAS'
    iterdb['T0cx']['specification'] = 'R|step*qqcx|units=keV  T0cx(~nrho_gas,ngsc0)'
    
    iterdb['T0sc0'] = {}
    iterdb['T0sc0']['data'] = None
    iterdb['T0sc0']['units'] = 'keV'
    iterdb['T0sc0']['section'] = 'STATE_PROFILES'
    iterdb['T0sc0']['long_name'] = 'neutral temperature (2/3)<E0>'
    iterdb['T0sc0']['component'] = 'GAS'
    iterdb['T0sc0']['specification'] = 'R|step*n0norm|units=keV        T0sc0(~nrho_gas,nspec_gas,ngsc0)'
    
    iterdb['T0_halo'] = {}
    iterdb['T0_halo']['data'] = None
    iterdb['T0_halo']['units'] = 'keV'
    iterdb['T0_halo']['section'] = 'STATE_PROFILES'
    iterdb['T0_halo']['long_name'] = 'halo neutral temperature (2/3)<E0>'
    iterdb['T0_halo']['component'] = 'NBI'
    iterdb['T0_halo']['specification'] = 'R|units=keV|step*n0_halo  T0_halo(~nrho_nbi,nspec_gas)'
    
    iterdb['T0_reco'] = {}
    iterdb['T0_reco']['data'] = None
    iterdb['T0_reco']['units'] = 'keV'
    iterdb['T0_reco']['section'] = 'STATE_PROFILES'
    iterdb['T0_reco']['long_name'] = 'reco neutral temperature (2/3)<E0>'
    iterdb['T0_reco']['component'] = 'GAS'
    iterdb['T0_reco']['specification'] = 'R|units=keV|step*n0_reco  T0_reco(~nrho_gas,nspec_gas)'
    
    iterdb['t1'] = {}
    iterdb['t1']['data'] = None
    iterdb['t1']['units'] = 'sec'
    iterdb['t1']['section'] = 'STATE_DATA'
    iterdb['t1']['long_name'] = 'time at end of IPS macro timestep'
    iterdb['t1']['component'] = 'PLASMA'
    iterdb['t1']['specification'] = 'R  t1'
    
    iterdb['Te_bdy'] = {}
    iterdb['Te_bdy']['data'] = None
    iterdb['Te_bdy']['units'] = 'KeV'
    iterdb['Te_bdy']['section'] = 'STATE_DATA'
    iterdb['Te_bdy']['long_name'] = 'Electron temperature at/beyond boundary'
    iterdb['Te_bdy']['component'] = 'PLASMA'
    iterdb['Te_bdy']['specification'] = 'R Te_bdy'
    
    iterdb['tfinal'] = {}
    iterdb['tfinal']['data'] = None
    iterdb['tfinal']['units'] = 'sec'
    iterdb['tfinal']['section'] = 'SIMULATION_INIT'
    iterdb['tfinal']['long_name'] = 'stop time of simulation (may be adjustable)'
    iterdb['tfinal']['component'] = 'PLASMA'
    iterdb['tfinal']['specification'] = 'R  tfinal'
    
    iterdb['TF_Data_Info'] = {}
    iterdb['TF_Data_Info']['data'] = None
    iterdb['TF_Data_Info']['units'] = None
    iterdb['TF_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['TF_Data_Info']['long_name'] = 'information on source of toroidal field data'
    iterdb['TF_Data_Info']['component'] = 'PLASMA'
    iterdb['TF_Data_Info']['specification'] = 'C*80   TF_Data_Info'
    
    iterdb['th_eq'] = {}
    iterdb['th_eq']['data'] = None
    iterdb['th_eq']['units'] = 'rad'
    iterdb['th_eq']['section'] = 'SIMULATION_INIT'
    iterdb['th_eq']['long_name'] = 'theta grid (EQ)'
    iterdb['th_eq']['component'] = 'EQ'
    iterdb['th_eq']['specification'] = 'G|CCW   th_eq(nth_eq)'
    
    iterdb['Ti'] = {}
    iterdb['Ti']['data'] = None
    iterdb['Ti']['units'] = 'keV'
    iterdb['Ti']['section'] = 'STATE_PROFILES'
    iterdb['Ti']['long_name'] = 'ion temperature'
    iterdb['Ti']['component'] = 'PLASMA'
    iterdb['Ti']['specification'] = 'R|units=keV|step*ni Ti(~nrho)'
    
    iterdb['tinit'] = {}
    iterdb['tinit']['data'] = None
    iterdb['tinit']['units'] = 'sec'
    iterdb['tinit']['section'] = 'SIMULATION_INIT'
    iterdb['tinit']['long_name'] = 'start time of simulation'
    iterdb['tinit']['component'] = 'PLASMA'
    iterdb['tinit']['specification'] = 'R  tinit'
    
    iterdb['Ti_bdy'] = {}
    iterdb['Ti_bdy']['data'] = None
    iterdb['Ti_bdy']['units'] = 'KeV'
    iterdb['Ti_bdy']['section'] = 'STATE_DATA'
    iterdb['Ti_bdy']['long_name'] = 'Ion temperature at/beyond boundary'
    iterdb['Ti_bdy']['component'] = 'PLASMA'
    iterdb['Ti_bdy']['specification'] = 'R Ti_bdy'
    
    iterdb['tmodel_bdy'] = {}
    iterdb['tmodel_bdy']['data'] = None
    iterdb['tmodel_bdy']['units'] = 'keV'
    iterdb['tmodel_bdy']['section'] = 'STATE_DATA'
    iterdb['tmodel_bdy']['long_name'] = 'model temperature, boundary value'
    iterdb['tmodel_bdy']['component'] = 'ANOM'
    iterdb['tmodel_bdy']['specification'] = 'R|units=keV    tmodel_bdy'
    
    iterdb['tokamak_id'] = {}
    iterdb['tokamak_id']['data'] = None
    iterdb['tokamak_id']['units'] = None
    iterdb['tokamak_id']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['tokamak_id']['long_name'] = 'Tokamak (Machine Description) ID'
    iterdb['tokamak_id']['component'] = 'PLASMA'
    iterdb['tokamak_id']['specification'] = 'N  tokamak_id'
    
    iterdb['tq0_reco'] = {}
    iterdb['tq0_reco']['data'] = None
    iterdb['tq0_reco']['units'] = 'Nt*m'
    iterdb['tq0_reco']['section'] = 'STATE_PROFILES'
    iterdb['tq0_reco']['long_name'] = 'torque of recombination neutral source'
    iterdb['tq0_reco']['component'] = 'GAS'
    iterdb['tq0_reco']['specification'] = 'R|step*dV   tq0_reco(~nrho_gas)'
    
    iterdb['tqb0_halo'] = {}
    iterdb['tqb0_halo']['data'] = None
    iterdb['tqb0_halo']['units'] = 'Nt*m'
    iterdb['tqb0_halo']['section'] = 'STATE_PROFILES'
    iterdb['tqb0_halo']['long_name'] = 'torque of halo neutral source'
    iterdb['tqb0_halo']['component'] = 'NBI'
    iterdb['tqb0_halo']['specification'] = 'R|step*dV   tqb0_halo(~nrho_nbi)'
    
    iterdb['tqbe'] = {}
    iterdb['tqbe']['data'] = None
    iterdb['tqbe']['units'] = 'Nt*m'
    iterdb['tqbe']['section'] = 'STATE_PROFILES'
    iterdb['tqbe']['long_name'] = 'collisional beam torque to electrons'
    iterdb['tqbe']['component'] = 'NBI'
    iterdb['tqbe']['specification'] = 'R|step*dV   tqbe(~nrho_nbi)'
    
    iterdb['tqbi'] = {}
    iterdb['tqbi']['data'] = None
    iterdb['tqbi']['units'] = 'Nt*m'
    iterdb['tqbi']['section'] = 'STATE_PROFILES'
    iterdb['tqbi']['long_name'] = 'collisional beam torque to thermal ions'
    iterdb['tqbi']['component'] = 'NBI'
    iterdb['tqbi']['specification'] = 'R|step*dV   tqbi(~nrho_nbi)'
    
    iterdb['tqbjxb'] = {}
    iterdb['tqbjxb']['data'] = None
    iterdb['tqbjxb']['units'] = 'Nt*m'
    iterdb['tqbjxb']['section'] = 'STATE_PROFILES'
    iterdb['tqbjxb']['long_name'] = 'JxB beam torque'
    iterdb['tqbjxb']['component'] = 'NBI'
    iterdb['tqbjxb']['specification'] = 'R|step*dV   tqbjxb(~nrho_nbi)'
    
    iterdb['tqbth'] = {}
    iterdb['tqbth']['data'] = None
    iterdb['tqbth']['units'] = 'Nt*m'
    iterdb['tqbth']['section'] = 'STATE_PROFILES'
    iterdb['tqbth']['long_name'] = 'momentum in thermalization of beam ions'
    iterdb['tqbth']['component'] = 'NBI'
    iterdb['tqbth']['specification'] = 'R|step*dV   tqbth(~nrho_nbi)'
    
    iterdb['tqcx_halo'] = {}
    iterdb['tqcx_halo']['data'] = None
    iterdb['tqcx_halo']['units'] = 'Nt*m'
    iterdb['tqcx_halo']['section'] = 'STATE_PROFILES'
    iterdb['tqcx_halo']['long_name'] = 'beam halo driven CX momentum torque'
    iterdb['tqcx_halo']['component'] = 'NBI'
    iterdb['tqcx_halo']['specification'] = 'R|step*dV   tqcx_halo(~nrho_nbi)'
    
    iterdb['tqcx_reco'] = {}
    iterdb['tqcx_reco']['data'] = None
    iterdb['tqcx_reco']['units'] = 'Nt*m'
    iterdb['tqcx_reco']['section'] = 'STATE_PROFILES'
    iterdb['tqcx_reco']['long_name'] = 'reco driven CX momentum torque'
    iterdb['tqcx_reco']['component'] = 'GAS'
    iterdb['tqcx_reco']['specification'] = 'R|step*dV   tqcx_reco(~nrho_gas)'
    
    iterdb['tqioniz'] = {}
    iterdb['tqioniz']['data'] = None
    iterdb['tqioniz']['units'] = 'Nt*m/(#/sec)'
    iterdb['tqioniz']['section'] = 'STATE_PROFILES'
    iterdb['tqioniz']['long_name'] = 'ionization torque per unit influx (sc0)'
    iterdb['tqioniz']['component'] = 'GAS'
    iterdb['tqioniz']['specification'] = 'R|step*dV|units=Nt*m/(#/sec)     tqioniz(~nrho_gas,ngsc0)'
    
    iterdb['tqqcx'] = {}
    iterdb['tqqcx']['data'] = None
    iterdb['tqqcx']['units'] = 'Nt*m/(#/sec)/(rad/sec)'
    iterdb['tqqcx']['section'] = 'STATE_PROFILES'
    iterdb['tqqcx']['long_name'] = 'cx torque per unit influx per (omeg0-omegi)'
    iterdb['tqqcx']['component'] = 'GAS'
    iterdb['tqqcx']['specification'] = 'R|step*dV|units=Nt*m/(#/sec)/(rad/sec)  tqqcx(~nrho_gas,ngsc0)'
    
    iterdb['tqsc_halo'] = {}
    iterdb['tqsc_halo']['data'] = None
    iterdb['tqsc_halo']['units'] = 'Nt*m'
    iterdb['tqsc_halo']['section'] = 'STATE_PROFILES'
    iterdb['tqsc_halo']['long_name'] = 'beam halo torque: recapture - tqb0_halo'
    iterdb['tqsc_halo']['component'] = 'NBI'
    iterdb['tqsc_halo']['specification'] = 'R|step*dV   tqsc_halo(~nrho_nbi)'
    
    iterdb['tqsc_reco'] = {}
    iterdb['tqsc_reco']['data'] = None
    iterdb['tqsc_reco']['units'] = 'Nt*m'
    iterdb['tqsc_reco']['section'] = 'STATE_PROFILES'
    iterdb['tqsc_reco']['long_name'] = 'reco torque: recapture - tq0_reco'
    iterdb['tqsc_reco']['component'] = 'GAS'
    iterdb['tqsc_reco']['specification'] = 'R|step*dV   tqsc_reco(~nrho_gas)'
    
    iterdb['tq_trans'] = {}
    iterdb['tq_trans']['data'] = None
    iterdb['tq_trans']['units'] = 'Nt*m'
    iterdb['tq_trans']['section'] = 'STATE_PROFILES'
    iterdb['tq_trans']['long_name'] = 'angular momentum transport (loss)'
    iterdb['tq_trans']['component'] = 'PLASMA'
    iterdb['tq_trans']['specification'] = 'R|units=Nt*m|step*dV  tq_trans(~nrho)'
    
    iterdb['trace_flag'] = {}
    iterdb['trace_flag']['data'] = None
    iterdb['trace_flag']['units'] = None
    iterdb['trace_flag']['section'] = 'SIMULATION_INIT'
    iterdb['trace_flag']['long_name'] = 'trace element flag'
    iterdb['trace_flag']['component'] = 'NBI'
    iterdb['trace_flag']['specification'] = 'I  trace_flag(nbeam)'
    
    iterdb['triang'] = {}
    iterdb['triang']['data'] = None
    iterdb['triang']['units'] = None
    iterdb['triang']['section'] = 'STATE_PROFILES'
    iterdb['triang']['long_name'] = 'triangularity (symmetrized)'
    iterdb['triang']['component'] = 'EQ'
    iterdb['triang']['specification'] = 'R|pclin  triang(nrho_eq_geo)'
    
    iterdb['triangL'] = {}
    iterdb['triangL']['data'] = None
    iterdb['triangL']['units'] = None
    iterdb['triangL']['section'] = 'STATE_PROFILES'
    iterdb['triangL']['long_name'] = 'lower triangularity'
    iterdb['triangL']['component'] = 'EQ'
    iterdb['triangL']['specification'] = 'R|pclin  triangL(nrho_eq_geo)'
    
    iterdb['triangU'] = {}
    iterdb['triangU']['data'] = None
    iterdb['triangU']['units'] = None
    iterdb['triangU']['section'] = 'STATE_PROFILES'
    iterdb['triangU']['long_name'] = 'upper triangularity'
    iterdb['triangU']['component'] = 'EQ'
    iterdb['triangU']['specification'] = 'R|pclin  triangU(nrho_eq_geo)'
    
    iterdb['triang_miller_L'] = {}
    iterdb['triang_miller_L']['data'] = None
    iterdb['triang_miller_L']['units'] = None
    iterdb['triang_miller_L']['section'] = 'STATE_PROFILES'
    iterdb['triang_miller_L']['long_name'] = 'Miller lower triangularity'
    iterdb['triang_miller_L']['component'] = 'EQ'
    iterdb['triang_miller_L']['specification'] = 'R|pclin  triang_miller_L(nrho_eq_geo)'
    
    iterdb['triang_miller_U'] = {}
    iterdb['triang_miller_U']['data'] = None
    iterdb['triang_miller_U']['units'] = None
    iterdb['triang_miller_U']['section'] = 'STATE_PROFILES'
    iterdb['triang_miller_U']['long_name'] = 'Miller upper triangularity'
    iterdb['triang_miller_U']['component'] = 'EQ'
    iterdb['triang_miller_U']['specification'] = 'R|pclin  triang_miller_U(nrho_eq_geo)'
    
    iterdb['Ts'] = {}
    iterdb['Ts']['data'] = None
    iterdb['Ts']['units'] = 'keV'
    iterdb['Ts']['section'] = 'STATE_PROFILES'
    iterdb['Ts']['long_name'] = 'thermal specie temperature'
    iterdb['Ts']['component'] = 'PLASMA'
    iterdb['Ts']['specification'] = 'R|units=keV|alias=T|step*ns  Ts(~nrho,0:nspec_th)'
    
    iterdb['Ts_Data_Info'] = {}
    iterdb['Ts_Data_Info']['data'] = None
    iterdb['Ts_Data_Info']['units'] = None
    iterdb['Ts_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['Ts_Data_Info']['long_name'] = 'information on source of Temperature data'
    iterdb['Ts_Data_Info']['component'] = 'PLASMA'
    iterdb['Ts_Data_Info']['specification'] = 'C*80   Ts_Data_Info'
    
    iterdb['Ts_is_input'] = {}
    iterdb['Ts_is_input']['data'] = None
    iterdb['Ts_is_input']['units'] = None
    iterdb['Ts_is_input']['section'] = 'STATE_DATA'
    iterdb['Ts_is_input']['long_name'] = 'specie temperature measurement flag'
    iterdb['Ts_is_input']['component'] = 'PLASMA'
    iterdb['Ts_is_input']['specification'] = 'I Ts_is_input(0:nspec_th)'
    
    iterdb['upwind_pfrac_ns'] = {}
    iterdb['upwind_pfrac_ns']['data'] = None
    iterdb['upwind_pfrac_ns']['units'] = None
    iterdb['upwind_pfrac_ns']['section'] = 'STATE_PROFILES'
    iterdb['upwind_pfrac_ns']['long_name'] = 'specie density forward upwind fractions'
    iterdb['upwind_pfrac_ns']['component'] = 'PLASMA'
    iterdb['upwind_pfrac_ns']['specification'] = 'R|units=-|pclin upwind_pfrac_ns(nrho,0:nspec_th)'
    
    iterdb['upwind_pfrac_omega'] = {}
    iterdb['upwind_pfrac_omega']['data'] = None
    iterdb['upwind_pfrac_omega']['units'] = None
    iterdb['upwind_pfrac_omega']['section'] = 'STATE_PROFILES'
    iterdb['upwind_pfrac_omega']['long_name'] = 'omega (ang. velocity) forward upwind fraction'
    iterdb['upwind_pfrac_omega']['component'] = 'PLASMA'
    iterdb['upwind_pfrac_omega']['specification'] = 'R|pclin upwind_pfrac_omega(nrho)'
    
    iterdb['upwind_pfrac_Te'] = {}
    iterdb['upwind_pfrac_Te']['data'] = None
    iterdb['upwind_pfrac_Te']['units'] = None
    iterdb['upwind_pfrac_Te']['section'] = 'STATE_PROFILES'
    iterdb['upwind_pfrac_Te']['long_name'] = 'Te (electron energy advection) forward upwind fraction'
    iterdb['upwind_pfrac_Te']['component'] = 'PLASMA'
    iterdb['upwind_pfrac_Te']['specification'] = 'R|pclin upwind_pfrac_Te(nrho)'
    
    iterdb['upwind_pfrac_Ti'] = {}
    iterdb['upwind_pfrac_Ti']['data'] = None
    iterdb['upwind_pfrac_Ti']['units'] = None
    iterdb['upwind_pfrac_Ti']['section'] = 'STATE_PROFILES'
    iterdb['upwind_pfrac_Ti']['long_name'] = 'Ti (ion energy advection) forward upwind fraction'
    iterdb['upwind_pfrac_Ti']['component'] = 'PLASMA'
    iterdb['upwind_pfrac_Ti']['specification'] = 'R|pclin upwind_pfrac_Ti(nrho)'
    
    iterdb['vee_trans'] = {}
    iterdb['vee_trans']['data'] = None
    iterdb['vee_trans']['units'] = 'm/sec'
    iterdb['vee_trans']['section'] = 'STATE_PROFILES'
    iterdb['vee_trans']['long_name'] = 'electron energy radial velocity'
    iterdb['vee_trans']['component'] = 'PLASMA'
    iterdb['vee_trans']['specification'] = 'R|pclin   vee_trans(nrho)'
    
    iterdb['velb_fusi'] = {}
    iterdb['velb_fusi']['data'] = None
    iterdb['velb_fusi']['units'] = 'm/sec'
    iterdb['velb_fusi']['section'] = 'STATE_PROFILES'
    iterdb['velb_fusi']['long_name'] = 'fusion ion anom. radial velocity'
    iterdb['velb_fusi']['component'] = 'ANOM'
    iterdb['velb_fusi']['specification'] = 'R|pclin  velb_fusi(nrho_anom)'
    
    iterdb['velb_nbi'] = {}
    iterdb['velb_nbi']['data'] = None
    iterdb['velb_nbi']['units'] = 'm/sec'
    iterdb['velb_nbi']['section'] = 'STATE_PROFILES'
    iterdb['velb_nbi']['long_name'] = 'beam ion anom. radial velocity'
    iterdb['velb_nbi']['component'] = 'ANOM'
    iterdb['velb_nbi']['specification'] = 'R|pclin  velb_nbi(nrho_anom)'
    
    iterdb['velb_rfmi'] = {}
    iterdb['velb_rfmi']['data'] = None
    iterdb['velb_rfmi']['units'] = 'm/sec'
    iterdb['velb_rfmi']['section'] = 'STATE_PROFILES'
    iterdb['velb_rfmi']['long_name'] = 'RF minority ion anom. radial velocity'
    iterdb['velb_rfmi']['component'] = 'ANOM'
    iterdb['velb_rfmi']['specification'] = 'R|pclin  velb_rfmi(nrho_anom)'
    
    iterdb['vie_trans'] = {}
    iterdb['vie_trans']['data'] = None
    iterdb['vie_trans']['units'] = 'm/sec'
    iterdb['vie_trans']['section'] = 'STATE_PROFILES'
    iterdb['vie_trans']['long_name'] = 'ion energy radial velocity'
    iterdb['vie_trans']['component'] = 'PLASMA'
    iterdb['vie_trans']['specification'] = 'R|pclin   vie_trans(nrho)'
    
    iterdb['vmo_trans'] = {}
    iterdb['vmo_trans']['data'] = None
    iterdb['vmo_trans']['units'] = 'm/sec'
    iterdb['vmo_trans']['section'] = 'STATE_PROFILES'
    iterdb['vmo_trans']['long_name'] = 'angular momentum radial velocity'
    iterdb['vmo_trans']['component'] = 'PLASMA'
    iterdb['vmo_trans']['specification'] = 'R|pclin   vmo_trans(nrho)'
    
    iterdb['vn_trans'] = {}
    iterdb['vn_trans']['data'] = None
    iterdb['vn_trans']['units'] = 'm/sec'
    iterdb['vn_trans']['section'] = 'STATE_PROFILES'
    iterdb['vn_trans']['long_name'] = 'specie radial velocity'
    iterdb['vn_trans']['component'] = 'PLASMA'
    iterdb['vn_trans']['specification'] = 'R|units=m/sec|pclin   vn_trans(nrho,0:nspec_th)'
    
    iterdb['vol'] = {}
    iterdb['vol']['data'] = None
    iterdb['vol']['units'] = 'm^3'
    iterdb['vol']['section'] = 'STATE_PROFILES'
    iterdb['vol']['long_name'] = 'enclosed volume'
    iterdb['vol']['component'] = 'EQ'
    iterdb['vol']['specification'] = 'R|units=m^3|Spline_00  vol(nrho_eq)'
    
    iterdb['vphi0_av'] = {}
    iterdb['vphi0_av']['data'] = None
    iterdb['vphi0_av']['units'] = 'm/sec'
    iterdb['vphi0_av']['section'] = 'STATE_DATA'
    iterdb['vphi0_av']['long_name'] = 'average toroidal velocity of neutral source'
    iterdb['vphi0_av']['component'] = 'GAS'
    iterdb['vphi0_av']['specification'] = 'R|units=m/sec vphi0_av(ngsc0)'
    
    iterdb['vpol_Data_Info'] = {}
    iterdb['vpol_Data_Info']['data'] = None
    iterdb['vpol_Data_Info']['units'] = None
    iterdb['vpol_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['vpol_Data_Info']['long_name'] = 'information on source of poloidal velocity data'
    iterdb['vpol_Data_Info']['component'] = 'PLASMA'
    iterdb['vpol_Data_Info']['specification'] = 'C*80   vpol_Data_Info'
    
    iterdb['vpol_inmp'] = {}
    iterdb['vpol_inmp']['data'] = None
    iterdb['vpol_inmp']['units'] = 'm/sec'
    iterdb['vpol_inmp']['section'] = 'STATE_PROFILES'
    iterdb['vpol_inmp']['long_name'] = 'poloidal velocity, inner half midplane'
    iterdb['vpol_inmp']['component'] = 'PLASMA'
    iterdb['vpol_inmp']['specification'] = 'R|units=m/sec|step*ns vpol_inmp(~nrho,0:nspec_th)'
    
    iterdb['vpol_is_input'] = {}
    iterdb['vpol_is_input']['data'] = None
    iterdb['vpol_is_input']['units'] = None
    iterdb['vpol_is_input']['section'] = 'STATE_DATA'
    iterdb['vpol_is_input']['long_name'] = 'specie outer midplane poloidal velocit flag'
    iterdb['vpol_is_input']['component'] = 'PLASMA'
    iterdb['vpol_is_input']['specification'] = 'I vpol_is_input(0:nspec_th)'
    
    iterdb['vpol_omp'] = {}
    iterdb['vpol_omp']['data'] = None
    iterdb['vpol_omp']['units'] = 'm/sec'
    iterdb['vpol_omp']['section'] = 'STATE_PROFILES'
    iterdb['vpol_omp']['long_name'] = 'poloidal velocity, outer half midplane'
    iterdb['vpol_omp']['component'] = 'PLASMA'
    iterdb['vpol_omp']['specification'] = 'R|units=m/sec|step*ns vpol_omp(~nrho,0:nspec_th)'
    
    iterdb['vsur'] = {}
    iterdb['vsur']['data'] = None
    iterdb['vsur']['units'] = 'Volts'
    iterdb['vsur']['section'] = 'STATE_DATA'
    iterdb['vsur']['long_name'] = 'toroidal voltage at surface'
    iterdb['vsur']['component'] = 'PLASMA'
    iterdb['vsur']['specification'] = 'R  vsur'
    
    iterdb['VSUR_Data_Info'] = {}
    iterdb['VSUR_Data_Info']['data'] = None
    iterdb['VSUR_Data_Info']['units'] = None
    iterdb['VSUR_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['VSUR_Data_Info']['long_name'] = 'information on source of surface voltage data'
    iterdb['VSUR_Data_Info']['component'] = 'PLASMA'
    iterdb['VSUR_Data_Info']['specification'] = 'C*80   VSUR_Data_Info'
    
    iterdb['vtor_Data_Info'] = {}
    iterdb['vtor_Data_Info']['data'] = None
    iterdb['vtor_Data_Info']['units'] = None
    iterdb['vtor_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['vtor_Data_Info']['long_name'] = 'information on source of toroidal velocity data'
    iterdb['vtor_Data_Info']['component'] = 'PLASMA'
    iterdb['vtor_Data_Info']['specification'] = 'C*80   vtor_Data_Info'
    
    iterdb['vtor_inmp'] = {}
    iterdb['vtor_inmp']['data'] = None
    iterdb['vtor_inmp']['units'] = 'm/sec'
    iterdb['vtor_inmp']['section'] = 'STATE_PROFILES'
    iterdb['vtor_inmp']['long_name'] = 'toroidal velocity, inner half midplane'
    iterdb['vtor_inmp']['component'] = 'PLASMA'
    iterdb['vtor_inmp']['specification'] = 'R|units=m/sec|step*ns vtor_inmp(~nrho,0:nspec_th)'
    
    iterdb['vtor_is_input'] = {}
    iterdb['vtor_is_input']['data'] = None
    iterdb['vtor_is_input']['units'] = None
    iterdb['vtor_is_input']['section'] = 'STATE_DATA'
    iterdb['vtor_is_input']['long_name'] = 'specie outer midplane toroidal velocit flag'
    iterdb['vtor_is_input']['component'] = 'PLASMA'
    iterdb['vtor_is_input']['specification'] = 'I vtor_is_input(0:nspec_th)'
    
    iterdb['vtor_omp'] = {}
    iterdb['vtor_omp']['data'] = None
    iterdb['vtor_omp']['units'] = 'm/sec'
    iterdb['vtor_omp']['section'] = 'STATE_PROFILES'
    iterdb['vtor_omp']['long_name'] = 'toroidal velocity, outer half midplane'
    iterdb['vtor_omp']['component'] = 'PLASMA'
    iterdb['vtor_omp']['specification'] = 'R|units=m/sec|step*ns vtor_omp(~nrho,0:nspec_th)'
    
    iterdb['V_loop'] = {}
    iterdb['V_loop']['data'] = None
    iterdb['V_loop']['units'] = 'Volts'
    iterdb['V_loop']['section'] = 'STATE_PROFILES'
    iterdb['V_loop']['long_name'] = 'loop voltage'
    iterdb['V_loop']['component'] = 'PLASMA'
    iterdb['V_loop']['specification'] = 'R|units=Volts|pclin	V_loop(nrho)'
    
    iterdb['v_pars'] = {}
    iterdb['v_pars']['data'] = None
    iterdb['v_pars']['units'] = 'm/sec'
    iterdb['v_pars']['section'] = 'STATE_PROFILES'
    iterdb['v_pars']['long_name'] = 'thermal specie <vpll>'
    iterdb['v_pars']['component'] = 'PLASMA'
    iterdb['v_pars']['specification'] = 'R|units=m/sec|alias=vpll_|step*ns v_pars(~nrho,0:nspec_th)'
    
    iterdb['v_pers'] = {}
    iterdb['v_pers']['data'] = None
    iterdb['v_pers']['units'] = 'm/sec'
    iterdb['v_pers']['section'] = 'STATE_PROFILES'
    iterdb['v_pers']['long_name'] = 'thermal specie <vper>'
    iterdb['v_pers']['component'] = 'PLASMA'
    iterdb['v_pers']['specification'] = 'R|units=m/sec|alias=vper_|step*ns v_pers(~nrho,0:nspec_th)'
    
    iterdb['xRjcos_momeq'] = {}
    iterdb['xRjcos_momeq']['data'] = None
    iterdb['xRjcos_momeq']['units'] = 'm'
    iterdb['xRjcos_momeq']['section'] = 'STATE_PROFILES'
    iterdb['xRjcos_momeq']['long_name'] = 'scaled R cos moments'
    iterdb['xRjcos_momeq']['component'] = 'EQ'
    iterdb['xRjcos_momeq']['specification'] = 'R|units=m|Hermite_explicit  xRjcos_momeq(nrho_eq,neqmom)'
    
    iterdb['xRjsin_momeq'] = {}
    iterdb['xRjsin_momeq']['data'] = None
    iterdb['xRjsin_momeq']['units'] = 'm'
    iterdb['xRjsin_momeq']['section'] = 'STATE_PROFILES'
    iterdb['xRjsin_momeq']['long_name'] = 'scaled R sin moments'
    iterdb['xRjsin_momeq']['component'] = 'EQ'
    iterdb['xRjsin_momeq']['specification'] = 'R|units=m|Hermite_explicit  xRjsin_momeq(nrho_eq,neqmom)'
    
    iterdb['xZjcos_momeq'] = {}
    iterdb['xZjcos_momeq']['data'] = None
    iterdb['xZjcos_momeq']['units'] = 'm'
    iterdb['xZjcos_momeq']['section'] = 'STATE_PROFILES'
    iterdb['xZjcos_momeq']['long_name'] = 'scaled Z cos moments'
    iterdb['xZjcos_momeq']['component'] = 'EQ'
    iterdb['xZjcos_momeq']['specification'] = 'R|units=m|Hermite_explicit  xZjcos_momeq(nrho_eq,neqmom)'
    
    iterdb['xZjsin_momeq'] = {}
    iterdb['xZjsin_momeq']['data'] = None
    iterdb['xZjsin_momeq']['units'] = 'm'
    iterdb['xZjsin_momeq']['section'] = 'STATE_PROFILES'
    iterdb['xZjsin_momeq']['long_name'] = 'scaled Z sin moments'
    iterdb['xZjsin_momeq']['component'] = 'EQ'
    iterdb['xZjsin_momeq']['specification'] = 'R|units=m|Hermite_explicit  xZjsin_momeq(nrho_eq,neqmom)'
    
    iterdb['Z0max'] = {}
    iterdb['Z0max']['data'] = None
    iterdb['Z0max']['units'] = None
    iterdb['Z0max']['section'] = 'SIMULATION_INIT'
    iterdb['Z0max']['long_name'] = 'maximum Z of non-impurity species'
    iterdb['Z0max']['component'] = 'PLASMA'
    iterdb['Z0max']['specification'] = 'IS  Z0max = 2'
    
    iterdb['Z0_momeq'] = {}
    iterdb['Z0_momeq']['data'] = None
    iterdb['Z0_momeq']['units'] = 'm'
    iterdb['Z0_momeq']['section'] = 'STATE_PROFILES'
    iterdb['Z0_momeq']['long_name'] = 'Z0 of flux surface'
    iterdb['Z0_momeq']['component'] = 'EQ'
    iterdb['Z0_momeq']['specification'] = 'R|units=m|Hermite_explicit  Z0_momeq(nrho_eq)'
    
    iterdb['Zbap'] = {}
    iterdb['Zbap']['data'] = None
    iterdb['Zbap']['units'] = 'm'
    iterdb['Zbap']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['Zbap']['long_name'] = 'elevation of beam centerline at aperture'
    iterdb['Zbap']['component'] = 'NBI'
    iterdb['Zbap']['specification'] = 'R|units=m       Zbap(nbeam)'
    
    iterdb['Zbsc'] = {}
    iterdb['Zbsc']['data'] = None
    iterdb['Zbsc']['units'] = 'm'
    iterdb['Zbsc']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['Zbsc']['long_name'] = 'elevation of beam source'
    iterdb['Zbsc']['component'] = 'NBI'
    iterdb['Zbsc']['specification'] = 'R|units=m       Zbsc(nbeam)'
    
    iterdb['Zeff'] = {}
    iterdb['Zeff']['data'] = None
    iterdb['Zeff']['units'] = None
    iterdb['Zeff']['section'] = 'STATE_PROFILES'
    iterdb['Zeff']['long_name'] = 'Zeff (sum[nj*Zj**2]/ne)'
    iterdb['Zeff']['component'] = 'PLASMA'
    iterdb['Zeff']['specification'] = 'R|step*ns(:,ps_elec_index)  Zeff(~nrho)'
    
    iterdb['ZEFF_Data_Info'] = {}
    iterdb['ZEFF_Data_Info']['data'] = None
    iterdb['ZEFF_Data_Info']['units'] = None
    iterdb['ZEFF_Data_Info']['section'] = 'SIMULATION_INIT'
    iterdb['ZEFF_Data_Info']['long_name'] = 'information on source of Zeff data'
    iterdb['ZEFF_Data_Info']['component'] = 'PLASMA'
    iterdb['ZEFF_Data_Info']['specification'] = 'C*80   ZEFF_Data_Info'
    
    iterdb['Zeff_fi'] = {}
    iterdb['Zeff_fi']['data'] = None
    iterdb['Zeff_fi']['units'] = None
    iterdb['Zeff_fi']['section'] = 'STATE_PROFILES'
    iterdb['Zeff_fi']['long_name'] = 'Fast ion contribution to Zeff'
    iterdb['Zeff_fi']['component'] = 'PLASMA'
    iterdb['Zeff_fi']['specification'] = 'R|step*ns(:,ps_elec_index)  Zeff_fi(~nrho)'
    
    iterdb['Zeff_th'] = {}
    iterdb['Zeff_th']['data'] = None
    iterdb['Zeff_th']['units'] = None
    iterdb['Zeff_th']['section'] = 'STATE_PROFILES'
    iterdb['Zeff_th']['long_name'] = 'Thermal ion contribution to Zeff'
    iterdb['Zeff_th']['component'] = 'PLASMA'
    iterdb['Zeff_th']['specification'] = 'R|step*ns(:,ps_elec_index)  Zeff_th(~nrho)'
    
    iterdb['Zimp1'] = {}
    iterdb['Zimp1']['data'] = None
    iterdb['Zimp1']['units'] = None
    iterdb['Zimp1']['section'] = 'SIMULATION_INIT'
    iterdb['Zimp1']['long_name'] = 'lower limit on Z of impurity in reduced species list SA;'
    iterdb['Zimp1']['component'] = 'PLASMA'
    iterdb['Zimp1']['specification'] = 'IS  Zimp1 = 2'
    
    iterdb['Zimp2'] = {}
    iterdb['Zimp2']['data'] = None
    iterdb['Zimp2']['units'] = None
    iterdb['Zimp2']['section'] = 'SIMULATION_INIT'
    iterdb['Zimp2']['long_name'] = 'upper limit on Z of impurity in SA species list;'
    iterdb['Zimp2']['component'] = 'PLASMA'
    iterdb['Zimp2']['specification'] = 'IS  Zimp2 = 1000'
    
    iterdb['zlim'] = {}
    iterdb['zlim']['data'] = None
    iterdb['zlim']['units'] = 'm'
    iterdb['zlim']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['zlim']['long_name'] = 'Z points in closed (R,Z) contour sequence'
    iterdb['zlim']['component'] = 'EQ'
    iterdb['zlim']['specification'] = 'R|units=m  zlim(num_rzlim)'
    
    iterdb['Z_axis'] = {}
    iterdb['Z_axis']['data'] = None
    iterdb['Z_axis']['units'] = 'm'
    iterdb['Z_axis']['section'] = 'STATE_DATA'
    iterdb['Z_axis']['long_name'] = 'Z of magnetic axis'
    iterdb['Z_axis']['component'] = 'EQ'
    iterdb['Z_axis']['specification'] = 'R  Z_axis'
    
    iterdb['Z_EC_launch'] = {}
    iterdb['Z_EC_launch']['data'] = None
    iterdb['Z_EC_launch']['units'] = 'm'
    iterdb['Z_EC_launch']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['Z_EC_launch']['long_name'] = 'Z of center of launcher'
    iterdb['Z_EC_launch']['component'] = 'EC'
    iterdb['Z_EC_launch']['specification'] = 'R|units=m   Z_EC_launch(necrf_src)'
    
    iterdb['Z_geo'] = {}
    iterdb['Z_geo']['data'] = None
    iterdb['Z_geo']['units'] = 'm'
    iterdb['Z_geo']['section'] = 'STATE_PROFILES'
    iterdb['Z_geo']['long_name'] = 'flux surfaces Z(rho,theta)'
    iterdb['Z_geo']['component'] = 'EQ'
    iterdb['Z_geo']['specification'] = 'R|units=m|Hermite_explicit Z_geo(nrho_eq,nth_eq)'
    
    iterdb['Z_grid'] = {}
    iterdb['Z_grid']['data'] = None
    iterdb['Z_grid']['units'] = 'm'
    iterdb['Z_grid']['section'] = 'SIMULATION_INIT'
    iterdb['Z_grid']['long_name'] = 'Z grid'
    iterdb['Z_grid']['component'] = 'EQ'
    iterdb['Z_grid']['specification'] = 'G   Z_grid(nZ)'
    
    iterdb['Z_max_box'] = {}
    iterdb['Z_max_box']['data'] = None
    iterdb['Z_max_box']['units'] = 'm'
    iterdb['Z_max_box']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['Z_max_box']['long_name'] = 'Z_max of bounding box'
    iterdb['Z_max_box']['component'] = 'EQ'
    iterdb['Z_max_box']['specification'] = 'R  Z_max_box'
    
    iterdb['Z_max_lcfs'] = {}
    iterdb['Z_max_lcfs']['data'] = None
    iterdb['Z_max_lcfs']['units'] = 'm'
    iterdb['Z_max_lcfs']['section'] = 'STATE_DATA'
    iterdb['Z_max_lcfs']['long_name'] = 'Z_max of last closed flux surface'
    iterdb['Z_max_lcfs']['component'] = 'EQ'
    iterdb['Z_max_lcfs']['specification'] = 'R  Z_max_lcfs'
    
    iterdb['Z_midp'] = {}
    iterdb['Z_midp']['data'] = None
    iterdb['Z_midp']['units'] = 'm'
    iterdb['Z_midp']['section'] = 'STATE_PROFILES'
    iterdb['Z_midp']['long_name'] = 'flux surface midplane elevation'
    iterdb['Z_midp']['component'] = 'EQ'
    iterdb['Z_midp']['specification'] = 'R|pclin  Z_midp(nrho_eq_geo)'
    
    iterdb['Z_min_box'] = {}
    iterdb['Z_min_box']['data'] = None
    iterdb['Z_min_box']['units'] = 'm'
    iterdb['Z_min_box']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['Z_min_box']['long_name'] = 'Z_min of bounding box'
    iterdb['Z_min_box']['component'] = 'EQ'
    iterdb['Z_min_box']['specification'] = 'R  Z_min_box'
    
    iterdb['Z_min_lcfs'] = {}
    iterdb['Z_min_lcfs']['data'] = None
    iterdb['Z_min_lcfs']['units'] = 'm'
    iterdb['Z_min_lcfs']['section'] = 'STATE_DATA'
    iterdb['Z_min_lcfs']['long_name'] = 'Z_min of last closed flux surface'
    iterdb['Z_min_lcfs']['component'] = 'EQ'
    iterdb['Z_min_lcfs']['specification'] = 'R  Z_min_lcfs'
    
    iterdb['Z_surfMax'] = {}
    iterdb['Z_surfMax']['data'] = None
    iterdb['Z_surfMax']['units'] = 'm'
    iterdb['Z_surfMax']['section'] = 'STATE_PROFILES'
    iterdb['Z_surfMax']['long_name'] = 'max Z on flux surface'
    iterdb['Z_surfMax']['component'] = 'EQ'
    iterdb['Z_surfMax']['specification'] = 'R|pclin  Z_surfMax(nrho_eq_geo)'
    
    iterdb['Z_surfMin'] = {}
    iterdb['Z_surfMin']['data'] = None
    iterdb['Z_surfMin']['units'] = 'm'
    iterdb['Z_surfMin']['section'] = 'STATE_PROFILES'
    iterdb['Z_surfMin']['long_name'] = 'min Z on flux surface'
    iterdb['Z_surfMin']['component'] = 'EQ'
    iterdb['Z_surfMin']['specification'] = 'R|pclin  Z_surfMin(nrho_eq_geo)'
    
    iterdb['ant_model'] = {}
    iterdb['ant_model']['data'] = None
    iterdb['ant_model']['units'] = None
    iterdb['ant_model']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['ant_model']['long_name'] = 'antenna model filenames (1 per antenna source)'
    iterdb['ant_model']['component'] = 'IC'
    iterdb['ant_model']['specification'] = 'F ant_model(nicrf_src)'
    
    iterdb['cdicrf'] = {}
    iterdb['cdicrf']['data'] = None
    iterdb['cdicrf']['units'] = 'A'
    iterdb['cdicrf']['section'] = 'STATE_PROFILES'
    iterdb['cdicrf']['long_name'] = 'ICRF current drive'
    iterdb['cdicrf']['component'] = 'IC'
    iterdb['cdicrf']['specification'] = 'R|units=A|step*dA   cdicrf(~nrho_icrf,nicrf_src)'
    
    iterdb['cdicrf_nphi'] = {}
    iterdb['cdicrf_nphi']['data'] = None
    iterdb['cdicrf_nphi']['units'] = 'A'
    iterdb['cdicrf_nphi']['section'] = 'STATE_PROFILES'
    iterdb['cdicrf_nphi']['long_name'] = 'ICRF current drive'
    iterdb['cdicrf_nphi']['component'] = 'IC'
    iterdb['cdicrf_nphi']['specification'] = 'R|units=A|step*dA   cdicrf_nphi(~nrho_icrf,num_nphi(),nicrf_src)'
    
    iterdb['curich'] = {}
    iterdb['curich']['data'] = None
    iterdb['curich']['units'] = 'A'
    iterdb['curich']['section'] = 'STATE_PROFILES'
    iterdb['curich']['long_name'] = 'total driven current (all IC srcs)'
    iterdb['curich']['component'] = 'IC'
    iterdb['curich']['specification'] = 'R|units=A|step*dA   curich(~nrho_icrf)'
    
    iterdb['curmino'] = {}
    iterdb['curmino']['data'] = None
    iterdb['curmino']['units'] = 'A'
    iterdb['curmino']['section'] = 'STATE_PROFILES'
    iterdb['curmino']['long_name'] = 'minority ion driven cur (shielded).'
    iterdb['curmino']['component'] = 'IC'
    iterdb['curmino']['specification'] = 'R|step*dA|units=A   curmino(~nrho_icrf)'
    
    iterdb['dx_fshield'] = {}
    iterdb['dx_fshield']['data'] = None
    iterdb['dx_fshield']['units'] = 'm'
    iterdb['dx_fshield']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['dx_fshield']['long_name'] = 'distance, antenna to Faraday shield'
    iterdb['dx_fshield']['component'] = 'IC'
    iterdb['dx_fshield']['specification'] = 'R|units=m dx_fshield(nicrf_src)'
    
    iterdb['eperp_mini'] = {}
    iterdb['eperp_mini']['data'] = None
    iterdb['eperp_mini']['units'] = 'keV'
    iterdb['eperp_mini']['section'] = 'STATE_PROFILES'
    iterdb['eperp_mini']['long_name'] = 'minority species <Eperp>, lab frame'
    iterdb['eperp_mini']['component'] = 'IC'
    iterdb['eperp_mini']['specification'] = 'R|units=keV|alias=eperp_|step*nmini eperp_mini(~nrho_icrf,nspec_rfmin)'

    iterdb['epll_mini'] = {}
    iterdb['epll_mini']['data'] = None
    iterdb['epll_mini']['units'] = 'keV'
    iterdb['epll_mini']['section'] = 'STATE_PROFILES'
    iterdb['epll_mini']['long_name'] = 'minority species <Epll>, lab frame'
    iterdb['epll_mini']['component'] = 'IC'
    iterdb['epll_mini']['specification'] = 'R|units=keV|alias=epll_|step*nmini  epll_mini(~nrho_icrf,nspec_rfmin)'
    
    iterdb['fracmin'] = {}
    iterdb['fracmin']['data'] = None
    iterdb['fracmin']['units'] = None
    iterdb['fracmin']['section'] = 'SIMULATION_INIT'
    iterdb['fracmin']['long_name'] = 'minority density fraction if kdens_rfmin="fraction"'
    iterdb['fracmin']['component'] = 'IC'
    iterdb['fracmin']['specification'] = 'R|units=- fracmin(nspec_rfmin)'
    
    iterdb['freq_ic'] = {}
    iterdb['freq_ic']['data'] = None
    iterdb['freq_ic']['units'] = 'Hz'
    iterdb['freq_ic']['section'] = 'SHOT_CONFIGURATION'
    iterdb['freq_ic']['long_name'] = 'frequency on each ICRF source'
    iterdb['freq_ic']['component'] = 'IC'
    iterdb['freq_ic']['specification'] = 'R|units=Hz freq_ic(nicrf_src)'
    
    iterdb['icrf_src_name'] = {}
    iterdb['icrf_src_name']['data'] = None
    iterdb['icrf_src_name']['units'] = None
    iterdb['icrf_src_name']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['icrf_src_name']['long_name'] = 'number & name of ICRF sources'
    iterdb['icrf_src_name']['component'] = 'IC'
    iterdb['icrf_src_name']['specification'] = 'L|icrf_source   icrf_src_name(nicrf_src)'
    
    iterdb['isThermal'] = {}
    iterdb['isThermal']['data'] = None
    iterdb['isThermal']['units'] = None
    iterdb['isThermal']['section'] = 'STATE_DATA'
    iterdb['isThermal']['long_name'] = '=1 if minority specie is thermalized'
    iterdb['isThermal']['component'] = 'IC'
    iterdb['isThermal']['specification'] = 'I  isThermal(nspec_rfmin)'
    
    iterdb['m_RFMIN'] = {}
    iterdb['m_RFMIN']['data'] = None
    iterdb['m_RFMIN']['units'] = 'kg'
    iterdb['m_RFMIN']['section'] = 'SHOT_CONFIGURATION'
    iterdb['m_RFMIN']['long_name'] = 'RFMIN specie mass'
    iterdb['m_RFMIN']['component'] = 'IC'
    iterdb['m_RFMIN']['specification'] = 'S|RF_minority  RFMIN(nspec_rfmin)'
    
    iterdb['nmini'] = {}
    iterdb['nmini']['data'] = None
    iterdb['nmini']['units'] = 'm^-3'
    iterdb['nmini']['section'] = 'STATE_PROFILES'
    iterdb['nmini']['long_name'] = 'minority species density'
    iterdb['nmini']['component'] = 'IC'
    iterdb['nmini']['specification'] = 'R|units=m^-3|alias=n|step  nmini(~nrho_icrf,nspec_rfmin)'

    iterdb['nphi'] = {}
    iterdb['nphi']['data'] = None
    iterdb['nphi']['units'] = None
    iterdb['nphi']['section'] = 'SHOT_CONFIGURATION'
    iterdb['nphi']['long_name'] = 'n_phi wave spectrum from antenna'
    iterdb['nphi']['component'] = 'IC'
    iterdb['nphi']['specification'] = 'I nphi(num_nphi(),nicrf_src)'
    
    iterdb['nrz_antgeo'] = {}
    iterdb['nrz_antgeo']['data'] = None
    iterdb['nrz_antgeo']['units'] = None
    iterdb['nrz_antgeo']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['nrz_antgeo']['long_name'] = 'number of (R,Z) points, antenna geometries'
    iterdb['nrz_antgeo']['component'] = 'IC'
    iterdb['nrz_antgeo']['specification'] = 'I|ENUM nrz_antgeo(nicrf_src)'
    
    iterdb['num_nphi'] = {}
    iterdb['num_nphi']['data'] = None
    iterdb['num_nphi']['units'] = None
    iterdb['num_nphi']['section'] = 'SHOT_CONFIGURATION'
    iterdb['num_nphi']['long_name'] = 'number of non-zero n_phi values'
    iterdb['num_nphi']['component'] = 'IC'
    iterdb['num_nphi']['specification'] = 'I|ENUM:nphi  num_nphi(nicrf_src)'
    
    iterdb['num_nphi_vac'] = {}
    iterdb['num_nphi_vac']['data'] = None
    iterdb['num_nphi_vac']['units'] = None
    iterdb['num_nphi_vac']['section'] = 'SHOT_CONFIGURATION'
    iterdb['num_nphi_vac']['long_name'] = 'number of non-zero n_phi values'
    iterdb['num_nphi_vac']['component'] = 'IC'
    iterdb['num_nphi_vac']['specification'] = 'I|ENUM num_nphi_vac(nicrf_src)'
    
    iterdb['n_straps'] = {}
    iterdb['n_straps']['data'] = None
    iterdb['n_straps']['units'] = None
    iterdb['n_straps']['section'] = 'SHOT_CONFIGURATION'
    iterdb['n_straps']['long_name'] = 'number of straps in the antenna'
    iterdb['n_straps']['component'] = 'IC'
    iterdb['n_straps']['specification'] = 'I|ENUM n_straps(nicrf_src)'
    
    iterdb['picrf_abs'] = {}
    iterdb['picrf_abs']['data'] = None
    iterdb['picrf_abs']['units'] = 'W'
    iterdb['picrf_abs']['section'] = 'STATE_DATA'
    iterdb['picrf_abs']['long_name'] = 'RF power absorbed inside plasma'
    iterdb['picrf_abs']['component'] = 'IC'
    iterdb['picrf_abs']['specification'] = 'R|units=W picrf_abs(nicrf_src)'
    
    iterdb['picrf_ext'] = {}
    iterdb['picrf_ext']['data'] = None
    iterdb['picrf_ext']['units'] = 'W'
    iterdb['picrf_ext']['section'] = 'STATE_DATA'
    iterdb['picrf_ext']['long_name'] = 'RF power deposited outside plasma'
    iterdb['picrf_ext']['component'] = 'IC'
    iterdb['picrf_ext']['specification'] = 'R|units=W picrf_ext(nicrf_src)'

    iterdb['picrf_nphi_srcs'] = {}
    iterdb['picrf_nphi_srcs']['data'] = None
    iterdb['picrf_nphi_srcs']['units'] = 'W'
    iterdb['picrf_nphi_srcs']['section'] = 'STATE_PROFILES'
    iterdb['picrf_nphi_srcs']['long_name'] = 'direct ICRF power deposition'
    iterdb['picrf_nphi_srcs']['component'] = 'IC'
    iterdb['picrf_nphi_srcs']['specification'] = 'R|units=W|alias=picrf_nphi_|step*dV   picrf_nphi_srcs(~nrho_icrf,num_nphi(),nicrf_src,0:nspec_alla)'
    
    iterdb['picrf_srcs'] = {}
    iterdb['picrf_srcs']['data'] = None
    iterdb['picrf_srcs']['units'] = 'W'
    iterdb['picrf_srcs']['section'] = 'STATE_PROFILES'
    iterdb['picrf_srcs']['long_name'] = 'direct ICRF power deposition'
    iterdb['picrf_srcs']['component'] = 'IC'
    iterdb['picrf_srcs']['specification'] = 'R|units=W|alias=picrfs_|step*dV   picrf_srcs(~nrho_icrf,nicrf_src,0:nspec_alla)'
    
    iterdb['picrf_totals'] = {}
    iterdb['picrf_totals']['data'] = None
    iterdb['picrf_totals']['units'] = 'W'
    iterdb['picrf_totals']['section'] = 'STATE_PROFILES'
    iterdb['picrf_totals']['long_name'] = 'direct ICRF power deposition'
    iterdb['picrf_totals']['component'] = 'IC'
    iterdb['picrf_totals']['specification'] = 'R|units=W|alias=picrf_|step*dV    picrf_totals(~nrho_icrf,0:nspec_alla)'
    
    iterdb['picth'] = {}
    iterdb['picth']['data'] = None
    iterdb['picth']['units'] = 'W'
    iterdb['picth']['section'] = 'STATE_PROFILES'
    iterdb['picth']['long_name'] = 'direct thermal ion heating by ICRF'
    iterdb['picth']['component'] = 'IC'
    iterdb['picth']['specification'] = 'R|step*dV|units=W   picth(~nrho_icrf)'
    
    iterdb['pmine'] = {}
    iterdb['pmine']['data'] = None
    iterdb['pmine']['units'] = 'W'
    iterdb['pmine']['section'] = 'STATE_PROFILES'
    iterdb['pmine']['long_name'] = 'electron heating by minority ions'
    iterdb['pmine']['component'] = 'IC'
    iterdb['pmine']['specification'] = 'R|step*dV   pmine(~nrho_icrf)'
    
    iterdb['pmini'] = {}
    iterdb['pmini']['data'] = None
    iterdb['pmini']['units'] = 'W'
    iterdb['pmini']['section'] = 'STATE_PROFILES'
    iterdb['pmini']['long_name'] = 'thermal ion heating by minority ions'
    iterdb['pmini']['component'] = 'IC'
    iterdb['pmini']['specification'] = 'R|step*dV   pmini(~nrho_icrf)'
    
    iterdb['pminth'] = {}
    iterdb['pminth']['data'] = None
    iterdb['pminth']['units'] = 'W'
    iterdb['pminth']['section'] = 'STATE_PROFILES'
    iterdb['pminth']['long_name'] = '(de)thermalization of minority ions'
    iterdb['pminth']['component'] = 'IC'
    iterdb['pminth']['specification'] = 'R|step*dV   pminth(~nrho_icrf)'

    iterdb['power_ic'] = {}
    iterdb['power_ic']['data'] = None
    iterdb['power_ic']['units'] = 'W'
    iterdb['power_ic']['section'] = 'STATE_DATA'
    iterdb['power_ic']['long_name'] = 'power on each ICRF source'
    iterdb['power_ic']['component'] = 'IC'
    iterdb['power_ic']['specification'] = 'R|units=W  power_ic(nicrf_src)'
    
    iterdb['qatom_RFMIN'] = {}
    iterdb['qatom_RFMIN']['data'] = None
    iterdb['qatom_RFMIN']['units'] = 'C'
    iterdb['qatom_RFMIN']['section'] = 'SHOT_CONFIGURATION'
    iterdb['qatom_RFMIN']['long_name'] = 'RFMIN atomic number'
    iterdb['qatom_RFMIN']['component'] = 'IC'
    iterdb['qatom_RFMIN']['specification'] = 'S|RF_minority  RFMIN(nspec_rfmin)'
    
    iterdb['q_RFMIN'] = {}
    iterdb['q_RFMIN']['data'] = None
    iterdb['q_RFMIN']['units'] = 'C'
    iterdb['q_RFMIN']['section'] = 'SHOT_CONFIGURATION'
    iterdb['q_RFMIN']['long_name'] = 'RFMIN specie charge'
    iterdb['q_RFMIN']['component'] = 'IC'
    iterdb['q_RFMIN']['specification'] = 'S|RF_minority  RFMIN(nspec_rfmin)'
    
    iterdb['RFMIN_name'] = {}
    iterdb['RFMIN_name']['data'] = None
    iterdb['RFMIN_name']['units'] = None
    iterdb['RFMIN_name']['section'] = 'SHOT_CONFIGURATION'
    iterdb['RFMIN_name']['long_name'] = 'ICRF minority species'
    iterdb['RFMIN_name']['component'] = 'IC'
    iterdb['RFMIN_name']['specification'] = 'S|RF_minority  RFMIN(nspec_rfmin)'
    
    iterdb['rfmin_to_all'] = {}
    iterdb['rfmin_to_all']['data'] = None
    iterdb['rfmin_to_all']['units'] = None
    iterdb['rfmin_to_all']['section'] = 'SIMULATION_INIT'
    iterdb['rfmin_to_all']['long_name'] = 'map rfmin index to "all" list'
    iterdb['rfmin_to_all']['component'] = 'PLASMA'
    iterdb['rfmin_to_all']['specification'] = 'I  rfmin_to_all(nspec_rfmin)'
    
    iterdb['rfmin_to_alla'] = {}
    iterdb['rfmin_to_alla']['data'] = None
    iterdb['rfmin_to_alla']['units'] = None
    iterdb['rfmin_to_alla']['section'] = 'SIMULATION_INIT'
    iterdb['rfmin_to_alla']['long_name'] = 'map rfmin index to "alla" list'
    iterdb['rfmin_to_alla']['component'] = 'PLASMA'
    iterdb['rfmin_to_alla']['specification'] = 'I  rfmin_to_alla(nspec_rfmin)'
    
    iterdb['RFMIN_type'] = {}
    iterdb['RFMIN_type']['data'] = None
    iterdb['RFMIN_type']['units'] = None
    iterdb['RFMIN_type']['section'] = 'SHOT_CONFIGURATION'
    iterdb['RFMIN_type']['long_name'] = 'RFMIN specie types'
    iterdb['RFMIN_type']['component'] = 'IC'
    iterdb['RFMIN_type']['specification'] = 'S|RF_minority  RFMIN(nspec_rfmin)'

    iterdb['rho_icrf'] = {}
    iterdb['rho_icrf']['data'] = None
    iterdb['rho_icrf']['units'] = None
    iterdb['rho_icrf']['section'] = 'SIMULATION_INIT'
    iterdb['rho_icrf']['long_name'] = 'rho grid (RF)'
    iterdb['rho_icrf']['component'] = 'IC'
    iterdb['rho_icrf']['specification'] = 'G  rho_icrf(nrho_icrf)'
    
    iterdb['R_ant'] = {}
    iterdb['R_ant']['data'] = None
    iterdb['R_ant']['units'] = 'm'
    iterdb['R_ant']['section'] = 'SHOT_CONFIGURATION'
    iterdb['R_ant']['long_name'] = 'major radius of antenna'
    iterdb['R_ant']['component'] = 'IC'
    iterdb['R_ant']['specification'] = 'R|units=m R_ant(nicrf_src)'
    
    iterdb['R_antgeo'] = {}
    iterdb['R_antgeo']['data'] = None
    iterdb['R_antgeo']['units'] = 'm'
    iterdb['R_antgeo']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['R_antgeo']['long_name'] = 'antenna geo: R pts'
    iterdb['R_antgeo']['component'] = 'IC'
    iterdb['R_antgeo']['specification'] = 'R|units=m R_antgeo(nrz_antgeo(),nicrf_src)'
    
    iterdb['wt_nphi'] = {}
    iterdb['wt_nphi']['data'] = None
    iterdb['wt_nphi']['units'] = None
    iterdb['wt_nphi']['section'] = 'SHOT_CONFIGURATION'
    iterdb['wt_nphi']['long_name'] = 'vacuum spectrum n_phi weight'
    iterdb['wt_nphi']['component'] = 'IC'
    iterdb['wt_nphi']['specification'] = 'R|units=- wt_nphi(num_nphi(),nicrf_src)'
    
    iterdb['wt_nphi_abs'] = {}
    iterdb['wt_nphi_abs']['data'] = None
    iterdb['wt_nphi_abs']['units'] = None
    iterdb['wt_nphi_abs']['section'] = 'STATE_DATA'
    iterdb['wt_nphi_abs']['long_name'] = 'absorbed spectrum n_phi weight'
    iterdb['wt_nphi_abs']['component'] = 'IC'
    iterdb['wt_nphi_abs']['specification'] = 'R|units=- wt_nphi_abs(num_nphi(),nicrf_src)'
    
    iterdb['wt_nphi_ext'] = {}
    iterdb['wt_nphi_ext']['data'] = None
    iterdb['wt_nphi_ext']['units'] = None
    iterdb['wt_nphi_ext']['section'] = 'STATE_DATA'
    iterdb['wt_nphi_ext']['long_name'] = 'fraction of power deposited outside'
    iterdb['wt_nphi_ext']['component'] = 'IC'
    iterdb['wt_nphi_ext']['specification'] = 'R|units=- wt_nphi_ext(num_nphi(),nicrf_src)'
    
    iterdb['Z_ant'] = {}
    iterdb['Z_ant']['data'] = None
    iterdb['Z_ant']['units'] = 'm'
    iterdb['Z_ant']['section'] = 'SHOT_CONFIGURATION'
    iterdb['Z_ant']['long_name'] = 'height of antenna'
    iterdb['Z_ant']['component'] = 'IC'
    iterdb['Z_ant']['specification'] = 'R|units=m Z_ant(nicrf_src)'

    iterdb['Z_antgeo'] = {}
    iterdb['Z_antgeo']['data'] = None
    iterdb['Z_antgeo']['units'] = 'm'
    iterdb['Z_antgeo']['section'] = 'MACHINE_DESCRIPTION'
    iterdb['Z_antgeo']['long_name'] = 'antenna geo: Z pts'
    iterdb['Z_antgeo']['component'] = 'IC'
    iterdb['Z_antgeo']['specification'] = 'R|units=m Z_antgeo(nrz_antgeo(),nicrf_src)'
    
    iterdb['Z_mid_ant'] = {}
    iterdb['Z_mid_ant']['data'] = None
    iterdb['Z_mid_ant']['units'] = 'm'
    iterdb['Z_mid_ant']['section'] = 'SHOT_CONFIGURATION'
    iterdb['Z_mid_ant']['long_name'] = 'center of antenna relative to TF coil midplane'
    iterdb['Z_mid_ant']['component'] = 'IC'
    iterdb['Z_mid_ant']['specification'] = 'R|units=m Z_mid_ant(nicrf_src)'

    return iterdb


def test_state_file(fpath):
    cdfid = ncdf.Dataset(fpath)
    icount = 0
    txtid = open("cdf_fields.txt",'w')
    attrnames = ["units","section","long_name","component","specification"]
    for name, variable in cdfid.variables.items():
        icount += 1
        text = "iterdb['%s'] = {}\n" % name
        text += "iterdb['%s']['data'] = None\n" % name
        for attrname in attrnames:
            try:
                text += "iterdb['%s']['%s'] = '%s'\n" % (name,attrname,getattr(variable, attrname))
            except AttributeError:
                text += "iterdb['%s']['units'] = None\n" % name
        text += "\n"
        txtid.write(text)
    txtid.close()
    return 1

def read_state_file(fpath):
    iterdb = get_iterdb_vars()
    iterdb['file_type'] = 'state'

    if os.path.isfile(fpath): fid = ncdf.Dataset(fpath)
    else:                     raise IOError("ONETWO STATE FILE DOES NOT EXIST!" % fpath)

    fvars = fid.variables.keys()
    for fvar in fvars:
        try:
           iterdb[fvar]['data'] = fid.variables[fvar][:]
        except KeyError:
            print(fvar)
            pass

    amu = 1.6605402e-27
    iterdb['plasma_specs_Znum'] = [round(i/abs(iterdb['qatom_S']['data'][0]),0) for i in iterdb['qatom_S']['data']]
    iterdb['plasma_specs_Anum'] = [round(i/amu,2) for i in iterdb['m_S']['data']]
    
    if 'ni_bdy' not in iterdb:
        iterdb['ni_bdy'] = {}
        iterdb['ni_bdy']['data'] = sum(iterdb['ns_bdy']['data'][1:])
        iterdb['ni_bdy']['units'] = 'm^-3'
        iterdb['ni_bdy']['section'] = 'STATE_DATA'
        iterdb['ni_bdy']['long_name'] = 'ion density at/beyond boundary'
        iterdb['ni_bdy']['component'] = 'PLASMA'
        iterdb['ni_bdy']['specification'] = 'R|units=m^-3 ni_bdy'

    if 'Te' not in iterdb:
        iterdb['Te'] = {}
        iterdb['Te']['data'] = iterdb['Ti']['data'].copy()
        iterdb['Te']['units'] = 'keV'
        iterdb['Te']['section'] = 'STATE_PROFILES'
        iterdb['Te']['long_name'] = 'electron temperature'
        iterdb['Te']['component'] = 'PLASMA'
        iterdb['Te']['specification'] = 'R|units=keV|step*ne Te(~nrho)'

    if 'ne_bdy' not in iterdb:
        iterdb['ne_bdy'] = {}
        iterdb['ne_bdy']['data'] = iterdb['ns_bdy']['data'][0]
        iterdb['ne_bdy']['units'] = 'm^-3'
        iterdb['ne_bdy']['section'] = 'STATE_DATA'
        iterdb['ne_bdy']['long_name'] = 'electron density at/beyond boundary'
        iterdb['ne_bdy']['component'] = 'PLASMA'
        iterdb['ne_bdy']['specification'] = 'R|units=m^-3 ne_bdy'

    if 'ne' not in iterdb:
        Zeff  = 0.0
        for ind in range(1,len(iterdb['plasma_specs_Znum'])):
            Zeff += iterdb['ns']['data'][ind] * iterdb['plasma_specs_Znum'][ind]**2
        ne = Zeff / iterdb['Zeff']['data']

        iterdb['ne'] = {}
        iterdb['ne']['data'] = ne
        iterdb['ne']['units'] = 'm^-3'
        iterdb['ne']['section'] = 'STATE_DATA'
        iterdb['ne']['long_name'] = 'thermal electron density'
        iterdb['ne']['component'] = 'PLASMA'
        iterdb['ne']['specification'] = 'R|units=m^-3|step ne(~nrho)'

    if 'Zeff_bdy' not in iterdb:
        Zeff_bdy  = 0.0
        for ind in range(1,len(iterdb['plasma_specs_Znum'])):
            Zeff_bdy += iterdb['ns_bdy']['data'][ind] * iterdb['plasma_specs_Znum'][ind]**2
        Zeff_bdy /= iterdb['ns_bdy']['data'][0]

        iterdb['Zeff_bdy'] = {}
        iterdb['Zeff_bdy']['data'] = Zeff_bdy
        iterdb['Zeff_bdy']['units'] = None
        iterdb['Zeff_bdy']['section'] = 'STATE_PROFILES'
        iterdb['Zeff_bdy']['long_name'] = 'Zeff (sum[nj*Zj**2]/ne)'
        iterdb['Zeff_bdy']['component'] = 'PLASMA'
        iterdb['Zeff_bdy']['specification'] = 'R|step*ns(:,ps_elec_index)  Zeff(~nrho)'
    

    if 't0' in iterdb:
        iterdb['TIME_ID'] = "%05d" % int(iterdb['t0']['data'])
    if 'RunID' in iterdb:
        digits = []
        for ind in range(len(iterdb['RunID']['data'])):
            try:
              digit = iterdb['RunID']['data'][ind].decode().strip()
              if digit.isnumeric(): digits.append(digit)
            except AttributeError:
                break
        iterdb['SHOT_ID'] = "%06d" % int(''.join(digits))
    if 'tokamak_id' in iterdb:
        digits = []
        for ind in range(len(iterdb['tokamak_id']['data'])):
            try:
              digits.append(iterdb['tokamak_id']['data'][ind].decode().strip())
            except AttributeError:
                break
        iterdb['TOKAMAK_ID'] = ''.join(digits)

    nrho = len(iterdb['rho']['data'])
    if len(iterdb['ni']['data']) < nrho:
        iterdb['ni']['data'] = numpy.append(iterdb['ni']['data'],iterdb['ni_bdy']['data'])
    if len(iterdb['ne']['data']) < nrho:
        iterdb['ne']['data'] = numpy.append(iterdb['ne']['data'],iterdb['ne_bdy']['data'])
    if len(iterdb['Ti']['data']) < nrho:
        iterdb['Ti']['data'] = numpy.append(iterdb['Ti']['data'],iterdb['Ti_bdy']['data'])
    if len(iterdb['Te']['data']) < nrho:
        iterdb['Te']['data'] = numpy.append(iterdb['Te']['data'],iterdb['Te_bdy']['data'])
    if len(iterdb['Zeff']['data']) < nrho:
        iterdb['Zeff']['data'] = numpy.append(iterdb['Zeff']['data'],iterdb['Zeff_bdy']['data'])

    plasma_nspecs = len(iterdb['S_type']['data'])
    plasma_specs_name = []
    ns = numpy.zeros([plasma_nspecs,nrho])
    Ts = numpy.zeros([plasma_nspecs,nrho])
    for ind in range(plasma_nspecs):
        digits = []
        for subind in range(len(iterdb['S_name']['data'][ind])):
            try:
              digits.append(iterdb['S_name']['data'][ind][subind].decode().strip())
            except AttributeError:
                pass
        plasma_specs_name.append(''.join(digits))

        if len(iterdb['ns']['data'][ind]) < nrho:
            ns[ind] = numpy.append(iterdb['ns']['data'][ind], iterdb['ns_bdy']['data'][ind])
        if len(iterdb['Ts']['data'][ind]) < nrho:
            if 'Ts_bdy' in iterdb:
                Ts[ind] = numpy.append(iterdb['Ts']['data'][ind], iterdb['Ts_bdy']['data'][ind])
            else:
                Ts[ind] = numpy.append(iterdb['Ts']['data'][ind], iterdb['Ti_bdy']['data'])
    iterdb['ns']['data'] = ns.copy(); del ns
    iterdb['Ts']['data'] = Ts.copy(); del Ts

    if type(iterdb['nbeami']['data']) != type_none:
        nbeami_nspecs = len(iterdb['nbeami']['data'])
        nbeami = numpy.zeros([nbeami_nspecs,nrho])
        for ind in range(nbeami_nspecs):
            nbeami[ind] = numpy.append(iterdb['nbeami']['data'][ind], iterdb['nbeami_bdy']['data'][ind])
        iterdb['nbeami']['data'] = nbeami.copy(); del nbeami

# # print("Zimp1 = ",iterdb['Zimp1']['data'])
# # print("Zimp2 = ",iterdb['Zimp2']['data'])
# # print("Z0max = ",iterdb['Z0max']['data'])
# # print("s_to_sa = ",iterdb['s_to_sa']['data'])
# # print("qatom_SA = ",iterdb['qatom_SA']['data'])
#   print("S_type = ",iterdb['S_type']['data'])
#   print("S_name = ",iterdb['S_name']['data'])
#   print("m_S = ",iterdb['m_S']['data'])
#   print("qatom_S = ",iterdb['qatom_S']['data'])
#   print("ns = ",iterdb['ns']['data'])
#   print("Ts = ",iterdb['Ts']['data'])

#   amu = 1.6605402e-27

#   time_id = "%05d" % int(iterdb['t0']['data'])
#   shot_id = ''.join([digit.decode().strip() for digit in iterdb['RunID']['data']])
#   shotid = ''
#   for digit in shot_id:
#       if digit.isnumeric(): shotid += digit
#       else: break
#   shot_id = "%06d" % int(shotid)
#   tokamak_id = ''.join([digit.decode().strip() for digit in iterdb['tokamak_id']['data']])

#   nspecs = len(iterdb['S_type']['data'])
#   specs_name = []
#   for ind in range(nspecs):
#       specs_name.append(''.join([digit.decode().strip() for digit in iterdb['S_name']['data'][ind]]))
#   specs_Znum = [i/abs(iterdb['qatom_S']['data'][0]) for i in iterdb['qatom_S']['data']]
#   specs_Anum = [round(i/amu,2) for i in iterdb['m_S']['data']]

#   specs_ntot = []
#   for ind in range(nspecs):
#       specs_ntot.append(sum(iterdb['ns']['data'][ind]))
#   print(specs_ntot[0],sum(specs_ntot[1:7]),sum(iterdb['ni']['data']))

#    if 'rho_grid' in iterdb and iterdb['rho_grid']['data']:
#        iterdb['rho']['data']  = (iterdb['rho_grid']['data']     - iterdb['rho_grid']['data'][0])
#        iterdb['rho']['data'] /= (iterdb['rho_grid']['data'][-1] - iterdb['rho_grid']['data'][0])
#
#    if iterdb['qcx']['data']   and all(iterdb['qcx']['data']) > 0.0:   iterdb['qcx']['data'] *= -1.0
#    if iterdb['qrad']['data']  and all(iterdb['qrad']['data']) > 0.0:  iterdb['qrad']['data'] *= -1.0
#    if iterdb['qione']['data'] and all(iterdb['qione']['data']) > 0.0: iterdb['qione']['data'] *= -1.0
##   iterdb['qdelt']['data']     = numpy.abs(iterdb['qdelt']['data'])
##   iterdb['q_value']['data']   = numpy.abs(iterdb['q_value']['data'])
#    iterdb['dudtsv']['data']    = numpy.transpose(iterdb['dudtsv']['data'])
#    iterdb['stsource']['data']  = numpy.transpose(iterdb['stsource']['data'])

    return iterdb

def test_binary_file(fname):
    textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
    is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
    return is_binary_string(open(fname,'rb').read(1024))

def read_iterdb_file(fpath):
    if test_binary_file(fpath):
        iterdb = read_state_file(fpath)
    else:
        iterdb = read_iterdb_file(fpath)
    return iterdb


def to_instate(fpath,gfpath={},setParam={}):
    iterdb = read_iterdb_file(fpath)
        
    if gfpath:
        geqdskdata = read_eqdsk_file(gfpath)
    instate = get_instate_vars()

    if   'SHOT_ID' in setParam:
          SHOT_ID = setParam['SHOT_ID']
    elif 'shot_id' in setParam:
          SHOT_ID = setParam['shot_id']
    else:
          SHOT_ID = "%06d" % (int(iterdb['shot']['data']))
          
    if   'TIME_ID' in setParam:
          TIME_ID = setParam['TIME_ID']
    elif 'time_id' in setParam:
          TIME_ID = setParam['time_id']
    else:
          TIME_ID = "%05d" % (int(numpy.ceil(iterdb['time']['data']*1.0e4)))
          
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

    iterdb['eps']['data'] = iterdb['rMinor_mean']['data']/iterdb['Rmajor_mean']['data']

    instate['R0']     = [round(float(iterdb['R_axis']['data']),                             7)]
    instate['B0']     = [round(float(abs(iterdb['B_axis']['data'])),                        7)]
    instate['IP']     = [round(float(iterdb['tot_cur']['data']) * 1.0e-6,                   7)]
    instate['KAPPA']  = [round(float(iterdb['elong']['data']),                              7)]
    instate['DELTA']  = [round(float(iterdb['triang']['data']),                             7)]
    instate['RMAJOR'] = [round(float(iterdb['R_axis']['data']),                             7)]
    instate['ASPECT'] = [round(float(iterdb['eps']['data'][-1]),                            7)]
    instate['AMINOR'] = [round(float(iterdb['R_axis']['data'] * iterdb['eps']['data'][-1]), 7)]

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

    instate['RHO']    = [round(i,2) for i in iterdb['rho']['data']          ]
    instate['NRHO']   = [numpy.size(instate['RHO'])                         ]
    instate['PSIPOL'] = [round(i,7) for i in iterdb['psipol']['data']       ]

    numpy.append(iterdb['ni']['data'],iterdb['ni_bdy']['data'])
    numpy.append(iterdb['Ti']['data'],iterdb['Ti_bdy']['data'])
    numpy.append(iterdb['omegat']['data'],iterdb['omegat_bdy']['data'])

    instate['NE']      = [round(i,7) for i in (iterdb['ne']['data']*1.0e-19)]
    instate['NI']      = [round(i,7) for i in (iterdb['ni']['data']*1.0e-19)]
    instate['TE']      = [round(i,7) for i in iterdb['Ti']['data']          ]
    instate['TI']      = [round(i,7) for i in iterdb['Ti']['data']          ]
    instate['ZEFF']    = [round(i,7) for i in iterdb['Zeff']['data']        ]
    instate['OMEGA']   = [round(i,7) for i in iterdb['omegat']['data']      ]

    iterdb['psiaxis']['data'] = iterdb['psipol']['data'][0]
    iterdb['psibdry']['data'] = iterdb['psipol']['data'][-1]

    PSI    = (iterdb['psibdry']['data']-iterdb['psiaxis']['data'])
    PSI   *= numpy.arange(iterdb['nj']['data'])/(iterdb['nj']['data']-1.0)
    PSIN   = (PSI-PSI[0])/(PSI[-1]-PSI[0])
    RHOPSI = numpy.sqrt(PSIN)
    instate['RHOPSI']  = [round(i,7) for i in RHOPSI]

    instate['SCALE_NE'] = [1.0]

    instate['SCALE_SION'] = [1.0]
    instate['SION']       = [round(i,7) for i in (iterdb['sion']['data']*1.0e-19)]

    instate['Q']       = [round(i,7) for i in iterdb['q_value']['data']]
    instate['P_EQ']    = [round(i,7) for i in iterdb['press']['data']]
    if type(iterdb['pprim']['data']) != type(None):
        instate['PPRIME']  = [round(i,7) for i in iterdb['pprim']['data']]
    if type(iterdb['ffprim']['data']) != type(None):
        instate['FFPRIME'] = [round(i,7) for i in iterdb['ffprim']['data']]

    instate['J_RF']  = [round(i,7) for i in (iterdb['currf']['data']   * 1.0e-6)]
    instate['J_OH']  = [round(i,7) for i in (iterdb['curohm']['data']  * 1.0e-6)]
    instate['J_NB']  = [round(i,7) for i in (iterdb['curbeam']['data'] * 1.0e-6)]
    instate['J_BS']  = [round(i,7) for i in (iterdb['curboot']['data'] * 1.0e-6)]
    instate['J_EC']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['J_IC']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['J_LH']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['J_HC']  = [round(0.0,7) for i in range(instate['NRHO'][0])         ]
    instate['J_TOT'] = [round(i,7) for i in (iterdb['curden']['data']  * 1.0e-6)]

    instate['PE_RF']  = [round(i,7) for i in (iterdb['qrfe']['data']   * 1.0e-6)]
    instate['PI_RF']  = [round(i,7) for i in (iterdb['qrfi']['data']   * 1.0e-6)]
    instate['PE_NB']  = [round(i,7) for i in (iterdb['qbeame']['data'] * 1.0e-6)]
    instate['PI_NB']  = [round(i,7) for i in (iterdb['qbeami']['data'] * 1.0e-6)]
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
        instate['P_EI']   = [round(i,7) for i in (iterdb['qdelt']['data'] * 1.0e-6)]
    elif fiterdb_flag:
        instate['P_EI']   = [-round(i,7) for i in (iterdb['qdelt']['data'] * 1.0e-6)]
    instate['P_RAD']  = [round(i,7) for i in (iterdb['qrad']['data']    * 1.0e-6)]
    instate['P_OHM']  = [round(i,7) for i in (iterdb['qohm']['data']    * 1.0e-6)]
    instate['PI_CX']  = [round(i,7) for i in (iterdb['qcx']['data']     * 1.0e-6)]
    instate['PI_FUS'] = [round(i,7) for i in (iterdb['qfusi']['data']   * 1.0e-6)]
    instate['PE_FUS'] = [round(i,7) for i in (iterdb['qfuse']['data']   * 1.0e-6)]

    instate['CHIE']          = [round(i,7) for i in iterdb['chieinv']['data']            ]
    instate['CHII']          = [round(i,7) for i in iterdb['chiinv']['data']             ]
    if type(iterdb['wbeam']['data']) != type(None):
        instate['WBEAM']         = [round(i,7) for i in (iterdb['wbeam']['data']  *1.603e-22)]
    if type(iterdb['walp']['data']) != type(None):
        instate['WALPHA']        = [round(i,7) for i in (iterdb['walp']['data']   *1.603e-22)]
    instate['TORQUE_NB']     = [round(i,7) for i in iterdb['storqueb']['data']           ]
    instate['TORQUE_IN']     = [round(0.0,7) for i in range(instate['NRHO'][0])          ]
    instate['DENSITY_BEAM']  = [round(i,7) for i in (iterdb['enbeam']['data'][0]*1.0e-19)]
    if type(iterdb['enalp']['data']) != type(None):
        instate['DENSITY_ALPHA'] = [round(i,7) for i in iterdb['enalp']['data']              ]
    instate['SE_IONIZATION'] = [round(0.0,7) for i in range(instate['NRHO'][0])          ]
    instate['SI_IONIZATION'] = [round(0.0,7) for i in range(instate['NRHO'][0])          ]
    instate['PE_IONIZATION'] = [round(0.0,7) for i in range(instate['NRHO'][0])          ]
    instate['PI_IONIZATION'] = [round(0.0,7) for i in range(instate['NRHO'][0])          ]


    if instate['NRHO'][0] != 101:
        old_rho  = instate['RHO']
        new_nrho = 101
        new_rho  = numpy.linspace(0.0,1.0,new_nrho)

        instate['NRHO'         ] = [101]
        instate['RHO'          ] = [round(i,7) for i in new_rho                                               ]
        instate['PSIPOL'       ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PSIPOL'       ])]
        instate['NE'           ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['NE'           ])]
        instate['TE'           ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['TE'           ])]
        instate['TI'           ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['TI'           ])]
        instate['ZEFF'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['ZEFF'         ])]
        instate['SION'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['SION'         ])]
        instate['OMEGA'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['OMEGA'        ])]

        instate['Q'            ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['Q'            ])]
        instate['P_EQ'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['P_EQ'         ])]
        instate['PPRIME'       ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PPRIME'       ])]
        instate['FFPRIME'      ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['FFPRIME'      ])]

        PSI    = (iterdb['psibdry']['data']-iterdb['psiaxis']['data'])
        PSI   *= numpy.arange(instate['NRHO'][0])/(instate['NRHO'][0]-1.0)
        PSIN   = (PSI-PSI[0])/(PSI[-1]-PSI[0])
        RHOPSI = numpy.sqrt(PSIN)
        instate['RHOPSI'       ] = [round(i,7) for i in RHOPSI                                                ]

        instate['J_RF'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_RF'         ])]
        instate['J_OH'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_OH'         ])]
        instate['J_NB'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_NB'         ])]
        instate['J_BS'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_BS'         ])]
        instate['J_EC'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_EC'         ])]
        instate['J_IC'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_IC'         ])]
        instate['J_LH'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_LH'         ])]
        instate['J_HC'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_HC'         ])]
        instate['J_TOT'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_TOT'        ])]

        instate['PE_RF'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PE_RF'        ])]
        instate['PE_NB'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PE_NB'        ])]
        instate['PE_EC'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PE_EC'        ])]
        instate['PE_IC'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PE_IC'        ])]
        instate['PE_LH'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PE_LH'        ])]
        instate['PE_HC'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PE_HC'        ])]
        instate['PI_RF'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PI_RF'        ])]
        instate['PI_NB'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PI_NB'        ])]
        instate['PI_EC'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PI_EC'        ])]
        instate['PI_IC'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PI_IC'        ])]
        instate['PI_LH'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PI_LH'        ])]
        instate['PI_HC'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PI_HC'        ])]
        instate['SE_NB'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['SE_NB'        ])]
        instate['SI_NB'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['SI_NB'        ])]

        instate['P_EI'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['P_EI'         ])]
        instate['P_RAD'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['P_RAD'        ])]
        instate['P_OHM'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['P_OHM'        ])]
        instate['PI_CX'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PI_CX'        ])]
        instate['PI_FUS'       ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PI_FUS'       ])]
        instate['PE_FUS'       ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PE_FUS'       ])]

        instate['CHIE'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['CHIE'         ])]
        instate['CHII'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['CHII'         ])]

        instate['WBEAM'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['WBEAM'        ])]
        instate['WALPHA'       ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['WALPHA'       ])]

        instate['TORQUE_NB'    ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['TORQUE_NB'    ])]
        instate['TORQUE_IN'    ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['TORQUE_IN'    ])]

        instate['SE_IONIZATION'] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['SE_IONIZATION'])]
        instate['SI_IONIZATION'] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['SI_IONIZATION'])]
        instate['PE_IONIZATION'] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PE_IONIZATION'])]
        instate['PI_IONIZATION'] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PI_IONIZATION'])]

        instate['DENSITY_BEAM' ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['DENSITY_BEAM' ])]
        instate['DENSITY_ALPHA'] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['DENSITY_ALPHA'])]


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
        instate['NBDRY'] = [numpy.size(iterdb['rplasbdry']['data'])]
       #if max(iterdb['rplasbdry']['data']) > 100.0:
       #    instate['RBDRY'] = [round(i/100.0,7) for i in iterdb['rplasbdry']['data']]
       #    instate['ZBDRY'] = [round(i/100.0,7) for i in iterdb['zplasbdry']['data']]
       #else:
       #    instate['RBDRY'] = [round(i,7) for i in iterdb['rplasbdry']['data']]
       #    instate['ZBDRY'] = [round(i,7) for i in iterdb['zplasbdry']['data']]
        NBDRYmax = 85
        NBDRY = numpy.size(iterdb['rplasbdry']['data'])
        if NBDRY > NBDRYmax:
           RBDRY = iterdb['rplasbdry']['data']
           ZBDRY = iterdb['zplasbdry']['data']
           BDRY = zip(RBDRY,ZBDRY)
           BDRYINDS = sorted(random.sample(range(NBDRY),NBDRYmax))
           instate['NBDRY'] = [NBDRYmax]
           instate['RBDRY'] = [round(i,7) for i in RBDRY[BDRYINDS]]
           instate['ZBDRY'] = [round(i,7) for i in ZBDRY[BDRYINDS]]
        else:
           instate['NBDRY'] = [numpy.size(iterdb['rplasbdry']['data'])]
           instate['RBDRY'] = [round(i,7) for i in iterdb['rplasbdry']['data']]
           instate['ZBDRY'] = [round(i,7) for i in iterdb['zplasbdry']['data']]


        if type(iterdb['rlimiter']['data']) != type(None):
            if LIMITER_MODEL == 1:
               NLIMTmax = 86
               NLIMT = numpy.size(iterdb['rlimiter']['data'])
               if NLIMT > NLIMTmax:
                  RLIMT = iterdb['rlimiter']['data']
                  ZLIMT = iterdb['zlimiter']['data']
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
                  instate['NLIM']  = [numpy.size(iterdb['rlimiter']['data'])]
                  instate['RLIM']  = [round(i,7) for i in iterdb['rlimiter']['data'] ]
                  instate['ZLIM']  = [round(i,7) for i in iterdb['zlimiter']['data'] ]

            elif LIMITER_MODEL == 2:
               RLIM_MAX = max(iterdb['rlimiter']['data'])
               RLIM_MIN = min(iterdb['rlimiter']['data'])
               ZLIM_MAX = max(iterdb['zlimiter']['data'])
               ZLIM_MIN = min(iterdb['zlimiter']['data'])
               instate['RLIM'] = [RLIM_MAX, RLIM_MIN, RLIM_MIN, RLIM_MAX, RLIM_MAX]
               instate['ZLIM'] = [ZLIM_MAX, ZLIM_MAX, ZLIM_MIN, ZLIM_MIN, ZLIM_MAX]
               instate['NLIM'] = [len(instate['RLIM'])]
        else:
            RLIM_MAX = max(instate['RBDRY']) + 0.10
            RLIM_MIN = min(instate['RBDRY']) - 0.10
            ZLIM_MAX = max(instate['ZBDRY']) + 0.10
            ZLIM_MIN = min(instate['ZBDRY']) - 0.10
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

def calculate_line_average(profile,grid): 
    ngrid = len(grid)
    line_average = 0.0
    for i in range(ngrid-1):
        line_average += 0.5 * (profile[i+1] + profile[i]) * (grid[i+1] - grid[i])
    line_average /= grid[-1]
    return line_average

if __name__ == "__main__":
    iterdbfname = "statefile_2.026000E+00.nc"
    instate_from_pstate = to_instate(fpath=iterdbfname,setParam={"TOKAMAK_ID":"d3d","LIMITER_MODEL":2})
    iterdbfname = "iterdb.150139"
    instate_from_iterdb = to_instate(fpath=iterdbfname,setParam={"TOKAMAK_ID":"d3d","LIMITER_MODEL":2})

    sys.exit()

