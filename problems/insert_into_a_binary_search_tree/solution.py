# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root
        pre = None
        while curr:
            pre = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if not pre: return TreeNode(val)
        if pre.val < val:
            pre.right = TreeNode(val)
        else:
            pre.left = TreeNode(val)
        return root
        
        