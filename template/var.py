from plot.colors import CRED, CEND

class var():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ['input-1','input-2','input-3']

    def checkdependencies(self,ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ not in ps:
                    raise IOError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps):
        var = ps['input-1']/ps['input-2']+ps['input-3'] # units [None]
        return var

    def __call__(self, ps):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps)

if __name__=='__main__':
    ps = {}
    ps['input-1'] = 10.0
    ps['input-2'] = 20.0
    ps['input-3'] =  1.5
    calc_var = var()
    print(calc_var(ps))
