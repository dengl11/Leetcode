# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        nodes = {} # {s: node}
        ans = []
        added = set()
        def dfs(node):
            if not node: return "#"
            left = dfs(node.left)
            right = dfs(node.right)
            me =  "{}({})({})".format(node.val, left, right)
            if me in nodes and me not in added:
                ans.append(nodes[me])
                added.add(me)
            else:
                nodes[me] = node
            return me
        dfs(root)
        return ans