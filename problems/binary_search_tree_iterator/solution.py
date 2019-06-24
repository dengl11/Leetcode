class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.push_lefts(root)
    
    def push_lefts(self,node):
        while node:
            self.stack.append(node)
            node = node.left
            
    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        self.push_lefts(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
        
