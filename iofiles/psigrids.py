from numpy                  import arange,sqrt
from plot.colors            import CRED, CEND
from os.path                import realpath
from iofiles.efit.read_efit import read_efit

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

if __name__=='__main__':
    efit_file_path = realpath('../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(efitfpath=efit_file_path)
    calc_psigrids = psigrids()
    print(calc_psigrids(efitdata,ps_update=True))
    print(efitdata.keys())
