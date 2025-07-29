import os
import sys
import numpy

import linecache


def get_gacode_variables():
    gacode                       = {}

    gacode['ze']                 = {}
    gacode['ze']['data']         = None
    gacode['ze']['unit']         = None
    gacode['ze']['Info']         = "Atomic charge number of electrons"

    gacode['zi']                 = {}
    gacode['zi']['data']         = None
    gacode['zi']['unit']         = None
    gacode['zi']['Info']         = "Atomic charge number of ions. There is a column for every ion species."

    gacode['nrho']               = {}
    gacode['nrho']['data']       = None
    gacode['nrho']['unit']       = None
    gacode['nrho']['Info']       = "Number of experimental data gridpoints"

    gacode['nion']               = {}
    gacode['nion']['data']       = None
    gacode['nion']['unit']       = None
    gacode['nion']['Info']       = "Total number of ions (thermal and fast)"

    gacode['iname']              = {}
    gacode['iname']['data']      = None
    gacode['iname']['unit']      = None
    gacode['iname']['Info']      = "Name of ions. There is a column for every ion species."

    gacode['itype']              = {}
    gacode['itype']['data']      = None
    gacode['itype']['unit']      = None
    gacode['itype']['Info']      = "Type of ions (thermal and fast). There is a column for every ion species."

    gacode['emass']              = {}
    gacode['emass']['data']      = None
    gacode['emass']['unit']      = "kg"
    gacode['emass']['Info']      = "Mass of electrons"

    gacode['imass']              = {}
    gacode['imass']['data']      = None
    gacode['imass']['unit']      = "kg"
    gacode['imass']['Info']      = "Mass of ions. There is a column for every ion species."

    gacode['timeid']             = {}
    gacode['timeid']['data']     = 1.0
    gacode['timeid']['unit']     = None
    gacode['timeid']['Info']     = "Shot Timestamp"

    gacode['shotid']             = {}
    gacode['shotid']['data']     = 1.0
    gacode['shotid']['unit']     = None
    gacode['shotid']['Info']     = "Shot number"

    gacode['rcentr']             = {}
    gacode['rcentr']['data']     = None
    gacode['rcentr']['unit']     = "m"
    gacode['rcentr']['Info']     = "Experimental major radius at axis"

    gacode['bcentr']             = {}
    gacode['bcentr']['data']     = None
    gacode['bcentr']['unit']     = "T"
    gacode['bcentr']['Info']     = "Experimental magnetic field at axis"

    gacode['current']            = {}
    gacode['current']['data']    = None
    gacode['current']['unit']    = None
    gacode['current']['Info']    = "Plasma current"

    gacode['torfluxa']           = {} 
    gacode['torfluxa']['data']   = None
    gacode['torfluxa']['unit']   = None
    gacode['torfluxa']['info']   = None

    gacode['rho']                = {} 
    gacode['rho']['data']        = None
    gacode['rho']['unit']        = None
    gacode['rho']['info']        = "The dimensionless ONETWO flux-surface label"

    gacode['ne']                 = {} 
    gacode['ne']['data']         = None
    gacode['ne']['unit']         = "/m^3"
    gacode['ne']['info']         = "The electron density"

    gacode['ni']                 = {} 
    gacode['ni']['data']         = None
    gacode['ni']['unit']         = "1/m^3"
    gacode['ni']['info']         = "The ion density. There is a column for every ion species."

    gacode['te']                 = {} 
    gacode['te']['data']         = None
    gacode['te']['unit']         = "keV"
    gacode['te']['info']         = "The electron temperature"

    gacode['ti']                 = {} 
    gacode['ti']['data']         = None
    gacode['ti']['unit']         = "keV"
    gacode['ti']['info']         = "The ion temperature. There is a column for every ion species."

    gacode['z_eff']              = {} 
    gacode['z_eff']['data']      = None
    gacode['z_eff']['unit']      = None
    gacode['z_eff']['info']      = "The (dimensionless) effective ion charge"

    gacode['ptot']               = {} 
    gacode['ptot']['data']       = None
    gacode['ptot']['unit']       = "Pa"
    gacode['ptot']['info']       = "Total plasma pressure"

    gacode['q']                  = {} 
    gacode['q']['data']          = None
    gacode['q']['unit']          = None
    gacode['q']['info']          = "Safety factor"

    gacode['johm']               = {} 
    gacode['johm']['data']       = None
    gacode['johm']['unit']       = "MA/m^2"
    gacode['johm']['info']       = "Ohmic current"

    gacode['jbs']                = {} 
    gacode['jbs']['data']        = None
    gacode['jbs']['unit']        = "MA/m^2"
    gacode['jbs']['info']        = "Bootstrap current (parallel)"

    gacode['jbstor']             = {} 
    gacode['jbstor']['data']     = None
    gacode['jbstor']['unit']     = "MA/m^2"
    gacode['jbstor']['info']     = "Bootstrap current (toroidal)"

    gacode['vtor']               = {} 
    gacode['vtor']['data']       = None
    gacode['vtor']['unit']       = "m/s"
    gacode['vtor']['info']       = "Ion toroidal velocity"

    gacode['vpol']               = {} 
    gacode['vpol']['data']       = None
    gacode['vpol']['unit']       = "m/s"
    gacode['vpol']['info']       = "Ion poloidal velocity"

    gacode['omega0']             = {} 
    gacode['omega0']['data']     = None
    gacode['omega0']['unit']     = "rad/s"
    gacode['omega0']['info']     = "Rotation frequency"

    gacode['polflux']            = {} 
    gacode['polflux']['data']    = None
    gacode['polflux']['unit']    = "Wb/rad"
    gacode['polflux']['info']    = "Poloidal flux over 2*pi"

    gacode['rmaj']               = {} 
    gacode['rmaj']['data']       = None
    gacode['rmaj']['unit']       = "m"
    gacode['rmaj']['info']       = "The generalized major radius"

    gacode['rmin']               = {} 
    gacode['rmin']['data']       = None
    gacode['rmin']['unit']       = "m"
    gacode['rmin']['info']       = "The generalized minor radius"

    gacode['zmag']               = {} 
    gacode['zmag']['data']       = None
    gacode['zmag']['unit']       = "m"
    gacode['zmag']['info']       = "Flux-surface elevation"

    gacode['kappa']              = {} 
    gacode['kappa']['data']      = None
    gacode['kappa']['unit']      = None
    gacode['kappa']['info']      = "Flux-surface elongation"

    gacode['delta']              = {} 
    gacode['delta']['data']      = None
    gacode['delta']['unit']      = None
    gacode['delta']['info']      = "Flux-surface triangularity"

    gacode['zeta']               = {} 
    gacode['zeta']['data']       = None
    gacode['zeta']['unit']       = None
    gacode['zeta']['info']       = "Flux-surface squareness"

    gacode['shape_sin3']         = {} 
    gacode['shape_sin3']['data'] = None
    gacode['shape_sin3']['unit'] = None
    gacode['shape_sin3']['info'] = "Flux-surface tilt"

    gacode['shape_sin4']         = {} 
    gacode['shape_sin4']['data'] = None
    gacode['shape_sin4']['unit'] = None
    gacode['shape_sin4']['info'] = "Flux-surface tilt"

    gacode['shape_sin5']         = {} 
    gacode['shape_sin5']['data'] = None
    gacode['shape_sin5']['unit'] = None
    gacode['shape_sin5']['info'] = "Flux-surface tilt"

    gacode['shape_sin6']         = {} 
    gacode['shape_sin6']['data'] = None
    gacode['shape_sin6']['unit'] = None
    gacode['shape_sin6']['info'] = "Flux-surface tilt"

    gacode['shape_cos0']         = {} 
    gacode['shape_cos0']['data'] = None
    gacode['shape_cos0']['unit'] = None
    gacode['shape_cos0']['info'] = "Flux-surface tilt"

    gacode['shape_cos1']         = {} 
    gacode['shape_cos1']['data'] = None
    gacode['shape_cos1']['unit'] = None
    gacode['shape_cos1']['info'] = "Flux-surface tilt"

    gacode['shape_cos2']         = {} 
    gacode['shape_cos2']['data'] = None
    gacode['shape_cos2']['unit'] = None
    gacode['shape_cos2']['info'] = "Flux-surface tilt"

    gacode['shape_cos3']         = {} 
    gacode['shape_cos3']['data'] = None
    gacode['shape_cos3']['unit'] = None
    gacode['shape_cos3']['info'] = "Flux-surface tilt"

    gacode['shape_cos4']         = {} 
    gacode['shape_cos4']['data'] = None
    gacode['shape_cos4']['unit'] = None
    gacode['shape_cos4']['info'] = "Flux-surface tilt"

    gacode['shape_cos5']         = {} 
    gacode['shape_cos5']['data'] = None
    gacode['shape_cos5']['unit'] = None
    gacode['shape_cos5']['info'] = "Flux-surface tilt"

    gacode['shape_cos6']         = {} 
    gacode['shape_cos6']['data'] = None
    gacode['shape_cos6']['unit'] = None
    gacode['shape_cos6']['info'] = "Flux-surface tilt"

    gacode['qei']                = {} 
    gacode['qei']['data']        = None
    gacode['qei']['unit']        = "MW/m^3"
    gacode['qei']['info']        = "Electron-ion exchange"

    gacode['qfusi']              = {} 
    gacode['qfusi']['data']      = None
    gacode['qfusi']['unit']      = "MW/m^3"
    gacode['qfusi']['info']      = "Fusion power to ions"

    gacode['qfuse']              = {} 
    gacode['qfuse']['data']      = None
    gacode['qfuse']['unit']      = "MW/m^3"
    gacode['qfuse']['info']      = "Fusion power to electrons"

    gacode['qcxi']               = {} 
    gacode['qcxi']['data']       = None
    gacode['qcxi']['unit']       = "MW/m^3"
    gacode['qcxi']['info']       = "Charge-exchange power to ions"

    gacode['qbrem']              = {} 
    gacode['qbrem']['data']      = None
    gacode['qbrem']['unit']      = "MW/m^3"
    gacode['qbrem']['info']      = "Bremsstrahlung radiation"

    gacode['qline']              = {} 
    gacode['qline']['data']      = None
    gacode['qline']['unit']      = "MW/m^3"
    gacode['qline']['info']      = "Electron line radiation"

    gacode['qsync']              = {} 
    gacode['qsync']['data']      = None
    gacode['qsync']['unit']      = "MW/m^3"
    gacode['qsync']['info']      = "Electron synchrotron radiation"

    gacode['qbeami']             = {} 
    gacode['qbeami']['data']     = None
    gacode['qbeami']['unit']     = "MW/m^3"
    gacode['qbeami']['info']     = "Beam power to ions"

    gacode['qbeame']             = {} 
    gacode['qbeame']['data']     = None
    gacode['qbeame']['unit']     = "MW/m^3"
    gacode['qbeame']['info']     = "Beam power to electrons"

    gacode['qohme']              = {} 
    gacode['qohme']['data']      = None
    gacode['qohme']['unit']      = "MW/m^3"
    gacode['qohme']['info']      = "Ohmic power to electrons"

    gacode['qrfe']               = {} 
    gacode['qrfe']['data']       = None
    gacode['qrfe']['unit']       = "MW/m^3"
    gacode['qrfe']['info']       = "RF power to electrons"

    gacode['qrfi']               = {} 
    gacode['qrfi']['data']       = None
    gacode['qrfi']['unit']       = "MW/m^3"
    gacode['qrfi']['info']       = "RF power to ions"

    gacode['jnb']                = {} 
    gacode['jnb']['data']        = None
    gacode['jnb']['unit']        = "MW/m^2"
    gacode['jnb']['info']        = "Beam-driven current"

    gacode['jrf']                = {} 
    gacode['jrf']['data']        = None
    gacode['jrf']['unit']        = "MW/m^2"
    gacode['jrf']['info']        = "RF-driven current"

    gacode['qpar_beam']          = {} 
    gacode['qpar_beam']['data']  = None
    gacode['qpar_beam']['unit']  = "1/m^3/s"
    gacode['qpar_beam']['info']  = "Beam-particle source density"

    gacode['qpar_wall']          = {} 
    gacode['qpar_wall']['data']  = None
    gacode['qpar_wall']['unit']  = "1/m^3/s"
    gacode['qpar_wall']['info']  = "Wall-particle source density"

    gacode['qmom']               = {} 
    gacode['qmom']['data']       = None
    gacode['qmom']['unit']       = "N/m^2"
    gacode['qmom']['info']       = "The total (convected and conducted) torque density"

    return gacode


