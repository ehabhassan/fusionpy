from numpy                          import linspace,argmin
from os.path                        import realpath
from plot.colors                    import CRED, CEND
from iofiles.efit.lref              import lref
from iofiles.efit.phigrids          import phigrids
from tokamak.constants              import e,md
from iofiles.efit.read_efit         import read_efit
from iofiles.fastran.read_fastran   import read_fastran
from tokamak.plasma.parameters.cs   import cs
from tokamak.plasma.parameters.rhos import rhos

class qgb():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["ne", "te", "rho", "rhos", "cs", "lref"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == "rhos":
                    if "rhos" in ps:
                        self.rhos = ps['rhos']
                    else:
                        calc_rhos = rhos()
                        self.rhos = calc_rhos(ps)
                elif independ == "cs":
                    if "cs" in ps:
                        self.cs = ps['cs']
                    else:
                        calc_cs = cs()
                        self.cs = calc_cs(ps)
                elif independ == "lref":
                    if "lref" in ps:
                        self.lref = ps['lref']
                    else:
                        calc_lref = lref()
                        self.lref = calc_lref(ps)
                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, rho0, ps_update=False):
        irho = argmin(abs(ps['rho']-rho0))
        t0 = ps['te'][irho]*1.0e3*e
        n0 = ps['ne'][irho]*1.0e19
        qgb = n0*t0*self.rhos[irho]**2*self.cs[irho]/self.lref**2  # units [1/s]
        if ps_update:
            ps['qgb'] = qgb
        return qgb

    def __call__(self, ps, rho0, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, rho0, ps_update)

if __name__=='__main__':
    fast_file_path = realpath('../../../testsuite/state_files/fastran.nc')
    fastdata = read_fastran(fast_file_path)
    efit_file_path = realpath('../../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(efitfpath=efit_file_path)

    ps = efitdata.copy()
    ps['rho'] = fastdata['rho']['data']
    ps['bt']  = fastdata['b0']['data'][-1]
    ps['te']  = fastdata['te']['data'][-1,:]
    ps['ne']  = fastdata['ne']['data'][-1,:]
    ps['mi']  = md
    rho0      = 0.975

    calc_qgb = qgb()
    print(calc_qgb(ps, rho0))
