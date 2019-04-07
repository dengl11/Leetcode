from collections import Counter
from bisect import bisect
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.ans = []
        self.times = times
        counts = Counter()
        for i, p in enumerate(persons):
            counts[p] += 1
            most = max(counts.values())
            candidates = set([c for c in counts if counts[c] == most])
            j = i
            while j >= 0:
                if persons[j] in candidates:
                    self.ans.append(persons[j])
                    break
                j -= 1
            
    def q(self, t: int) -> int:
        idx = bisect(self.times, t) - 1
        return self.ans[idx]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)