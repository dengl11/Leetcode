from math import factorial
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def is_prime(x):
            if x <= 1: return False
            i = 2
            while i ** 2 <= x:
                if x % i == 0: return False
                i += 1
            return True
        nprime = sum(is_prime(i) for i in range(1, n + 1))
        return (factorial(nprime) * factorial(n - nprime)) % (10** 9 + 7)
