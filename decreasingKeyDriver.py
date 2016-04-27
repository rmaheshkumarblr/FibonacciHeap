import FibonacciHeap
import matplotlib.pyplot as plt
from random import randint
import time
import numpy as np

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
    deletedValue = fibonacciHeap.decreaseKey(fibonacciHeap.rootList,1)
    end_time = time.time()
    t.append(end_time - start_time)
    nRange1.append(n)
    print "Time taken for " , n , " nodes is " , end_time - start_time , " seconds"

axes = plt.gca()
axes.set_ylim([0,0.0001])

axes.plot(nRange1,t,alpha=1 ,color='r', label="Decrease Key - O(1)",marker='.')
plt.xlabel('Number of Nodes in the Fibonacci Heap at the time of Decease Key operation')
plt.ylabel('Time in Seconds')
plt.legend(loc=2)
plt.savefig('Algorithms Report/Figures/fibonacciHeapPerformanceDecreaseKey')
#plt.show()