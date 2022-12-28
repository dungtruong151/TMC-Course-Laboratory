import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 5*math.exp(-2*x)*x

def derivative_f(x):
    return 5 * np.exp(-2*x) - 10 * x * np.exp(-2*x)
def Romberg_Integration(f,x):
    h = 1
    d1 = (f(x + h) - f(x)) / h 
    while True:
        h/=2
        d2 = d1
        d1 = (f(x + h) - f(x)) / h 
        if abs(d1 - d2) < np.exp(-6):
            return d1

def Graph(f, array):
    a = []
    for i in range(len(array)):
        t = Romberg_Integration(f,array[i])
        a.append(t)
    print("The derivative of f(x) at ",array[-1]," is: ", a[-1])
    print("The true error is: ", abs(derivative_f(array[-1] - a[-1])))
    return a 


x = np.linspace(0,3,100)
a = Graph(f,x)
plt.plot(x, a)
plt.xlabel('x')
plt.ylabel('R(x)')
plt.title('Romberg Integration')
plt.show()