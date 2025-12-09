import numpy

def get_plasma_shape(major,minor,delta,kappa,zeta):

    theta = numpy.linspace(-numpy.pi,numpy.pi,100)

    R = major + minor * numpy.cos(theta + delta * numpy.sin(theta) - zeta * numpy.sin(2.0 * theta))
    Z = kappa * minor * numpy.sin(theta + zeta * numpy.sin(2.0 * theta))

    return R,Z
