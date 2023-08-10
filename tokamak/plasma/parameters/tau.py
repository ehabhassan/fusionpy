from plot.colors import CRED, CEND

class tau():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["te", "ti", "zeff"]

    def checkdependencies(self,ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        tau = (ps['te']/ps['ti'])*ps['zeff'] # units [None]
        if ps_update:
            ps['tau'] = tau
        return tau

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

if __name__=='__main__':
    ps = {}
    ps['te']   = 10.0
    ps['ti']   = 20.0
    ps['zeff'] =  1.5
    calc_tau = tau()
    print(calc_tau(ps))
