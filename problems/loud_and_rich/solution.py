from collections import defaultdict
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        poorThan = defaultdict(list) # {i: [j]} where person j is poor than person i
        for i, j in richer:
            poorThan[j].append(i)
        ans = [None] * len(quiet)
        def search(i):
            if ans[i] is not None: return ans[i]
            curr = i
            for child in poorThan[i]:
                if quiet[search(child)] < quiet[curr]:
                    curr = search(child)
            ans[i] = curr
            return curr
        for i in range(len(quiet)):
            search(i)
        return ans