# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, premax = -float('inf')) -> int:
        if root is None: return 0
        if root.val >= premax: return 1 + self.goodNodes(root.left, root.val) + self.goodNodes(root.right, root.val)
        return self.goodNodes(root.left, premax) + self.goodNodes(root.right, premax)
        
        