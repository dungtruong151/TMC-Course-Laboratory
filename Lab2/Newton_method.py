import math

def f(x):
    return -x**4 - 2*x**3 - 8*x**2 - 5*x

def g(x):
    return -4*x**3 - 6*x**2 - 16*x - 5

def h(x):
    return -12*x**2 - 12*x - 16

def nextX(x):
    return x - g(x)/h(x)

x = -1
es = 1
ea= 100
iteration = 0
print("%s%20s%20s%20s%20s%20s" % ("Iteration", "x", "f(x)", "f'(x)","f''(x)", "ea"))
print("%9d%20.5f%20.5f%20.5f%20.5f%20.5f" % (iteration, x, f(x), g(x), h(x), ea))
while ea > es:
    
    x1 = nextX(x)
    ea = abs((x1 - x)/x1)*100
    x = x1
    iteration += 1
    print("%9d%20.5f%20.5f%20.5f%20.5f%20.5f" % (iteration, x, f(x), g(x), h(x), ea))