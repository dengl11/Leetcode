# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root: return ans
        q = [root]
        while q:
            ans.append([x.val for x in q])
            nq = []
            for node in q:
                if node.left: nq.append(node.left)
                if node.right: nq.append(node.right)
            q = nq
        return ans
                