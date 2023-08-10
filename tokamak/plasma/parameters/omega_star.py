from numpy                      import argmin
from os.path                    import realpath
from plot.colors                import CRED, CEND
from tokamak.constants          import md
from iofiles.read_iterdb        import read_iterdb
from iofiles.efit.read_efit     import read_efit
from tokamak.plasma.parameters  import kymin
from tokamak.plasma.parameters  import lne,lte

class omega_star():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["lte", "lne", "kymin"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == 'lne':
                    if independ not in ps:
                        calc_lne = lne.lne()
                        self.lne = calc_lne(ps)
                    else:
                        self.lne = ps['lne']

                elif independ == 'lte':
                    if independ not in ps:
                        calc_lte = lte.lte()
                        self.lte = calc_lte(ps)
                    else:
                        self.lte = ps['lte']

                elif independ == 'kymin':
                    if independ not in ps:
                        calc_kymin = kymin.kymin()
                        self.kymin = calc_kymin(ps)
                    else:
                        self.kymin = ps['kymin']

                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        omega_star = self.kymin * (self.lte + self.lne)
        if ps_update:
            ps['omega_star'] = omega_star
        return omega_star

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
        calc_omega_star = omega_star()
        print(calc_omega_star(efitdata, ps_update=True))

