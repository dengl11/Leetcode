# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):

    def __init__(self, nl):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nls = nl[::-1]
        self.data = self.fetch()
        
            
    def fetch(self):
        if not self.nls: return
        nl = self.nls.pop()
        if nl.isInteger():
             return nl.getInteger()
        else:
            for l in nl.getList()[::-1]:
                self.nls.append(l)
            return self.fetch()
            

    def next(self):
        """
        :rtype: int
        """
        ans = self.data
        self.data = self.fetch()
        return ans
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.data is not None
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())