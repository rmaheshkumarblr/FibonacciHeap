import unittest

#Creating a node class that contains all the parameter a node used in Fibonacci must have.

class FibonacciHeap:

    #Properties/Variables/Pointers of Fibonacci Heap
    rootList = None
    minNode = None
    totalNodes = 0



    # Based on the parameters present in pg 480 of Introduction to Algorithms (Cormen)
    class Node:
        def __init__(self,key):
            self.key = key
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
        if ( self.minNode is None or n.key < self.minNode.key ):
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
        if ( h1.minNode is None or (h2.minNode is not None and h2.minNode.key < h1.minNode.key) ):
            h1.minNode = h2.minNode
        # Update total Nodes
        h1.totalNodes = self.totalNodes + h2.totalNodes
        # return the Fibonacci Heap
        return h1

    # Extracting the Minimum Node
    def extractMin(self):
        z = self.minNode
        if ( z is not None ):
            if z.child is not None:
                # Get children of the of the minNode
                children = self.iterateNodeDoubleLinkList(z.child)
                # Add the node's children to the root list of H
                for x in xrange(0,len(children)):
                    self.mergeNewNodeWithRootList(children[x])
                    children[x].parent = None
            # Remove z from the root list of H
            self.removeFromRootList(z)
            # Updating the minNode with the smallest value
            if z == z.right: # No other elements present
                self.minNode = None
            else:
                self.minNode = z.right
                # Need to find the actual min node hence use consolidate
                self.consolidate()
            self.totalNodes -= 1
        return z

    # Reduce number of trees in the Fibonacci Heap is consolidating the root list of H
    def consolidate(self):
        # Create an array with Null value - Size is same as the total number of Nodes.
        A = [None] * self.totalNodes
        # Get all the nodes in the root list
        rootListNodes = self.iterateNodeDoubleLinkList(self.rootList)
        for w in xrange(0, len(rootListNodes)):
            #print  "Intermediate Root List: " , [x.key for x in fibonacciHeap.iterateNodeDoubleLinkList(self.rootList)]
            x = rootListNodes[w]
            d = x.degree
            while A[d] is not None:
                y = A[d]  # Check for multiple nodes with the same degree
                if x.key > y.key:
                    temp = x
                    x = y
                    y = temp
                self.heapLink(y,x)
                A[d] = None
                d += 1
            A[d] = x
        #Assuming the minNode to be null for now.
        self.minNode = None
        for i in xrange(0,len(A)):
            if A[i] is not None:
                if self.minNode is None or A[i].key < self.minNode.key:
                    self.minNode = A[i]

    # Remove node y from the rootList and add it is a child to x and maintain the double linked list
    def heapLink(self,y,x):
        self.removeFromRootList(y)
        y.left = y.right = y # Making the node independent
        self.mergeWithChild(x,y) # Merge y with the child of x
        x.degree += 1
        y.parent = x
        y.mark = False

    # Remove a node from the double linked root list of H
    def removeFromRootList(self,node):
        if node == self.rootList:
            self.rootList = node.right
        node.left.right = node.right
        node.right.left = node.left

    # Iterating over the Double Linked List
    def iterateNodeDoubleLinkList(self,node):
        if node is None:
            return None
        else:
            startNode = node
            levelList = []
            while True:
                levelList.append(node)
                node = node.right
                if node == startNode:
                    break;
        return levelList



    # Joining two Double Linked Root List
    def mergeRootListWithExistingRootList(self,h1,h2):
        tempStorage = h2.rootList.left
        h2.rootList.left = h1.rootList.left
        h1.rootList.left.right = h2.rootList
        h1.rootList.left = tempStorage
        h1.rootList.left.right = h1.rootList


    # Joining a Node to a Double Linked Root List
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

    # Joining a Node to the child of a given parent node
    def mergeWithChild(self,parent,node):
        if parent.child is None: # If parent has no child initially
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node

    # Decreasing a key and deleting a node
    def decreaseKey(self,x,k):
        if k > x.key :
            return None # New key is greater than current key
        x.key = k
        y = x.parent
        if y is not None and x.key < y.key:
            self.cut(x,y)
            self.cascadingCut(y)
        if x.key < self.minNode.key:
            self.minNode = x

    # If child node was smaller than its parent after the change in decreaseKey then we cut the child and bring it to the root list
    def cut(self,x,y):
        self.removeFromChildList(y,x)
        y.degree -= 1
        self.mergeNewNodeWithRootList(x)
        x.parent = None
        x.mark = False

    # Remove a node x from it's parent y
    def removeFromChildList(self,parent,node):
        if parent.child == parent.child.right: # Only one child exists
            parent.child = None
        elif parent.child == node:
            parent.child = node.right
            node.right.parent = parent
        node.left.right = node.right
        node.right.left = node.left

    # Cascading cut of parent node
    def cascadingCut(self,y):
        z = y.parent
        if z is not None:
            if y.mark is False:
                y.mark = True
            else:
                self.cut(y,z)
                self.cascadingCut(z)




if __name__ == '__main__':
    pass

    # fibonacciHeap2 = FibonacciHeap();
    # fibonacciHeap2.insert(100);
    # fibonacciHeap2.insert(56);
    #
    # fibonacciHeap3 = fibonacciHeap.union(fibonacciHeap2);
    # x = fibonacciHeap3.rootList.right
    # print "Value of X: " , x.key
    # fibonacciHeap3.decreaseKey(x,1)
    #
    # print [x.key for x in fibonacciHeap3.iterateNodeDoubleLinkList(fibonacciHeap3.rootList)]
    #
    # q = fibonacciHeap3.extractMin()
    # print "Key of q: " , q.key;
    #


