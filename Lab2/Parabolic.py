import math

def f(x):
    return -x**4-2*x**3-8*x**2-5*x
    #return 4*x-1.8*x**2+1.2*x**3-0.3*x**4

def x3(x0,x1,x2,count):
    a=f(x0)*(x1*x1-x2*x2)+f(x1)*(x2*x2-x0*x0)+f(x2)*(x0*x0-x1*x1)
    b=2*(f(x0)*(x1-x2)+f(x1)*(x2-x0)+f(x2)*(x0-x1))
    c=a/b
    if (count==5):
        return 0
    else:
        print("%d%25.4f%15.4f%17.4f%12.4f%18.4f%12.4f%18.4f%12.4f" % (count, x0, f(x0),x1,f(x1),x2,f(x2),c,f(c)))
        if (c<x0):
            return x3(c,x0,x1,count+1)
        if (x0<c<x1):
            return x3(x0,c,x1,count+1)
        if (x1<c<x2):
            return x3(x1,c,x2,count+1)
        if (x2<c):
            return x3(x1,x2,c,count+1)

print("%s%15s%15s%15s%15s%15s%15s%15s%15s" % ("Iteration", "x0", "f(x0)","x1","f(x1)","x2","f(x2)","x3","f(x3)"))
x3(1.75,2.0,2.5,1)