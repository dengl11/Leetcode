# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.ans = float('inf')
        def explore(node):
            if not node: return None
            left = explore(node.left)
            right = explore(node.right)
            mi = ma =node.val
            diff = float('inf')
            if left:
                mi = min(mi, left[0])
                diff = min(diff, node.val - left[1])
            if right:
                ma = max(ma, right[1])
                diff = min(diff, -node.val + right[0])
            self.ans = min(self.ans, diff)
            return mi,ma
        explore(root)
        return self.ans
            