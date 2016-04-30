import FibonacciHeap
import matplotlib.pyplot as plt
from random import randint
import time
import numpy as np

lowerBoundConstant = 0.0000008
upperBoundConstant = 0.0000015

nRange = np.arange(1,30000,100,dtype=int)

t = []
n = 0
nRange1 = []
fibonacciHeap = FibonacciHeap.FibonacciHeap()
for i in xrange(0,len(nRange)):
    overallTime = 0
    r = randint(1,1000000)
    for j in xrange(0,nRange[i]):
        n += 1
        start_time = time.time()
        fibonacciHeap.insert(r)
        end_time = time.time()
        overallTime += (end_time - start_time)
        #while fibonacciHeap.totalNodes > 0:
    start_time = time.time()
    fibonacciHeap.deleteNode(fibonacciHeap.rootList)
    end_time = time.time()
    # print deletedValue.key
    end_time = time.time()
    overallTime +=  (end_time - start_time)
    t.append(overallTime/nRange[i])
    nRange1.append(n)
    print "Time taken for " , n , " nodes is " , overallTime/nRange[i] , " seconds" , " - Nrange: " , nRange[i]

nRangeNPArray = np.array(nRange1)
lowerBound = lowerBoundConstant * np.log(nRangeNPArray)
upperBound = upperBoundConstant * np.log(nRangeNPArray)
axes = plt.gca()
axes.set_ylim([0.000001,0.0001])
plt.scatter(nRange1,t,alpha=1 ,color='r', label="Delete - O(lg(n)))")
plt.plot(nRange1, lowerBound, alpha=1 , label="Lower Bound (0.0000008*lg(n))")
plt.plot(nRange1, upperBound, alpha=1 , label="Upper Bound (0.0000015*lg(n))")
plt.xlabel('Number of Nodes in the Fibonacci Heap at the time of Delete Operation')
plt.ylabel('Time in Seconds')
plt.xscale('log')
plt.legend(loc=2)
plt.savefig('Algorithms Report/Figures/fibonacciHeapPerformanceDelete')
# plt.show()

