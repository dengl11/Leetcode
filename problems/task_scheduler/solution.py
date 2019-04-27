from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        A, cA = c.most_common(1)[0]
        if cA <= 1: return len(tasks)
        mosts = set(k for k in c if c[k] == cA)
        buckets = [len(mosts)] * (cA-1)
        
        j = 0
        for k, v in c.items():
            if k in mosts: continue
            for _ in range(v):
                buckets[j] += 1
                j = (j + 1) % len(buckets)
        return sum(buckets) + sum(max(n+1 - b, 0) for b in buckets) + len(mosts)
            