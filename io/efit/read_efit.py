

def read_efit(eqdskfpath):
   #Developed by Ehab Hassan on 2019-02-27
    if os.path.isfile(eqdskfpath) == False:
       errorFunc = traceback.extract_stack(limit=2)[-2][3]
       errorLine = traceback.extract_stack(limit=2)[-2][1]
       errorFile = traceback.extract_stack(limit=2)[-2][2]
       errMSG    = 'Call %s line %5d in file %s Failed.\n'
       errMSG   += 'Fatal: file %s not found.'
       raise IOError(errMSG %(errorFunc,errorLine,errorFile,eqdskfpath))
    
    ofh = open(eqdskfpath,'r')
    efitdata = {}
    cline = ofh.readline()
    efitdata['idum']   = int(cline[48:52])
    efitdata['RDIM']   = int(cline[52:56])
    efitdata['ZDIM']   = int(cline[56:61])
    cline = ofh.readline()
    efitdata['RLEN']   = float(cline[0:16])
    efitdata['ZLEN']   = float(cline[16:32])
    efitdata['RCTR']   = float(cline[32:48])
    efitdata['RLFT']   = float(cline[48:64])
    efitdata['ZMID']   = float(cline[64:80])
    cline = ofh.readline()
    efitdata['RMAX']   = float(cline[0:16])
    efitdata['ZMAX']   = float(cline[16:32])
    efitdata['PSIMAX'] = float(cline[32:48])
    efitdata['PSIBND'] = float(cline[48:64])
    efitdata['BCTR']   = float(cline[64:80])
    cline = ofh.readline()
    efitdata['CURNT']  = float(cline[0:16])
    efitdata['PSIMAX'] = float(cline[16:32])
    efitdata['XDUM']   = float(cline[32:48])
    efitdata['RMAX']   = float(cline[48:64])
    efitdata['XDUM']   = float(cline[64:80])
    cline = ofh.readline()
    efitdata['ZMAX']   = float(cline[0:16])
    efitdata['XDUM']   = float(cline[16:32])
    efitdata['PSIBND'] = float(cline[32:48])
    efitdata['XDUM']   = float(cline[48:64])
    efitdata['XDUM']   = float(cline[64:80])

    nlines1D = int(npy.ceil(efitdata['RDIM']/5.0))

    efitdata['fpol'] = npy.zeros(efitdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            efitdata['fpol'][iline*5+0] = float(cline[0:16])
            efitdata['fpol'][iline*5+1] = float(cline[16:32])
            efitdata['fpol'][iline*5+2] = float(cline[32:48])
            efitdata['fpol'][iline*5+3] = float(cline[48:64])
            efitdata['fpol'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'

    efitdata['pressure'] = npy.zeros(efitdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            efitdata['pressure'][iline*5+0] = float(cline[0:16])
            efitdata['pressure'][iline*5+1] = float(cline[16:32])
            efitdata['pressure'][iline*5+2] = float(cline[32:48])
            efitdata['pressure'][iline*5+3] = float(cline[48:64])
            efitdata['pressure'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'

    efitdata['ffprime'] = npy.zeros(efitdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            efitdata['ffprime'][iline*5+0] = float(cline[0:16])
            efitdata['ffprime'][iline*5+1] = float(cline[16:32])
            efitdata['ffprime'][iline*5+2] = float(cline[32:48])
            efitdata['ffprime'][iline*5+3] = float(cline[48:64])
            efitdata['ffprime'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'

    efitdata['pprime'] = npy.zeros(efitdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            efitdata['pprime'][iline*5+0] = float(cline[0:16])
            efitdata['pprime'][iline*5+1] = float(cline[16:32])
            efitdata['pprime'][iline*5+2] = float(cline[32:48])
            efitdata['pprime'][iline*5+3] = float(cline[48:64])
            efitdata['pprime'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'

    nlines2D = int(npy.ceil(efitdata['RDIM']*efitdata['ZDIM']/5.0))

    efitdata['psiRZ'] = npy.zeros(efitdata['RDIM']*efitdata['ZDIM'])
    for iline in range(nlines2D):
        cline = ofh.readline()
        try:
            efitdata['psiRZ'][iline*5+0] = float(cline[0:16])
            efitdata['psiRZ'][iline*5+1] = float(cline[16:32])
            efitdata['psiRZ'][iline*5+2] = float(cline[32:48])
            efitdata['psiRZ'][iline*5+3] = float(cline[48:64])
            efitdata['psiRZ'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'
    efitdata['psiRZ'] = npy.reshape(efitdata['psiRZ'],(efitdata['ZDIM'],efitdata['RDIM']))

    efitdata['qpsi'] = npy.zeros(efitdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            efitdata['qpsi'][iline*5+0] = float(cline[0:16])
            efitdata['qpsi'][iline*5+1] = float(cline[16:32])
            efitdata['qpsi'][iline*5+2] = float(cline[32:48])
            efitdata['qpsi'][iline*5+3] = float(cline[48:64])
            efitdata['qpsi'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'
 
    cline = ofh.readline()
    efitdata['nbound'] = int(cline[0:5])
    efitdata['nlimit'] = int(cline[5:10])

    if efitdata['nbound'] > 0:
       nlines1D = int(npy.ceil(2*efitdata['nbound']/5.0))

       Ary1D = npy.zeros(2*efitdata['nbound'])
       for iline in range(nlines1D):
           cline = ofh.readline()
           try:
               Ary1D[iline*5+0] = float(cline[0:16])
               Ary1D[iline*5+1] = float(cline[16:32])
               Ary1D[iline*5+2] = float(cline[32:48])
               Ary1D[iline*5+3] = float(cline[48:64])
               Ary1D[iline*5+4] = float(cline[64:80])
           except:
               error = 'empty records'

       efitdata['rbound'] = Ary1D[0::2]
       efitdata['zbound'] = Ary1D[1::2]


    if efitdata['nlimit'] > 0:
       nlines1D = int(npy.ceil(2*efitdata['nlimit']/5.0))

       Ary1D = npy.zeros(2*efitdata['nlimit'])
       for iline in range(nlines1D):
           cline = ofh.readline()
           try:
               Ary1D[iline*5+0] = float(cline[0:16])
               Ary1D[iline*5+1] = float(cline[16:32])
               Ary1D[iline*5+2] = float(cline[32:48])
               Ary1D[iline*5+3] = float(cline[48:64])
               Ary1D[iline*5+4] = float(cline[64:80])
           except:
               error = 'empty records'

       efitdata['rlimit'] = Ary1D[0::2]
       efitdata['zlimit'] = Ary1D[1::2]

 
    efitdata['Z1D']  = npy.arange(efitdata['ZDIM'],dtype=float)*efitdata['ZLEN']/(efitdata['ZDIM']-1.0)
    efitdata['Z1D'] += efitdata['ZMID']-efitdata['ZMID']/2.0

    efitdata['R1D']  = npy.arange(efitdata['RDIM'],dtype=float)*efitdata['RLEN']/(efitdata['RDIM']-1.0)
    efitdata['R1D'] += efitdata['RLFT']

    efitdata['psiRZ'] = (efitdata['psiRZ']-efitdata['PSIMAX'])/(efitdata['PSIBND']-efitdata['PSIMAX'])

    efitdata['PSI']    = (efitdata['PSIBND']-efitdata['PSIMAX'])*npy.arange(efitdata['RDIM'])/(efitdata['RDIM']-1.0)
    efitdata['PSIN']   = (efitdata['PSI']-efitdata['PSI'][0])/(efitdata['PSI'][-1]-efitdata['PSI'][0])
    efitdata['rhopsi'] = npy.sqrt(efitdata['PSIN'])

    extendPSI    = npy.linspace(efitdata['PSI'][0],efitdata['PSI'][-1],10*npy.size(efitdata['PSI']))
    extendPHI    = npy.empty_like(extendPSI)
    extendPHI[0] = 0.0
    qfunc        = CubicSpline(efitdata['PSI'],efitdata['qpsi'])
    for i in range(1,npy.size(extendPSI)):
        x           = extendPSI[:i+1]
        y           = qfunc(x)
        extendPHI[i]= npy.trapz(y,x)

    efitdata['PHIMAX'] = extendPHI[0]
    efitdata['PHIBND'] = extendPHI[-1]

    efitdata['PHI'] = npy.empty_like(efitdata['PSI'])
    phifunc          = CubicSpline(extendPSI,extendPHI)
    for i in range(npy.size(efitdata['PSI'])):
        efitdata['PHI'][i] = phifunc(efitdata['PSI'][i])
    efitdata['PHIN']   = (efitdata['PHI']-efitdata['PHI'][0])/(efitdata['PHI'][-1]-efitdata['PHI'][0])
    efitdata['rhotor'] = npy.sqrt(efitdata['PHIN'])

    efitdata['Jtot'] = efitdata['R1D']*efitdata['pprime']+efitdata['ffprime']/efitdata['R1D']

    return efitdata

if __name__=='__main__':
    print(calc_var(ps))

