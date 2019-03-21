# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        def trace(curr, p):
            """
            return number of coins needed from outside to make the subtree at curr balanced
            """
            if not curr: return 0
            left = trace(curr.left, curr)
            right = trace(curr.right, curr)
            total_need = - (curr.val - 1)
            if p: p.val -= total_need
            self.moves += abs(left) + abs(right)
            return total_need
        trace(root, None)
        return self.moves
            
            
            
            