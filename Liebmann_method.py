import numpy as np

def T0j(j):
    new = (2*T[1][j] + T[0][j+1] + T[0][j-1])/4
    T[0][j] = 1.2*new + (1-1.2)*T[0][j]
    return T[0][j]

def Tij(i,j):
    new = (T[i-1][j] + T[i][j+1] + T[i][j-1] + T[i+1][j])/4
    T[i][j] = 1.2*new + (1-1.2)*T[i][j]
    return T[i][j]

def Liebmann_method(n):
    for i in range(0,5):
        for j in range(0,5):
            Told[i][j] = T[i][j]

    for j in range(1,4):
        T0j(j)

    for i in range(1,4):
        for j in range(1,4):
            Tij(i,j)

    print("Iteration %d:" % (n))
    for i in range(0,4):
        for j in range(1,4):
            print("T[%d][%d] = %.5f" % (i,j,T[i][j]), end="\t")
            if (T[i][j] != 0):
                ea[i][j] = abs((T[i][j] - Told[i][j])/T[i][j])*100
        print()
    
    print("Error: %.5f" % np.max(ea))

    if (np.max(ea) > 1):
        Liebmann_method(n+1)

T = [[0, 0, 0, 0, 150], 
    [0, 0, 0, 0, 150], 
    [0, 0, 0, 0, 150], 
    [0, 0, 0, 0, 150], 
    [50, 50, 50, 50, 50]]
Told = [[0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]]
ea = [[0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0]]

Liebmann_method(1)