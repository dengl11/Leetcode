# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        stack = []
        for x in nums:
            newNode = TreeNode(x)
            curr = None
            while stack and stack[-1].val < x:
                curr = stack.pop()
            if curr:
                newNode.left = curr
            if stack:
                stack[-1].right = newNode
            stack.append(newNode)
        return stack[0]
                