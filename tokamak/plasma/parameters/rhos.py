from plot.colors               import CRED, CEND
from tokamak.plasma.parameters import cs, omegai

class rhos():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["cs", "omegai"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == 'cs':
                    if 'cs' in ps:
                        self.cs = ps['cs']
                    elif 'te' in ps and 'mi' in ps:
                        calc_cs = cs.cs()
                        self.cs = calc_cs(ps)
                    else:
                        raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)

                elif independ == 'omegai':
                    if 'omegai' in ps:
                        self.omegai = ps['omegai']
                    elif 'bt' in ps and 'mi' in ps:
                        calc_omegai = omegai.omegai()
                        self.omegai = calc_omegai(ps)
                    else:
                        raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        rhos = self.cs/self.omegai # units [None]
        if ps_update:
            ps['rhos'] = rhos
        return rhos

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps,ps_update)

if __name__=='__main__':
    ps = {}
    ps['cs']       = 18.0
   #ps['te']       = 648.0
    ps['bt']       =   2.0
    ps['mi']       =   2.0*1.67e-27
   #ps['omegai']   = 16.0
    calc_rhos = rhos()
    print(calc_rhos(ps))
