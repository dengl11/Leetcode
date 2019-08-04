# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        children = dict()
        nodes = dict()
        def count(node):
            if not node: return 0
            nodes[node.val] = node
            left = count(node.left)
            right = count(node.right)
            children[node.val] = left + right + 1
            return children[node.val]
        
        count(root)
        xc = children[x]
        root = nodes[x]
        left = children[root.left.val] if root.left else 0
        right = children[root.right.val] if root.right else 0
        return max(left, right) > n / 2 or xc < n / 2
        