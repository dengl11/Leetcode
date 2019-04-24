from collections import deque
class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = [int(c) for c in str(num)]
        ans = []
        expected = deque(sorted([(x, -i) for (i, x) in enumerate(arr)], reverse=True))
        idx = 0
        while idx < len(arr):
            if arr[idx] == expected[0][0]: 
                expected.popleft()
                ans.append(arr[idx])
                idx += 1
            else:
                j =0
                while j < len(expected)-1 and expected[j+1][0] == expected[j][0]:
                     j += 1
                arr[idx], arr[-expected[j][1]] = arr[-expected[j][1]], arr[idx]
                ans += arr[idx:]
                break
        return int("".join(str(c) for c in ans))
            