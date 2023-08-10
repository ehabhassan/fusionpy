from plot.colors       import CRED, CEND
from tokamak.constants import mp,e
from iofiles.efit.bref import bref

class omegai():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["zi", "bt", "mi"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
               #if independ == "bt":
               #    if "bt" in ps:
               #        self.bt = ps['bt']
               #    else:
               #        calc_bref = bref()
               #        self.bt = calc_bref(ps)
               #elif independ not in ps:
               #    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
                if independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
       #omegai = e*ps['zi']*self.bt/ps['mi'] # units [1/s]
        omegai = e*ps['zi']*ps['bt']/ps['mi'] # units [1/s]
        if ps_update:
            ps['omegai'] = omegai
        return omegai

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

if __name__=='__main__':
    ps = {}
    ps['bt'] = 2.0
   #ps['mi'] = 2.0*1.67e-27
    calc_omegai = omegai()
    print(calc_omegai(ps))
