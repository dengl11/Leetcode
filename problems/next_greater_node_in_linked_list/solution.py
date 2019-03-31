# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ans = []
        stack = []
        i = 0
        while head:
            while stack and stack[-1][1] < head.val:
                pos, _ = stack.pop()
                if pos >= len(ans):
                    ans += [0] * (pos - len(ans) + 1)
                ans[pos] = head.val
            stack.append((i, head.val))
            head = head.next
            i += 1
        ans += [0] * (i - len(ans))
        return ans
            