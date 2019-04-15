class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def is_prime(x):
            if x < 2: return False
            for i in range(2, x//2 + 1):
                if x % i == 0: return False
            return True
        ans = 0
        for i in range(L, R + 1):
            if is_prime(bin(i)[2:].count("1")):
                ans += 1
        return ans
        