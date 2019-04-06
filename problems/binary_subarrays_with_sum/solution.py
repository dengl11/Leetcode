class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        if not A or sum(A) < S: return 0
        curr = 0
        zeros = []
        for x in A:
            if x == 1:
                zeros.append(curr)
                curr = 0
            else:
                curr += 1
        zeros.append(curr)
        if S == 0:
            return sum(x * (x + 1) // 2 for x in zeros)
        
        before = zeros[:-1]
        after = zeros[1:]
        ans = 0
        for i in range(len(before) - S + 1):
            x, y = before[i],  after[i + S - 1]
            ans += 1 + x + y + x * y
        return ans
        