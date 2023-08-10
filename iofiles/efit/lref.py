from numpy                  import sqrt
from os.path                import realpath
from plot.colors            import CRED, CEND
from iofiles.efit.bref      import bref
from iofiles.efit.phigrids  import phigrids
from iofiles.efit.read_efit import read_efit

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

if __name__=='__main__':
    efit_file_path = realpath('../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(efitfpath=efit_file_path)
    calc_lref = lref()
    print(calc_lref(efitdata,ps_update=True))
    print(efitdata.keys())
