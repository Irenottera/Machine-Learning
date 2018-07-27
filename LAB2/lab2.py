import numpy, random, math
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from datageneration import *
from kernels import *
from plots import *


global M

def pre_comp_matrix(inputs, targets, kernel, arg):
    n = len(inputs)
    M = numpy.zeros((n,n))
    if kernel == 1: #'radial':
        for i in range(n):
            for j in range(n):
                M[i][j] = targets[i] * targets[j] * radial_kernel(inputs[i], inputs[j], arg)
    if kernel == 2:# 'polynomial':
        for i in range(n):
            for j in range(n):
                M[i][j] = targets[i] * targets[j] * polynomial_kernel(inputs[i], inputs[j], arg)
    if kernel == 3: #'linear':
        for i in range(n):
            for j in range(n):
                M[i][j] = targets[i] * targets[j] * linear_kernel(inputs[i], inputs[j], arg)
    return(M)

def objective(alpha):
    #TRY TO REFORMULATE!!
    n = len(alpha)
    expr = 0
    for i in range(n):
        for j in range(n):
            expr = expr + 0.5*(alpha[i]*alpha[j]*M[i][j])
    for i in range(n):
        expr = expr - alpha[i]
    return(expr)

def zerofun(alpha):
    k = numpy.dot(alpha, targets)
    ris = numpy.sum(k)
    return(k)

def indicator (new_x, new_y, b, alpha, inputs, targets, kernel, sigma):
    ind = 0
    new = numpy.array((new_x, new_y))
    if kernel == 1:
        for i in range(n):
            ind = ind + alpha[i]*targets[i]*radial_kernel(new, inputs[i], sigma)
        ind = ind - b

    if kernel == 2:
        for i in range(n):
            ind = ind + alpha[i]*targets[i]*polynomial_kernel(new, inputs[i], sigma)
        ind = ind - b

    if kernel == 3:
        for i in range(n):
            ind = ind + alpha[i]*targets[i]*linear_kernel(new, inputs[i], sigma )
        ind = ind - b

    return(ind)



######################################################################


#DATA GENERATION

inputs , targets , classA , classB = data_generation2()


#NEW POINTS
new = [0.,0.]
plotclasses(classA,classB,new)
#parameters
C = 1
n = len(targets)
sigma = 3 #radial or polynomial
kernel = 1
M = pre_comp_matrix(inputs, targets, kernel, sigma)

#SOLVE OPTIMIZATION PROBLEM - find alpha vector
start = numpy.zeros(n)
B=[(0, C) for b in range(n)]
XC ={'type':'eq', 'fun':zerofun}
ret = minimize(objective , start , bounds=B, constraints=XC)
alpha = ret['x']
#print(alpha)

#SELECTION OF NON-ZERO ALPHAS
kk = 0
save_nonzeros=[]
indeces = numpy.zeros((n,2))

for i in range(n):
    indeces[i][0]=i
    if numpy.absolute(alpha[i]) > 1e-5:
        conc=numpy.concatenate(([alpha[i]], inputs[i], [targets[i]]))
        save_nonzeros.append(conc)
        kk = kk+1
        indeces[i][1] = kk

#COMPUTE b
b = 0
for i in range(kk):
    if save_nonzeros[i][0]>0 and save_nonzeros[i][0]<=C:
        sv_index = i+1
        #print(sv_index)
        break

#find global index for sv_index
for i in range(n):
    if indeces[i][1] == sv_index:
        ind = i
        #print (ind)
        break
#compute b
for i in range(n):
    #print(targets[ind])
    MM = M[ind][i]/(targets[ind])
    b = b + alpha[i]*MM
b = b - targets[ind]
#print(b)

#INDICATOR FUNCTION &   CLASSIFICATION
ind = indicator(new[0], new[1], b, alpha, inputs, targets, kernel, sigma)
if ind > 0:
    new_target=1
else:
    new_target=-1
print (new_target)

#PLOT THE HYPERPLANE
plotboundary(indicator,b, alpha, inputs, targets, kernel, sigma)

print('inputs')
print (inputs)
print('targets')
print(targets)
print('class A')
print(classA)
print('class B')
print(classB)
