#Creating a node class that contains all the parameter a node used in Fibonacci must have.

class FibonacciHeap:

    #Properties/Variables/Pointers of Fibonacci Heap
    rootList = None
    minNode = None
    totalNodes = 0



    # Based on the parameters present in pg 480 of Introduction to Algorithms (Cormen)
    class Node:
        def __init__(self,x):
            self.x = x
            self.degree = 0
            self.parent = self.child = self.left = self.right = None
            self.mark = False

    # Inserting a new node into a Fibonacci Heap
    def insert(self,x):
        # Creating a Fibonacci Node ( A Fibonacci Heap )
        n = self.Node(x)
        # Making the two pointers point to itself
        n.left = n.right = n
        # Concatenate the root list containing x with root list H
        self.mergeNewNodeWithRootList(n)
        if ( self.minNode is None or n.x < self.minNode.x ):
            self.minNode = n
        self.totalNodes += 1

    # Finding the minimum node
    def findMinNode(self):
        return self.minNode

    # Uniting two Fibonacci Heaps
    def union(self,h2):
        # Creating a new Fibonacci Heap
        h1 = FibonacciHeap()
        # Assigning the properties of the current Fibonacci Heap to the newly created Fibonacci Heap
        h1.rootList = self.rootList
        h1.minNode = self.minNode
        # Concatenate the root list of h2 with the root list of h1
        self.mergeRootListWithExistingRootList(h1,h2)
        # Update minNode if required
        if ( h1.minNode is None or (h2.minNode is not None and h2.minNode.x < h1.minNode.x) ):
            h1.minNode = h2.minNode
        # Update total Nodes
        h1.totalNodes = self.totalNodes + h2.totalNodes
        # return the Fibonacci Heap
        return h1




    def mergeRootListWithExistingRootList(self,h1,h2):
        tempStorage = h2.rootList.left
        h2.rootList.left = h1.rootList.left
        h1.rootList.left.right = h2.rootList
        h1.rootList.left = tempStorage
        h1.rootList.left.right = h1.rootList



    def mergeNewNodeWithRootList(self,node):
        if self.rootList is None:
            self.rootList = node
        else:
            # Updating the node with values of the rootList Node and including the node to be part of the rootList
            node.right = self.rootList.right
            node.left = self.rootList
            # Note: Insertion of a node between two double-linkedList nodes
            self.rootList.right.left = node
            self.rootList.right = node






