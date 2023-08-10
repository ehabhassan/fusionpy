from numpy               import pi
from os.path             import realpath
from plot.colors         import CRED, CEND
from iofiles.read_iterdb import read_iterdb

class omega_doppler():
    def __init__(self, model='default'):
        self.model = model
        self.dependencies = ["vrot", "ntor"]

    def checkdependencies(self, ps):
        if self.dependencies:
            for independ in self.dependencies:
                if independ not in ps:
                    raise ValueError(CRED + "DEPENDENT VARIABLE (%s) IS MISSING!" % independ + CEND)
        return True

    def default(self, ps, ps_update=False):
        omega_doppler = ps['vrot'] * ps['ntor'] / 2.0 / pi
        if ps_update:
            ps['omega_doppler'] = omega_doppler
        return omega_doppler

    def __call__(self, ps, ps_update=False):
        self.checkdependencies(ps)
        if self.model == 'default': return self.default(ps, ps_update)

if __name__=='__main__':
    iterdb_file_path = realpath('../../../testsuite/state_files/plasma_prof.iterdb')
    iterdbdata = read_iterdb(fpath=iterdb_file_path)

    ps = {}
    ps['vrot'] = iterdbdata['Vrot']
    ps['ntor'] = 10
    calc_omega_doppler = omega_doppler()
    print(calc_omega_doppler(ps))


