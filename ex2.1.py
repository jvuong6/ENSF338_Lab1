#This program takes the coefficients of a quadratic equation and finds the roots using the quadratic formula

import sys
import math
def do_stuff():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    d = b**2 - 4*a*c
    #The error occurs when the first entered value 'a' is zero. it fails because in line 17 the program will divide by 'a', and thus zero
    #To fix this we simply add a condition that if 'a' is equal to zero, then exit the program.
    if a == 0:
        print('Value a cannot be zero to use the quadratic formula')
        exit()

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f'The solutions are: {root1}, {root2}')
    elif d == 0:
        root = -b / (2*a)
        print(f'The solution is: {root}')
    else:
        print('There are no real solutions.')
do_stuff()