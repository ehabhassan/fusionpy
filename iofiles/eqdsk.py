from numpy             import reshape,ceil,zeros
from numpy             import argmin,abs
from numpy             import linspace
from numpy             import arange,sqrt
from numpy             import linspace,size
from numpy             import empty_like,trapz
from os.path           import isfile,realpath
from traceback         import extract_stack
from plot.colors       import CRED, CEND
from maths.interp      import interp
from maths.fd_d1_o4    import fd_d1_o4
from scipy.interpolate import CubicSpline

def read_eqdsk(fpath):
   #Developed by Ehab Hassan on 2019-02-27
    if isfile(fpath) == False:
       errorFunc = extract_stack(limit=2)[-2][3]
       errorLine = extract_stack(limit=2)[-2][1]
       errorFile = extract_stack(limit=2)[-2][2]
       errMSG    = 'Call %s line %5d in file %s Failed.\n'
       errMSG   += 'Fatal: file %s not found.'
       raise IOError(errMSG %(errorFunc,errorLine,errorFile,fpath))
    
    ofh = open(fpath,'r')
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

    nlines1D = int(ceil(efitdata['RDIM']/5.0))

    efitdata['fpol'] = zeros(efitdata['RDIM'])
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

    efitdata['pressure'] = zeros(efitdata['RDIM'])
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

    efitdata['ffprime'] = zeros(efitdata['RDIM'])
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

    efitdata['pprime'] = zeros(efitdata['RDIM'])
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

    nlines2D = int(ceil(efitdata['RDIM']*efitdata['ZDIM']/5.0))

    efitdata['psiRZ'] = zeros(efitdata['RDIM']*efitdata['ZDIM'])
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
    efitdata['psiRZ'] = reshape(efitdata['psiRZ'],(efitdata['ZDIM'],efitdata['RDIM']))
   #efitdata['psiRZ'] = (efitdata['psiRZ']-efitdata['PSIMAX'])/(efitdata['PSIBND']-efitdata['PSIMAX'])

    efitdata['qpsi'] = zeros(efitdata['RDIM'])
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
       nlines1D = int(ceil(2*efitdata['nbound']/5.0))

       Ary1D = zeros(2*efitdata['nbound'])
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
       nlines1D = int(ceil(2*efitdata['nlimit']/5.0))

       Ary1D = zeros(2*efitdata['nlimit'])
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
 
    return efitdata

