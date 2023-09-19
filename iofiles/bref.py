from os.path                import realpath
from plot.colors            import CRED, CEND
from iofiles.efit.bfields   import bfields 
from iofiles.efit.read_efit import read_efit

class bref():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["btor"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == "btor":
                    if "btor" not in ps:
                        calc_bfields = bfields()
                        bpol, self.btor, a, b  = calc_bfields(ps)
                    else:
                        self.btor = ps['btor']
                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        bref = abs(self.btor[0])
        if ps_update:
            ps['bref'] = bref
        return bref

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

if __name__=='__main__':
    efit_file_path = realpath('../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(efitfpath=efit_file_path)
    calc_bref = bref()
    print(calc_bref(efitdata,ps_update=True))
    print(efitdata.keys())
