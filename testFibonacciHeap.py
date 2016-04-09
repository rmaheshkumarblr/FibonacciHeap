import FibonacciHeap
import unittest
import sys


class TestFibonacciHeap(unittest.TestCase):

    def setUp(self):
        self.fibonacciHeap = FibonacciHeap.FibonacciHeap();
        self.fibonacciHeap.insert(1)
        self.fibonacciHeap.insert(10)
        self.fibonacciHeap.insert(9)
        self.fibonacciHeap.insert(8)
        self.fibonacciHeap.insert(7)
        self.fibonacciHeap.insert(6)
        self.fibonacciHeap.insert(5)
        self.fibonacciHeap.insert(4)
        self.fibonacciHeap.insert(3)
        self.fibonacciHeap.insert(2)

        self.fibonacciHeap2 = FibonacciHeap.FibonacciHeap();
        self.fibonacciHeap2.insert(11);
        self.fibonacciHeap2.insert(12);

        self.fibonacciHeap3 = FibonacciHeap.FibonacciHeap();

    def tearDown(self):
        pass

    def test_RootList(self):
        rootList = [x.key for x in self.fibonacciHeap.iterateNodeDoubleLinkList(self.fibonacciHeap.rootList)]
        self.assertItemsEqual(rootList, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , msg="The root list does not contain the expected nodes")

    def test_findMinimum(self):
        self.assertEqual(self.fibonacciHeap.findMinNode().key,1,msg="The minimum does not match the expected minimum")

    def test_extractMinimum(self):
        self.fibonacciHeap.extractMin();
        rootList = [x.key for x in self.fibonacciHeap.iterateNodeDoubleLinkList(self.fibonacciHeap.rootList)]
        # Checking if the root list is correct
        self.assertItemsEqual(rootList,[2, 10], msg="The root list is wrong");
        # Checking if the second level is correct
        level2 = [x.key for x in self.fibonacciHeap.iterateNodeDoubleLinkList(self.fibonacciHeap.rootList.child)]
        level2Nodes = [x for x in self.fibonacciHeap.iterateNodeDoubleLinkList(self.fibonacciHeap.rootList.child)]
        self.assertItemsEqual(level2, [3, 6, 4], msg="The level 2 list is wrong");
        level3 = []
        level3Nodes = []
        for node in level2Nodes:
             if node.child is not None:
                level3.extend(x.key for x in self.fibonacciHeap.iterateNodeDoubleLinkList(node.child))
                level3Nodes.extend(x for x in self.fibonacciHeap.iterateNodeDoubleLinkList(node.child))
        self.assertItemsEqual(level3, [5, 7, 8], msg="The level 3 list is wrong");
        level4 = []
        for node in level3Nodes:
             if node.child is not None:
                level4.extend(x.key for x in self.fibonacciHeap.iterateNodeDoubleLinkList(node.child))
        self.assertItemsEqual(level4, [9]);

    def test_union(self):
        self.fibonacciHeap3 = self.fibonacciHeap.union(self.fibonacciHeap2);
        newRootList = [x.key for x in self.fibonacciHeap3.iterateNodeDoubleLinkList(self.fibonacciHeap3.rootList)]
        self.assertItemsEqual(newRootList, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], msg="The level 2 list is wrong");

    def test_decreaseKey(self):
        self.fibonacciHeap.extractMin();
        rootList = [x.key for x in self.fibonacciHeap.iterateNodeDoubleLinkList(self.fibonacciHeap.rootList)]
        level2Nodes = [x for x in self.fibonacciHeap.iterateNodeDoubleLinkList(self.fibonacciHeap.rootList.child)]
        level3Nodes = []
        for node in level2Nodes:
             if node.child is not None:
                level3Nodes.extend(x for x in self.fibonacciHeap.iterateNodeDoubleLinkList(node.child))
        level4Nodes = []
        for node in level3Nodes:
             if node.child is not None:
                level4Nodes.extend(x for x in self.fibonacciHeap.iterateNodeDoubleLinkList(node.child))
        self.fibonacciHeap.decreaseKey(level4Nodes[0],1)
        newRootList = [x.key for x in self.fibonacciHeap.iterateNodeDoubleLinkList(self.fibonacciHeap.rootList)]
        self.assertItemsEqual(newRootList,[2, 10,1], msg="The root list is wrong");
        # Checking if the second level is correct
        level2 = [x.key for x in self.fibonacciHeap.iterateNodeDoubleLinkList(self.fibonacciHeap.rootList.child)]
        level2Nodes = [x for x in self.fibonacciHeap.iterateNodeDoubleLinkList(self.fibonacciHeap.rootList.child)]
        self.assertItemsEqual(level2, [3, 6, 4], msg="The level 2 list is wrong");
        level3 = []
        level3Nodes = []
        for node in level2Nodes:
             if node.child is not None:
                level3.extend(x.key for x in self.fibonacciHeap.iterateNodeDoubleLinkList(node.child))
                level3Nodes.extend(x for x in self.fibonacciHeap.iterateNodeDoubleLinkList(node.child))
        self.assertItemsEqual(level3, [5, 7, 8], msg="The level 3 list is wrong");






def main(*argv):
    unittest.main()


if __name__ == '__main__':
    main(sys.argv)


