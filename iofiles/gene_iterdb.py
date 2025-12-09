import os
import re
import traceback

import numpy as npy

from maths.interp      import interp
from maths.derivative  import derivative

from iofiles.eqdsk     import read_eqdsk
from iofiles.phigrids  import phigrids
from iofiles.psigrids  import psigrids


def get_next(data_linesplit,lnum,num):
    sec_num_lines = num/6
    if num % 6 != 0:
        sec_num_lines += 1
    keep_going=1
    while keep_going:
        test=re.search('-DEPENDENT VARIABLE LABEL',data_linesplit[lnum])
        if test :
            quantity=data_linesplit[lnum].split()[0]
            units=data_linesplit[lnum].split()[1]
        test=re.search('DATA FOLLOW',data_linesplit[lnum])
        if test:
            keep_going=(1==2)
        lnum=lnum+1

    rhot=npy.empty(0)
    lnum0 = lnum
    for j in range(lnum0,lnum0+int(sec_num_lines)):
        for k in range(6):
            str_temp=data_linesplit[j][1+k*13:1+(k+1)*13]
            if(str_temp):
                temp=npy.array(data_linesplit[j][1+k*13:1+(k+1)*13],dtype='float')
                rhot=npy.append(rhot,temp)
        lnum=lnum+1
    lnum=lnum+1

    arr=npy.empty(0)
    lnum0 = lnum
    for j in range(lnum0,lnum0+int(sec_num_lines)):
        for k in range(6):
            str_temp=data_linesplit[j][1+k*13:1+(k+1)*13]
            if(str_temp):
                temp=npy.array(data_linesplit[j][1+k*13:1+(k+1)*13],dtype='float')
                arr=npy.append(arr,temp)
        lnum=lnum+1

    lnum_out=lnum
    try_again=1
    if len(data_linesplit)-lnum < 10:
        try_again=False
    return lnum_out, try_again,quantity,units,rhot,arr


def read_iterdb_file(filename):
    '''
    This Code is Written by: David R. Hatch
    It reads the iterdb file and returns three dictionaries,
    each diectionary has five quantities:
    electron density (NE) and temperature (TE),
    ion density (NM1) and temperatures (TI),
    impurity density (NM2), if any,
    rotational velocity (VROT).
    The three dictionaries provide the toroidal coordinate (rhotor),
    profiles, and units for each quantity.
    '''
    f=open(filename,'r')
    data_in=f.read()
    data_linesplit=data_in.split('\n')

    keep_going=1
    i=0
    while keep_going:
        test=re.search(';-# OF X PTS',data_linesplit[i])
        if test:
            num=data_linesplit[i].split()[0]
            num=float(num)
            num=int(num)
            keep_going=(1==2)
        if i == len(data_linesplit):
            keep_going=(1==2)
        i=i+1

    lnum=0
    try_again=1
    prof_out = {}
    rhot_out = {}
    units_out = {}
    while try_again:
        lnum,try_again,quantity,units,rhot,arr=get_next(data_linesplit,lnum,num)
        prof_out[quantity]=arr
        units_out[quantity]=units
        rhot_out[quantity]=rhot
    return rhot_out,prof_out,units_out


