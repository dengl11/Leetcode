# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(node, curr):
            # return True if deleted
            if not node: return (None, 0)
            curr += node.val
            node.left, left = dfs(node.left, curr)
            node.right, right = dfs(node.right, curr)
            if curr + max(left, right) >= limit: return (node, node.val + max(left, right))
            return (None, node.val + max(left, right))
        return dfs(root, 0)[0]
                
        