class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(set([x[::-1] for x in words]))
        ans = 0
        for i in range(len(words)-1):
            if not words[i+1].startswith(words[i]):
                ans += len(words[i]) + 1
        ans += len(words[-1]) + 1
        return ans
                