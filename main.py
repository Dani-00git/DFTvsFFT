# This is a sample Python script.
import math
import numpy as np
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def DFT(x):
    N0 = len(x)
    n = np.arange(N0)
    k = n.reshape((N0,1))
    e = np.exp(-2j*np.pi*k*n/N0)
    X = np.dot(e, x)
    return X

def FFT(x):
    n = len(x)
    l=n
    while l%2 == 0:
        l/=2
    if l!=1: return -1
    if n==1:return x
    Re = math.cos(2*math.pi/n)
    Im = math.sin(2*math.pi/n)
    if Re<0.000001: Re=0
    if Im<0.000001: Im=0
    Wn=complex(Re, Im)
    W=1
    xp=[]
    xd=[]
    i=0
    for j in x:
        if i%2 == 0:
            xp.append(x[i])
        else:
            xd.append(x[i])
        i=i+1
    Xo = FFT(xp)
    X1 = FFT(xd)
    X = np.zeros((n), dtype=np.complex_)
    for k in range(int(n/2)):
        X[k] = Xo[k]+W*X1[k]
        X[k+int(n/2)] = Xo[k]-W*X1[k]
        W=W*Wn
    return X

def print_hi(name):
    x = np.random.randint(0,100,512)
    print(DFT(x))
    print(FFT(x))
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
