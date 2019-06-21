class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        uf = dict()
        
        def find(w):
            if uf.get(w, w) != w:
                uf[w] = find(uf.get(w, w))
            return uf.get(w, w)
    
        def union(w1, w2):
            uf[find(w1)] = find(w2)
        
        for w1, w2 in pairs:
            union(w1, w2)
            
        for w1, w2 in zip(words1, words2):
            if w1 == w2: continue
            if find(w1) == find(w2): continue
            return False
        return True