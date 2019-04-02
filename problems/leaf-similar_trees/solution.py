# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leaves(root):
            stack = [root]
            ans = []
            while stack:
                curr = stack.pop()
                if not curr.left and not curr.right:
                    ans.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
            return ans
        
        return leaves(root1) == leaves(root2)
        