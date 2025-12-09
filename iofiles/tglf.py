import os
import sys
import numpy

def read_inputs(fpath):
    if os.path.isdir(fpath):    fpath = os.path.join(fpath,"input.tglf.gen")
    elif os.path.isfile(fpath): fpath = os.path.join(".",fpath)

    path_to_file = os.getcwd()

    fhand = open(fpath,"r")
    lines = fhand.readlines()
    nline = len(lines)

    input_vars = {}
    for i in range(1,nline):
        contents = lines[i].split()
        if   contents[0] == 'T':
             contents[0] = True
             input_vars[contents[1]] = contents[0]
        elif contents[0] == 'F':
             contents[0] = False
             input_vars[contents[1]] = contents[0]
        else:
             input_vars[contents[1]] = float(contents[0])
    input_vars['NFIELDS'] = 1
    if input_vars['USE_BPAR']: input_vars['NFIELDS'] += 1
    if input_vars['USE_BPER']: input_vars['NFIELDS'] += 1

    return input_vars

def read_sum_flux_spectrum(fpath):
    if os.path.isdir(fpath):    fpath = os.path.join(fpath,"out.tglf.sum_flux_spectrum")
    elif os.path.isfile(fpath): fpath = os.path.join(".",fpath)
    path_to_file = os.path.dirname(fpath)

    input_vars = read_inputs(path_to_file)

    fluxes = {}

    fhand = open(fpath,"r")
    lines = fhand.readlines()
    nline = len(lines)
    i = 0
    while True:
        if i >= nline:
           fluxes[fluxes_ind]['field'          ] = field
           fluxes[fluxes_ind]['species'        ] = species
           fluxes[fluxes_ind]['exchange'       ] = exchange[:]
           fluxes[fluxes_ind]['energy_flux'    ] = energy_flux[:]
           fluxes[fluxes_ind]['particle_flux'  ] = particle_flux[:]
           fluxes[fluxes_ind]['toroidal_stress'] = toroidal_stress[:]
           fluxes[fluxes_ind]['parallel_stress'] = parallel_stress[:]
           break

        if "species" in lines[i]:
           if i > 0:
              fluxes[fluxes_ind]['field'          ] = field
              fluxes[fluxes_ind]['species'        ] = species
              fluxes[fluxes_ind]['exchange'       ] = exchange[:]
              fluxes[fluxes_ind]['energy_flux'    ] = energy_flux[:]
              fluxes[fluxes_ind]['particle_flux'  ] = particle_flux[:]
              fluxes[fluxes_ind]['toroidal_stress'] = toroidal_stress[:]
              fluxes[fluxes_ind]['parallel_stress'] = parallel_stress[:]
           _,_,species,_,_,field = lines[i].split()
           fluxes_ind = '%d%d' % (int(species),int(field))
           fluxes[fluxes_ind] = {}
           exchange        = []
           energy_flux     = []
           particle_flux   = []
           toroidal_stress = []
           parallel_stress = []
           i += 1
        elif "particle" in lines[i]:
           i += 1
           pass
        else:
           contents = lines[i].split()
           particle_flux.append(  float(contents[0]))
           energy_flux.append(    float(contents[1]))
           toroidal_stress.append(float(contents[2]))
           i += 1
           contents = lines[i].split()
           parallel_stress.append(float(contents[0]))
           exchange.append(       float(contents[1]))
           i += 1
    return fluxes

def read_ky_spectrum(fpath):
    if os.path.isdir(fpath):    fpath = os.path.join(fpath,"out.tglf.ky_spectrum")
    elif os.path.isfile(fpath): fpath = os.path.join(".",fpath)
    path_to_file = os.path.dirname(fpath)

    input_vars = read_inputs(path_to_file)

    ky = []

    fhand = open(fpath,"r")
    lines = fhand.readlines()
    nline = len(lines)
    nky = int(lines[1])
    for iky in range(nky): ky.append(float(lines[2+iky]))

    return ky

def read_eigenvalue_spectrum(fpath):
    if os.path.isdir(fpath):    fpath = os.path.join(fpath,"out.tglf.eigenvalue_spectrum")
    elif os.path.isfile(fpath): fpath = os.path.join(".",fpath)
    path_to_file = os.path.dirname(fpath)

    input_vars = read_inputs(path_to_file)
    nmodes = int(input_vars['NMODES'])

    nrecords = 2 * int(nmodes)
    lines_per_records = int((nrecords+2) / 3)

    fhand = open(fpath,"r")
    lines = fhand.readlines()
    nline = len(lines)

    eigenvalues = {}
    eigenvalues['nmodes'] = nmodes

    i = 2
    iky = 1
    while True:
          if i >= nline: break
          eigenvalues[iky] = {}
          records = []
          for iline in range(lines_per_records):
              records.extend([float(record) for record in lines[i].split()])
              i += 1
          eigenvalues[iky]['gamma'] = records[0:nrecords-1:2]
          eigenvalues[iky]['omega'] = records[1:nrecords  :2]
          iky += 1
    return eigenvalues

