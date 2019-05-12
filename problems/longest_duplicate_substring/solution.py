from functools import reduce
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        s = S
        S = [ord(c)-ord('a') for c in S]
        A = S
        mod = (1<<63)-1
        
        def check(L):
            p = pow(26, (L-1), mod)
            h = reduce(lambda x, y: (26*x+y)%mod, S[:L], 0)
            seen = set([h])
            for i in range(1, len(S)-L+1):
                h = (h - S[i-1]*p) * 26 + S[i+L-1]
                h %= mod
                if h in seen: return i
                seen.add(h)
            return None
        # def check(L):
        #     p = pow(26, L, mod)
        #     cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
        #     seen = {cur}
        #     for i in range(L, len(S)):
        #         cur = (cur * 26 + A[i] - A[i - L] * p) % mod
        #         if cur in seen: return i - L + 1
        #         seen.add(cur)
        # binary search
        lo, hi, ans = 0, len(S), 0
        while lo < hi:
            # print(lo,  hi)
            mid = (lo + hi + 1) // 2
            curr = check(mid)
            if curr is None: 
                hi = mid - 1
            else:
                ans = curr
                lo = mid 
        return "".join(chr(x + ord('a')) for x in S[ans:ans+lo])