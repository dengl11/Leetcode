# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(node, k):
            if not node: return None, 0
            left = dfs(node.left, k)
            if left[0] is not None: return left[0], 0
            k -= left[1]
            if k == 1: return node.val, 0
            right = dfs(node.right, k - 1)
            if right[0] is not None: return right
            return None, left[1] + right[1] + 1
        
        return dfs(root, k)[0]
        