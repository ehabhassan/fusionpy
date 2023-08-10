from numpy             import dot,zeros,pi
from numpy             import cos,linspace
from plot.colors       import CRED, CEND
from scipy.interpolate import splrep,splev
from matplotlib.pyplot import plot,legend,show

class interp():
    def __init__(self, model='default'):
        self.model = model

    def default(self, xin, fxin, xnew, ynew=[], yout=[]):
        #splrep returns knots and coefficients for cubic spline
        #Use these knots and coefficients with splev to get a new y
    
        fknots = splrep(xin,fxin)
        fxnew  = splev(xnew,fknots,der=0)
    
        if len(ynew)>0 and len(yout)>0:
           yknots = splrep(ynew,fxnew)
           fxout  = splev(yout,yknots,der=0)
    
           x_knots = splrep(ynew,xnew)
           xout    = splev(yout,x_knots,der=0)
        else:
           fxout = fxnew[:]
        return fxout

    def __call__(self, xin, fxin, xnew, ynew=[], yout=[]):
        if self.model == 'default': return self.default(xin, fxin, xnew, ynew, yout)

if __name__=='__main__':
    calc_interp = interp()
    xx = linspace(-pi,pi,10)
    fx = cos(xx)
    zz = linspace(-pi,pi,100)
    fz = calc_interp(xx,fx,zz)
    plot(xx,fx,label="f(x)")
    plot(zz,fz,label="f(z)")
    legend()
    show()


