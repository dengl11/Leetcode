class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        if not indexes: return S
        curr = 0
        ans = ""
        for idx, s, t in sorted(zip(indexes, sources, targets)):
            if idx > curr:
                ans += S[curr:idx]
                curr = idx
            if S[idx:idx + len(s)] == s:
                ans += t
                curr = idx + len(s)
        if curr < len(S):
            ans += S[curr:]
        return ans
        
        