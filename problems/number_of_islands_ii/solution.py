class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = dict()
        def find(i):
            if uf.get(i, i) != i:
                uf[i] = find(uf.get(i, i))
            return uf.get(i, i)
            
        def union(i, j):
            uf[find(i)] = find(j)
        
        def hash(i, j): # use a number to identify (i, j)
            return i * (m*n) + j
        
        ans = []
        added = set()
        islands = set()
        used = set()
        for i, j in positions:
            if (i, j) in used: 
                ans.append(ans[-1])
                continue
            used.add((i, j))
            added.add((i, j))
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if ni >= m or ni < 0 or nj < 0 or nj >= n: continue
                if (ni, nj) not in added: continue
                islands.discard(find(hash(ni, nj)))
                union(hash(ni, nj), hash(i, j))
            islands.add(hash(i, j))
            ans.append(len(islands))
        return ans
            