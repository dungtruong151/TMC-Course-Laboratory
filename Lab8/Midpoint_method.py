#Truong Tri Dung - ITCSIU21126

import math
import numpy as np
import matplotlib.pyplot as p

'''
y = e^(-x) + C*e^(-200000x)
y(0)=0 <=> C=-1
'''

def yi(x):
    return math.exp(x**4/4-1.5*x)

def f(x,y):
    return y*(x**3)-1.5*y

def Euler_method(x,y,i):
    if (x<2.0):
        x_euler.append(x + h)
        y_euler.append(y + h*f(x,y))
        y_real.append(yi(x+h))
        Euler_method(x_euler[i],y_euler[i],i+1)

def Midpoint_method(i):
    if (i<=4):
        x_euler1.append(x_euler[2*i])
        y_euler1.append(y_euler1[i-1] + h*f(x_euler[i+(i-1)],y_euler[i+(i-1)]))
        y_real.append(yi(x_euler1[i]))
        Midpoint_method(i+1)

x_euler = []
y_euler = []
y_real = []
x_euler.append(0.0)
y_euler.append(1.0)
y_real.append(1.0)
h = 0.25
Euler_method(x_euler[0],y_euler[0],1)
x_euler1 = []
y_euler1 = []
y_real = []
x_euler1.append(0.0)
y_euler1.append(1.0)
y_real.append(1.0)
h = 0.5
Midpoint_method(1)

print("%s\t%s\t\t%s" % ("x", "y_real", "y_euler"))
for i in range(0,len(x_euler1)):
    #if (i % 2 == 0):
        print("%.2f\t%f\t%f " % (x_euler1[i],y_real[i],y_euler1[i]))