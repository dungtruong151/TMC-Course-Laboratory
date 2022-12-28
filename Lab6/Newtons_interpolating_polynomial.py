#Truong Tri Dung - ITCSIU21126
import math
import numpy as np
import matplotlib.pyplot as p

x=[0,1,2.5,3,4.5,5,6]
y=[2,5.4375,7.3516,7.5625,8.4453,9.1875,12]

def f(i,j):
    if (j-i==1):
        return (y[j]-y[i])/(x[j]-x[i])
    else:
        return (f(i+1,j)-f(i,j-1))/(x[j]-x[i])
    
x_needfind=3.5
for i in range(len(x)):
    if (x_needfind>=x[i]) and (x_needfind<=x[i+1]):
        index=i
        break

#Newton's interpolating polynomial zero-order
p.plot(x,y,'bo')
p.plot(x_needfind,y[index],'ro')
p.text(x_needfind-0.5,y[index]+1,'(%s,%s)'%(x_needfind,y[index]))
print("Newton's interpolating polynomial zero order (error = %f) " % (abs(f(index,index+1)*(x_needfind-x[index]))))
X=np.linspace(0,6,100)
p.legend(['Data collected','Target Point'])
p.plot(X,y[index]*np.ones(len(X)),'g-')
p.show()

#Newton's interpolating polynomial first order
index=0
min=abs(f(index,index+2)*(x_needfind-x[index])*(x_needfind-x[index+1]))
for i in range(0,len(x)-2):
    if (abs(f(i,i+2)*(x_needfind-x[i])*(x_needfind-x[i+1]))<min):
        min=abs(f(i,i+2)*(x_needfind-x[i])*(x_needfind-x[i+1]))
        index=i
p.plot(x,y,'bo')
y_needfind=y[index]+f(index,index+1)*(x_needfind-x[index])
p.plot(x_needfind,y_needfind,'ro')
p.text(x_needfind-0.5,y[index]+1,'(%s,%s)'%(x_needfind,y_needfind))
print("\nNewton's interpolating polynomial first order (error = %f) " % (min))
X=np.linspace(0,6,100)
p.legend(['Data collected','Target Point'])
p.plot(X,y[index]+f(index,index+1)*(X-x[index]),'g-')
p.show()

#Newton's interpolating polynomial second order
index=0
min=abs(f(index,index+3)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2]))
for i in range(0,len(x)-3):
    if (abs(f(i,i+3)*(x_needfind-x[i])*(x_needfind-x[i+1])*(x_needfind-x[i+2]))<min):
        min=abs(f(i,i+3)*(x_needfind-x[i])*(x_needfind-x[i+1])*(x_needfind-x[i+2]))
        index=i
p.plot(x,y,'bo')
y_needfind=y[index]+f(index,index+1)*(x_needfind-x[index])+f(index,index+2)*(x_needfind-x[index])*(x_needfind-x[index+1])
p.plot(x_needfind,y_needfind,'ro')
p.text(x_needfind-0.5,y[index]+1,'(%s,%s)'%(x_needfind,y_needfind))
print("\nNewton's interpolating polynomial second order (error = %f) " % (min))
X=np.linspace(0,6,100)
p.legend(['Data collected','Target Point'])
p.plot(X,y[index]+f(index,index+1)*(X-x[index])+f(index,index+2)*(X-x[index])*(X-x[index+1]),'g-')
p.show()

#Newton's interpolating polynomial third order
index=0
min=abs(f(index,index+4)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2])*(x_needfind-x[index+3]))
for i in range(0,len(x)-4):
    if (abs(f(i,i+4)*(x_needfind-x[i])*(x_needfind-x[i+1])*(x_needfind-x[i+2])*(x_needfind-x[i+3]))<min):
        min=abs(f(i,i+4)*(x_needfind-x[i])*(x_needfind-x[i+1])*(x_needfind-x[i+2])*(x_needfind-x[i+3]))
        index=i
p.plot(x,y,'bo')
y_needfind=y[index]+f(index,index+1)*(x_needfind-x[index])+f(index,index+2)*(x_needfind-x[index])*(x_needfind-x[index+1])+f(index,index+3)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2])
p.plot(x_needfind,y_needfind,'ro')
p.text(x_needfind-0.5,y[index]+1,'(%s,%s)'%(x_needfind,y_needfind))
print("\nNewton's interpolating polynomial third order (error = %f) " % (min))
X=np.linspace(0,6,100)
p.legend(['Data collected','Target Point'])
p.plot(X,y[index]+f(index,index+1)*(X-x[index])+f(index,index+2)*(X-x[index])*(X-x[index+1])+f(index,index+3)*(X-x[index])*(X-x[index+1])*(X-x[index+2]),'g-')
p.show()

