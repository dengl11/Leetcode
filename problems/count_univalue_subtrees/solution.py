# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def query(node):
            if not node: return 0, None
            left, right = query(node.left), query(node.right)
            uni = True
            if left[0] and left[1] is None: uni = False
            if right[0] and right[1] is None: uni = False
            if uni:
                s = {node.val}
                if left[1] is not None: s.add(left[1])
                if right[1] is not None: s.add(right[1])
                if len(s) > 1: uni = False
            return left[0] + right[0] + uni, (node.val if uni else None)
        return query(root)[0]
        