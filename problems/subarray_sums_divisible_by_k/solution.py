class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        count = [1] + [0] * K
        curr = 0
        ans = 0
        for x in A:
            curr = (curr + x) % K
            ans += count[curr]
            count[curr] += 1
        return ans
            