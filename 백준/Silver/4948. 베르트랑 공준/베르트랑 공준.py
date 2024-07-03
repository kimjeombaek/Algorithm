from math import *

def prime_number(n):
    sieve= [True] * n
    m = int(sqrt(n))
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

while 1:
    n=int(input())
    if n==0:break
    li=prime_number(2*n+1)
    print(len([i for i in li if i>n]))

