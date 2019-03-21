class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        signs = []
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                signs.append(1)
            elif A[i] < A[i-1]:
                signs.append(-1)
            else: signs.append(0)
        ans = 1
        pre = 0
        if not signs: return ans
        for i, s in enumerate(signs):
            if s == 0: 
                ans = max(ans, i - pre + 1)
                pre = i + 1
                continue
            if i == 0: continue
            if signs[i-1] == s:
                ans = max(ans, i - pre + 1)
                pre = i
        ans = max(ans, len(A) - pre)
        return ans
                
            
            
            
            