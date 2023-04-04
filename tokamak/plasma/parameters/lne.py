from maths       import fd_d1_o4
from numpy       import pi,cos,linspace
from plot.colors import CRED, CEND

class lne():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["ne", "rho"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps):
        Df = fd_d1_o4.fd_d1_o4()
        lne = -Df(ps['ne'],ps['rho'])/ps['ne']
        return lne

    def __call__(self, ps):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps)

if __name__=='__main__':
    ps = {}
    ps['rho'] = linspace(-pi,pi,100)
    ps['ne']  = cos(ps['rho'])
    calc_lne = lne()
    print(calc_lne(ps))


