# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        parent = {} # {node_val: parent_node}
        stack = [(root, None)]
        targetNode = None
        while stack:
            node, p = stack.pop()
            parent[node.val] = p
            if node == target:
                targetNode = node
            if node.left: stack.append((node.left, node))
            if node.right: stack.append((node.right, node))
        ans = []
        def collect(node, depth):
            if not node: return
            q = deque([(node, 0)])
            while q:
                node, d = q.popleft()
                if d == depth:
                    ans.append(node.val)
                elif d < depth:
                    if node.left: q.append((node.left, d + 1))
                    if node.right: q.append((node.right, d + 1))
        path = [targetNode]
        while True:
            node = path[-1]
            if node == root: break
            path.append(parent[node.val])
        for i, node in enumerate(path):
            if K == 0:
                ans.append(node.val)
                break
            if i == 0:
                collect(node, K)
            else:
                if node.left == path[i-1]:
                    collect(node.right, K-1)
                else:
                    collect(node.left, K-1)
            K -= 1
        return ans
            