# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def dfs(node):
            if not node: return
            dfs(node.right)
            self.sum += node.val
            node.val = self.sum
            dfs(node.left)
        dfs(root)
        return root
        