def read_gacode_file(fpath):
    if not os.path.isfile(fpath): raise IOError("CAN NOT FIND GACODE.INPUT FILE IN THIS PATH: %s" % fpath)
    fhand = open(fpath,'r')
    nlines = len(fhand.readlines())
    fhand.close()

    gacode = get_gacode_variables()
    fields = list(gacode.keys())

    iline = 0
    while True:
          record = linecache.getline(fpath,iline).split()
          if   'nexp' in record:
               iline += 1
               gacode['nrho']['data'] = int(linecache.getline(fpath,iline).strip())
          elif 'nion' in record:
               iline += 1
               gacode['nion']['data'] = int(linecache.getline(fpath,iline).strip())
          elif 'shot' in record:
               iline += 1
               gacode['shotid']['data'] = int(linecache.getline(fpath,iline).strip())
          elif 'masse' in record:
               iline += 1
               gacode['emass']['data'] = float(linecache.getline(fpath,iline).strip())
          elif 'ze' in record:
               iline += 1
               gacode['ze']['data'] = float(linecache.getline(fpath,iline).strip())
          elif 'torfluxa' in record:
               iline += 1
               gacode['torfluxa']['data'] = float(linecache.getline(fpath,iline).strip())
          elif 'rcentr' in record:
               iline += 1
               gacode['rcentr']['data'] = float(linecache.getline(fpath,iline).strip())
          elif 'bcentr' in record:
               iline += 1
               gacode['bcentr']['data'] = float(linecache.getline(fpath,iline).strip())
          elif 'current' in record:
               iline += 1
               gacode['current']['data'] = float(linecache.getline(fpath,iline).strip())
          elif 'name' in record:
               iline += 1
               gacode['iname']['data'] = [i.strip() for i in linecache.getline(fpath,iline).split()]
          elif 'type' in record:
               iline += 1
               gacode['itype']['data'] = [i.strip() for i in linecache.getline(fpath,iline).split()]
          elif 'mass' in record:
               iline += 1
               gacode['imass']['data'] = [float(i.strip()) for i in linecache.getline(fpath,iline).split()]
          elif 'z' in record:
               iline += 1
               gacode['zi']['data'] = [float(i.strip()) for i in linecache.getline(fpath,iline).split()]
          else:
               if record and len(record) > 1:
                  varname = record[1].strip()
                  if   varname in ['ni','ti','vtor','vpol']:
                       gacode[varname]['data'] = [[] for i in range(gacode['nion']['data'])]
                       for irecord in range(gacode['nrho']['data']):
                           iline += 1
                           if iline == nlines: return(gacode)
                           record = linecache.getline(fpath,iline).split()
                           for i in range(gacode['nion']['data']):
                               gacode[varname]['data'][i].append(float(record[i+1]))
                  elif varname in fields:
                       gacode[varname]['data'] = []
                       for irecord in range(gacode['nrho']['data']):
                           iline += 1
                           record = linecache.getline(fpath,iline).split()
                           gacode[varname]['data'].append(float(record[1]))
                       if iline == nlines: return(gacode)
          iline += 1

    return gacode

