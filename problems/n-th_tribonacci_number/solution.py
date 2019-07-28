class Solution:
    def tribonacci(self, n: int) -> int:
        acc = [0, 1, 1]
        if n <= 2: return acc[n]
        for _ in range(n-2):
            acc.append(sum(acc[-3:]))
        return acc[-1]
        