from collections import defaultdict
from functools import reduce
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = [w for w in words if w]
        T = lambda: defaultdict(T)
        trie = T()
        for i, w in enumerate(words):
            reduce(lambda node, c: node[c], w, trie)['$'] = i
        
        def check(i, w):
            # return True if w can be constructed by other words
            # i is the index of w in words, to filter out the case that it is matched by itself
            def dfs(node, remain):
                # print("".join(remain))
                if not remain:
                    return node.get("$", i) != i
                if "$" in node:
                    if dfs(trie, remain): return True
                c = remain.pop()
                ans = False
                if c in node:
                    ans = dfs(node[c], remain)
                remain.append(c)
                return ans
            return dfs(trie, list(w)[::-1])
        
        return [w for (i, w) in enumerate(words) if check(i, w)]
