
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import reduce
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        q = [root]
        ans = []
        d = 1
        while q:
            curr = max(n.val for n in q)
            ans.append(curr)
            q = reduce(lambda x,y: x + y, ([n.left, n.right] for n in q))
            q = [n for n in q if n is not None]
        return ans
            