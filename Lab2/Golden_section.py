import math as m
import numpy
import matplotlib.pyplot as p

def sign(x):
    if x < 0: 
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def f(x):
    return -(x**4) - 2*(x**3) - 8*x*x - 5*x;

xl = -2
xu = 1
d = ((m.sqrt(5) - 1) / 2) * (xu - xl)
x1 = xl + d
x2 = xu - d
ea = 100
es = 1
cnt = 0
print("%s%5s%5s%5s%5s%5s%5s%5s%5s%5s" % ("\nIteration", "xl", "f(xl)", "x2", "f(x2)", "x1", "f(x1)", "xu", "f(xu)", "d"))
cnt +=1
while (ea >= es) :
    if f(x2) > f(x1):
        xu = x1
        x1 = x2
        d = ((m.sqrt(5) - 1) / 2) * (xu - xl)
        ea = abs(((xu-d) - x2)*100 / (xu-d))
        x2 = xu - d
        print("\n%d%20.4f%20.4f%20.4f%20.4f%20.4f%20.4f%20.4f%20.4f%20.4f" % (cnt, xl, f(xl), x2, f(x2), x1, f(x1), xu, f(xu), d))
    elif f(x2) < f(x1):
        xl = x2
        x2 = x1
        d = ((m.sqrt(5) - 1) / 2) * (xu - xl)
        ea = abs(((xl+d) - x1)*100 / (xl+d))
        x1 = xl + d
        print("\n%d%20.4f%20.4f%20.4f%20.4f%20.4f%20.4f%20.4f%20.4f%20.4f" % (cnt, xl, f(xl), x2, f(x2), x1, f(x1), xu, f(xu), d))
    
    cnt += 1
print("The real root:\n%.6f\n" % (x2))