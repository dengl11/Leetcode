# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        def explore(node, curr_min, curr_max):
            if not node: return
            self.ans = max(self.ans, curr_max - node.val, node.val - curr_min)
            curr_min = min(curr_min, node.val)
            curr_max = max(curr_max, node.val)
            explore(node.left, curr_min, curr_max)
            explore(node.right, curr_min, curr_max)
            
        explore(root, root.val, root.val)
        return self.ans