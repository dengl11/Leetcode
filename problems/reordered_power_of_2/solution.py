from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        c = Counter(str(N))
        return any(c == Counter(str(1<<i)) for i in range(32))