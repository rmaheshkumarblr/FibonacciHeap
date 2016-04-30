import FibonacciHeap
import matplotlib.pyplot as plt
from random import randint
import time
import numpy as np

nRange = np.arange(1,100000,1000,dtype=int)
t = []


for n in nRange:
    fibonacciHeap = FibonacciHeap.FibonacciHeap()
    for i in xrange(0,n):
        r = randint(1,1000000)
        fibonacciHeap.insert(r)
    fibonacciHeap2 = FibonacciHeap.FibonacciHeap()
    for i in xrange(0,n):
        r = randint(1,1000000)
        fibonacciHeap2.insert(r)

    start_time = time.time()
    #while fibonacciHeap.totalNodes > 0:
    fibonacciHeap.union(fibonacciHeap2)
    end_time = time.time()
    t.append(end_time - start_time)
    print "Time taken for " , n , " nodes is " , end_time - start_time , " seconds"
axes = plt.gca()
axes.set_ylim([0,0.0001])
upperBound = [0.00003 ] * len(t)
axes.plot(nRange,upperBound,alpha=1 ,color='b',label="Upper Bound: 0.00003")
axes.plot(nRange,t,alpha=1 ,color='r', label="Union runtime - O(1)",marker=".")
plt.xlabel('Number of Nodes in both the Fibonacci Heap at the time of reunion')
plt.ylabel('Time in Seconds')
plt.legend(loc=2)
plt.savefig('Algorithms Report/Figures/fibonacciHeapPerformanceUnion')
#plt.show()