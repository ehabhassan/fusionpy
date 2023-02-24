from plot.colors import CRED, CEND

class zeff():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["ne", "ni", "zi", "zz", "nz"]

    def checkdependencies(self,ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == 'zz' and 'zz' not in ps:
                    ps['zz'] = 0.0
                if independ == 'nz' and 'nz' not in ps:
                    if ps['zz'] == 0.0:
                        ps['nz'] = 0.0
                    else:
                        ps['nz'] = ps['ne'] - ps['ni']
                if independ not in ps:
                    raise IOError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps):
        zeff = (ps['zi']**2*ps['ni'] + ps['zz']**2*ps['nz'])/ps['ne'] # units [None]
        return zeff

    def __call__(self, ps):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps)

if __name__=='__main__':
    ps = {}
    ps['ne']   = 18.0
    ps['ni']   = 16.0
    ps['zi']   =  2.0
    ps['zz']   =  5.0
    calc_zeff = zeff()
    print(calc_zeff(ps))
