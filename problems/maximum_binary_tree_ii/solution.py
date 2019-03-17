# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        newNode = TreeNode(val)
        curr = root
        pre = None
        while curr and curr.val > val:
            pre = curr
            curr = curr.right
        if not pre:
            newNode.left = root
            return newNode
        if curr:
            pre.right = newNode
            newNode.left = curr
        else:
            pre.right = newNode
        return root
        