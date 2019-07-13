# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.ans = -float('inf')
        def dfs(node):
            if not node: return (0, 0)
            lc, lv = dfs(node.left)
            rc, rv = dfs(node.right)
            self.ans = max(self.ans, float(node.val + lv + rv) / (1 + lc + rc))
            return 1 + lc + rc, node.val + lv + rv
        dfs(root)
        return self.ans