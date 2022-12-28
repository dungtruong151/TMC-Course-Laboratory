import math

def f(x,y):
    return (1+4*x)*math.sqrt(y)

def Adaptive_RK_method(i):
    if (i<4):
        k1 = f(x[i],y[i])
        k2 = f(x[i]+h/2,y[i]+h*k1/2)
        k3 = f(x[i]+h/2,y[i]+h*k2/2)
        k4 = f(x[i]+h,y[i]+h*k3)
        y.append(y[i]+h*(k1+2*k2+2*k3+k4)/6)
        x.append(x[i]+h)
        Adaptive_RK_method(i+1)

x = []
y = []
x.append(0.0)
y.append(1.0)
h=0.25
Adaptive_RK_method(0)
print("%s\t%s" % ("x", "y"))
for i in range(0,len(x)):
    print("%.2f\t%f " % (x[i],y[i]))
