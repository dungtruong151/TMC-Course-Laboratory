import math

#đạo hàm bậc n của f(x)
def Derivative(x,n):
    return math.pow(-1,n)*math.factorial(n+1)*math.pow(x,-(n+2))

def Taylor(x,base):
    print("%5s%20s" % ("Order", "Taylor Series"))
    result=0
    for i in range(5):
        result+=Derivative(base,i)*math.pow(x-base,i)/math.factorial(i)
        print("%5d%20.10f" % (i, result))
    return result

x=int(input("Enter x: "))
if x>0:
    trunc_error=math.fabs(Taylor(x,x+1)-Derivative(x,0))
else:
    trunc_error=math.fabs(Taylor(x,x-1)-Derivative(x,0))
print("\nTruncation errors: %.10f" % trunc_error)