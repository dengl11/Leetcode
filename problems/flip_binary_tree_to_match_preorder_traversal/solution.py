# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        flips = []
        positions = [0] * (len(voyage) + 1)
        for i, x in enumerate(voyage):
            positions[x] = i
        def match(node, i, j):
            if not node: return True
            if j < i: return False
            if node.val != voyage[i]: return False
            i += 1
            if not node.left:
                return match(node.right, i, j)
            if not node.right:
                return match(node.left, i, j)
            if i >= len(voyage): 
                return False
            right_pos = positions[node.right.val]
            if node.left.val != voyage[i]:
                flips.append(node.val)  
                right_pos = positions[node.left.val]
                return match(node.right, i, right_pos - 1) and match(node.left, right_pos, j) 
            return match(node.left, i, right_pos - 1) and match(node.right, right_pos, j) 
        
        if match(root, 0, len(voyage) - 1): return flips
        return [-1]
                
        