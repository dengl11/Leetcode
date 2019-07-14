from collections import defaultdict
from functools import lru_cache
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skills = {s:i for (i, s) in enumerate(req_skills)}
        people = [[skills[s] for s in g] for g in people]
        candidates = defaultdict(list) # {skill_index: [people_index]}
        for i, ss in enumerate(people):
            for s in ss:
                candidates[s].append(i)
            
        @lru_cache(None)
        def query(todo : int) -> []:
            if not todo: return []
            ans = list(range(len(people)))
            for i in range(len(skills)):
                if todo & (1 << i) == 0: continue
                for c in candidates[i]:
                    next_todo = todo
                    for s in people[c]:
                        next_todo &= ~(1 << s)
                    curr = query(next_todo)
                    if len(curr) + 1 <= len(ans):
                        ans = [c] + curr
            return ans
        todo = (1 << (len(skills))) - 1
        return query(todo)
                