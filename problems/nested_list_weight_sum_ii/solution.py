# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nls: List[NestedInteger]) -> int:
        self.ans = 0
        def depth(node):
            if node.isInteger(): return 1
            return max([depth(nl) for nl in node.getList()], default = -1) + 1
        
        def collect(nl, d):
            if nl.isInteger(): 
                self.ans += d * nl.getInteger()
            else:
                for nnl in nl.getList():
                    collect(nnl, d - 1)

        root = NestedInteger()
        for x in nls:
            root.add(x)
            
        collect(root, depth(root))
        return self.ans
                
            
        