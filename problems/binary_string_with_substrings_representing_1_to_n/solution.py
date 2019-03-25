class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for x in range(1, N + 1):
            s = bin(x)[2:]
            if not s in S: return False
        return True
        