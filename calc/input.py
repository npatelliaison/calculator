from common import *

x = int(input("Please enter First numbers: "))
y = int(input("Please enter second number: "))
z = int(input("Which operation: "))

if (z == 1):
    add(x, y)
elif (z == 2):
    sub(x, y)
elif (z == 3):
    multiply(x, y)
else:
    divide(x, y)

'''
# def math(z):
options =  {
            1: add(x, y),
            2: sub(x, y),
            3: multiply(x, y),
            4: divide(40, 10),
            }
'''