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
        ans = ""
        stack = [root]
        while stack:
            node = stack.pop()
            if not node: ans += "^$"
            else:
                ans += "^{}(".format(node.val)
                stack.append(node.right)
                stack.append(node.left)
            
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def parse(i):
            assert data[i] == "^"
            i += 1
            if data[i] == "$": return None, i+1
            j = i
            while data[i] != "(": i += 1
            val = int(data[j:i])
            i += 1 # skip (
            left, i = parse(i)
            right, i = parse(i)
            root = TreeNode(val)
            root.left = left
            root.right = right
            return root, i
        return parse(0)[0]
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))