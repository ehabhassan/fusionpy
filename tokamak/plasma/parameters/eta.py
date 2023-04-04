from numpy                     import pi,cos,sin,linspace
from plot.colors               import CRED, CEND
from tokamak.plasma.parameters import lne,lte

class eta():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["lne", "lte"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == 'lne':
                    if independ not in ps:
                        calc_lne = lne.lne()
                        self.lne = calc_lne(ps)
                    else:
                        self.lne = ps['lne']
                elif independ == 'lte':
                    if independ not in ps:
                        calc_lte = lte.lte()
                        self.lte = calc_lte(ps)
                    else:
                        self.lte = ps['lte']
        return True

    def default(self, ps):
        eta = self.lte/self.lne
        return eta

    def __call__(self, ps):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps)

if __name__=='__main__':
    ps = {}
    ps['rho'] = linspace(-pi,pi,100)
    ps['ne']  = cos(ps['rho'])
    ps['te']  = sin(ps['rho'])
    calc_eta = eta()
    print(calc_eta(ps))


