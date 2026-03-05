# Folder 10: Video - 11 : Timing your code with python

import time

def powers(limit):
    return [x**2 for x in range(limit)]

print(powers(5)) # [0, 1, 4, 9, 16]

start = time.time() # current time (no. of seconds passwes since 1970)

powers(50000000)
end = time.time()

print(end-start)

def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end-start)

def powers(limit):
    return [x**2 for x in range(limit)]

measure_runtime(lambda: powers(500000))

import timeit

print(timeit.timeit("[x ** 2 for x in range(10)]"))

