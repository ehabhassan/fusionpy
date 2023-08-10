from numpy       import dot,zeros,pi
from numpy       import cos,linspace
from plot.colors import CRED, CEND
from matplotlib.pyplot import plot,legend,show

class fd_d1_o4():
    def __init__(self, model='default'):
        self.model = model

    def default(self, x, f, DX=False):
        """
        - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        Centered finite difference, first derivative, 4th order.
        - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        x : grid for var
        f : quantity to be differentiated.
        DX: matrix for the finite-differencing operator. if mat=False then it is created
        - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        """
        if not DX:
            nx = len(f)
            dx = x[1] - x[0]

            DX=zeros((nx,nx),dtype='float')
            for i in range(nx):
                if i-1 >= 0:
                    DX[i,i-1]=-8
                if i-2 >= 0:
                    DX[i,i-2]=1
                if i+1 <= nx-1:
                    DX[i,i+1]=8
                if i+2 <= nx-1:
                    DX[i,i+2]=-1
            DX *= 1.0/(12.0*dx)

        df     = -dot(DX,f)
        df[0]  = 0.0
        df[1]  = 0.0
       #df[2]  = 0.0
        df[-1] = 0.0
        df[-2] = 0.0
       #df[-3] = 0.0
        return -df

    def __call__(self, f, x, DX=False):
        if self.model == 'default': return self.default(f,x,DX)

if __name__=='__main__':
    calc_fd_d1_o4 = fd_d1_o4()
    xx = linspace(-pi,pi,100)
    ff = cos(xx)
    df = calc_fd_d1_o4(ff,xx)
    plot(xx,ff,label="f(x)")
    plot(xx,df,label="Df(x)")
    legend()
    show()

