from numpy       import sqrt
from plot.colors import CRED, CEND

class cs():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["te", "mi"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps):
        cs = sqrt(ps['te']/ps['mi']) # units [None]
        return cs

    def __call__(self, ps):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps)

if __name__=='__main__':
    ps = {}
    ps['te']   = 18.0
    ps['mi']   = 16.0
    calc_cs = cs()
    print(calc_cs(ps))