def read_iterdb(fpath,setParam={},**kwargs):
    if os.path.isfile(fpath) == False:
       errorFunc = traceback.extract_stack(limit=2)[-2][3]
       errorLine = traceback.extract_stack(limit=2)[-2][1]
       errorFile = traceback.extract_stack(limit=2)[-2][2]
       errMSG    = 'Call %s line %5d in file %s Failed.\n'
       errMSG   += 'Fatal: file %s not found.'
       raise IOError(errMSG %(errorFunc,errorLine,errorFile,fpath))

    rhopsiflag = False; rhotorflag = False
    if   'nrhomesh' in setParam:
         if   setParam['nrhomesh'] in [0,'rhopsi']: rhopsiflag = True
         elif setParam['nrhomesh'] in [1,'rhotor']: rhotorflag = True
    elif kwargs.items():
         rhopsiflag = True
    else:
         rhotorflag = True

    rhotors,profiles,units = read_iterdb_file(fpath)

    '''
    Normalizing the rhotor vectors before using them to interpolate the physical quantities
    '''
    if int(rhotors['NE'][-1]) == 1:
       rhotorNE    = rhotors['NE'][:]
       rhotorTE    = rhotors['TE'][:]
       rhotorNM1   = rhotors['NM1'][:]
       rhotorTI    = rhotors['TI'][:]
       if 'NM2' in profiles:
          rhotorNM2  = rhotors['NM2'][:]
       if 'VROT' in profiles:
          rhotorVROT = rhotors['VROT'][:]
    else:
       rhotorNE    = (rhotors['NE']-rhotors['NE'][0])/(rhotors['NE'][-1]-rhotors['NE'][0])
       rhotorTE    = (rhotors['TE']-rhotors['TE'][0])/(rhotors['TE'][-1]-rhotors['TE'][0])
       rhotorNM1   = (rhotors['NM1']-rhotors['NM1'][0])/(rhotors['NM1'][-1]-rhotors['NM1'][0])
       rhotorTI    = (rhotors['TI']-rhotors['TI'][0])/(rhotors['TI'][-1]-rhotors['TI'][0])
       if 'NM2' in profiles:
        rhotorNM2  = (rhotors['NM2']-rhotors['NM2'][0])/(rhotors['NM2'][-1]-rhotors['NM2'][0])
       if 'VROT' in profiles:
        rhotorVROT = (rhotors['VROT']-rhotors['VROT'][0])/(rhotors['VROT'][-1]-rhotors['VROT'][0])

    eqdskflag    = False
    cheaseflag   = False
    interpflag   = False
    importedflag = False
    for key,value in kwargs.items():
        if   key in ['chease','cheasedata','cheasefpath']:
             if    type(value)==str and os.path.isfile(value.strip()):
                   cheasedata = read_chease(fpath=value.strip())
             else: raise IOError('%s file not found!' % value.strip())
             if 'rhopsi' in cheasedata: rhopsi = cheasedata['rhopsi'][:]; interpflag = True
             if 'rhotor' in cheasedata: rhotor = cheasedata['rhotor'][:]; interpflag = True
             cheaseflag = True
        elif key in ['eqdsk','eqdskdata','eqdskfpath']:
             if    type(value)==dict:
                   eqdskdata = value.copy()
             elif  type(value)==str and os.path.isfile(value.strip()):
                   eqdskdata = read_eqdsk(fpath=value.strip())
             else: raise IOError('%s file not found!' % value.strip())
             if 'rhopsi' in eqdskdata: rhopsi = eqdskdata['rhopsi'][:]; interpflag = True
             else:
                 calc_rho = psigrids()
                 _,_,rhopsi = calc_rho(eqdskdata)
                 interpflag = True
             if 'rhotor' in eqdskdata: rhotor = eqdskdata['rhotor'][:]; interpflag = True
             else:
                 calc_rho = phigrids()
                 _,_,_,_,rhotor = calc_rho(eqdskdata)
                 interpflag = True
             eqdskflag = True
        elif key in ['imported','external','other']:
             imported = value.copy()
             if 'rhopsi' in imported: rhopsi = imported['rhopsi'][:]; interpflag = True
             if 'rhotor' in imported: rhotor = imported['rhotor'][:]; interpflag = True
             importedflag = True
        else:
             rhotor  = rhotorNE[:]

    ITERDBdata       = {}
    ITERDBdata['Zi'] = 1.0
    ITERDBdata['Zz'] = 6.0

    if   rhopsiflag and interpflag:
         ITERDBdata['rhopsi'] = rhopsi
         ITERDBdata['rhotor'] = rhotor
    elif rhotorflag and interpflag:
         ITERDBdata['rhopsi'] = rhopsi
         ITERDBdata['rhotor'] = rhotor
    elif rhopsiflag and not interpflag:
         print("WARNING: setParam['nrhomesh'] = 0 or rhopsi, but the path to a target rhopsi is not provided.")
         print("         Converting the profiles to poloidal (psi) coordinates could not be done, and")
         print("         all profiles are provided in the toroidal (phi) coordinates.")
    else:
         ITERDBdata['rhotor'] = rhotorNE

    nrhosize = npy.size(ITERDBdata['rhotor'])

    if   rhopsiflag and interpflag:
         calc_interp = interp()
         ITERDBdata['Te']      = calc_interp(rhotors['TE'],profiles['TE'],rhotor,rhopsi,rhopsi)
         ITERDBdata['Ti']      = calc_interp(rhotors['TI'],profiles['TI'],rhotor,rhopsi,rhopsi)
         ITERDBdata['ne']      = calc_interp(rhotors['NE'],profiles['NE'],rhotor,rhopsi,rhopsi)
         ITERDBdata['ni']      = calc_interp(rhotors['NM1'],profiles['NM1'],rhotor,rhopsi,rhopsi)
         if 'NM2' in profiles:
            ITERDBdata['nz']   = calc_interp(rhotors['NM2'],profiles['NM2'],rhotor,rhopsi,rhopsi)
         else:
            ITERDBdata['nz']   = npy.zeros(nrhosize)
         if 'VROT' in profiles :
            ITERDBdata['Vrot']   = calc_interp(rhotors['VROT'],profiles['VROT'],rhotor,rhopsi,rhopsi)
         else:
            ITERDBdata['Vrot'] = npy.zeros(nrhosize)
    elif rhotorflag and interpflag:
         calc_interp = interp()
         ITERDBdata['ne']      = calc_interp(rhotors['NE'],profiles['NE'],rhotor)
         ITERDBdata['Te']      = calc_interp(rhotors['TE'],profiles['TE'],rhotor)
         ITERDBdata['ni']      = calc_interp(rhotors['NM1'],profiles['NM1'],rhotor)
         ITERDBdata['Ti']      = calc_interp(rhotors['TI'],profiles['TI'],rhotor)
         if 'NM2' in profiles:
            ITERDBdata['nz']   = calc_interp(rhotors['NM2'],profiles['NM2'],rhotor)
         else:
            ITERDBdata['nz']   = npy.zeros(nrhosize)
         if 'VROT' in profiles :
            ITERDBdata['Vrot'] = calc_interp(rhotors['VROT'],profiles['VROT'],rhotor)
         else:
            ITERDBdata['Vrot'] = npy.zeros(nrhosize)
    else:
         calc_interp = interp()
         ITERDBdata['ne']      = calc_interp(rhotors['NE'],profiles['NE'],rhotorNE)
         ITERDBdata['Te']      = calc_interp(rhotors['TE'],profiles['TE'],rhotorNE)
         ITERDBdata['ni']      = calc_interp(rhotors['NM1'],profiles['NM1'],rhotorNE)
         ITERDBdata['Ti']      = calc_interp(rhotors['TI'],profiles['TI'],rhotorNE)
         if 'NM2' in profiles:
            ITERDBdata['nz']   = calc_interp(rhotors['NM2'],profiles['NM2'],rhotorNE)
         else:
            ITERDBdata['nz']   = npy.zeros(nrhosize)
         if 'VROT' in profiles :
            ITERDBdata['Vrot'] = calc_interp(rhotors['VROT'],profiles['VROT'],rhotorNE)
         else:
            ITERDBdata['Vrot'] = npy.zeros(nrhosize)

    ITERDBdata['Zeff']    = ITERDBdata['ni']*ITERDBdata['Zi']**2
    ITERDBdata['Zeff']   += ITERDBdata['nz']*ITERDBdata['Zz']**2
    ITERDBdata['Zeff']   /= ITERDBdata['ne']

    ITERDBdata['pressure']   = ITERDBdata['Te']*ITERDBdata['ne']
    ITERDBdata['pressure']  += ITERDBdata['Ti']*ITERDBdata['ni']
    ITERDBdata['pressure']  += ITERDBdata['Ti']*ITERDBdata['nz']
    ITERDBdata['pressure']  *= 1.602e-19

    if   rhopsiflag and interpflag:
         calc_derivative = derivative()
         ITERDBdata['pprime']= calc_derivative(x=ITERDBdata['rhopsi'],f=ITERDBdata['pressure'],method='CubicSpline')
    else:
         calc_derivative = derivative()
         ITERDBdata['pprime']= calc_derivative(x=ITERDBdata['rhotor'],f=ITERDBdata['pressure'],method='CubicSpline')

    return ITERDBdata


