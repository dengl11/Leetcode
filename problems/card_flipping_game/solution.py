class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        candidates = set(fronts) | set(backs)
        for f, n in zip(fronts, backs):
            if f == n:
                if f in candidates:
                    candidates.remove(f)
        if not candidates: return 0
        return min(candidates)
        