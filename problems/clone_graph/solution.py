"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return None
        new = Node(node.val, None)
        m = {node: new}
        stack = [(new, node)]
        while stack:
            curr, old = stack.pop()
            curr.neighbors = []
            for c in old.neighbors:
                if c in m: 
                    curr.neighbors.append(m[c])
                else:
                    cnew = Node(c.val, None)
                    m[c] = cnew
                    curr.neighbors.append(cnew)
                    stack.append((cnew, c))
        return new
            