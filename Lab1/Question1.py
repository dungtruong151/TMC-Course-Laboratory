import math
import numpy
import matplotlib.pyplot as p

real_value = numpy.exp(-5)
l1 = []
l2 = []
def first_way(x, term) :
    result = 0
    prev_result = 0
    e_t = 0
    e_a = 0
    print("Calculation using the first way : ")
    print("%s%20s%20s%20s" % ("Iteration", "Approximation", "E_a", "E_t"))
    for n in range(0, term) : 
        prev_result = result #calculate the value
        result += math.pow(-x, n) / math.factorial(n) #formular of the first way
        l1.append(result)

        e_t = ((real_value - result) / real_value) # calculate true error
        e_a = ((result - prev_result) / result)  # calculate approximate relative error

        print("%9d%20.10f%20.10f%20.10f" % (n, result, e_a, e_t))


# Seconfd way
def second_way(x, term) :
    result = 0
    prev_result = 0
    e_t = 0
    e_a = 0
    print("Calculation using the second way : ")
    print("%s%20s%20s%20s" % ("Iteration", "Approximation", "E_a", "E_t"))
    for n in range(0, term) : 
        prev_result = result #calculate the value
        if result != 0:
            flip_result = 1 / result
        else:
            flip_result = 0
        flip_result += (math.pow(x, n) / math.factorial(n))
        result = 1/ flip_result
        l2.append(result)
        e_t = ((real_value - result) / real_value) # calculate true error
        e_a = ((result - prev_result) / result)  # calculate approximate relative error

        print("%9d%20.10f%20.10f%20.10f" % (n, result, e_a, e_t))


first_way(5,21)
print("\n")
second_way(5,21)
fig = p.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.plot(l1)

ax2.plot(l2)

ax1.title.set_text("The first way")
ax2.title.set_text("The second way")
p.show()
