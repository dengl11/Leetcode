class Solution:
    def countSubstrings(self, s: str) -> int:
        chars = "^#" + "#".join(s) + "#$"
        Ls = [0] * len(chars)
        center = right = 1
        for i in range(1, len(chars)-1):
            if i < right:
                Ls[i] = min(right - i, Ls[2 * center - i])
            while chars[i + Ls[i]+1] == chars[i-Ls[i]-1]:
                Ls[i] += 1
            if i + Ls[i] > right:
                center, right = i, i + Ls[i]
        return sum((x+1)//2 for x in Ls)
            