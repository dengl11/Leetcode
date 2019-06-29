from collections import defaultdict
class Solution:
    def findOrder(self, nc: int, prerequisites: List[List[int]]) -> List[int]:
        dependOn = defaultdict(set)
        depentBy = defaultdict(set)
        for s, t in prerequisites:
            dependOn[s].add(t)
            depentBy[t].add(s)
        todo = [i for i in range(nc) if i not in dependOn]
        take = []
        while todo:
            c = todo.pop()
            take.append(c)
            for cc in depentBy[c]:
                dependOn[cc].remove(c)
                if not dependOn[cc]:
                    todo.append(cc)
                    
        
        return take if len(take) == nc else []
