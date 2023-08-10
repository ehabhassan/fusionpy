from numpy                          import argmin
from os.path                        import realpath
from plot.colors                    import CRED, CEND
from iofiles.efit.lref              import lref
from iofiles.efit.qtor              import qtor
from iofiles.read_iterdb            import read_iterdb
from iofiles.efit.phigrids          import phigrids
from iofiles.efit.read_efit         import read_efit
from tokamak.plasma.parameters.rhos import rhos

class kymin():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["qtor", "ntor", "rhos", "lref", "rho"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == 'lref':
                    if independ not in ps:
                        calc_lref = lref()
                        self.lref = calc_lref(ps)
                    else:
                        self.lref = ps['lref']

                elif independ == 'rho':
                    if independ not in ps:
                        calc_rho = phigrids()
                        PHIMAX,PHIBND,PHI,PHIN,self.rho = calc_rho(ps)
                    else:
                        self.rho = ps['rho']

                elif independ == 'rhos':
                    if independ not in ps:
                        calc_rhos = rhos()
                        self.rhos = calc_rhos(ps)
                    else:
                        self.rhos = ps['rhos']

                elif independ == 'qtor':
                    if independ not in ps:
                        calc_qtor = qtor()
                        self.qtor = calc_qtor(ps)
                    else:
                        self.qtor = ps['qtor']

                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, rho0, ps_update=False):
        if rho0:
            rho_ind = argmin(abs(self.rho-rho0))
            kymin  = ps['ntor'] * self.qtor[rho_ind] * self.rhos[rho_ind]
            kymin /= self.lref * self.rho[rho_ind]
        else:
            kymin  = ps['ntor'] * self.qtor * self.rhos
            kymin /= self.lref * self.rho
        if ps_update:
            ps['kymin'] = kymin
        return kymin

    def __call__(self, ps, rho0 = None, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, rho0, ps_update)

if __name__=='__main__':
    from tokamak.constants import md
    efit_file_path = realpath('../../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(fpath=efit_file_path)
    iterdb_file_path = realpath('../../../testsuite/state_files/plasma_prof.iterdb')
    iterdbdata = read_iterdb(fpath=iterdb_file_path,eqdsk=efit_file_path)
    efitdata['zi']  = 1
    efitdata['bt']  = efitdata['BCTR']
    efitdata['te']  = iterdbdata['Te']
    efitdata['mi']  = md
    efitdata['rho'] = iterdbdata['rhotor']
    for in0 in range(10,30,2):
        efitdata["ntor"] = in0
        calc_kymin = kymin()
        print(calc_kymin(efitdata, rho0=0.975, ps_update=True))


