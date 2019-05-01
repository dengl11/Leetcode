import random
class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.n = n_rows * n_cols
        self.curr = self.n
        self.col = n_cols
        self.used = dict()

    def flip(self) -> List[int]:
        self.curr -= 1
        i = random.randint(0, self.curr)
        val = self.used.get(i, i)
        self.used[i] = self.used.get(self.curr, self.curr)
        r, c = divmod(val, self.col)
        return r, c

    def reset(self) -> None:
        self.curr = self.n
        self.used = dict()
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()