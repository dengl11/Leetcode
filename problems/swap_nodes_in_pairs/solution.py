class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, curr = dummy, head
        while curr and curr.next:
            t = curr.next.next
            pre.next = curr.next
            curr.next.next = curr
            curr.next = t
            pre, curr = curr, t
        return dummy.next
            