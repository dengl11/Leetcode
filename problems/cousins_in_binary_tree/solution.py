# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        px = py = None
        dx = dy = -1
        stack = [(root, None, 0)]
        while stack:
            curr, p, d = stack.pop()
            if curr.val == x:
                px = p
                dx = d
            if curr.val == y:
                py = p
                dy = d
            d += 1
            if curr.left:
                stack.append((curr.left, curr, d))
            if curr.right:
                stack.append((curr.right, curr, d))
        if dx != dy or px == py: return False
        return True