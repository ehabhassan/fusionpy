from plot.colors       import CRED, CEND
from tokamak.constants import mp,e

class omegai():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["zi", "bt", "mi"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ in ['zi','mi']:
                    if 'zi' not in ps: self.zi = 1.0
                    else:              self.zi = ps['zi']
                    if 'mi' not in ps: self.mi = mp
                    else:              self.mi = ps['mi']
                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps):
        omegai = e*self.zi*ps['bt']/self.mi # units [1/s]
        return omegai

    def __call__(self, ps):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps)

if __name__=='__main__':
    ps = {}
    ps['bt'] = 2.0
   #ps['mi'] = 2.0*1.67e-27
    calc_omegai = omegai()
    print(calc_omegai(ps))
