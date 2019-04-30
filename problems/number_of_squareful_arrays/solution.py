from collections import defaultdict
from functools import lru_cache
class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        A.sort()
        @lru_cache(None)
        def squareful(x):
            i = 0
            while i ** 2 < x: i += 1
            return i ** 2 == x
        
        graph = defaultdict(list)
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if squareful(A[i]+A[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        if not all(graph[k] for k in range(len(A))):
            return 0
        self.ans = 0
        def explore(s, visited):
            if len(visited) == len(A):
                self.ans += 1
            else:
                pre = -1
                for j in graph[s]:
                    if j in visited or A[j] == pre: continue
                    visited.add(j)
                    explore(j, visited)
                    visited.remove(j)
                    pre = A[j]
        for i in range(len(A)):
            if i == 0 or A[i] != A[i-1]:
                explore(i, {i})
        return self.ans
            
            
        