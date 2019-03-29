# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if not node.left and not node.right: return (node, node)
            lefts = []
            curr = node
            oldRight = curr.right
            curr.right = None
            while curr:
                lefts.append(curr)
                oldLeft = curr.left
                curr.left = None
                curr = oldLeft
            newRoot, curr = helper(lefts.pop())
            while lefts:
                curr.right, newCurr = helper(lefts.pop())
                curr = newCurr
                
            if oldRight:
                curr.right, newCurr = helper(oldRight)
                curr = newCurr
            return newRoot, curr
        return helper(root)[0]
        