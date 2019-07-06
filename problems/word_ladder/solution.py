class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        
        def next(w):
            for i in range(len(w)):
                for j in range(26):
                    cw = w[:i] + chr(97 + j) + w[i+1:]
                    if cw in words:
                        yield cw
        
        q = [beginWord]
        c = 1
        visited = set([beginWord])
        while q:
            newq = []
            for w in q:
                if w == endWord: return c
                for nw in next(w):
                    if nw not in visited:
                        visited.add(nw)
                        newq.append(nw)
            c += 1
            q = newq
        return 0
            
            
        
        