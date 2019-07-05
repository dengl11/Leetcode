"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        s = ""
        if not root: return "^$"
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                s += "^$"
            else:
                s += "^{}({})".format(node.val, len(node.children))
            for c in node.children[::-1]:
                stack.append(c)
        return s
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        def parse(i):
            assert data[i] == "^"
            i += 1 # skip ^
            if data[i] == "$": return None, i + 1
            assert data[i].isdigit()
            j = i
            while data[i]!='(': i += 1
            val = int(data[j:i])
            i += 1 # skip (
            assert data[i].isdigit()
            k = i
            while data[i] != ")": i += 1
            C = int(data[k:i])
            children = []
            i += 1 # skip )
            for _ in range(C):
                c, i = parse(i)
                children.append(c)
            node = Node(val, children)
            return node, i
        return parse(0)[0]
            
            
            
            
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))