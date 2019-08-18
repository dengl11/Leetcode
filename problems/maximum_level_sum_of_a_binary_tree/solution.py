# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        sums = Counter()
        l = 1
        q = [root]
        while q:
            nq = []
            curr = 0
            for node in q:
                curr += node.val
                if node.left: nq.append(node.left)
                if node.right: nq.append(node.right)
            q = nq
            sums[l] = curr
            l += 1
        t = max(sums.values())
        return min(k for k in sums if sums[k] == t)