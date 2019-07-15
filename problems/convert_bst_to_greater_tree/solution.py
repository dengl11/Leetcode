# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(node, pre = 0):
            if not node: return pre
            right = dfs(node.right, pre)
            node.val += right
            return dfs(node.left, node.val)
        
        dfs(root)
        
        return root
        