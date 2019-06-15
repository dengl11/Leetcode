# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        carry = 0
        pre = head
        while l1 or l2:
            curr = ListNode(0)
            carry, curr.val  = divmod((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry, 10)
            pre.next = curr
            pre = curr
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry:
            pre.next = ListNode(carry)
            
        return head.next
            
            
            
            
        