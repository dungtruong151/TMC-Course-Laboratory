#Truong Tri Dung - ITCSIU21126
import math

from numpy import fix

def fx(x,y):
    return (x*x-y)/(5*y)
def fy(x,y):
    return -x*x+x+0.75

def fixed_point(x,y,count):
    es=0.02
    eax=math.fabs((fx(x,y)-x)/fx(x,y))*100
    x=fx(x,y)
    eay=math.fabs((fy(x,y)-y)/fy(x,y))*100
    print("%d%30f%25f" % (count, x, fy(x,y)))
    if (eax<es) and (eay<es):
        print("(%f,%f)"%(x,fy(x,y)))
        return 0
    else:
        fixed_point(x,fy(x,y),count+1)

def dux(x,y):
    return 2*x-1
def duy(x,y):
    return 1
def dvx(x,y):
    return 2*x-5*y
def dvy(x,y):
    return -1-5*x
def u(x,y):
    return x*x-x-0.75+y
def v(x,y):
    return x*x-y-5*x*y

def Newton_Raphson(x,y,count):
    determinant=dux(x,y)*dvy(x,y)-duy(x,y)*dvx(x,y)
    es=0.2
    xnew=x-(u(x,y)*dvy(x,y)-v(x,y)*duy(x,y))/determinant
    eax=math.fabs((xnew-x)/xnew)
    ynew=y-(v(x,y)*dux(x,y)-u(x,y)*dvx(x,y))/determinant
    eay=math.fabs((ynew-y)/ynew)
    print("%d%30f%25f%25f%25f" % (count, xnew,ynew, eax, eay))
    if (eax<es) and (eay<es):
        print("(%f,%f)"%(xnew,ynew))
        return 0
    else:
        Newton_Raphson(xnew,ynew,count+1)

print("Using Fixed-point iteration:")
print("%s%20s%25s" % ("Iteration", "xi", "yi"))
fixed_point(1.2,1.2,1)
print("\n")
print("Using Newton-Raphson:")
print("%s%20s%20s%40s%30s" % ("Iteration", "xi", "yi","RelativeApproxErrorX","RelativeApproxErrorY"))
Newton_Raphson(1.2,1.2,0)