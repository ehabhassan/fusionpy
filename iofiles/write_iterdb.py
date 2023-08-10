

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
    header += ';----END-OF-ORIGINAL-HEADER------COMMENTS:-----------\n'
    fhand.write(header)

    write_iterdb_field(fhand,iterdbdata['rho'],1.0e3*iterdbdata['te'],'TE', 'eV',  SHOT_ID,TIME_ID)
    write_iterdb_field(fhand,iterdbdata['rho'],1.0e3*iterdbdata['ti'],'TI', 'eV',  SHOT_ID,TIME_ID)
    write_iterdb_field(fhand,iterdbdata['rho'],1.0e19*iterdbdata['ne'],'NE', 'm^-3',SHOT_ID,TIME_ID)
    write_iterdb_field(fhand,iterdbdata['rho'],1.0e19*iterdbdata['ni'],'NM1','m^-3',SHOT_ID,TIME_ID)
    if "nz" in iterdbdata and iterdbdata["nz"].any():
        write_iterdb_field(fhand,iterdbdata['rho'],1.0e19*iterdbdata['nz'],'NM2','m^-3',SHOT_ID,TIME_ID)
    if "omega" in iterdbdata and iterdbdata["omega"].any():
        write_iterdb_field(fhand,iterdbdata['rho'],iterdbdata['omega'],'VROT','rad/s',SHOT_ID,TIME_ID)

    fhand.close()

    return iterdbfname


