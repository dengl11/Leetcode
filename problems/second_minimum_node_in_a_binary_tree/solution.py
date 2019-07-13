# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [root]
        self.ans = None
        while stack:
            node = stack.pop()
            if node.val > root.val:
                if self.ans is None or self.ans > node.val:
                    self.ans = node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return self.ans if self.ans is not None else -1
        