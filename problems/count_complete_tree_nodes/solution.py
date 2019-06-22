# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def depth(node):
    if not node: return 0
    return 1 + depth(node.left)
        
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        dl, dr = depth(root.left), depth(root.right)
        if dl == dr:
            return (1 if dl == 0 else (1 << dl)) + self.countNodes(root.right)
        return (1 if dr == 0 else (1 << dr)) + self.countNodes(root.left)
        