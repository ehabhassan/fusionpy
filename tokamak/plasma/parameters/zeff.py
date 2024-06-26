from numpy       import dot
from plot.colors import CRED, CEND

class zeff():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["ne", "ni", "zi", "zz", "nz"]

    def checkdependencies(self,ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == 'zz':
                    if 'zz' not in ps:
                        ps['zz'] = 0.0
                elif independ == 'nz':
                    if 'nz' not in ps:
                        if ps['zz'] == 0.0:
                            ps['nz'] = 0.0
                        else:
                            ps['nz'] = ps['ne'] - ps['ni']
                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        if type(ps['zz']) in [list,tuple] and type(ps['nz']) in [list,tuple]:
            if len(ps['zz']) == len(ps['nz']):    
                zeff = (ps['zi']**2*ps['ni'] + dot(ps['zz']**2,*ps['nz']))/ps['ne'] # units [None]
        else:
                zeff = (ps['zi']**2*ps['ni'] + ps['zz']**2*ps['nz'])/ps['ne'] # units [None]
        if ps_update:
            ps['zeff'] = zeff
        return zeff

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

if __name__=='__main__':
    ps = {}
    ps['ne']   = 19.3
    ps['ni']   = 19.3
    ps['zi']   =  2.0
    ps['zz']   =  5.0
    calc_zeff = zeff()
    print(calc_zeff(ps))
