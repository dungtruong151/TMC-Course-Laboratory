import math
import numpy
import matplotlib.pyplot as p

l1 = []
def calculate_cos(x):
    result=0
    prev_result=1
    i=0
    print("%s%20s" % ("Iteration", "Approximation"))
    while round(prev_result,8)!=round(result,8):
        prev_result=result
        result+=math.pow(-1,i)*math.pow(x,2*i)/math.factorial(2*i)
        l1.append(result)
        print("%9d%20.10f" % (i, result))
        i+=1

calculate_cos(0.3*math.pi)
fig = p.figure()
ax1 = fig.add_subplot(211)

ax1.plot(l1)

ax1.title.set_text("Cos(0.3*pi)")
p.show()