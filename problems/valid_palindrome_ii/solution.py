class Solution:
    def validPalindrome(self, s: str) -> bool:
        s2 = s[::-1]
        n=len(s)
        swap = -1
        for i, (a, b) in enumerate(zip(s, s2)):
            if a == b: continue
            swap = i
            break
        if swap < 0: return True
        if s[:swap] + s[swap + 1:] == s2[:(n-swap-1)] + s2[n-swap:]:
            return True
        if s[:(n-swap-1)] + s[n-swap:] == s2[:swap] + s2[swap + 1:]:
            return True
        return False
                
            