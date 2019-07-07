# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        def search(node, val):
            if not node: return []
            if node.val == val: return [node]
            left = search(node.left, val)
            if left: 
                return [node] + left
            right = search(node.right, val)
            if right:
                return [node] + right
            return []
    
        path = search(root, k)
        visited = set()
        def leaf(node):
            q = deque([(node, 0)])
            visited.add(node.val)
            while q:
                node, dis = q.popleft()
                if not node.left and not node.right: return (node.val, dis)
                if node.left and node.left.val not in visited:
                    q.append((node.left, dis + 1))
                if node.right and node.right.val not in visited:
                    q.append((node.right, dis + 1))
            return float('inf'), float('inf')
                    
        ans, dis = leaf(path.pop())
        extra = 1
        while path:
            ca, cd = leaf(path.pop())
            if cd + extra < dis: 
                ans, dis = ca, cd + extra
            extra += 1
        return ans
                