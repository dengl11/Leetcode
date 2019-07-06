# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

inf = float('inf')

class Solution:
    def isValidBST(self, root: TreeNode, mi = -inf, ma = inf) -> bool:
        if not root: return True
        if root.val >= ma or root.val <= mi: return False
        return self.isValidBST(root.left, mi, root.val) and self.isValidBST(root.right, root.val, ma)
        