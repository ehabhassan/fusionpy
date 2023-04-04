from plot.colors       import CRED, CEND
from tokamak.constants import e, me

class omegae():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["e", "bt", "me"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if 'e' not in ps:  ps['e']  = e
                if 'me' not in ps: ps['me'] = me
                if independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps):
        omegae = ps['e']*ps['bt']/ps['me'] # units [1/s]
        return omegae


    def __call__(self, ps):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps)

if __name__=='__main__':
    ps = {}
    ps['e']  = 1.6e-19
    ps['bt'] = 2.0
    ps['me'] = 9.1e-31 
    calc_omegae = omegae()
    print(calc_omegae(ps))
