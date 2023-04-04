from plot.colors import CRED, CEND

class read_eqdsk():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ['eqdskfpath','eqdskfname']

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
                elif independe == 'eqdskfpath' and not os.path.isdir(ps[independ]):
                    raise IOError(CRED + "PATH: % CAN NOT BE FOUND" % ps[independ] + CEND)
                elif independe == 'eqdskfname' and not os.path.isfile(ps[independ]):
                    raise IOError(CRED + "FILE: % CAN NOT BE FOUND" % ps[independ] + CEND)
        return True

    def default(self, ps):
        var = ps['input-1']/ps['input-2']+ps['input-3'] # units [None]
        return var

    def __call__(self, ps):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps)

if __name__=='__main__':
    ps = {}
    ps['input-1'] = 10.0
    ps['input-2'] = 20.0
    ps['input-3'] =  1.5
    calc_var = var()
    print(calc_var(ps))


def read_efit_file(eqdskfpath,setparam={}):
   #Developed by Ehab Hassan on 2019-02-27
    if os.path.isfile(eqdskfpath) == False:
       errorFunc = traceback.extract_stack(limit=2)[-2][3]
       errorLine = traceback.extract_stack(limit=2)[-2][1]
       errorFile = traceback.extract_stack(limit=2)[-2][2]
       errMSG    = 'Call %s line %5d in file %s Failed.\n'
       errMSG   += 'Fatal: file %s not found.'
       raise IOError(errMSG %(errorFunc,errorLine,errorFile,eqdskfpath))
    
    ofh = open(eqdskfpath,'r')
    eqdskdata = {}
    cline = ofh.readline()
    eqdskdata['idum']   = int(cline[48:52])
    eqdskdata['RDIM']   = int(cline[52:56])
    eqdskdata['ZDIM']   = int(cline[56:61])
    cline = ofh.readline()
    eqdskdata['RLEN']   = float(cline[0:16])
    eqdskdata['ZLEN']   = float(cline[16:32])
    eqdskdata['RCTR']   = float(cline[32:48])
    eqdskdata['RLFT']   = float(cline[48:64])
    eqdskdata['ZMID']   = float(cline[64:80])
    cline = ofh.readline()
    eqdskdata['RMAX']   = float(cline[0:16])
    eqdskdata['ZMAX']   = float(cline[16:32])
    eqdskdata['PSIMAX'] = float(cline[32:48])
    eqdskdata['PSIBND'] = float(cline[48:64])
    eqdskdata['BCTR']   = float(cline[64:80])
    cline = ofh.readline()
    eqdskdata['CURNT']  = float(cline[0:16])
    eqdskdata['PSIMAX'] = float(cline[16:32])
    eqdskdata['XDUM']   = float(cline[32:48])
    eqdskdata['RMAX']   = float(cline[48:64])
    eqdskdata['XDUM']   = float(cline[64:80])
    cline = ofh.readline()
    eqdskdata['ZMAX']   = float(cline[0:16])
    eqdskdata['XDUM']   = float(cline[16:32])
    eqdskdata['PSIBND'] = float(cline[32:48])
    eqdskdata['XDUM']   = float(cline[48:64])
    eqdskdata['XDUM']   = float(cline[64:80])

    nlines1D = int(npy.ceil(eqdskdata['RDIM']/5.0))

    eqdskdata['fpol'] = npy.zeros(eqdskdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            eqdskdata['fpol'][iline*5+0] = float(cline[0:16])
            eqdskdata['fpol'][iline*5+1] = float(cline[16:32])
            eqdskdata['fpol'][iline*5+2] = float(cline[32:48])
            eqdskdata['fpol'][iline*5+3] = float(cline[48:64])
            eqdskdata['fpol'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'

    eqdskdata['pressure'] = npy.zeros(eqdskdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            eqdskdata['pressure'][iline*5+0] = float(cline[0:16])
            eqdskdata['pressure'][iline*5+1] = float(cline[16:32])
            eqdskdata['pressure'][iline*5+2] = float(cline[32:48])
            eqdskdata['pressure'][iline*5+3] = float(cline[48:64])
            eqdskdata['pressure'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'

    eqdskdata['ffprime'] = npy.zeros(eqdskdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            eqdskdata['ffprime'][iline*5+0] = float(cline[0:16])
            eqdskdata['ffprime'][iline*5+1] = float(cline[16:32])
            eqdskdata['ffprime'][iline*5+2] = float(cline[32:48])
            eqdskdata['ffprime'][iline*5+3] = float(cline[48:64])
            eqdskdata['ffprime'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'

    eqdskdata['pprime'] = npy.zeros(eqdskdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            eqdskdata['pprime'][iline*5+0] = float(cline[0:16])
            eqdskdata['pprime'][iline*5+1] = float(cline[16:32])
            eqdskdata['pprime'][iline*5+2] = float(cline[32:48])
            eqdskdata['pprime'][iline*5+3] = float(cline[48:64])
            eqdskdata['pprime'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'

    nlines2D = int(npy.ceil(eqdskdata['RDIM']*eqdskdata['ZDIM']/5.0))

    eqdskdata['psiRZ'] = npy.zeros(eqdskdata['RDIM']*eqdskdata['ZDIM'])
    for iline in range(nlines2D):
        cline = ofh.readline()
        try:
            eqdskdata['psiRZ'][iline*5+0] = float(cline[0:16])
            eqdskdata['psiRZ'][iline*5+1] = float(cline[16:32])
            eqdskdata['psiRZ'][iline*5+2] = float(cline[32:48])
            eqdskdata['psiRZ'][iline*5+3] = float(cline[48:64])
            eqdskdata['psiRZ'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'
    eqdskdata['psiRZ'] = npy.reshape(eqdskdata['psiRZ'],(eqdskdata['ZDIM'],eqdskdata['RDIM']))

    eqdskdata['qpsi'] = npy.zeros(eqdskdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            eqdskdata['qpsi'][iline*5+0] = float(cline[0:16])
            eqdskdata['qpsi'][iline*5+1] = float(cline[16:32])
            eqdskdata['qpsi'][iline*5+2] = float(cline[32:48])
            eqdskdata['qpsi'][iline*5+3] = float(cline[48:64])
            eqdskdata['qpsi'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'
 
    cline = ofh.readline()
    eqdskdata['nbound'] = int(cline[0:5])
    eqdskdata['nlimit'] = int(cline[5:10])

    if eqdskdata['nbound'] > 0:
       nlines1D = int(npy.ceil(2*eqdskdata['nbound']/5.0))

       Ary1D = npy.zeros(2*eqdskdata['nbound'])
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

       eqdskdata['rbound'] = Ary1D[0::2]
       eqdskdata['zbound'] = Ary1D[1::2]


    if eqdskdata['nlimit'] > 0:
       nlines1D = int(npy.ceil(2*eqdskdata['nlimit']/5.0))

       Ary1D = npy.zeros(2*eqdskdata['nlimit'])
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

       eqdskdata['rlimit'] = Ary1D[0::2]
       eqdskdata['zlimit'] = Ary1D[1::2]

 
    eqdskdata['ZR1D']  = npy.arange(eqdskdata['ZDIM'],dtype=float)*eqdskdata['ZLEN']/(eqdskdata['ZDIM']-1.0)
    eqdskdata['ZR1D'] += eqdskdata['ZMID']-eqdskdata['ZMID']/2.0

    eqdskdata['RR1D']  = npy.arange(eqdskdata['RDIM'],dtype=float)*eqdskdata['RLEN']/(eqdskdata['RDIM']-1.0)
    eqdskdata['RR1D'] += eqdskdata['RLFT']

    eqdskdata['psiRZ'] = (eqdskdata['psiRZ']-eqdskdata['PSIMAX'])/(eqdskdata['PSIBND']-eqdskdata['PSIMAX'])

    eqdskdata['PSI']    = (eqdskdata['PSIBND']-eqdskdata['PSIMAX'])*npy.arange(eqdskdata['RDIM'])/(eqdskdata['RDIM']-1.0)
    eqdskdata['PSIN']   = (eqdskdata['PSI']-eqdskdata['PSI'][0])/(eqdskdata['PSI'][-1]-eqdskdata['PSI'][0])
    eqdskdata['rhopsi'] = npy.sqrt(eqdskdata['PSIN'])

    extendPSI    = npy.linspace(eqdskdata['PSI'][0],eqdskdata['PSI'][-1],10*npy.size(eqdskdata['PSI']))
    extendPHI    = npy.empty_like(extendPSI)
    extendPHI[0] = 0.0
    qfunc        = CubicSpline(eqdskdata['PSI'],eqdskdata['qpsi'])
    for i in range(1,npy.size(extendPSI)):
        x           = extendPSI[:i+1]
        y           = qfunc(x)
        extendPHI[i]= npy.trapz(y,x)

    eqdskdata['PHI'] = npy.empty_like(eqdskdata['PSI'])
    phifunc          = CubicSpline(extendPSI,extendPHI)
    for i in range(npy.size(eqdskdata['PSI'])):
        eqdskdata['PHI'][i] = phifunc(eqdskdata['PSI'][i])

    eqdskdata['PHIN']   = (eqdskdata['PHI']-eqdskdata['PHI'][0])/(eqdskdata['PHI'][-1]-eqdskdata['PHI'][0])

    eqdskdata['rhotor'] = npy.sqrt(eqdskdata['PHIN'])

    return eqdskdata
