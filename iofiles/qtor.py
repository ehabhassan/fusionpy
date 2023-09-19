from os.path                import realpath
from plot.colors            import CRED, CEND
from iofiles.efit.psigrids  import psigrids
from iofiles.efit.phigrids  import phigrids
from iofiles.efit.read_efit import read_efit
from scipy.interpolate      import interp1d

class qtor():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["qpsi", "PSIN", "PHIN"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == "PSIN":
                    if "PSIN" not in ps:
                        calc_psin = psigrids()
                        _,self.psin,_ = calc_psin(ps)
                    else:
                        self.psin = ps['PSIN']

                elif independ == "PHIN":
                    if "PHIN" not in ps:
                        calc_phigrids = phigrids()
                        phimax, phibnd, phi, self.phin, rhotor  = calc_phigrids(ps)
                    else:
                        self.phi = ps['PHIN']
                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        fqpsi = interp1d(self.psin,ps['qpsi'])
        qtor  = fqpsi(self.phin)
        if ps_update:
            ps['qtor'] = qtor
        return qtor

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

if __name__=='__main__':
    efit_file_path = realpath('../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(fpath=efit_file_path)
    calc_qtor = qtor()
    print(calc_qtor(efitdata,ps_update=True))
