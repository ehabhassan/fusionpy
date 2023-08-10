from numpy             import sqrt
from plot.colors       import CRED, CEND
from tokamak.constants import e

class cs():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["te", "mi"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        cs = sqrt(e*ps['te']*1.0e3/ps['mi']) # units [m/s]
        if ps_update:
            ps['cs'] = cs
        return cs

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

if __name__=='__main__':
    ps = {}
    ps['te']   = 18.0
    ps['mi']   = 16.0
    calc_cs = cs()
    print(calc_cs(ps))
