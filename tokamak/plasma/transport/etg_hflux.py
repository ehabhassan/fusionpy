from numpy                          import argmin,sqrt,pi
from os.path                        import realpath
from plot.colors                    import CRED, CEND
from iofiles.efit.lref              import lref
from iofiles.efit.bref              import bref
from tokamak.constants              import e,me,md
from iofiles.efit.read_efit         import read_efit
from iofiles.fastran.read_fastran   import read_fastran
from tokamak.plasma.transport.qgb   import qgb
from tokamak.plasma.parameters.cs   import cs
from tokamak.plasma.parameters.lte  import lte
from tokamak.plasma.parameters.eta  import eta
from tokamak.plasma.parameters.tau  import tau
from tokamak.plasma.parameters.rhos import rhos

class etg_hflux():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["ne", "te", "rho", "lte", "eta", "lref", "tau"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ == "lte":
                    if "lte" in ps:
                        self.lte = ps['lte']
                    else:
                        calc_lte = lte()
                        self.lte = calc_lte(ps)

                elif independ == "eta":
                    if "eta" in ps:
                        self.eta = ps['eta']
                    else:
                        calc_eta = eta()
                        self.eta = calc_eta(ps)

                elif independ == "tau":
                    if "tau" in ps:
                        self.tau = ps['tau']
                    else:
                        calc_tau = tau()
                        self.tau = calc_tau(ps)

                elif independ == "lref":
                    if "lref" in ps:
                        self.lref = ps['lref']
                    else:
                        calc_lref = lref()
                        self.lref = calc_lref(ps)

                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, rho0, a0=0.0, b0=0.0, model=1, ps_update=False):
        calc_qgb = qgb()
        QGB = calc_qgb(ps, rho0)

        irho = argmin(abs(ps['rho']-rho0))
        lte0 = self.lte[irho]
        eta0 = self.eta[irho]
        tau0 = self.tau[irho]

        te0 = ps['te'][irho]*1.0e3*e
        ne0 = ps['ne'][irho]*1.0e19

        if   model == 1:
            if a0==0.0: a0=-1.30
            if b0==0.0: b0= 0.92
            Qnorm = sqrt(me/ps['mi'])*lte0**2*(a0+b0*eta0)
        elif model == 2:
            if a0==0.0: a0=-12.0
            if b0==0.0: b0=  6.70
            Qnorm = sqrt(me/ps['mi'])*lte0**2*(a0+b0*eta0**2)
        elif model == 3:
            if a0==0.0: a0=1.40
            if b0==0.0: b0=0.50
            Qnorm = sqrt(me/ps['mi'])*lte0**2*(a0+b0*eta0**4)
        elif model == 4:
            if a0==0.0: a0=3.20
            if b0==0.0: b0=0.63
            Qnorm = sqrt(me/ps['mi'])*lte0**2*(a0+b0*eta0**4/tau0)
        elif model == 5: 
            if a0==0.0: a0=0.043
            if b0==0.0: b0=0.023
            Qnorm = sqrt(me/ps['mi'])*lte0**2*(eta0-1.0)*(a0+b0*eta0**2/tau0)
        else: 
            if a0==0.0: a0=0.043
            if b0==0.0: b0=0.053
            Qnorm = sqrt(me/ps['mi'])*lte0**2*(eta0-1)*(a0+b0*eta0**2)

        S = (2.0*pi*ps['rmajor'])*(2.0*pi*self.lref)
        QSI  = Qnorm*QGB
        QTSI = QSI*S
        chiSI = QSI/ne0/te0*self.lref/lte0

        if ps_update:
            ps['etg_q']    = QSI
            ps['etg_qt']   = QTSI
            ps['etg_chiq'] = chiQSI
        return QSI,QTSI,chiSI

    def __call__(self, ps, rho0, a0=0.0, b0=0.0, model=1, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, rho0, a0, b0, model, ps_update)

if __name__=='__main__':
    fast_file_path = realpath('../../../testsuite/state_files/fastran.nc')
    fastdata = read_fastran(fast_file_path)
    efit_file_path = realpath('../../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(fpath=efit_file_path)

    ps = efitdata.copy()
    ps['rmajor'] = fastdata['rmajor']['data'][-1,0]
    ps['rho']    = fastdata['rho']['data']
    ps['te']     = fastdata['te']['data'][-1,:]
    ps['ne']     = fastdata['ne']['data'][-1,:]
    ps['mi']     = md
    ps['zi']     = 1.0
    
   #ps['bt']     = fastdata['b0']['data'][-1]
    calc_bref    = bref()
    ps['bt']     = calc_bref(ps)
    a0   = 0.043
    b0   = 0.053
    rho0 = 0.980

    calc_etg_hflux = etg_hflux()
    print(calc_etg_hflux(ps, rho0, a0, b0))
