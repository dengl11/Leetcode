class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set(tuple(x) for x in blocked)
        if not blocked: return True
        source, target = tuple(source), tuple(target)
        f1, f2 = set([source]), set([target])
        v1, v2 = set([source]), set([target])
        
        def ner(x, y, v):
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                cx, cy = x + dx, y + dy
                if cx < 0 or cx >= 1000000 or cy < 0 or cy >= 1000000: continue
                if (cx, cy) in blocked or (cx, cy) in v: continue
                v.add((cx, cy))
                yield (cx, cy)
                
        n1 = n2 = 0
        while f1 and f2:
            if target in f1 or source in f2: return True
            nf1 = set()
            nf2 = set()
            for (x, y) in f1:
                for nx, ny in ner(x, y, v1):
                    nf1.add((nx, ny))
                    n1 += 1
            for (x, y) in f2:
                for nx, ny in ner(x, y, v2):
                    nf2.add((nx, ny))
                    n2 += 1
            f1, f2 = nf1, nf2
            if n1 >= 20000 or n2 >= 20000: return True
        return False
            