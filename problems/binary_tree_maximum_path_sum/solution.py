# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def recurse(node):
            """
            return (max_path_sum, max_single_subtree_sum)
            """
            if not node: return (-float('inf'), -float('inf'))
            # if not node.left and not node.right:
            #     return (node.val, node.val)
            left_total, left_single = recurse(node.left)
            right_total, right_single = recurse(node.right)
            total = max(left_total, right_total, node.val + max(left_single, 0) + max(right_single, 0))
            single = max(left_single, right_single, 0) + node.val
            # print(node.val, total, single)
            return (total, single)
        return max(recurse(root))
            
        