from collections import Counter
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        negs, zeros, pos = [], [], []
        for x in A:
            if x<0: negs.append(-x)
            elif x == 0: zeros.append(0)
            else:pos.append(x)
        if len(negs) % 2 or len(zeros)%2 or len(pos) % 2:
            return False
        negs.sort()
        pos.sort()
        def can_pair(arr):
            arr.sort()
            c = Counter(arr)    
            for x in arr:
                if c[x] == 0: continue
                c[x] -= 1
                if c[2 * x ] == 0: return False
                c[2 * x ] -= 1
            return True
        return can_pair(negs) and can_pair(pos)
        