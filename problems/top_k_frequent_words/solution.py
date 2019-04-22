from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans = sorted((-v, k) for (k, v) in Counter(words).items())[:k]
        return [x[1] for x in ans]
        