# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        root.left = left
        root.right = right
        if left or right or root.val: return root
        return None
        