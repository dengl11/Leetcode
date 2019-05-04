# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        covered = set()
        self.ans = 0
        def dfs(n, par = None):
            if not n: return
            dfs(n.left, n)
            dfs(n.right, n)
            if (n.left and n.left not in covered) or (n.right and n.right not in covered) or (n not in covered and par is None):
                covered.update({n, par})
                self.ans += 1
        dfs(root)
        return self.ans
        