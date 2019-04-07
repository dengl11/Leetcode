from collections import deque
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        zerosBefore = [0]  * n
        i = 1
        while i < n:
            zerosBefore[i] = zerosBefore[i-1] + (S[i-1] == '0')
            i += 1
        
        zerosAfter = [0]  * n
        i = n - 2
        while i >= 0:
            zerosAfter[i] = zerosAfter[i+1] + (S[i+1] == '0')
            i -= 1
        
        ans = n
        for i, c in enumerate(S):
            if c == '0':
                ans = min(ans, i - zerosBefore[i] + min(zerosAfter[i], n - i - 1 - zerosAfter[i]))
            else:
                ans = min(ans, min(zerosBefore[i], i - zerosBefore[i]) + zerosAfter[i])
        return ans
                
            
        
            
            