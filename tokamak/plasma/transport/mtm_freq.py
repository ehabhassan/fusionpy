from numpy                          import linspace,argmin
from os.path                        import realpath
from plot.colors                    import CRED, CEND
from iofiles.efit.lref              import lref
from iofiles.efit.phigrids          import phigrids
from iofiles.efit.read_efit         import read_efit
from iofiles.fastran.read_fastran   import read_fastran
from tokamak.plasma.parameters.cs   import cs
from tokamak.plasma.parameters.rhos import rhos

from tokamak.constants              import e,md,me

class mtm_freq():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = []
        self.dependencies.extned(["rho", "rhos", "ntor", "freq"])
        self.dependencies.extend(["lref", "bref", "omegapct", "rholim"])

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == 'ntor':
                    if 'ntor' in ps:
                       if type(ps['ntor']) in [int,float,str]:
                          self.n0bgn  = int(ps['ntor'])
                          self.n0end  = int(ps['ntor'])
                          self.nrange = range(n0bgn,n0end+1)
                       else:
                          if   len(ps['ntor']) == 2:
                               self.n0bgn  = int(ps['ntor'][0])
                               self.n0end  = int(ps['ntor'][1])
                               self.nrange = range(n0bgn,n0end+1)
                          elif len(ps['ntor']) == 3:
                               self.n0bgn  = int(ps['ntor'][0])
                               self.n0stp  = int(ps['ntor'][1])
                               self.n0end  = int(ps['ntor'][2])
                               self.nrange = range(n0bgn,n0end+1,n0stp)
                          elif len(ps['ntor']) >= 4:
                               self.n0bgn  = int(ps['ntor'][0])
                               self.n0end  = int(ps['ntor'][-1])
                               self.nrange = []
                               for in0 in ps['ntor']:
                                   self.nrange.append(in0)
                    else:
                          self.n0bgn = 1
                          self.n0end = 100
                          self.nrange = range(n0bgn,n0end+1)

                elif independ == 'freq':
                    if 'freq' in ps:
                       if type(ps['freq']) in [int,float,str]:
                          self.f0bgn = float(ps['freq'])
                          self.f0end = 500.0e3
                       else:
                          if type(ps['freq'][0]) in [int,float,str]:
                             self.f0bgn = float(ps['freq'][0])
                             self.f0end = float(ps['freq'][1])
                          else:
                             self.f0bgn = []
                             self.f0end = []
                             for i in range(len(ps['freq'])):
                                 self.f0bgn.append(ps['freq'][i][0])
                                 self.f0end.append(ps['freq'][i][1])
                    else:
                          self.f0bgn = 1.0e3
                          self.f0end = 500.0e3

                elif independ == "rholim":
                    if 'rholim' in ps:
                       if type(ps['rholim']) == float:
                          self.bgnrho = ps['rholim']
                       else:
                          self.bgnrho = ps['rholim'][0]
                          self.endrho = ps['rholim'][-1]

                elif independ == "omegapct":
                    if 'omegapct' in ps:
                       if ps['omegapct']> 1.0:
                          self.omegapct = ps['omegapct']/100.0
                       else:
                          self.omegapct = ps['omegapct']
                    else:
                          self.omegapct = 0.8

                elif independ == "rhos":
                    if "rhos" in ps:
                        self.rhos = ps['rhos']
                    else:
                        calc_rhos = rhos()
                        self.rhos = calc_rhos(ps)

                elif independ == "cs":
                    if "cs" in ps:
                        self.cs = ps['cs']
                    else:
                        calc_cs = cs()
                        self.cs = calc_cs(ps)

                elif independ == "bref":
                    if "bref" in ps:
                        self.bref = ps['bref']
                    else:
                        calc_bref = bref()
                        self.bref = calc_bref(ps)

                elif independ == "lref":
                    if "lref" in ps:
                        self.lref = ps['lref']
                    else:
                        calc_lref = lref()
                        self.lref = calc_lref(ps)

                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, rho0, ps_update=False):
        return qgb

    def __call__(self, ps, rho0, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, rho0, ps_update)

if __name__=='__main__':
    fast_file_path = realpath('../../../testsuite/state_files/fastran.nc')
    fastdata = read_fastran(fast_file_path)
    efit_file_path = realpath('../../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(efitfpath=efit_file_path)

    ps = efitdata.copy()
    ps['rho'] = fastdata['rho']['data']
    ps['bt']  = fastdata['b0']['data'][-1]
    ps['te']  = fastdata['te']['data'][-1,:]
    ps['ne']  = fastdata['ne']['data'][-1,:]
    ps['mi']  = md
    rho0      = 0.975

    calc_qgb = qgb()
    print(calc_qgb(ps, rho0))
