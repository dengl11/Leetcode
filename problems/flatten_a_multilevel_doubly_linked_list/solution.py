"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node', pre = None) -> 'Node':
        def helper(curr):
            if curr is None: return None
            if curr.child:
                c = curr.child
                child_last = helper(c)
                n = curr.next
                curr.next = c
                c.prev = curr
                curr.child = None
                if child_last:
                    child_last.next = n
                if n:
                    n.prev = child_last
                return helper(n)
            else:
                if curr.next:
                    return helper(curr.next)
                return curr
        helper(head)
        return head
                

