#Truong Tri Dung - ITCSIU21126

import math
import numpy as np
import matplotlib.pyplot as p

'''
y = e^(-x) + C*e^(-200000x)
y(0)=0 <=> C=-1
'''
x_euler = []
y_euler = []
y_real = []

def yi(x):
    return math.exp(-x) - math.exp(-200000*x)
    #return -0.5*x**4+4*x**3-10*x**2+8.5*x+1

def f(x,y):
    return -200000*y+200000*math.exp(-x)-math.exp(-x)
    #return -2*x**3+12*x**2-20*x+8.5

def Euler_method(x,y,i):
    if (x<2.0):
        x_euler.append(x + h)
        y_euler.append(y + h*f(x,y)/(1+h*200000))
        y_real.append(yi(x+h))
        Euler_method(x_euler[i],y_euler[i],i+1)

x_euler.append(0.0)
y_euler.append(0.0)
y_real.append(0.0)
h = 0.1
Euler_method(x_euler[0],y_euler[0],1)

print("%s\t%s\t\t%s" % ("x", "y_real", "y_euler"))
for i in range(0,len(x_euler)):
    print("%.1f\t%f\t%f " % (x_euler[i],y_real[i],y_euler[i]))

p.plot(x_euler,y_euler,'bo')
p.plot(x_euler,y_real,'ro')
p.legend(['euler','real'])
p.show()