def to_instate(fpath,setParam={}):
    gacode = read_gacode_file(fpath)

    type_none = type(None)

    from iofiles.plasmastate import get_instate_vars
    instate = get_instate_vars()

    if   'SHOT_ID' in setParam:
          SHOT_ID = setParam['SHOT_ID']
    elif 'shot_id' in setParam:
          SHOT_ID = setParam['shot_id']
    else:
          SHOT_ID = "%06d" % (int(gacode['shotid']['data']))

    if   'TIME_ID' in setParam:
          TIME_ID = setParam['TIME_ID']
    elif 'time_id' in setParam:
          TIME_ID = setParam['time_id']
    else:
          TIME_ID = "%05d" % (int(numpy.ceil(gacode['timeid']['data']*1.0e4)))

    if   'TOKAMAK_ID' in setParam:
          TOKAMAK_ID = setParam['TOKAMAK_ID']
    elif 'tokamak_id' in setParam:
          TOKAMAK_ID = setParam['tokamak_id']
    else:
          TOKAMAK_ID = "tokamak"

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

    instate['R0']     = [round(float(gacode['rcentr']['data']),                              7)]
    instate['B0']     = [round(float(abs(gacode['bcentr']['data'])),                         7)]
    instate['IP']     = [round(float(gacode['current']['data']) * 1.0e-6,                    7)]
    instate['KAPPA']  = [round(float(gacode['kappa']['data'][-1]),                           7)]
    instate['DELTA']  = [round(float(gacode['delta']['data'][-1]),                           7)]
    instate['RMAJOR'] = [round(float(gacode['rmaj']['data'][-1]),                            7)]
    instate['ASPECT'] = [round(float(gacode['rmaj']['data'][-1]/gacode['rmin']['data'][-1]), 7)]
    instate['AMINOR'] = [round(float(gacode['rmin']['data'][-1]),                            7)]

    ion_inds = []
    imp_inds = []
    for iname in gacode['iname']['data']:
        if iname in ['T','D']: ion_inds.append(gacode['iname']['data'].index(iname))
        else:                  imp_inds.append(gacode['iname']['data'].index(iname))

    N_ION = [len(ion_inds)]
    Z_ION = list(gacode['zi']['data'][i] for i in ion_inds)
    A_ION = list(gacode['imass']['data'][i] for i in ion_inds)
    nitot = 0.0
    for ind in ion_inds: nitot += sum(gacode['ni']['data'][ind])
    F_ION = [round(sum(gacode['ni']['data'][i])/nitot,2) for i in ion_inds]

    N_IMP = [len(imp_inds)]
    Z_IMP = list(gacode['zi']['data'][i] for i in imp_inds)
    A_IMP = list(gacode['imass']['data'][i] for i in imp_inds)
    nitot = 0.0
    for ind in imp_inds: nitot += sum(gacode['ni']['data'][ind])
    F_IMP = [round(sum(gacode['ni']['data'][i])/nitot,2) for i in imp_inds]

    instate['N_ION']    = N_ION
    instate['Z_ION']    = Z_ION
    instate['A_ION']    = A_ION
    instate['F_ION']    = F_ION

    instate['N_IMP']    = N_IMP
    instate['Z_IMP']    = Z_IMP
    instate['A_IMP']    = A_IMP
    instate['F_IMP']    = F_IMP

    instate['N_MIN']    = [0]
    instate['Z_MIN']    = [1]
    instate['A_MIN']    = [1]

    instate['N_BEAM']   = [1]
    instate['Z_BEAM']   = [1]
    instate['A_BEAM']   = [2]

    instate['N_FUSION'] = N_ION
    instate['Z_FUSION'] = Z_ION
    instate['A_FUSION'] = A_ION
    instate['F_FUSION'] = F_ION

    instate['RHO']    = [round(i,2) for i in gacode['rho']['data']    ]
    instate['NRHO']   = [numpy.size(instate['RHO'])                   ]
    instate['PSIPOL'] = [round(i,7) for i in gacode['polflux']['data']]

    instate['NE']      = [round(i,7) for i in gacode['ne']['data']                                     ]
    instate['NI']      = [round(i,7) for i in sum(numpy.array(gacode['ni']['data'])[ion_inds])         ]
    instate['TE']      = [round(i,7) for i in gacode['te']['data']                                     ]
    instate['TI']      = [round(i,7) for i in numpy.mean(numpy.array(gacode['ti']['data'])[ion_inds],0)]
    instate['ZEFF']    = [round(i,7) for i in gacode['z_eff']['data']                                  ]

    instate['OMEGA']   = [round(i,7) for i in gacode['omega0']['data']]

    instate['Q']       = [round(-i,7) for i in gacode['q']['data']     ]
    instate['P_EQ']    = [round(i,7) for i in gacode['ptot']['data']  ]

    instate['SCALE_NE'           ] = [1.0]
    instate['SCALE_SION'         ] = [1.0]
    instate['SCALE_SE_NB'        ] = [1.0]
    instate['SCALE_SI_NB'        ] = [1.0]
    instate['SCALE_SE_IONIZATION'] = [1.0]
    instate['SCALE_SI_IONIZATION'] = [1.0]

    qrad = [i+j+k for (i,j,k) in zip(gacode['qbrem']['data'],gacode['qsync']['data'],gacode['qline']['data'])]
    gacode['qrad'] = {'data':qrad,'unit':'MA/m^3','Info':'Total Radiation'}

    instate['P_EI']   = [round(i,7) for i in (gacode['qei']['data'  ])]
    instate['P_RAD']  = [round(-i,7) for i in (gacode['qrad']['data' ])]
    instate['P_OHM']  = [round(i,7) for i in (gacode['qohme']['data'])]
    instate['PI_CX']  = [round(i,7) for i in (gacode['qcxi']['data' ])]
    instate['PI_FUS'] = [round(i,7) for i in (gacode['qfusi']['data'])]
    instate['PE_FUS'] = [round(i,7) for i in (gacode['qfuse']['data'])]

    if type(gacode['qrfe']['data']) != type_none:
       instate['PE_RF']  = [round(i,7) for i in (gacode['qrfe']['data']  )]
    else:
       instate['PE_RF']  = [round(0.0,7)      for i in range(gacode['nrho']['data'])]
    if type(gacode['qrfi']['data']) != type_none:
       instate['PI_RF']  = [round(i7) for i in (gacode['qrfi']['data']  )]
    else:
       instate['PI_RF']  = [round(0.0,7)      for i in range(gacode['nrho']['data'])]
    instate['PE_NB']  = [round(i,7) for i in (gacode['qbeame']['data'])]
    instate['PI_NB']  = [round(i,7) for i in (gacode['qbeami']['data'])]

    jtot = [i+j+k+m for (i,j,k,m) in zip(gacode['jbs']['data'],gacode['johm']['data'],gacode['jnb']['data'],gacode['jrf']['data'])]
    gacode['jtot'] = {'data':jtot,'unit':'MA/m^2','Info':'Total parallel (inductive + non-inductive) current'}

    instate['J_RF']  = [round(i,7) for i in (gacode['jrf' ]['data'])]
    instate['J_OH']  = [round(i,7) for i in (gacode['johm']['data'])]
    instate['J_NB']  = [round(i,7) for i in (gacode['jnb' ]['data'])]
    instate['J_BS']  = [round(i,7) for i in (gacode['jbs' ]['data'])]
    instate['J_TOT'] = [round(i,7) for i in (gacode['jtot']['data'])]

    instate['TORQUE_NB']     = [round(i,7) for i in gacode['qmom']['data']                  ]
    instate['DENSITY_BEAM']  = [round(i*1.0e-19,7) for i in (gacode['qpar_beam']['data'])]
    instate['SE_IONIZATION'] = [round(i*1.0e-19,7) for i in (gacode['qpar_wall']['data'])]

    if 'J_EC'          in instate and type(instate['J_EC'         ][0]) == type_none: del instate['J_EC'         ]
    if 'J_IC'          in instate and type(instate['J_IC'         ][0]) == type_none: del instate['J_IC'         ]
    if 'J_LH'          in instate and type(instate['J_LH'         ][0]) == type_none: del instate['J_LH'         ]
    if 'J_HC'          in instate and type(instate['J_HC'         ][0]) == type_none: del instate['J_HC'         ]
    if 'CHIE'          in instate and type(instate['CHIE'         ][0]) == type_none: del instate['CHIE'         ]
    if 'CHII'          in instate and type(instate['CHII'         ][0]) == type_none: del instate['CHII'         ]
    if 'PE_EC'         in instate and type(instate['PE_EC'        ][0]) == type_none: del instate['PE_EC'        ]
    if 'PI_EC'         in instate and type(instate['PI_EC'        ][0]) == type_none: del instate['PI_EC'        ]
    if 'PE_IC'         in instate and type(instate['PE_IC'        ][0]) == type_none: del instate['PE_IC'        ]
    if 'PI_IC'         in instate and type(instate['PI_IC'        ][0]) == type_none: del instate['PI_IC'        ]
    if 'PE_LH'         in instate and type(instate['PE_LH'        ][0]) == type_none: del instate['PE_LH'        ]
    if 'PI_LH'         in instate and type(instate['PI_LH'        ][0]) == type_none: del instate['PI_LH'        ]
    if 'PE_HC'         in instate and type(instate['PE_HC'        ][0]) == type_none: del instate['PE_HC'        ]
    if 'PI_HC'         in instate and type(instate['PI_HC'        ][0]) == type_none: del instate['PI_HC'        ]
    if 'SE_NB'         in instate and type(instate['SE_NB'        ][0]) == type_none: del instate['SE_NB'        ]
    if 'SI_NB'         in instate and type(instate['SI_NB'        ][0]) == type_none: del instate['SI_NB'        ]
    if 'WBEAM'         in instate and type(instate['WBEAM'        ][0]) == type_none: del instate['WBEAM'        ]
    if 'WALPHA'        in instate and type(instate['WALPHA'       ][0]) == type_none: del instate['WALPHA'       ]
    if 'PPRIME'        in instate and type(instate['PPRIME'       ][0]) == type_none: del instate['PPRIME'       ]
    if 'FFPRIME'       in instate and type(instate['FFPRIME'      ][0]) == type_none: del instate['FFPRIME'      ]
    if 'TORQUE_IN'     in instate and type(instate['TORQUE_IN'    ][0]) == type_none: del instate['TORQUE_IN'    ]
    if 'DENSITY_ALPHA' in instate and type(instate['DENSITY_ALPHA'][0]) == type_none: del instate['DENSITY_ALPHA']
    if 'SI_IONIZATION' in instate and type(instate['SI_IONIZATION'][0]) == type_none: del instate['SI_IONIZATION']
    if 'PE_IONIZATION' in instate and type(instate['PE_IONIZATION'][0]) == type_none: del instate['PE_IONIZATION']
    if 'PI_IONIZATION' in instate and type(instate['PI_IONIZATION'][0]) == type_none: del instate['PI_IONIZATION']

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
        instate['OMEGA'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['OMEGA'        ])]

        instate['Q'            ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['Q'            ])]
        instate['P_EQ'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['P_EQ'         ])]

        psiaxis = 0.0
        psibdry = 1.0
        PSI    = (psibdry-psiaxis)
        PSI   *= numpy.arange(instate['NRHO'][0])/(instate['NRHO'][0]-1.0)
        PSIN   = (PSI-PSI[0])/(PSI[-1]-PSI[0])
        RHOPSI = numpy.sqrt(PSIN)
        instate['RHOPSI'       ] = [round(i,7) for i in RHOPSI                                                ]

        instate['J_RF'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_RF'         ])]
        instate['J_OH'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_OH'         ])]
        instate['J_NB'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_NB'         ])]
        instate['J_BS'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_BS'         ])]
        instate['J_TOT'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['J_TOT'        ])]

        instate['PE_RF'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PE_RF'        ])]
        instate['PE_NB'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PE_NB'        ])]
        instate['PI_NB'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PI_NB'        ])]

        instate['P_EI'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['P_EI'         ])]
        instate['P_RAD'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['P_RAD'        ])]
        instate['P_OHM'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['P_OHM'        ])]
        instate['PI_CX'        ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PI_CX'        ])]
        instate['PI_FUS'       ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PI_FUS'       ])]
        instate['PE_FUS'       ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['PE_FUS'       ])]

        instate['TORQUE_NB'    ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['TORQUE_NB'    ])]

        instate['SION'         ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['SE_IONIZATION'])]
        instate['SE_IONIZATION'] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['SE_IONIZATION'])]

        instate['DENSITY_BEAM' ] = [round(i,7) for i in numpy.interp(new_rho,old_rho,instate['DENSITY_BEAM' ])]

    from tokamak.plasma.get_plasma_shape import get_plasma_shape
    rmajor = gacode['rmaj' ]['data'][-1]
    rminor = gacode['rmin' ]['data'][-1]
    kappa  = gacode['kappa']['data'][-1]
    delta  = gacode['delta']['data'][-1]
    zeta   = gacode['zeta' ]['data'][-1]
    Rlcfs,Zlcfs = get_plasma_shape(rmajor,rminor,delta,kappa,zeta)

    gacode['Rlcfs'] = {'data':Rlcfs,'unit':None,'Info':None}
    gacode['Zlcfs'] = {'data':Zlcfs,'unit':None,'Info':None}

    NBDRYmax = 85
    NBDRY = numpy.size(Rlcfs)
    if NBDRY > NBDRYmax:
       BDRY = zip(Rlcfs,Zlcfs)
       import random
       BDRYINDS = sorted(random.sample(range(NBDRY),NBDRYmax))
       instate['NBDRY'] = [NBDRYmax]
       instate['RBDRY'] = [round(i,7) for i in Rlcfs[BDRYINDS]]
       instate['ZBDRY'] = [round(i,7) for i in Zlcfs[BDRYINDS]]
    else:
       instate['NBDRY'] = [numpy.size(lcfs)]
       instate['RBDRY'] = [round(i,7) for i in Rlcfs]
       instate['ZBDRY'] = [round(i,7) for i in Zlcfs]

    if type(instate['NLIM'][0]) == type_none:
       RLIM_MAX = max(instate['RBDRY']) + 0.10
       RLIM_MIN = min(instate['RBDRY']) - 0.10
       ZLIM_MAX = max(instate['ZBDRY']) + 0.10
       ZLIM_MIN = min(instate['ZBDRY']) - 0.10
       instate['RLIM'] = [RLIM_MAX, RLIM_MIN, RLIM_MIN, RLIM_MAX, RLIM_MAX]
       instate['ZLIM'] = [ZLIM_MAX, ZLIM_MAX, ZLIM_MIN, ZLIM_MIN, ZLIM_MAX]
       instate['NLIM'] = [len(instate['RLIM'])]

    from iofiles.Namelist    import Namelist
    INSTATE = Namelist()
    INSTATE['instate'] = {}
    INSTATE['instate'].update(instate)
    INSTATE.write("instate_%s_%s.%s" % (TOKAMAK_ID,SHOT_ID,TIME_ID))

    return gacode


if __name__ == "__main__":
   fpath = sys.argv[1]
  #gacode = read_gacode_file(fpath)
  #import matplotlib.pyplot as plt
  #plt.plot(gacode['rho']['data'],gacode['ni']['data'][0],label="T")
  #plt.plot(gacode['rho']['data'],gacode['ni']['data'][1],label='D')
  #plt.plot(gacode['rho']['data'],gacode['ni']['data'][2],label='He')
  #plt.plot(gacode['rho']['data'],gacode['ni']['data'][3],label='N')
  #plt.legend()
  #plt.show()
   gacode = to_instate(fpath)

