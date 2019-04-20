# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        l = 0
        curr = root
        while curr:
            l += 1
            curr = curr.next
        g, r = divmod(l, k)
        groups = [g] * k
        for i in range(r):
            groups[i] += 1
        gi = 0
        ans = []
        while root:
            l = 1
            head = root
            while l < groups[gi]:
                root = root.next
                l += 1
            n = root.next
            root.next = None
            ans.append(head)
            root = n
            gi += 1
        return ans + [None] * (k - len(ans))
                
            
        