from plot.colors       import CRED, CEND
from tokamak.constants import e

class omegai():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["zi","e", "bt", "mi"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if 'e' not in ps:  ps['e']  = e
                if 'zi' not in ps: ps['zi'] = 1.0
                if independ not in ps:
                    raise IOError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps):
        omegai = ps['zi']*ps['e']*ps['bt']/ps['mi'] # units [1/s]
        return omegai

    def __call__(self, ps):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps)

if __name__=='__main__':
    ps = {}
    ps['e']  = 1.6e-19
    ps['bt'] = 2.0
    ps['mi'] = 2.0*1.67e-27
    calc_omegai = omegai()
    print(calc_omegai(ps))
