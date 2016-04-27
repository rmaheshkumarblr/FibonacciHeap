import FibonacciHeap
import matplotlib.pyplot as plt
from random import randint
import time
import numpy as np

lowerBoundConstant = 0.012
upperBoundConstant = 0.028

range1 = np.arange(1,25000,100,dtype=int)
range2 = range1[::-1]
nRange = np.hstack((range1,range2))

t = []
n = 0
nRange1 = []
fibonacciHeap = FibonacciHeap.FibonacciHeap()
for i in xrange(0,len(nRange)):
    r = randint(1,1000000)
    for j in xrange(0,nRange[i]):
        n += 1
        fibonacciHeap.insert(r)
    start_time = time.time()
    #while fibonacciHeap.totalNodes > 0:
    extractedValue = fibonacciHeap.extractMin()
    end_time = time.time()
    t.append(end_time - start_time)
    #print extractedValue.key
    nRange1.append(n)
    print "Time taken for " , n , " nodes is " , end_time - start_time , " seconds" , " - Nrange: " , nRange[i]

nRangeNPArray = np.array(nRange1)
lowerBound = lowerBoundConstant * np.log(nRangeNPArray)
upperBound = upperBoundConstant * np.log(nRangeNPArray)
plt.plot(nRange1,t,alpha=1 ,color='r', label="Extract-Min - O(lg(n)))",marker=".")
plt.plot(nRange1, lowerBound, alpha=1 , label="Lower Bound (0.012*lg(n))")
plt.plot(nRange1, upperBound, alpha=1 , label="Upper Bound (0.028*lg(n))")
plt.xlabel('Number of Nodes in the Fibonacci Heap')
plt.ylabel('Time in Seconds')
plt.legend(loc=4)
plt.savefig('Algorithms Report/Figures/fibonacciHeapPerformanceExtractMin')
#plt.show()