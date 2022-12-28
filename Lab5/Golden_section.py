#Truong Tri Dung - ITCSIU21126
import math
import matplotlib.pyplot as p

def f(x):
    return 4*x-1.8*x**2+1.2*x**3-0.3*x**4

l1 = []
l2 = []
def golden_section(iteration,xl,xu):
    r=(math.sqrt(5)-1)/2
    d=r*(xu-xl)
    x1=xl+d
    x2=xu-d
    interval=xl-xu
    if (f(x1)<f(x2)):
        xu=x1
        opt=x2
    else:
        xl=x2
        opt=x1
    ea=math.fabs((1-r)*interval*100/opt)
    print("%9d%15.5f%15.5f%15.5f%15.5f%15.5f%15.5f%15.5f%15.5f%15.5f%15.5f%15.5f" % (iteration,xl,f(xl),x2, f(x2),x1,f(x1),xu,f(xu),d,opt,ea))
    l1.append(opt)
    l2.append(f(opt))
    if (ea > 1) and (iteration < 100):
        golden_section(iteration+1,xl,xu)
    else:
        print("(%f,%f)" % (opt,f(opt)))

print("%s%15s%15s%15s%15s%15s%15s%15s%15s%15s%15s%15s" % ("Iteration", "xl", "f(xl)","x2" ,"f(x2)","x1","f(x1)","xu","f(xu)","d", "Opt","ea"))
golden_section(0,2,4)
print("Text(0.5, 1.0, 'Golden section search')")
fig = p.figure()
ax1 = fig.add_subplot(211)

ax1.plot(l1,l2)

ax1.title.set_text("Golden section search")
p.show()