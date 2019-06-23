class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        return sum(c in J for c in S)