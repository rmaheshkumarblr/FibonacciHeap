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
    def Insert(self,x):
        # Creating a Fibonacci Node ( A Fibonacci Heap )
        n = self.Node(x)
        # Making the two pointers point to itself
        n.left = n.right = n
        # Concatenate the root list containing x with root list H
        self.mergeWithRootList(n)
        if ( self.minNode is None or n.x < self.minNode.x ):
            self.minNode = n
        self.totalNodes += 1

    # Finding the minimum node
    def findMinNode(self):
        return self.minNode


    def mergeWithRootList(self,node):
        if self.rootList is None:
            self.rootList = node
        else:
            # Updating the node with values of the rootList Node and including the node to be part of the rootList
            node.right = self.rootList.right
            node.left = self.rootList
            # Note: Insertion of a node between two double-linkedList nodes
            self.rootList.right.left = node
            self.rootList.right = node






