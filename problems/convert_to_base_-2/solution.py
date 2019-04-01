from collections import deque
from bisect import bisect_left
class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0: return "0"
        arr = deque([(1, 0)]) # [(val, i)]
        i = 1
        curr = -2
        while arr[-1][0] <= abs(N) or arr[0][0] >= -abs(N):
            if curr > 0:
                arr.append((curr, i))
            else:
                arr.appendleft((curr, i))
            curr *= -2
            i += 1
            
        def explore(x, used):
            if x == 0: return used
            i = bisect_left(arr, (x, 0))
            if arr[i][1] not in used:
                used.add(arr[i][1])
                if explore(x - arr[i][0], used): return used
                used.remove(arr[i][1])
            if arr[i-1][1] not in used:
                used.add(arr[i-1][1])
                if explore(x - arr[i-1][0], used): return used
                used.remove(arr[i-1][1])
            return None
        
        ans = explore(N,set())
        s = ["0"] * (1 + max(ans))
        for x in ans:
            s[~x] = "1"
        return "".join(s)
                    
                    
            
                    