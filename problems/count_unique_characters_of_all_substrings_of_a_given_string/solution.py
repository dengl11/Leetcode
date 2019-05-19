from collections import defaultdict
class Solution:
    def uniqueLetterString(self, S: str) -> int:
        n = len(S)
        pos = defaultdict(list)
        for i, c in enumerate(S):
            pos[c].append(i)
        ans = 0
        for k, arr in pos.items():
            for i, v in enumerate(arr):
                if i > 0: left = v - arr[i-1] - 1
                else: left = v
                if i < len(arr)-1: right = arr[i+1] - v - 1
                else: right = n-1-v
                # print(left, right)
                # print((left + 1) * (right + 1))
                ans += (left + 1) * (right + 1)
        return ans
                