#Truong Tri Dung - ITCSIU21126
import math

def dfa(x,a,b):
    return x*math.pow(math.e,b*x)
    #return 1-math.pow(math.e,-b*x)

def dfb(x,a,b):
    return a*x*x*math.pow(math.e,b*x)
    #return a*x*math.pow(math.e,-b*x)

def f(x,a,b):
    return a*x*math.pow(math.e,b*x)
    #return a*(1-math.pow(math.e,-b*x))

x=[0.1,0.2,0.4,0.6,0.9,1.3,1.5,1.7,1.8]
#x=[0.25,0.75,1.25,1.75,2.25]
y=[0.75,1.25,1.45,1.25,0.85,0.55,0.35,0.28,0.18]
#y=[0.28,0.57,0.68,0.74,0.79]
z=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
#z=[[0,0],[0,0],[0,0],[0,0],[0,0]]
zt=[[0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0]]
#zt=[[0,0,0,0,0],[0,0,0,0,0]]
n=len(x)
multiply=[[0,0],[0,0]]
inverse=[[0,0],[0,0]]

for j in range(n):
    z[j][0]=dfa(x[j],1,1)
    
for j in range(n):
    z[j][1]=dfb(x[j],1,1)

print("[Z]:")
for i in range(n):
    for j in range(2):
        print("%10.4f" % z[i][j],end=" ")
    print()

for i in range(2):
    for j in range(n):
        zt[i][j]=z[j][i]

print("\n[ZT]:")
for i in range(2):
    for j in range(n):
        print("%10.4f" % zt[i][j],end=" ")
    print()

for i in range(2):
    for j in range(2):
        for k in range(n):
            multiply[i][j]=multiply[i][j]+zt[i][k]*z[k][j]

print("\n[ZT][Z]:")
for i in range(2):
    for j in range(2):
        print("%10.4f" % multiply[i][j],end=" ")
    print()

inverse[0][0]=multiply[1][1]/(multiply[0][0]*multiply[1][1]-multiply[0][1]*multiply[1][0])
inverse[0][1]=-multiply[0][1]/(multiply[0][0]*multiply[1][1]-multiply[0][1]*multiply[1][0])
inverse[1][0]=-multiply[1][0]/(multiply[0][0]*multiply[1][1]-multiply[0][1]*multiply[1][0])
inverse[1][1]=multiply[0][0]/(multiply[0][0]*multiply[1][1]-multiply[0][1]*multiply[1][0])

print("\n[ZT][Z]-1:")
for i in range(2):
    for j in range(2):
        print("%10.4f" % inverse[i][j],end=" ")
    print()

d=[0,0,0,0,0,0,0,0,0]
for i in range(n):
    d[i]=y[i]-f(x[i],1,1)

print("\n[D]:")
for i in range(n):
    print("%10.4f" % d[i])

dzt=[0,0]
for i in range(2):
    for j in range(n):
        dzt[i]=dzt[i]+d[j]*zt[i][j]

print("\n[D][ZT]:")
for i in range(2):
    print("%10.4f" % dzt[i])    

deltaA=[0,0]
for i in range(2):
    for j in range(2):
        deltaA[i]=deltaA[i]+inverse[i][j]*dzt[j]

print("\n[A]:")
for i in range(2):
    print("%10.4f" % deltaA[i])

print("\n[Result]:")
for i in range(2):
    print("%10.4f" % (1+deltaA[i]))