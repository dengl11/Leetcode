# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        i = S.find("-")
        if i < 0: return TreeNode(int(S))
        parents = [TreeNode(int(S[:i]))]
        
        while i < len(S):
            d = 1
            j = i + 1
            while S[j] == "-":
                d += 1
                j += 1
            k = j + 1
            while k < len(S) and S[k].isdigit():
                k += 1
            val = int(S[j:k])
            curr = TreeNode(val)
            while len(parents) > d:
                parents.pop()
            p = parents[-1]
            if p.left is None:
                p.left = curr
            else:
                p.right = curr
            parents.append(curr)
            i = k
        return parents[0]
        