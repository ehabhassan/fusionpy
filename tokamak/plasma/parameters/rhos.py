from plot.colors    import CRED, CEND
from tokamak.plasma import cs, omegai

class rhos():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["cs", "omegai"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if 'te' in ps and 'mi' in ps:
                    calc_cs = cs.cs()
                    ps['cs'] = calc_cs(ps)
                if 'bt' in ps and 'mi' in ps:
                    calc_omegai = omegai.omegai()
                    ps['omegai'] = calc_omegai(ps)
                if independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps):
        rhos = ps['cs']/ps['omegai'] # units [None]
        return rhos

    def __call__(self, ps):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps)

if __name__=='__main__':
    ps = {}
    ps['cs']       = 18.0
   #ps['te']       = 648.0
    ps['bt']       =   2.0
    ps['mi']       =   2.0*1.67e-27
   #ps['omegai']   = 16.0
    calc_rhos = rhos()
    print(calc_rhos(ps))
