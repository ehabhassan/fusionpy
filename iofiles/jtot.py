from plot.colors            import CRED, CEND
from os.path                import realpath
from iofiles.efit.rzgrids   import rzgrids
from iofiles.efit.read_efit import read_efit

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

if __name__=='__main__':
    efit_file_path = realpath('../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(efitfpath=efit_file_path)
    calc_jtot = jtot()
    print(calc_jtot(efitdata,ps_update=True))
    print(efitdata.keys())
