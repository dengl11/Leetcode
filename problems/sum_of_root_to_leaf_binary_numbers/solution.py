# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def explore(node, val):
            if not node: return 0
            val += val + node.val
            if not node.left and not node.right:
                return val
            return explore(node.left, val) + explore(node.right, val)
    
        return explore(root, 0)
        