from numpy                  import arange
from plot.colors            import CRED, CEND
from os.path                import realpath
from iofiles.efit.read_efit import read_efit

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
    efit_file_path = realpath('../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(efitfpath=efit_file_path)
    calc_rzgrids = rzgrids()
    print(calc_rzgrids(efitdata,ps_update=False))
    print(efitdata.keys())
