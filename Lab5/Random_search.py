#Truong Tri Dung - ITCSIU21126
import math
import random
import matplotlib.pyplot as p

def f(x,y):
    return 3.5*x+2*y+x**2-x**4-2*x*y-y**2

def random_search(iteration,f_old,ea):
    x=random.uniform(-2,2)
    y=random.uniform(-2,2)
    if (f(x,y)>f_old):
        ea=math.fabs((1-f(x,y)/f_old)*100)
        print("%9d%15.5f%15.5f%15.5f%15.5f%15.5f" % (iteration,x,y,f(x,y),f_old,ea))
        if (ea > 1):
            random_search(iteration+1,f(x,y),ea)
        else:
            print("(%f,%f)=%f" % (x,y,f(x,y)))
    else: 
        print("%9d%15.5f%15.5f%15.5f%15.5f%15.5f" % (iteration,x,y,f(x,y),f_old,ea))
        random_search(iteration+1,f_old,ea)

print("%s%15s%15s%15s%15s%15s" % ("Iteration", "x","y" ,"f(x,y)_new","f(x,y)_old","ea"))
x=random.uniform(-2,2)
y=random.uniform(-2,2)
print("%9d%15.5f%15.5f%15.5f" % (0,x,y,f(x,y)))
random_search(1,f(x,y),100)