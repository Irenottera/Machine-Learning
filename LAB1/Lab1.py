import monkdata as m
import dtree as d
import random
import numpy as np
import math
#import matplotlib
import matplotlib.pyplot as plt

#import drawtree_qt5 as dd
#print(m.monk1)

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata)*fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

#ASSIGNMENT 1
# e1 = d.entropy(m.monk1)
# print(e1)
# e2 = d.entropy(m.monk2)
# print(e2)
# e3 = d.entropy(m.monk3)
# print(e3)

#ASSIGNMENT 3
# # print('M-MONK1')
# # for x in range(0, 6):
# #     print(d.averageGain(m.monk1, m.attributes[x]))
# # print('M-MONK2')
# # for x in range(0, 6):
# #     print(d.averageGain(m.monk2, m.attributes[x]))
# # print('M-MONK3')
# # for x in range(0, 6):
# #     print(d.averageGain(m.monk3, m.attributes[x]))
#
# #
# # print('a5=1')
# # for x in range(0,6):
# #     print(d.averageGain(d.select(m.monk1, m.attributes[4], 1) , m.attributes[x]    ))
# #     print ( d.mostCommon(d.select(m.monk1, m.attributes[4], 1)) )
# # print('a5=2')
# # for x in range(0,6):
# #     print(d.averageGain(d.select(m.monk1, m.attributes[4], 2) , m.attributes[x]    ))
# #
# # print('a5=3')
# # for x in range(0,6):
# #     print(d.averageGain(d.select(m.monk1, m.attributes[4], 3) , m.attributes[x]    ))
# # print('a5=4')
# # for x in range(0,6):
# #     print(d.averageGain(d.select(m.monk1, m.attributes[4], 4) , m.attributes[x]    ))
# #
# #
# # print ( d.mostCommon(d.select(d.select(m.monk1, m.attributes[4], 4), m.attributes[0],3)) )
#
# #ASSIGNMENT 5
# tree1 = d.buildTree(m.monk1, m.attributes)
# tree2 = d.buildTree(m.monk2, m.attributes)
# tree3 = d.buildTree(m.monk3, m.attributes)
# print(tree1)
# print(tree2)
# print(tree3)
#
# print('Percentages')
# print (d.check(tree1, m.monk1))
# print (d.check(tree1, m.monk1test))
# print (d.check(tree2, m.monk2))
# print (d.check(tree2, m.monk2test))
# print (d.check(tree3, m.monk3))
# print (d.check(tree3, m.monk3test))
#
# error1 = 1-d.check(tree1, m.monk1)
# error1test = 1-d.check(tree1, m.monk1test)
# error2 = 1-d.check(tree2, m.monk2)
# error2test = 1-d.check(tree2, m.monk2test)
# error3 = 1-d.check(tree3, m.monk3)
# error3test = 1-d.check(tree3, m.monk3test)
#
# print ('Errors')
# print(error1)
# print(error1test)
# print(error2)
# print(error2test)
# print(error3)
# print(error3test)
#
#
ciccia = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
aaa = np.zeros((1,1000))
bbb = np.zeros((2,6))
ccc = np.zeros((2,6))
fraction = 0.3
jj=0


for fraction in ciccia:

    for j in range(1000):

        monk1train, monk1val = partition(m.monk3, fraction)
        tree1 = d.buildTree(monk1train, m.attributes)
        aa=[0,0]
        #Choose the best subtree
        for i in range( 1, len(d.allPruned(tree1)) ) :
            a = d.check ( d.allPruned(tree1)[i] , monk1val)
            if a > aa[1]:
                aa[0] =  d.allPruned(tree1)[i]
                aa[1] = a
        aaa[0,j]=aa[1]

    #Compute the mean
    print('MEAN')
    mean=0
    for j in range(1000):
        mean = mean + (1-aaa[0,j])
    mean = mean/1000
    print(mean)
    #Compute variance
    print('VARIANCE')
    variance=0
    for j in range(1000):
        variance = variance + (1-aaa[0,j]-mean)**2
    variance = math.sqrt(variance/1000)
    print(variance)


#print(aaa)
    #Compute the mean
# x = ciccia
# y1 =[0.762873 , 0.793333 , 0.823387 , 0.850799 , 0.856315 , 0.869200 ]
# y2 =[0.865465 , 0.898378 , 0.904262 , 0.917142 , 0.916216 , 0.9264]
# plt.plot(x, y1, x, y2)
# plt.xlabel('fraction')
# plt.ylabel('mean')
# plt.show()

x = ciccia
y1 =[0.132465 , 0.109324 , 0.095868 , 0.088367 , 0.079567 , 0.070760]
y2 =[0.054846 , 0.043255 , 0.035193 , 0.033341 , 0.040131 , 0.046538]
plt.plot(x, y1, x, y2)
plt.xlabel('fraction')
plt.ylabel('mean and variance')
plt.show()


#
#
# print('MONK2')
# bb=[0,0]
#
# for i in range( 1, len(d.allPruned(tree2)) ) :
#     #print(i)
#     b = d.check ( d.allPruned(tree2)[i] , monk2val)
#     if b > bb[1]:
#         bb[0] =  d.allPruned(tree2)[i]
#         bb[1] = b
#         #print('change')
#
# print(bb[0])
# print(bb[1])
# #bbb[0,jj]=bb[0]
# #bbb[1,jj]=bb[1]
#
# print('MONK3')
# cc=[0,0]
#
# for i in range( 1, len(d.allPruned(tree3)) ) :
#     #print(i)
#     c = d.check ( d.allPruned(tree3)[i] , monk2val)
#     if c > cc[1]:
#         cc[0] =  d.allPruned(tree3)[i]
#         cc[1] = c
#         #print('change')
#
# print(cc[0])
# print(cc[1])
# #ccc[0,jj]=cc[0]
# #ccc[1,jj]=cc[1]
#
# #jj = jj+1
# print ('\n')
