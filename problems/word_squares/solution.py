from collections import defaultdict
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        prefixes = defaultdict(list)
        n = len(words[0])
        for w in words:
            for i in range(1, n+1):
                prefixes[w[:i]].append(w)
        
        ans = []
        def dfs(sq):
            if len(sq) == n:
                ans.append(sq)
                return
            for w in prefixes[''.join(list("".join(w) for w in zip(*sq))[len(sq)])]:
                dfs(sq + [w])
        
        
        for w in words:
            dfs([w])
        return ans
            