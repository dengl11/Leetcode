from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        dic = set(wordList)
        def nexts(w):
            for i, c in enumerate(w):
                for j in range(26):
                    cw = w[:i] + chr(97 + j) + w[i+1:]
                    if cw != w and cw in dic:
                        yield cw
        
        ans = []
        q = {beginWord: [[beginWord]]}
        while q:
            newq = defaultdict(list)
            for w in q:
                if w == endWord:
                    ans += q[w]
                else:
                    for nw in nexts(w):
                        newq[nw] += [path + [nw] for path in q[w]]
            q = newq
            dic -= set(q.keys())
        return ans
