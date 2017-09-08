# -*- coding: utf-8 -*
import sys
sys.setrecursionlimit(1005)
def power2(n):
    if n == 1:
        return [2]
    arr = power2(n-1)
    reszta = 0
    for i in range(0, len(arr) - 1):
        if(arr[i] * 2 + reszta >= 10):
            arr[i] = (arr[i] * 2 + reszta) % 10
            reszta = 1
        else:
            arr[i] = (arr[i] * 2 + reszta)
            reszta = 0
    if(arr[-1] * 2 + reszta >= 10):
        arr.append(1)
        arr[-2] = (arr[-2] * 2 + reszta) % 10
    else:
        arr[-1] = arr[-1] * 2 + reszta
    return arr

sum(power2(1000))
