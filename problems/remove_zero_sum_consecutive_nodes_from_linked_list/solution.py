# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from bisect import bisect, insort
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        pre = [0]
        for x in arr:
            pre.append(x + pre[-1])
        
        def convert(arr):
            head = curr = ListNode(None)
            for x in arr:
                if x == 0: continue
                n = ListNode(x)
                curr.next = n
                curr = n
            return head.next
        segs = []
        for dist in range(len(arr), 0, -1):
            for i in range(len(pre)):
                j = i + dist
                if j >= len(pre): continue
                if pre[j] == pre[i]:
                    idx = bisect(segs, (i, j -1))
                    if (idx == 0 or i > segs[idx-1][1]) and (idx == len(segs) or j-1 < segs[idx][0]):
                        # print(segs, idx, (i, j-1))
                        insort(segs, (i, j - 1))
        # print(segs)
        for i, j in segs:
            arr[i:j + 1] = [0] * (j - i + 1)
        
        return convert(arr)