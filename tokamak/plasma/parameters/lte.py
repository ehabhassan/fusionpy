from maths       import fd_d1_o4
from numpy       import pi,cos,linspace
from plot.colors import CRED, CEND

class lte():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["te", "rho"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == "rho":
                    if "rho" in ps:
                        self.rho = ps['rho']
                    elif "rhotor" in ps:
                        self.rho = ps['rhotor']
                    elif "PHIN" in ps:
                        self.rho = sqrt(ps['PHIN'])
                    else:
                        raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        Df = fd_d1_o4.fd_d1_o4()
        lte = -Df(self.rho,ps['te'])/ps['te']
        if ps_update:
            ps['lte'] = lte
        return lte

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

if __name__=='__main__':
    ps = {}
    ps['rho'] = linspace(-pi,pi,100)
    ps['te']  = cos(ps['rho'])
    calc_lte = lte()
    print(calc_lte(ps))


