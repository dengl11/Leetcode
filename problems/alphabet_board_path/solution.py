from string import ascii_lowercase
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        pos = dict()
        for i, c in enumerate(ascii_lowercase):
            pos[c] = divmod(i, 5)
        def trans(c1, c2):
            i1, j1 = pos[c1]
            i2, j2 = pos[c2]
            di = i2 - i1
            dj = j2 - j1
            if di == 0 and dj == 0: return "!"
            ans = ""
            todo = [0]*4 # [left, up, right, down]
            if dj > 0: todo[2] = dj
            elif dj: todo[0] = -dj
                
            if di > 0: todo[-1] = di
            elif di: todo[1] = -di
            return "".join(k * c for (k, c) in zip(todo, ['L', 'U', 'R', 'D'])) + "!"
        ans = ""
        curr = "a"
        for t in target:
            ans += trans(curr, t)
            curr = t
        return ans