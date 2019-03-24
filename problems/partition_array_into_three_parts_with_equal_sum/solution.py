class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        avg, r = divmod(s, 3)
        if r != 0: return False
        curr = 0
        for x in A:
            curr += x
            if curr == avg:
                curr = 0
        return curr == 0