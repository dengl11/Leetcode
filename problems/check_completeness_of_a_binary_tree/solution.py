# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        i = 0
        nodes = [(root, 1)]
        while i < len(nodes):
            node, code = nodes[i]
            i += 1
            if node.left:
                nodes.append((node.left, code * 2))
            if node.right:
                nodes.append((node.right, code * 2 + 1))
        return nodes[-1][1] == i
    
            