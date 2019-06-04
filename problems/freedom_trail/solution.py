from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        pos = defaultdict(list)
        n = len(ring)
        for i, c in enumerate(ring):
            pos[c].append(i)
        state = {0:0}
        for c in key:
            curr = {k: float('inf') for k in pos[c]}
            for pre in state:
                for i in pos[c]:
                    curr[i] = min(curr[i], state[pre] + min(abs(i-pre), n-abs(i-pre)))
            state = curr
        return min(state.values()) + len(key)
                
        