def read_field_spectrum(fpath):
    if os.path.isdir(fpath):    fpath = os.path.join(fpath,"out.tglf.field_spectrum")
    elif os.path.isfile(fpath): fpath = os.path.join(".",fpath)
    path_to_file = os.path.dirname(fpath)

    input_vars = read_inputs(path_to_file)
    nmodes = int(input_vars['NMODES'])

    nrecords = 2 * int(nmodes)
    lines_per_records = int((nrecords+2) / 3)

    fhand = open(fpath,"r")
    lines = fhand.readlines()
    nline = len(lines)

    fields = {}
    fields['nmodes'] = nmodes

    for imode in range(nmodes):
        fields[imode] = {}
        fields[imode]['ephi'] = []
        fields[imode]['apar'] = []
        fields[imode]['aper'] = []

    imode = 0
    for iline in range(6,nline,lines_per_records):
        imode = imode % nmodes
        records = []
        for irecord in range(lines_per_records):
            records.extend([float(record) for record in lines[iline+irecord].split()])
        fields[imode]['ephi'].append(float(records[1]))
        fields[imode]['apar'].append(float(records[2]))
        fields[imode]['aper'].append(float(records[3]))
        imode += 1

    return fields

def read_density_spectrum(fpath):
    if os.path.isdir(fpath):    fpath = os.path.join(fpath,"out.tglf.density_spectrum")
    elif os.path.isfile(fpath): fpath = os.path.join(".",fpath)
    path_to_file = os.path.dirname(fpath)

    input_vars = read_inputs(path_to_file)
    nspecs = int(input_vars['NS'])

    fhand = open(fpath,"r")
    lines = fhand.readlines()
    nline = len(lines)

    density = {}
    for ispec in range(nspecs):
        density[ispec] = []
    
    for iline in range(2,nline):
        records = [float(record) for record in lines[iline].split()]
        for ispec in range(nspecs):
            density[ispec].append(records[ispec])

    return density

def read_temperature_spectrum(fpath):
    if os.path.isdir(fpath):    fpath = os.path.join(fpath,"out.tglf.temperature_spectrum")
    elif os.path.isfile(fpath): fpath = os.path.join(".",fpath)
    path_to_file = os.path.dirname(fpath)

    input_vars = read_inputs(path_to_file)
    nspecs = int(input_vars['NS'])

    fhand = open(fpath,"r")
    lines = fhand.readlines()
    nline = len(lines)

    temperature = {}
    for ispec in range(nspecs):
        temperature[ispec] = []

    for iline in range(2,nline):
        records = [float(record) for record in lines[iline].split()]
        for ispec in range(nspecs):
            temperature[ispec].append(records[ispec])

    return temperature

def read_crossphase_spectrum(fpath):
    if os.path.isdir(fpath):    fpath = os.path.join(fpath,"out.tglf.nsts_crossphase_spectrum")
    elif os.path.isfile(fpath): fpath = os.path.join(".",fpath)
    path_to_file = os.path.dirname(fpath)

    input_vars = read_inputs(path_to_file)
    nspecs = int(input_vars['NS'])
    nmodes = int(input_vars['NMODES'])
    nky    = len(read_ky_spectrum(path_to_file))

    fhand = open(fpath,"r")
    lines = fhand.readlines()
    nline = len(lines)
    
    crossphase = {}
    for ispec in range(nspecs):
        crossphase[ispec] = {}
        for imode in range(nmodes):
            crossphase[ispec][imode] = []

    for ispec in range(nspecs):
        for iky in range(nky):
            records = [float(irecord) for irecord in lines[iky+ispec*nky+2*(ispec+1)+1].split()]
            for imode in range(nmodes):
                crossphase[ispec][imode].append(records[imode])

    return crossphase

def read_ql_flux_spectrum(fpath):
    if os.path.isdir(fpath):    fpath = os.path.join(fpath,"out.tglf.ql_flux_spectrum")
    elif os.path.isfile(fpath): fpath = os.path.join(".",fpath)
    path_to_file = os.path.dirname(fpath)

    fhand = open(fpath,"r")
    lines = fhand.readlines()
    nline = len(lines)

   #input_vars = read_inputs(path_to_file)
   #nspecs  = int(input_vars['NS'])
   #nmodes  = int(input_vars['NMODES'])
   #nfields = int(input_vars['NFIELDS'])
   #nky     = len(read_ky_spectrum(path_to_file))

    nfluxes,nspecs,nfields,nky,nmodes = [int(irecord) for irecord in lines[3].split()]

    nrecords = nfluxes
    lines_per_records = int((nrecords+2) / 3)

