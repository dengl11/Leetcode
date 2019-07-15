# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        slow, fast = head, head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, slow, pre = pre, slow.next, slow
        
        s1 = pre
        if fast:
            s2 = slow.next
        else:
            s2 = slow
        while s1 and s2:
            if s1.val != s2.val: return False
            s2 = s2.next
            s1 = s1.next
        return not s2 and not s1
            
            
        