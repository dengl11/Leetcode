# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def construct(i, j):
            """"
            return a tree constructed from preorder[i:j+1]
            """
            if j < i: return None
            root = TreeNode(preorder[i])
            if j == i: return root
            leftEnd = i
            while leftEnd + 1 <=j and preorder[leftEnd+1] <= preorder[i]:
                leftEnd += 1
            left = construct(i+1, leftEnd)
            right = construct(leftEnd + 1, j)
            root.left = left
            root.right = right
            return root
        return construct(0, len(preorder) - 1)
            
            
        