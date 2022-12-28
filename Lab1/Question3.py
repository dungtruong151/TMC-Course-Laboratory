import math

x=0.5
x0=1.0
exact_value=math.pow(x,4)*math.exp(-3*math.pow(x,2))
approximate_value=math.exp(-3)+(4*math.exp(-3)-6*math.exp(-3))*(x-x0)
print("The exact value of the function: \t%10.10f" % exact_value)
print("The approximate value of the function: \t%10.10f" % approximate_value)
print("Comparision: \t%10.10f" % (exact_value-approximate_value))