from collections import Counter
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        ans = 0
        window = Counter()
        for i in range(len(S)):
            window[S[i]] += 1
            if i >= K:
                window[S[i-K]] -= 1
                if window[S[i-K]] == 0: del window[S[i-K]]
            if len(window) == K:
                ans += 1
        return ans            
        