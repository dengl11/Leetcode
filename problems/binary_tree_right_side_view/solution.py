# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.rights = dict()
        def dfs(node, d):
            if not node: return
            if d not in self.rights:
                self.rights[d] = node.val
            dfs(node.right, d + 1)
            dfs(node.left, d + 1)
        
        dfs(root, 0)
        return [self.rights[i] for i in range(len(self.rights))]
        
        