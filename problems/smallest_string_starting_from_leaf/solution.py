# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
#         def mark():
#             index = {}
#             stack = [root]
#             i = 0
#             while stack:
#                 curr = stack.pop()
#                 index[curr.val] = i
#                 i += 1
#                 if curr.left: stack.append(curr.left)
#                 if curr.right: stack.append(curr.right)
    
#         nodeIndex = mark()
        starts = []
        stack = [(root, None)]
        parents = {}
        while stack:
            curr, p = stack.pop()
            parents[curr] = p
            if not curr.left and not curr.right:
                if not starts or starts[0].val == curr.val:
                    starts.append(curr)
                elif starts[0].val > curr.val:
                    starts = [curr]
            if curr.left: stack.append((curr.left, curr))
            if curr.right: stack.append((curr.right, curr))
        def traceBack(leaf):
            ans = [leaf]
            p = parents[leaf]
            while p:
                ans.append(p)
                p = parents[p]
            return ans
        def minTrace(t1, t2):
            i = 0
            while i < len(t1) and i < len(t2):
                if t1[i].val < t2[i].val: return t1
                if t1[i].val > t2[i].val: return t2
                i += 1
            return t1 if len(t1) < len(t2) else t2
        trace = traceBack(starts[0])
        for t in starts[1:]:
            trace = minTrace(trace, traceBack(t))
        return "".join(chr(ord('a') + x.val) for x in trace)
            
            
        