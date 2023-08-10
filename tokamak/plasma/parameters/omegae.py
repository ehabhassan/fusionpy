from plot.colors       import CRED, CEND
from tokamak.constants import e, me

class omegae():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["bt"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        omegae = e*ps['bt']/me # units [1/s]
        if ps_update:
            ps['omegae'] = omegae
        return omegae

    def __call__(self, ps):
        self.checkdependencies(ps, ps_update=False)
        if self.model == 'default': return self.default(ps, ps_update)

if __name__=='__main__':
    ps = {}
    ps['bt'] = 2.0
    calc_omegae = omegae()
    print(calc_omegae(ps))
