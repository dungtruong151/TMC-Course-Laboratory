#Truong Tri Dung - ITCSIU21126
import math
import numpy as np
import matplotlib.pyplot as p

def x(xd,a,b):
    a0=(b+a)/2
    a1=(b-a)/2
    return a0+a1*xd

def f(x,a,b):
    a1=(b-a)/2
    return pow(x,0.1)*(1.2-x)*(1-pow(np.e,20*(x-1)))*a1
    #return (0.2+25*x-200*pow(x,2)+675*pow(x,3)-900*pow(x,4)+400*pow(x,5))*a1

l = []
def GaussQuadra(n):
    i=0
    h=(1-0)/n
    I=0
    while (i<1):
        l.append(I)
        I=I+f(x(-0.5773502692,i,i+h),i,i+h)+f(x(0.5773502692,i,i+h),i,i+h)
        i+=h
    return I

I_true=0.602298
I_estimated=GaussQuadra(10000)
print("The integration by Gauss Quadrature: ",I_estimated)
print("The true error: ",abs(I_true-I_estimated)/I_true*100)
fig = p.figure()
ax1 = fig.add_subplot(211)
ax1.plot(l)
ax1.set_xlabel('x')
ax1.set_ylabel('I(x)')
ax1.title.set_text("Gauss Quadrature")
p.show()