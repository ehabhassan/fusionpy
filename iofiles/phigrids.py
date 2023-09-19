from numpy                  import arange,sqrt
from numpy                  import linspace,size
from numpy                  import empty_like,trapz
from os.path                import realpath
from plot.colors            import CRED, CEND
from scipy.interpolate      import CubicSpline
from iofiles.efit.psigrids  import psigrids
from iofiles.efit.read_efit import read_efit

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

if __name__=='__main__':
    efit_file_path = realpath('../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(efitfpath=efit_file_path)
    calc_phigrids = phigrids()
    print(calc_phigrids(efitdata,ps_update=True))
    print(efitdata.keys())