def write_iterdb_field(fhand,rho,field,fieldname,fieldunit,SHOT_ID,TIME_ID):
    header=' 99999  xyz 2              ;-SHOT #- F(X) DATA \n'
   #header=' ' + SHOT_ID + '              ;-SHOT #- F(X) DATA \n'
    header=header + '                              ;-SHOT DATE-  UFILES ASCII FILE SYSTEM\n'
    header=header + '   0                          ;-NUMBER OF ASSOCIATED SCALAR QUANTITIES\n'
    header=header + ' RHOTOR              -        ;-INDEPENDENT VARIABLE LABEL: X-\n'
    header=header + ' TIME                SECONDS  ;-INDEPENDENT VARIABLE LABEL: Y-\n'
    spaces = '                '
    if(len(fieldname)==3):
        spaces += ' '
    elif(len(fieldname)==2):
        spaces += '  '
    header=header+' '+fieldname+spaces+fieldunit+'           ;-DEPENDENT VARIABLE LABEL\n'
    header=header+' 3                            ;-PROC CODE- 0:RAW 1:AVG 2:SM. 3:AVG+SM\n'
    header=header+'      '+str(len(field))+'                   ;-# OF X PTS- \n'
    header=header+'      1                   ;-# OF Y PTS-  X,Y,F(X,Y) DATA FOLLOW:\n'

    footer=';----END-OF-DATA-----------------COMMENTS:-----------\n'
    footer=footer+'********************************************************************************\n'
    footer=footer+'********************************************************************************\n'

    fhand.write(header)
    for irec in range(0,len(rho),6):
        fieldrecord = ""
        for jrec in range(irec,irec+6):
            if jrec != len(rho): fieldrecord += "% 12e" % rho[jrec]
        fhand.write(" " + fieldrecord + "\n")
    fhand.write('  ' + TIME_ID + '\n')
    for irec in range(0,len(field),6):
        fieldrecord = ""
        for jrec in range(irec,irec+6):
            if jrec != len(field): fieldrecord += "% 12e" % field[jrec]
        fhand.write(" " + fieldrecord + "\n")
    fhand.write(footer)
    return header

def write_iterdb(iterdbdata,iterdbparam):
    if 'TOKAMAK'     in iterdbparam: TOKAMAK     = iterdbparam['TOKAMAK']
    else:                            TOKAMAK     = "TOKAMAK"
    if 'SHOT_ID'     in iterdbparam: SHOT_ID     = iterdbparam['SHOT_ID']
    else:                            SHOT_ID     = "000000"
    if 'TIME_ID'     in iterdbparam: TIME_ID     = iterdbparam['TIME_ID']
    else:                            TIME_ID     = "00000"
    if 'ITERDBFNAME' in iterdbparam: iterdbfname = iterdbparam['ITERDBFNAME']
    else:                            iterdbfname = "%s.%s.iterdb" % (SHOT_ID,TIME_ID)
                                    #iterdbfname = TOKAMAK + "_" + SHOT_ID + "_" + TIME_ID + ".iterdb"
    fhand=open(iterdbfname,'w')

    header  = ';Created with script write_iterdb.py for GENE input\n'

