#Truong Tri Dung - ITCSIU21126
import math

def log(x):
    switcher={
        8: 0.9030900,
        9: 0.9542425,
        11: 1.0413927,
        12: 1.0791812
    }
    return switcher.get(x,math.log10(x))
    
print("The common logarithm of 10 using linear interpolation between  log8=0.9030900  and  log12=1.0791812: ")
x0=8
x1=12
print("log10(10) = ", log(x0)+(log(x1)-log(x0))*(10-x0)/(x1-x0))
print("Error = ", abs((math.log10(10)-(log(x0)+(log(x1)-log(x0))*(10-x0)/(x1-x0)))/math.log10(10))*100, "%\n")
print("The common logarithm of 10 using linear interpolation between  log9=0.9542425  and  log11=1.0413927: ")
x0=9
x1=11
print("log10(10) = ", log(x0)+(log(x1)-log(x0))*(10-x0)/(x1-x0))
print("Error = ", abs((math.log10(10)-(log(x0)+(log(x1)-log(x0))*(10-x0)/(x1-x0)))/math.log10(10))*100, "%")