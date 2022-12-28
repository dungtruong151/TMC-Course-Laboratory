#Truong Tri Dung - ITCSIU21126
import math

def jacobi(k):
    es=0.02
    for i in range(n):
        sum=0
        for j in range(n):
            if i!=j:
                sum=sum+a[i][j]*x[j]
        xnew[i]=1/a[i][i]*(b[i]-sum)
    ea=[0,0,0]
    for i in range(n):
        ea[i]=math.fabs((xnew[i]-x[i])/xnew[i])
    print("%d%20.4f%20.4f%20.4f%20.4f%20.4f%20.4f\n" % (k,x[0],x[1],x[2],ea[0],ea[1],ea[2]))
    if max(ea)>es:
        x[:]=xnew[:]
        return jacobi(k+1)

def gauss_seidel(k):
    for i in range(n):
        sum=0
        for j in range(i):
            sum=sum+a[i][j]*xnew[j]
        if i+1<n:
            sum1=0
            for j in range(i+1,n):
                sum1=sum1+a[i][j]*x[j]
        xnew[i]=1/a[i][i]*(b[i]-sum-sum1)
    ea=[0,0,0]
    for i in range(n):
        ea[i]=math.fabs((xnew[i]-x[i])/xnew[i])
    print("%d%20.4f%20.4f%20.4f%20.4f%20.4f%20.4f\n" % (k,xnew[0],xnew[1],xnew[2],ea[0],ea[1],ea[2]))
    if k<3:
        x[:]=xnew[:]
        return gauss_seidel(k+1)

a=[[4,1,-1],[2,7,1],[1,-3,12]]
b=[3,19,31]
n=len(a)

print("Using Jacobi:")
print("%s%11s%20s%20s%30s" % ("Iteration", "x1", "x2","x3","E(a)"))
x=[0,0,0]
xnew=[0,0,0]
jacobi(0)
print("\n")
print("Using Gauss-Seidel:")
print("%s%11s%20s%20s%30s" % ("Iteration", "x1", "x2","x3","E(a)"))
x=[0,0,0]
xnew=[0,0,0]
gauss_seidel(1)