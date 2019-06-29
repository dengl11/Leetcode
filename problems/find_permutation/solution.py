class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ans = []
        for i, c in enumerate(s):
            if c != 'I': continue
            ans += list(range(i+1, len(ans), -1))
        ans += list(range(len(s)+1, len(ans), -1))
        return ans