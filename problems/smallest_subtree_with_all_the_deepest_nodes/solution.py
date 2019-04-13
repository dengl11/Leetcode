# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        deepest = 0
        nDeepest = 0
        stack = [(root, 0)]
        while stack:
            node, d = stack.pop()
            if d == deepest:
                nDeepest += 1
            if d > deepest:
                deepest = d
                nDeepest = 1
            if node.left:
                stack.append((node.left, d + 1))
            if node.right:
                stack.append((node.right, d + 1))
        def search(node, d):
            if not node: return 0
            if d == deepest:
                ans = 1
            else:
                ans = search(node.left, d + 1) + search(node.right, d + 1)
            if ans == nDeepest:
                self.ans = node
                return -1
            return ans
        search(root, 0)
        return self.ans
            
            
        