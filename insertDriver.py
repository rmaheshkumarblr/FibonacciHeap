import FibonacciHeap
import matplotlib.pyplot as plt
from random import randint
import time

nRange = [1, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
t = []
r = randint(1,1000)

for n in nRange:
    start_time = time.time()
    fibonacciHeap = FibonacciHeap.FibonacciHeap()
    for i in xrange(0,n):
        fibonacciHeap.insert(r)
    end_time = time.time()
    t.append(end_time - start_time)
    print "Time taken for " , n , " nodes is " , end_time - start_time , " seconds"

plt.plot(nRange,t)
plt.show()