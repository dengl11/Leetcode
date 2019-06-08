from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        expects = defaultdict(lambda :defaultdict(int))
        ans = 0
        for i in range(1, len(A)):
            x = A[i]
            ans += sum(expects[x].values())
            diffs = set()
            for j in range(i):
                diff = x - A[j]
                if diff not in diffs:
                    expects[x + diff][diff] += expects[x][diff]
                expects[x + diff][diff] += 1
                diffs.add(diff)
                
        return ans
        