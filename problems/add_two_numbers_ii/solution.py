# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def convert(l):
            ans = []
            while l:
                ans.append(l.val)
                l = l.next
            return ans
        l1, l2 = convert(l1), convert(l2)
        if len(l2) > len(l1): l1, l2 = l2, l1
        carry = 0
        for j in range(1, len(l2)+1):
            l1[-j] += l2[-j] + carry
            carry, l1[-j] = divmod(l1[-j], 10)
        for j in range(len(l2)+1, len(l1)+1):
            l1[-j] += carry
            carry, l1[-j] = divmod(l1[-j], 10)
        L = head = ListNode(carry)
        for x in l1:
            L.next = ListNode(x)
            L = L.next
        return head if carry else head.next
            
        
        