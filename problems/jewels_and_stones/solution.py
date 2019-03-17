class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        return sum([x in J for x in S] or [0])