from collections import Counter
class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows = Counter()
        cols = Counter()
        diags = Counter()
        adiags = Counter()
        lights = set()
        def hash(i, j):
            if i >= j: p1 = (i-j, 0)
            else: p1 = (0, j-i)
            
            if i + j >= N-1: p2 = (i - (N-1-j), N-1)
            else: p2 = (0, j + i)
                
            return p1, p2
        
        def ner(i, j):
            for di, dj in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                ci, cj = i + di, j + dj
                if ci < 0 or ci >= N or cj < 0 or cj >= N: continue
                yield ci, cj
        
        for (r, c) in lamps:
            lights.add((r, c))
            rows[r] += 1
            cols[c] += 1
            di, adi = hash(r, c)
            diags[di] += 1
            adiags[adi] += 1
        
        def answer(q):
            r, c = q
            di, adi = hash(r, c)
            lighted = rows[r] or cols[c] or diags[di] or adiags[adi]
            for r, c in ner(r, c):
                if (r, c) not in lights: continue
                di, adi = hash(r, c)
                lights.remove((r, c))
                if rows[r]>0: rows[r] -= 1
                if cols[c] >0: cols[c] -= 1
                if diags[di] >0: diags[di]-= 1
                if  adiags[adi] >0:  adiags[adi] -= 1
            return 1 if lighted > 0 else 0
        return [answer(q) for q in queries]
        
        
        