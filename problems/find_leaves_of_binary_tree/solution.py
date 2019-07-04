# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        nodes = defaultdict(list)
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            r = max(left, right) + 1
            nodes[r].append(node.val)
            return r
        dfs(root)
        return [nodes[k] for k in sorted(nodes.keys())]
            
            
            
            
        