# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = defaultdict(list)
        q = deque([(root, 0, 0)])
        while q:
            node, x, y = q.popleft()
            pre = []
            while nodes[x] and nodes[x][-1][1] == y and nodes[x][-1][0] > node.val:
                pre.append(nodes[x].pop())
            nodes[x].append((node.val, y))
            nodes[x] += pre[::-1]
            y += 1
            if node.left:
                q.append((node.left, x - 1, y))
            if node.right:
                q.append((node.right, x + 1, y))
        keys = sorted(nodes.keys())
        # print(nodes)
        return [[x[0] for x in nodes[k]] for k in keys]