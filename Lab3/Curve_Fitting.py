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
n=len(x)

def Curve_Fitting(iteration,a,b):
    z=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    #z=[[0,0],[0,0],[0,0],[0,0],[0,0]]
    zt=[[0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,0]]
    #zt=[[0,0,0,0,0],[0,0,0,0,0]]   
    multiply=[[0,0],[0,0]]
    inverse=[[0,0],[0,0]]

    for j in range(n):
        z[j][0]=dfa(x[j],a,b)
        
    for j in range(n):
        z[j][1]=dfb(x[j],a,b)

    for i in range(2):
        for j in range(n):
            zt[i][j]=z[j][i]

    for i in range(2):
        for j in range(2):
            for k in range(n):
                multiply[i][j]=multiply[i][j]+zt[i][k]*z[k][j]

    inverse[0][0]=multiply[1][1]/(multiply[0][0]*multiply[1][1]-multiply[0][1]*multiply[1][0])
    inverse[0][1]=-multiply[0][1]/(multiply[0][0]*multiply[1][1]-multiply[0][1]*multiply[1][0])
    inverse[1][0]=-multiply[1][0]/(multiply[0][0]*multiply[1][1]-multiply[0][1]*multiply[1][0])
    inverse[1][1]=multiply[0][0]/(multiply[0][0]*multiply[1][1]-multiply[0][1]*multiply[1][0])

    d=[0,0,0,0,0,0,0,0,0,]
    for i in range(n):
        d[i]=y[i]-f(x[i],a,b)

    dzt=[0,0]
    for i in range(2):
        for j in range(n):
            dzt[i]=dzt[i]+d[j]*zt[i][j]

    deltaA=[0,0]
    for i in range(2):
        for j in range(2):
            deltaA[i]=deltaA[i]+inverse[i][j]*dzt[j]

    eaa=math.fabs(deltaA[0]/(a+deltaA[0]))
    eab=math.fabs(deltaA[1]/(b+deltaA[1]))
    print("%d%20.4f%20.4f%20.4f%20.4f%20.4f%20.4f\n" % (iteration,a,b,a+deltaA[0],b+deltaA[1],eaa,eab))
    if (eaa>0.0001 or eab>0.0001):
        return Curve_Fitting(iteration+1,a+deltaA[0],b+deltaA[1])

print("%s%11s%20s%20s%20s%30s" % ("Iteration", "a", "b","a_new","b_new","E(a)"))
Curve_Fitting(1, 1, 1)