class bfields():
    def __init__(self, model='default'):
        self.model = model
        self.interp = interp()
        self.fd_d1_o4 = fd_d1_o4()
        self.dependencies = ["R1D", "Z1D", "RMAX", "ZMAX", "psiRZ", "PSIN", "PSIMAX", "PSIBND", "fpol", "RDIM"]

    def checkdependencies(self,ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ in ["R1D","Z1D"]:
                    if "R1D" in ps and "Z1D" in ps:
                        self.R1D = ps['R1D']
                        self.Z1D = ps['Z1D']
                    else:
                        calc_rzgrids = rzgrids()
                        self.R1D, self.Z1D = calc_rzgrids(ps)
                elif independ == "PSIN":
                    if "PSIN" in ps:
                        self.PSIN = ps['PSIN']
                    else:
                        calc_psigrids = psigrids()
                        PSI, self.PSIN, rhopsi = calc_psigrids(ps)
                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
       #Z0_ind is the index of Z1D of midplane
        Z0_ind = argmin(abs(self.Z1D-ps['ZMAX']))
       #psi_midplane is psi_pol at midplane on even Rgrid
        psi_pol_mp = ps['psiRZ'][Z0_ind,:]
       #R0_ind is index of unif_R1D at RMAX
        R0_ind = argmin(abs(self.R1D-ps['RMAX']))
        psi_pol_obmp = psi_pol_mp[R0_ind:]
       #Normalize psi_pol_obmp to psip_n_temp
        psip_n_temp = empty_like(psi_pol_obmp)
        for i in range(len(psi_pol_obmp)):
            psip_n_temp[i] = (psi_pol_obmp[i]-ps['PSIMAX'])/(ps['PSIBND']-ps['PSIMAX'])
        unif_R = linspace(self.R1D[R0_ind],self.R1D[-1],ps['RDIM']*10)
        psip_n_unifR = self.interp(self.R1D[R0_ind:],psip_n_temp,unif_R)
        psisep_ind = argmin(abs(psip_n_unifR-1.02))
        psip_n_obmp = psip_n_unifR[:psisep_ind]
        R_obmp = unif_R[:psisep_ind].copy()
       #B_pol is d psi_pol/ d R * (1/R)
       #B_pol = fd_d1_o4(psi_pol_obmp, unif_R[R0_ind:R0_ind+psisep_ind])/unif_R[R0_ind:R0_ind+psisep_ind]
        B_pol = self.fd_d1_o4(R_obmp,psip_n_obmp*(ps['PSIBND']-ps['PSIMAX'])+ps['PSIMAX'])/R_obmp
       #Convert F(on even psi_pol grid) to F(on even R grid)
        F_obmp = self.interp(self.PSIN, ps['fpol'], psip_n_obmp)
       #B_tor = F/R
        B_tor = F_obmp/R_obmp
    
        # psip_n_obmp is normalized psi_pol at outboard midplane on uniform unif_R
        # B_tor and B_pol are on uniform unif_R as well
        # psip_n_obmp is unlike psip_n ([0,1]), it goes from 0 to 1.06 here

        if ps_update:
            ps['bpol'] = B_pol
            ps['btor'] = B_tor
            ps['Robmp'] = R_obmp
            ps['psip_n_obmp'] = psip_n_obmp
        return B_pol, B_tor, psip_n_obmp, R_obmp 

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

class bref():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["btor"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == "btor":
                    if "btor" not in ps:
                        calc_bfields = bfields()
                        bpol, self.btor, a, b  = calc_bfields(ps)
                    else:
                        self.btor = ps['btor']
                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        bref = abs(self.btor[0])
        if ps_update:
            ps['bref'] = bref
        return bref

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

class jtot():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["R1D", "pprime", "ffprime"]

    def checkdependencies(self,ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == "R1D":
                    if "R1D" not in ps:
                        calc_rzgrids = rzgrids()
                        self.R1D,Z1D = calc_rzgrids(ps)
                    else:
                        self.R1D = ps['R1D']
                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        self.R1D[0] = 0.0025
        jtot = self.R1D*ps['pprime']+ps['ffprime']/self.R1D
        if ps_update:
            ps['jtot'] = jtot
        return jtot

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

class lref():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["bref", "PHIBND"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == "bref":
                    if "bref" not in ps:
                        calc_bref = bref()
                        self.bref = calc_bref(ps)
                    else:
                        self.bref = ps['bref']
                elif independ == "PHIBND":
                    if "PHIBND" not in ps:
                        calc_phigrids = phigrids()
                        phimax, self.phibnd, phi, phin, rhotor  = calc_phigrids(ps)
                    else:
                        self.phibnd = ps['PHIBND']
                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        lref = sqrt(2.0*(abs(self.phibnd/self.bref)))
        if ps_update:
            ps['lref'] = lref
        return lref

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

class psigrids():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["PSIBND", "PSIMAX", "RDIM"]

    def checkdependencies(self,ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        PSI    = (ps['PSIBND']-ps['PSIMAX'])*arange(ps['RDIM'])/(ps['RDIM']-1.0)
        PSIN   = (PSI-PSI[0])/(PSI[-1]-PSI[0])
        rhopsi = sqrt(PSIN)
        if ps_update:
            ps['PSI']    = PSI
            ps['PSIN']   = PSIN
            ps['rhopsi'] = rhopsi
        return PSI,PSIN,rhopsi

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

class phigrids():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["PSI", "qpsi"]

    def checkdependencies(self,ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == "PSI":
                    if "PSI" not in ps:
                        calc_psigrids = psigrids()
                        self.PSI, PSIN, rhopsi = calc_psigrids(ps)
                    else:
                        self.PSI = ps['PSI']
                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        extendPSI    = linspace(self.PSI[0],self.PSI[-1],10*size(self.PSI))
        extendPHI    = empty_like(extendPSI)
        extendPHI[0] = 0.0
        qfunc        = CubicSpline(self.PSI,ps['qpsi'])
        for i in range(1,size(extendPSI)):
            x           = extendPSI[:i+1]
            y           = qfunc(x)
            extendPHI[i]= trapz(y,x)
    
        PHIMAX = extendPHI[0]
        PHIBND = extendPHI[-1]
    
        PHI     = empty_like(self.PSI)
        phifunc = CubicSpline(extendPSI,extendPHI)
        for i in range(size(self.PSI)):
            PHI[i] = phifunc(self.PSI[i])
        PHIN   = (PHI-PHI[0])/(PHI[-1]-PHI[0])
        rhotor = sqrt(PHIN)

        if ps_update:
            ps['PHI']    = PHI
            ps['PHIN']   = PHIN
            ps['rhotor'] = rhotor
            ps['PHIMAX'] = PHIMAX
            ps['PHIBND'] = PHIBND
        return PHIMAX,PHIBND,PHI,PHIN,rhotor

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

class rzgrids():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["ZDIM", "ZLEN", "ZMID", "RDIM", "RLEN", "RLFT"]

    def checkdependencies(self,ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        R1D  = arange(ps['RDIM'],dtype=float)*ps['RLEN']/(ps['RDIM']-1.0)
        R1D += ps['RLFT']

        Z1D  = arange(ps['ZDIM'],dtype=float)*ps['ZLEN']/(ps['ZDIM']-1.0)
        Z1D += ps['ZMID']-ps['ZLEN']/2.0

        if ps_update:
            ps['R1D'] = R1D
            ps['Z1D'] = Z1D
        return R1D,Z1D

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

if __name__=='__main__':
    efit_file_path = realpath('../testsuite/state_files/plasma_eq.efit')
    efitdata = read_eqdsk(fpath=efit_file_path)

#   calc_rzgrids = rzgrids()
#   print(calc_rzgrids(efitdata,ps_update=False))
#   print(efitdata.keys())

#   calc_psigrids = psigrids()
#   print(calc_psigrids(efitdata,ps_update=True))
#   print(efitdata.keys())

#   calc_phigrids = phigrids()
#   print(calc_phigrids(efitdata,ps_update=True))
#   print(efitdata.keys())

#   calc_lref = lref()
#   print(calc_lref(efitdata,ps_update=True))
#   print(efitdata.keys())

#   calc_jtot = jtot()
#   print(calc_jtot(efitdata,ps_update=True))
#   print(efitdata.keys())

#   calc_bref = bref()
#   print(calc_bref(efitdata,ps_update=True))
#   print(efitdata.keys())

#   calc_bfields = bfields()
#   print(calc_bfields(efitdata,ps_update=True))
#   print(efitdata.keys())

