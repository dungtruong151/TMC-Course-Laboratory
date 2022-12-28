#Truong Tri Dung - ITCSIU21126
import math

'''
g(h) = f(x0 + dfx(x,y)*h, y0 + dfy(x,y)*h) = f(x0 + 2*(x0-3)*h, y0 + 2*(y0-2)*h) = (x0 + 2*(x0-3)*h - 3)**2 + (y0 + 2*(y0-2)*h - 2)**2
     = (x0 - 3)**2 * (1+2h)**2 + (y0 - 2)**2 * (1+2h)**2 = f(x0,y0) * (1+2h)**2
    
g'(h)=0 <=> h = -1/2
'''
h=-0.5

def f(x,y):
    return (x-3)**2+(y-2)**2

def dfx(x,y):
    return 2*(x-3)

def dfy(x,y):
    return 2*(y-2)

def steepest_descent_method(iteration,x,y):
    x_new = x+dfx(x,y)*h
    y_new = y+dfy(x,y)*h
    eax = abs((x_new - x)/x_new)*100
    eay = abs((y_new - y)/y_new)*100
    print("%9d%20.5f%20.5f%20.5f%20.5f%20.5f" % (iteration, x, y, f(x,y), eax, eay))
    if (eax > 1) and (eay > 1) and (iteration < 100):
        steepest_descent_method(iteration+1,x_new,y_new)
        
print("%s%20s%20s%20s%20s" % ("Iteration", "x", "y", "f(x,y)", "ea"))
x0=1
y0=1
steepest_descent_method(0,x0,y0)