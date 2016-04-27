import FibonacciHeap
import matplotlib.pyplot as plt
from random import randint
import time
import numpy as np

t = []

nRange = np.arange(1,100000,1000,dtype=int)


for n in nRange:
    fibonacciHeap = FibonacciHeap.FibonacciHeap()
    for i in xrange(0,n):
        r = randint(1,1000000)
        fibonacciHeap.insert(r)
    r = randint(1,1000000)
    start_time = time.time()
    fibonacciHeap.insert(r)
    end_time = time.time()
    print "Time taken for " , n , " nodes is " , end_time - start_time , " seconds"
    t.append(end_time - start_time)

axes = plt.gca()
axes.set_ylim([0,0.001])
axes.plot(nRange,t,alpha=1 ,color='r', label="Insert -> O(1)",marker=".")
plt.xlabel('Number of Nodes in the Fibonacci Heap when the Insertion occurred')
plt.ylabel('Time in Seconds')
plt.legend(loc=2)
plt.savefig('Algorithms Report/Figures/fibonacciHeapPerformanceInsert')
#plt.show()