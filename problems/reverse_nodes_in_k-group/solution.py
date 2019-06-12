# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, K: int) -> ListNode:
        dummy = jump = ListNode(None)
        dummy.next = l = r = head
        while 1:
            k = 0
            while r and k < K:
                r = r.next
                k += 1
            if k == K:
                pre, curr = r, l
                for _ in range(k):
                    curr.next, curr, pre = pre, curr.next, curr
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next