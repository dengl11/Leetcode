class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s: return 0
        neg = False
        i = 0
        if s[0] in "+-":
            if s[0] == "-": neg = True
            i = 1
        if i >= len(s) or not s[i].isdigit(): return 0
        j = i + 1
        ans = int(s[i])
        while j < len(s) and s[j].isdigit():
            ans = 10 * ans + int(s[j])
            j += 1
        if neg: ans *= -1
        return max(min(ans, (1<<31) - 1), -(1 << 31))
            
        