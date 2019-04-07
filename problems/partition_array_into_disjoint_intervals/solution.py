class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = 1
        need = 1
        for (val, idx) in sorted([(val, i) for (i, val) in enumerate(A)]):
            need = max(need, idx + 1)
            if n >= need:
                return n
            n += 1            
            