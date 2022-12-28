#Truong Tri Dung - ITCSIU21126
import math

def f(x):
    return -x**2+8*x-12

def g(x):
    return -2*x+8

def h(x):
    return -2

def newton_method(iteration,x):
    x_new = x-g(x)/h(x)
    ea = abs((x_new - x)/x_new)*100
    print("%9d%20.5f%20.5f%20.5f%20.5f%20.5f" % (iteration, x, f(x), g(x), h(x), ea))
    if (ea > 1) and (iteration < 100):
        newton_method(iteration+1,x_new)
        

print("%s%20s%20s%20s%20s%20s" % ("Iteration", "x", "f(x)", "f'(x)","f''(x)", "ea"))
x0=-4
newton_method(0,x0)