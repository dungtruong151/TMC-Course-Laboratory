#Truong Tri Dung - ITCSIU21126
import math

def f(x):
    return -26+85*x-91*x**2+44*x**3-8*x**4+x**5

def bisection(xl,xu,xrold,count):
    es=10.0
    xrnew=(xl+xu)/2
    ea=math.fabs((xrnew-xrold)/xrnew)*100
    print("%d%29.4f%20.4f%15.4f%20.4f%27.4f" % (count, xl, xu,xrnew,f(xl)*f(xrnew),ea))
    if ea<es:
        print("The real root:")
        return xrnew
    else:
        if f(xl)*f(xrnew)<0:
            return bisection(xl,xrnew,xrnew,count+1)
        if f(xl)*f(xrnew)>0:
            return bisection(xrnew,xu,xrnew,count+1)
        if f(xl)*f(xrnew)==0:
            print("The real root:")
            return xrnew

def false_position(xl,xu,xrold,count):
    es=0.2
    xrnew=(xl*f(xu)-xu*f(xl))/(f(xu)-f(xl))
    ea=math.fabs((xrnew-xrold)/xrnew)*100
    print("%d%29.4f%20.4f%15.4f%27.4f" % (count, xl, xu,xrnew,ea))
    if ea<es:
        print("The real root:")
        return xrnew
    else:
        if f(xrnew)<0:
            return false_position(xrnew,xu,xrnew,count+1)
        if f(xrnew)>0:
            return false_position(xl,xrnew,xrnew,count+1)
        if f(xrnew)==0:
            print("The real root:")
            return xrnew

print("Using Bisection:")
print("%s%20s%20s%20s%20s%20s" % ("Iteration", "Lower", "Upper","x_midpoint","f(l)*f(mid)","E(a)"))
print(bisection(0.5,1.0,1.0,0))
print("\n")
print("Using False-position:")
print("%s%20s%20s%20s%20s" % ("Iteration", "Lower", "Upper","CurrApprox","E(a)"))
print(false_position(0.5,1.0,1.0,0))