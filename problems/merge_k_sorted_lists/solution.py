# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappop, heappush
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = []
        for i, l in enumerate(lists):
            if l:
                heappush(q, (l.val, i))
        ans = ListNode(None)
        head = ans
        while q:
            val, i = heappop(q)
            head.next = ListNode(val)
            head = head.next
            if lists[i].next:
                heappush(q, (lists[i].next.val, i))
                lists[i] = lists[i].next
        return ans.next
        