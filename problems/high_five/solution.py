from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for id, s in items:
            if len(scores[id]) < 5:
                scores[id].append(s)
            else:
                idx = min(range(5), key = lambda i: scores[id][i])
                if scores[id][idx] < s:
                    scores[id][idx] = s
        ans = [None] * len(scores.keys())
        for id, ss in scores.items():
            ans[id - 1] = [id, sum(ss) // len(ss)]
        return ans
        