import numpy

def profile_error_rms_and_offset(pexp,psim):
    Nexp = len(pexp)
    Nsim = len(psim)
    if Nexp != Nsim:
       print("N(p1) = %d, N(p2) = %d" %(Nexp,Nsim))
       raise ValueError("input profiles do not match in length")
    rms  = numpy.sqrt(numpy.sum((pexp - psim)**2)/Nexp)
    rms /= numpy.sqrt(numpy.sum( pexp**2)        /Nexp)

    offset  =            numpy.sum(pexp - psim)/Nexp 
    offset /= numpy.sqrt(numpy.sum(pexp**2)    /Nexp)

    return rms,offset

def calculate_line_average(profile,grid): 
    ngrid = len(grid)
    line_average = 0.0
    for i in range(ngrid-1):
        line_average += 0.5 * (profile[i+1] + profile[i]) * (grid[i+1] - grid[i])
    line_average /= grid[-1]
    return line_average

