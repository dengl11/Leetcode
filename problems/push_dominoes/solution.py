class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        preR, nextL = [-1]*n, [-1]*n
        pre = -1
        for i in range(0, n):
            if dominoes[i] == "R": pre = i
            elif dominoes[i] == "L": pre = -1
            elif pre >= 0:
                preR[i] = pre
        pre = -1
        for i in range(n-1, -1, -1):
            if dominoes[i] == "R": pre = -1
            elif dominoes[i] == "L": pre = i
            elif pre >= 0:
                nextL[i] = pre
        ans = ""
        for i, c in enumerate(dominoes):
            if c != '.':
                ans += c
            else:
                l, r = nextL[i] - i, i - preR[i]
                if nextL[i] == -1:
                    l = n
                if preR[i] == -1:
                    r = n
                if l == r:
                    ans += "."
                elif l < r:
                    ans += "L"
                else:
                    ans += "R"
        return ans
            
                
                
        