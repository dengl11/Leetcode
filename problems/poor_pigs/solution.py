class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        P = 0
        x = minutesToTest // minutesToDie + 1
        while x ** P < buckets:
            P += 1
        return P
        