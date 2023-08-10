from numpy       import dot,zeros,pi
from plot.colors import CRED, CEND
from matplotlib.pyplot import plot,legend,show
from scipy.interpolate import CubicSpline

import numpy as npy

class derivative():
    def __init__(self, model='default'):
        self.model = model

    def default(self, x, f, axis=0, order=1, method="gradient"):
        """
        - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        Centered finite difference, first derivative, 4th order.
        - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        x : grid for var
        f : quantity to be differentiated.
        axis: axis along which the derivative is calculated (default: 0)
        order: order of the derivative (default: 1)
        mathod: derivative method (default: gradient)
        - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        """
        fxShape = npy.shape(f)
        nDim    = len(fxShape)
        if   method=='gradient':
             if   nDim == 1:
                  dfdx = npy.gradient(f,x)
        elif method=='CubicSpline':
             if   nDim == 1:
                  CS = CubicSpline(x,f)
                  dfdx = CS(x,order)
             elif nDim == 2:
                  m = fxShape[0]
                  n = fxShape[1]
                  dfdx=npy.zeros((m,n))
                  if   axis == 0:
                       for j in range(n):
                          CS = CubicSpline(x,f[:,j])
                          dfdx[:,j] = CS(x,order)
                  elif axis == 1:
                       for i in range(m):
                          CS = CubicSpline(x,f[i,:])
                          dfdx[i,:] = CS(x,order)
        return dfdx

    def __call__(self, x, f, axis=0, order=1, method="gradient"):
        if self.model == 'default': return self.default(x, f, axis, order, method)

if __name__=='__main__':
    calc_derivative = derivative()
    xx = npy.linspace(-pi,pi,100)
    ff = npy.cos(xx)
    df = calc_derivative(xx,ff)
    plot(xx,ff,label="f(x)")
    plot(xx,df,label="Df(x)")
    legend()
    show()

