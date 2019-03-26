class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [ch for ch in S if ch.isalpha()][::-1]
        ans = ""
        j = 0
        for ch in letters:
            while j < len(S) and not S[j].isalpha():
                ans += S[j]
                j += 1
                
            ans += ch
            j += 1
        while j < len(S):
            ans += S[j]
            j += 1
        return ans
        
        