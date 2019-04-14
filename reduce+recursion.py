# ruduce
import functools, random
#ресурсия
print("Hello")


def privet(x):
    if x == 0:
        return 0
    else:
        print("Hello")
        privet(x-1)

def sum(x):
    if x ==0:
        return 0
    elif x==1:
        return 1
    else:
        return x + sum(x-1)



def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

from functools import reduce
print(reduce((lambda x, y: x * y), [1, 2, 3, 4, 5]) )

def Fibobacci(x):
    if x ==0:
        return 0
    elif x==1:
        return 1
    else:
        return Fibobacci(x-1) + Fibobacci(x-2)




