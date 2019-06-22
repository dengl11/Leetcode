class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        ans = ""
        i = 0
        replacements = sorted(zip(indexes, sources, targets))
        j = 0
        while i < len(S):
            while j < len(replacements) and replacements[j][0] < i:
                j += 1
            curr = S[i]
            d = 1
            if j < len(replacements) and replacements[j][0] == i:
                src = replacements[j][1]
                if S[i:i + len(src)] == src:
                    curr = replacements[j][2]
                    d = max(1, len(src))
            i += d
            ans += curr
        return ans
                