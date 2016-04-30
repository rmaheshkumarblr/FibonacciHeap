import FibonacciHeap
import matplotlib.pyplot as plt
from random import randint
import time
import numpy as np

range1 = np.arange(1,30000,100,dtype=int)
nRange = range1
t = []
n = 0
nRange1 = []
fibonacciHeap = FibonacciHeap.FibonacciHeap()
for i in xrange(0,len(nRange)):
    overallTime = 0
    r = randint(1,10)
    for j in xrange(0,nRange[i]):
        n += 1
        start_time = time.time()
        fibonacciHeap.insert(r)
        end_time = time.time()
        overallTime += (end_time - start_time)
    start_time = time.time()
    fibonacciHeap.decreaseKey(fibonacciHeap.rootList,1)
    end_time = time.time()
    overallTime +=  (end_time - start_time)
    if ( overallTime/nRange[i] <= 0.00001 ):
        t.append(overallTime/nRange[i])
        nRange1.append(n)
    print "Time taken for " , n , " nodes is " , end_time - start_time , " seconds"


axes = plt.gca()
axes.set_ylim([0.000001,0.0001])
upperBound = [0.00001 ] * len(t)
axes.plot(nRange1,upperBound,alpha=1 ,color='b',label="Upper Bound: 0.00001")
axes.plot(nRange1,t,alpha=1 ,color='r', label="Decrease Key - O(1)",marker='.')
plt.xlabel('Number of Nodes in the Fibonacci Heap at the time of Decease Key operation')
plt.ylabel('Time in Seconds')
plt.legend(loc=4)
plt.yscale('log')
plt.xscale('log')
plt.savefig('Algorithms Report/Figures/fibonacciHeapPerformanceDecreaseKey')
#plt.show()