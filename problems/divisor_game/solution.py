class Solution:
    def divisorGame(self, N: int) -> bool:
        win = [False] * (N + 1)
        for i in range(2, N + 1):
            for j in range(1, i//2 + 1):
                if i % j == 0 and not win[i - j]:
                    win[i] = True
                    break
        return win[-1]
                    