class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        speaks = [0] * 5 # [c, r, o, a, k]
        t = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        ans = 1
        for c in croakOfFrogs:
            idx = t[c]
            for j in range(idx):
                if speaks[j] <= speaks[idx]: return -1
            speaks[idx] += 1
            ans = max(ans, max(speaks))
            if idx == 4:
                for i in range(5):
                    speaks[i] -= 1
        if any(x != 0 for x in speaks): return -1
        return ans
                