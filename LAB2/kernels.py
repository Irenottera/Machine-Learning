import numpy, random, math
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from math import exp


def linear_kernel(xi,xj,arg=0):
    k = numpy.dot(xi, xj)
    return(k)

def polynomial_kernel(xi,xj,p):
    k = numpy.power(numpy.dot(xi,xj) + 1 , p)
    return k

def radial_kernel(xi,xj,sigma=2):
    diff = xi-xj
    k = numpy.exp(-numpy.dot(diff,diff)/(2*sigma**2))
    return(k)

#def sigmoid_kernel(x, y, k=0.1, delta=0):
#    np.transpose(x)
#    return np.tanh(k * np.dot(x, y) - delta)
