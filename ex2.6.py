import sys
import math
import timeit

def pow2(n):
    
    return 2**n

n = float(sys.argv[1])

elapsed_time = timeit.timeit(lambda : pow2(10000), number=10000)
print(f'the elapsed time is {elapsed_time}')


def pow2for():
    for i in range(0, 1000):
        pow2(i)
    

elapsed_time_for = timeit.timeit(lambda : pow2for(), number=1000)
print(f'the elapsed time for the for loop is {elapsed_time_for}')

def pow2list():
    list_of_pows = [pow2(i) for i in range(0, 1000)]

elapsed_time_list = timeit.timeit(lambda : pow2list(), number=1000)
print(f'the elapsed time for the list comprehension is {elapsed_time_list}')