#Newton's interpolating polynomial fourth order
index=0
min=abs(f(index,index+5)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2])*(x_needfind-x[index+3])*(x_needfind-x[index+4]))
for i in range(0,len(x)-5):
    if (abs(f(i,i+5)*(x_needfind-x[i])*(x_needfind-x[i+1])*(x_needfind-x[i+2])*(x_needfind-x[i+3])*(x_needfind-x[i+4]))<min):
        min=abs(f(i,i+5)*(x_needfind-x[i])*(x_needfind-x[i+1])*(x_needfind-x[i+2])*(x_needfind-x[i+3])*(x_needfind-x[i+4]))
        index=i
p.plot(x,y,'bo')
y_needfind=y[index]+f(index,index+1)*(x_needfind-x[index])+f(index,index+2)*(x_needfind-x[index])*(x_needfind-x[index+1])+f(index,index+3)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2])+f(index,index+4)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2])*(x_needfind-x[index+3])
p.plot(x_needfind,y_needfind,'ro')
p.text(x_needfind-0.5,y[index]+1,'(%s,%s)'%(x_needfind,y_needfind))
print("\nNewton's interpolating polynomial fourth order (error = %f) " % (min))
X=np.linspace(0,6,100)
p.legend(['Data collected','Target Point'])
p.plot(X,y[index]+f(index,index+1)*(X-x[index])+f(index,index+2)*(X-x[index])*(X-x[index+1])+f(index,index+3)*(X-x[index])*(X-x[index+1])*(X-x[index+2])+f(index,index+4)*(X-x[index])*(X-x[index+1])*(X-x[index+2])*(X-x[index+3]),'g-')
p.show()

#Newton's interpolating polynomial fifth order
index=0
min=abs(f(index,index+6)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2])*(x_needfind-x[index+3])*(x_needfind-x[index+4])*(x_needfind-x[index+5]))
for i in range(0,len(x)-6):
    if (abs(f(i,i+6)*(x_needfind-x[i])*(x_needfind-x[i+1])*(x_needfind-x[i+2])*(x_needfind-x[i+3])*(x_needfind-x[i+4])*(x_needfind-x[i+5]))<min):
        min=abs(f(i,i+6)*(x_needfind-x[i])*(x_needfind-x[i+1])*(x_needfind-x[i+2])*(x_needfind-x[i+3])*(x_needfind-x[i+4])*(x_needfind-x[i+5]))
        index=i
p.plot(x,y,'bo')
y_needfind=y[index]+f(index,index+1)*(x_needfind-x[index])+f(index,index+2)*(x_needfind-x[index])*(x_needfind-x[index+1])+f(index,index+3)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2])+f(index,index+4)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2])*(x_needfind-x[index+3])+f(index,index+5)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2])*(x_needfind-x[index+3])*(x_needfind-x[index+4])
p.plot(x_needfind,y_needfind,'ro')
p.text(x_needfind-0.5,y[index]+1,'(%s,%s)'%(x_needfind,y_needfind))
print("\nNewton's interpolating polynomial fifth order (error = %f) " % (min))
X=np.linspace(0,6,100)
p.legend(['Data collected','Target Point'])
p.plot(X,y[index]+f(index,index+1)*(X-x[index])+f(index,index+2)*(X-x[index])*(X-x[index+1])+f(index,index+3)*(X-x[index])*(X-x[index+1])*(X-x[index+2])+f(index,index+4)*(X-x[index])*(X-x[index+1])*(X-x[index+2])*(X-x[index+3])+f(index,index+5)*(X-x[index])*(X-x[index+1])*(X-x[index+2])*(X-x[index+3])*(X-x[index+4]),'g-')
p.show()

#Newton's interpolating polynomial sixth order
index=0
p.plot(x,y,'bo')
y_needfind=y[index]+f(index,index+1)*(x_needfind-x[index])+f(index,index+2)*(x_needfind-x[index])*(x_needfind-x[index+1])+f(index,index+3)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2])+f(index,index+4)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2])*(x_needfind-x[index+3])+f(index,index+5)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2])*(x_needfind-x[index+3])*(x_needfind-x[index+4])+f(index,index+6)*(x_needfind-x[index])*(x_needfind-x[index+1])*(x_needfind-x[index+2])*(x_needfind-x[index+3])*(x_needfind-x[index+4])*(x_needfind-x[index+5])
p.plot(x_needfind,y_needfind,'ro')
p.text(x_needfind-0.5,y[index]+1,'(%s,%s)'%(x_needfind,y_needfind))
print("\nNewton's interpolating polynomial sixth order (Highest order)")
X=np.linspace(0,6,100)
p.legend(['Data collected','Target Point'])
p.plot(X,y[index]+f(index,index+1)*(X-x[index])+f(index,index+2)*(X-x[index])*(X-x[index+1])+f(index,index+3)*(X-x[index])*(X-x[index+1])*(X-x[index+2])+f(index,index+4)*(X-x[index])*(X-x[index+1])*(X-x[index+2])*(X-x[index+3])+f(index,index+5)*(X-x[index])*(X-x[index+1])*(X-x[index+2])*(X-x[index+3])*(X-x[index+4])+f(index,index+6)*(X-x[index])*(X-x[index+1])*(X-x[index+2])*(X-x[index+3])*(X-x[index+4])*(X-x[index+5]),'g-')
p.show()