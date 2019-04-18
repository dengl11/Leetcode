class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def dist(x):
            return abs(x[0] - target[0]) + abs(x[1] - target[1])
        return dist((0, 0)) < min([dist(g) for g in ghosts], default=float('inf'))
        