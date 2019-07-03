# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root: return [None,None]
        if root.val <= V:
            r1, r2 = self.splitBST(root.right, V)
            root.right = r1
            return [root, r2]
        l1, l2 = self.splitBST(root.left, V)
        root.left = l2
        return [l1, root]
        