# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot
        nodes = [root]
        for _ in range(d-2):
            new = []
            for n in nodes:
                if n.left: new.append(n.left)
                if n.right: new.append(n.right)
            nodes = new
        for n in nodes:
            left = n.left
            right = n.right
            n.left = TreeNode(v)
            n.right = TreeNode(v)
            n.left.left = left
            n.right.right = right
        return root