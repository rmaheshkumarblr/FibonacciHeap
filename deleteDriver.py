import FibonacciHeap
import matplotlib.pyplot as plt
from random import randint
import time
import numpy as np

lowerBoundConstant = 0.1
upperBoundConstant = 0.55

nRange = [1, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
t = []


for n in nRange:
    fibonacciHeap = FibonacciHeap.FibonacciHeap()
    for i in xrange(0,n):
        r = randint(1,1000000)
        fibonacciHeap.insert(r)
    start_time = time.time()
    #while fibonacciHeap.totalNodes > 0:
    deletedValue = fibonacciHeap.deleteNode(fibonacciHeap.rootList)
    print deletedValue.key
    end_time = time.time()
    t.append(end_time - start_time)
    print "Time taken for " , n , " nodes is " , end_time - start_time , " seconds"

nRangeNPArray = np.array(nRange)
lowerBound = lowerBoundConstant * np.log(nRangeNPArray)
upperBound = upperBoundConstant * np.log(nRangeNPArray)
plt.plot(nRange,t,alpha=1 ,color='r', label="Extract-Min function runtime O(lg(n)))")
plt.plot(nRange, lowerBound, alpha=1 , label="Lower Bound (0.1)")
plt.plot(nRange, upperBound, alpha=1 , label="Upper Bound (0.55)")
plt.xlabel('Number of Nodes in the Fibonacci Heap')
plt.ylabel('Time in Seconds')
plt.legend(loc=2)

plt.show()