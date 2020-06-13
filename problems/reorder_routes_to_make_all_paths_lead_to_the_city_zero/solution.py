from collections import defaultdict, deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        reachable = {0}
        froms = defaultdict(list)
        tos = defaultdict(list)
        for a, b in connections:
            froms[b].append(a)
            tos[a].append(b)
        
        q = deque([0])
        ans = 0
        while q:
            curr = q.popleft()
            for n in froms[curr]:
                if n in reachable: continue
                reachable.add(n)
                q.append(n)
            for n in tos[curr]:
                if n in reachable: continue
                reachable.add(n)
                ans += 1
                q.append(n)
        return ans
                