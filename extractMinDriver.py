import FibonacciHeap
import matplotlib.pyplot as plt
from random import randint
import time
import numpy as np

lowerBoundConstant = 0.0000008
upperBoundConstant = 0.0000015

nRange = np.arange(1,30000,100,dtype=int)
# range2 = range1[::-1]
# nRange = np.hstack((range1,range2))[0:250]
# print len(nRange)
# exit(0)
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
    fibonacciHeap.extractMin()
    end_time = time.time()
    overallTime +=  (end_time - start_time)

    t.append(overallTime/nRange[i])
    nRange1.append(n)

    print "Time taken for " , n , " nodes is " , overallTime/nRange[i] , " seconds" , " - Nrange: " , nRange[i]

axes = plt.gca()
nRangeNPArray = np.array(nRange1)
lowerBound = lowerBoundConstant * np.log(nRangeNPArray)
upperBound = upperBoundConstant * np.log(nRangeNPArray)
axes.set_ylim([0.000001,0.0001])
plt.scatter(nRange1,t,alpha=1 ,color='r', label="Extract-Min - O(lg(n)))")
plt.plot(nRange1, lowerBound, alpha=1 , label="Lower Bound (0.0000008*lg(n))")
plt.plot(nRange1, upperBound, alpha=1 , label="Upper Bound (0.0000015*lg(n))")
plt.xlabel('Number of Nodes in the Fibonacci Heap')
plt.ylabel('Time in Seconds')
#plt.yscale('log')
plt.xscale('log')
plt.legend(loc=2)
plt.savefig('Algorithms Report/Figures/fibonacciHeapPerformanceExtractMin1')
#plt.show()