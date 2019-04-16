# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G = set(G)
        connected = False
        ans = 0
        while head:
            if head.val in G:
                connected = True
            else:
                ans += connected
                connected = False
            head = head.next
        return ans + connected
        