class Solution:
    def primePalindrome(self, N: int) -> int:
        def is_prime(x):
            if x <= 2 or x % 2 == 0: return x == 2
            for i in range(3, int(x ** 0.5 + 1), 2):
                if x % i == 0: return False
            return True
        if N >= 8 and N <= 11: return 11
        for i in range(10 ** (len(str(N)) // 2), 10 ** 5):
            x = str(i) + str(i)[-2::-1]
            if int(x)  >= N and is_prime(int(x)): return int(x)
        