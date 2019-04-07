# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.nodes = [root]
        for n in self.nodes:
            if n.left: self.nodes.append(n.left)
            if n.right: self.nodes.append(n.right)
        self.nodes = [None] + self.nodes

    def insert(self, v: int) -> int:
        node = TreeNode(v)
        self.nodes.append(node)
        parent = self.nodes[(len(self.nodes) - 1)//2]
        if parent.left is None:
            parent.left = node
        else:
            parent.right = node
        return parent.val
        

    def get_root(self) -> TreeNode:
        return self.nodes[1]
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()