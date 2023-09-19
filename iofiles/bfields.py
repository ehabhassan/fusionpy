from maths.interp           import interp
from maths.fd_d1_o4         import fd_d1_o4
from numpy                  import argmin,abs
from numpy                  import linspace
from numpy                  import empty_like
from plot.colors            import CRED, CEND
from os.path                import realpath
from iofiles.efit.rzgrids   import rzgrids
from iofiles.efit.psigrids  import psigrids
from iofiles.efit.read_efit import read_efit

class bfields():
    def __init__(self, model='default'):
        self.model = model
        self.interp = interp()
        self.fd_d1_o4 = fd_d1_o4()
        self.dependencies = ["R1D", "Z1D", "RMAX", "ZMAX", "psiRZ", "PSIN", "PSIMAX", "PSIBND", "fpol", "RDIM"]

    def checkdependencies(self,ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ in ["R1D","Z1D"]:
                    if "R1D" in ps and "Z1D" in ps:
                        self.R1D = ps['R1D']
                        self.Z1D = ps['Z1D']
                    else:
                        calc_rzgrids = rzgrids()
                        self.R1D, self.Z1D = calc_rzgrids(ps)
                elif independ == "PSIN":
                    if "PSIN" in ps:
                        self.PSIN = ps['PSIN']
                    else:
                        calc_psigrids = psigrids()
                        PSI, self.PSIN, rhopsi = calc_psigrids(ps)
                elif independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
       #Z0_ind is the index of Z1D of midplane
        Z0_ind = argmin(abs(self.Z1D-ps['ZMAX']))
       #psi_midplane is psi_pol at midplane on even Rgrid
        psi_pol_mp = ps['psiRZ'][Z0_ind,:]
       #R0_ind is index of unif_R1D at RMAX
        R0_ind = argmin(abs(self.R1D-ps['RMAX']))
        psi_pol_obmp = psi_pol_mp[R0_ind:]
       #Normalize psi_pol_obmp to psip_n_temp
        psip_n_temp = empty_like(psi_pol_obmp)
        for i in range(len(psi_pol_obmp)):
            psip_n_temp[i] = (psi_pol_obmp[i]-ps['PSIMAX'])/(ps['PSIBND']-ps['PSIMAX'])
        unif_R = linspace(self.R1D[R0_ind],self.R1D[-1],ps['RDIM']*10)
        psip_n_unifR = self.interp(self.R1D[R0_ind:],psip_n_temp,unif_R)
        psisep_ind = argmin(abs(psip_n_unifR-1.02))
        psip_n_obmp = psip_n_unifR[:psisep_ind]
        R_obmp = unif_R[:psisep_ind].copy()
       #B_pol is d psi_pol/ d R * (1/R)
       #B_pol = fd_d1_o4(psi_pol_obmp, unif_R[R0_ind:R0_ind+psisep_ind])/unif_R[R0_ind:R0_ind+psisep_ind]
        B_pol = self.fd_d1_o4(R_obmp,psip_n_obmp*(ps['PSIBND']-ps['PSIMAX'])+ps['PSIMAX'])/R_obmp
       #Convert F(on even psi_pol grid) to F(on even R grid)
        F_obmp = self.interp(self.PSIN, ps['fpol'], psip_n_obmp)
       #B_tor = F/R
        B_tor = F_obmp/R_obmp
    
        # psip_n_obmp is normalized psi_pol at outboard midplane on uniform unif_R
        # B_tor and B_pol are on uniform unif_R as well
        # psip_n_obmp is unlike psip_n ([0,1]), it goes from 0 to 1.06 here

        if ps_update:
            ps['bpol'] = B_pol
            ps['btor'] = B_tor
            ps['Robmp'] = R_obmp
            ps['psip_n_obmp'] = psip_n_obmp
        return B_pol, B_tor, psip_n_obmp, R_obmp 

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

if __name__=='__main__':
    efit_file_path = realpath('../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(efitfpath=efit_file_path)
    calc_bfields = bfields()
    print(calc_bfields(efitdata,ps_update=True))
    print(efitdata.keys())
