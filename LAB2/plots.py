import numpy, random, math
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def plotclasses(classA,classB, new):
    plt.plot([p[0] for p in classA ] , [p[1] for p in classA ] , 'b.' )
    plt.plot([p[0] for p in classB ] , [p[1] for p in classB ] , 'r.' )
    #plt.plot(new[0], new[1], 'g.')
    plt.axis('equal')
    #plt.savefig('svmplot.pdf')
    #plt.show()
    return

def plotboundary(indicator, b, alpha, inputs, targets, kernel, sigma):
    xgrid=numpy.linspace(-5, 5)
    ygrid=numpy.linspace(-4, 4)
    grid=numpy.array( [[indicator(x, y, b, alpha, inputs, targets, kernel, sigma) for y in ygrid ] for x in xgrid ] )
    grid = numpy.transpose(grid)
    plt.contour( xgrid , ygrid , grid , (-1 , 0.0 , 1 ) , colors=( 'red' , 'black' , 'blue' ) , linewidths=(1 , 3 , 1) )
    plt.show()
