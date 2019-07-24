# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = [root]
        while q:
            nq = []
            i = 0
            j = len(q) - 1
            while i < j:
                if None in [q[i], q[j]]:
                    if q[i] is not None or q[j] is not None: return False
                else:
                    if q[i].val != q[j].val: return False
                i += 1
                j -= 1
            for x in q:
                if x is None: nq += [None, None]
                else: nq += [x.left, x.right]
            q = nq
            if all(x is None for x in q): return True
        return True
                    