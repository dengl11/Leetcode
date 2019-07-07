# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, todo):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        todo = set(todo)
        ans = []
        def dfs(node, p = None):
            if not node: return False
            if node.val in todo:
                dfs(node.left, None)
                dfs(node.right, None)
                return True
            else:
                l = dfs(node.left, node)
                r = dfs(node.right, node)
                if l: node.left = None
                if r: node.right = None
                if p is None:
                    ans.append(node)
                return False
        dfs(root)
        return ans
                
                
            
        