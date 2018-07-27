import numpy, random, math
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from datageneration import *
from kernels import *
from plots import *

inputs , targets , classA , classB = data_generation()
plotclasses(classA, classB)
print('inputs')
print (inputs)
print('targets')
print(targets)
print('class A')
print(classA)
print('class B')
print(classB)
