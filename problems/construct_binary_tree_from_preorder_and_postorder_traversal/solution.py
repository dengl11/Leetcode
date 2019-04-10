# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        n = len(pre)
        preIdx = [-1] * (n + 1)
        postIdx = [-1] * (n + 1)
        for i, x in enumerate(pre):
            preIdx[x] = i
        for i, x in enumerate(post):
            postIdx[x] = i
        def construct(i, j, m, n):
            if i > j: return None
            root = TreeNode(pre[i])
            if i == j: return root
            ii = i + 1
            jj = ii + postIdx[pre[ii]] - m
            root.left = construct(ii, jj, m, postIdx[pre[ii]])
            root.right = construct(jj+1, j, postIdx[pre[ii]]+1, n-1)
            return root
        return construct(0, n-1, 0, n-1)
        