#   particle, energy, toroidal stress, parallel stress, exchange

    fluxes = {}
    fluxes['nky'] = nky
    fluxes['nspecs'] = nspecs
    fluxes['nmodes'] = nmodes
    fluxes['nfields'] = nfields

    for imode in range(nmodes):
        for ispec in range(nspecs):
            for ifield in range(nfields):
                fluxes[imode,ispec,ifield] = {}
                fluxes[imode,ispec,ifield]['particle'       ] = []
                fluxes[imode,ispec,ifield]['energy'         ] = []
                fluxes[imode,ispec,ifield]['toroidal_stress'] = []
                fluxes[imode,ispec,ifield]['parallel_stress'] = []
                fluxes[imode,ispec,ifield]['exchange'       ] = []

    nbulk = nmodes * lines_per_records * nky + 3
    for iline in range(4,nline,nbulk):
        records = lines[iline].split()
        ispec  = int(records[2]) - 1
        ifield = int(records[5]) - 1
        iline += 1
        records = lines[iline].split()
        imode  = int(records[2]) - 1
        iline += 1
        for cline in range(iline,iline+lines_per_records*nky,lines_per_records):
            records = []
            for irecord in range(lines_per_records):
                records.extend([record for record in lines[cline+irecord].split()])
            fluxes[imode,ispec,ifield]['particle'       ].append(float(records[0]))
            fluxes[imode,ispec,ifield]['energy'         ].append(float(records[1]))
            fluxes[imode,ispec,ifield]['toroidal_stress'].append(float(records[2]))
            fluxes[imode,ispec,ifield]['parallel_stress'].append(float(records[3]))
            fluxes[imode,ispec,ifield]['exchange'       ].append(float(records[4]))
        iline = cline + 2
        records = lines[iline].split()
        imode  = int(records[2]) - 1
        iline += 1
        for cline in range(iline,iline+lines_per_records*nky,lines_per_records):
            records = []
            for irecord in range(lines_per_records):
                records.extend([record for record in lines[cline+irecord].split()])
            fluxes[imode,ispec,ifield]['particle'       ].append(float(records[0]))
            fluxes[imode,ispec,ifield]['energy'         ].append(float(records[1]))
            fluxes[imode,ispec,ifield]['toroidal_stress'].append(float(records[2]))
            fluxes[imode,ispec,ifield]['parallel_stress'].append(float(records[3]))
            fluxes[imode,ispec,ifield]['exchange'       ].append(float(records[4]))

    return fluxes

def read_wavefunction(fpath):
    if os.path.isdir(fpath):    fpath = os.path.join(fpath,"out.tglf.wavefunction")
    elif os.path.isfile(fpath): fpath = os.path.join(".",fpath)
    path_to_file = os.path.dirname(fpath)

   #input_vars = read_inputs(path_to_file)
   #nspecs  = int(input_vars['NS'])
   #nmodes  = int(input_vars['NMODES'])
   #nfields = int(input_vars['NFIELDS'])

    fhand = open(fpath,"r")
    lines = fhand.readlines()
    nline = len(lines)
    
    nmodes, nfields, nky = [int(record) for record in lines[0].split()]

    nrecords = 1 + 2*nfields*nmodes
    lines_per_records = int(numpy.ceil(nrecords / 3))

    wavefunction = {}
    wavefunction['nmodes']  = nmodes
    wavefunction['nfields'] = nfields
    wavefunction['ky']   = []
    wavefunction['ephi'] = [[] for i in range(nmodes)]
    wavefunction['apar'] = [[] for i in range(nmodes)]
    wavefunction['aper'] = [[] for i in range(nmodes)]
    for iline in range(2,nline,lines_per_records):
        records = []
        for irecord in range(lines_per_records):
            records.extend([float(record) for record in lines[iline+irecord].split()])
        wavefunction['ky'].append(records[0])
        for imode in range(nmodes):
            for ifield in range(nfields):
                irecord = nfields * nmodes * imode + nfields * ifield + 1
                if   ifield == 0:
                   wavefunction['ephi'][imode].append(complex(records[irecord],records[irecord+1]))
                elif ifield == 1:
                   wavefunction['aper'][imode].append(complex(records[irecord],records[irecord+1]))
                elif ifield == 2:
                   wavefunction['apar'][imode].append(complex(records[irecord],records[irecord+1]))
    
    return wavefunction

if __name__ == "__main__":
   fpath = sys.argv[1]
  #input_vars = read_inputs(fpath)
  #print(input_vars)
  #fluxes = read_sum_flux_spectrum(fpath) 
  #ky = read_ky_spectrum(fpath) 
  #eigenvalues = read_eigenvalue_spectrum(fpath)
  #fields = read_field_spectrum(fpath)
  #density = read_density_spectrum(fpath)
  #temperature = read_temperature_spectrum(fpath)
  #crossphase = read_crossphase_spectrum(fpath)
  #qlflux = read_ql_flux_spectrum(fpath)
   wavefunction = read_wavefunction(fpath)
   print(wavefunction)
