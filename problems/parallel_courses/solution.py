from collections import defaultdict, deque
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        pre = {i: set() for i in range(1, N + 1)}
        after = {i: set() for i in range(1, N + 1)}
        for i, j in relations:
            pre[j].add(i)
            after[i].add(j)
        ans = 0
        q = [i for i in range(1, N + 1) if not pre[i]]
        todo = set(i for i in range(1, N + 1))
        while q:
            nq = []
            for i in q:
                todo.remove(i)
                for j in after[i]:
                    pre[j].discard(i)
                    if not pre[j]:
                        nq.append(j)
            q = nq
            ans += 1
        return ans if not todo else -1
            