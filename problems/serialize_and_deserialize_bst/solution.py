# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(str(node.val))
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return " ".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        eles = [int(x) for x in data.split()]
        if not eles: return None
        def parse(i, upper = float('inf')):
            if i >= len(eles): return None, i
            if eles[i] >  upper: return None, i
            root = TreeNode(eles[i])
            root.left, i = parse(i+1, eles[i])
            root.right, i = parse(i, upper)
            return root, i
        return parse(0)[0]
            
            