from numpy                      import pi, sqrt
from os.path                    import realpath
from plot.colors                import CRED, CEND
from tokamak.constants          import e, md
from iofiles.efit.lref          import lref
from iofiles.read_iterdb        import read_iterdb
from iofiles.efit.read_efit     import read_efit
from tokamak.plasma.parameters  import omega_star

class omega_mtm():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["omega_star", "mi", "lref", "te"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == 'lref':
                    if independ not in ps:
                        calc_lref = lref()
                        self.lref = calc_lref(ps)
                    else:
                        self.lref = ps['lref']

                elif independ == 'omega_star':
                    if independ not in ps:
                        calc_omega_star = omega_star.omega_star()
                        self.omega_star = calc_omega_star(ps)
                    else:
                        self.omega_star = ps['omega_star']

                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        omega_gyro = sqrt(e * ps['te'] / md) / self.lref
        omega_mtm  = omega_gyro * self.omega_star / 2.0 / pi
        if ps_update:
            ps['omega_mtm'] = omega_mtm
        return omega_mtm

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

if __name__=='__main__':
    from tokamak.constants import md
    efit_file_path = realpath('../../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(fpath=efit_file_path)
    iterdb_file_path = realpath('../../../testsuite/state_files/plasma_prof.iterdb')
    iterdbdata = read_iterdb(fpath=iterdb_file_path,eqdsk=efit_file_path)
    efitdata['zi']  = 1
    efitdata['bt']  = efitdata['BCTR']
    efitdata['te']  = iterdbdata['Te']
    efitdata['ne']  = iterdbdata['ne']
    efitdata['mi']  = md
    efitdata['rho'] = iterdbdata['rhotor']
    for in0 in range(10,30,2):
        efitdata["ntor"] = in0
        calc_omega_mtm = omega_mtm()
        print(calc_omega_mtm(efitdata, ps_update=True))

