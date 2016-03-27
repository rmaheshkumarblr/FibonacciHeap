#Creating a node class that contains all the parameter a node used in Fibonacci must have.

#Based on the parameters present in pg 480 of Introduction to Algorithms (Cormen)
class Node:
    def __init__(self,data):
        self.data = data
        self.degree = 0
        self.parent = self.child = self.left = self.right = None
        self.mark = False



