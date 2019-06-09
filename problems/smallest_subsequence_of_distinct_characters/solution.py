from collections import defaultdict
from heapq import heappop, heappush, heapify
from bisect import bisect
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last = {c:i for i, c in enumerate(text)}
        stack = []
        seen = set()
        for i, c in enumerate(text):
            if c in seen: continue
            while stack and c < stack[-1] and last[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        return ''.join(stack)
