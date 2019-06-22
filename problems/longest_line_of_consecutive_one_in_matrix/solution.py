class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M or not M[0]: return 0
        hor, ver, dig, adig = set(), set(), set(), set()
        m, n = len(M), len(M[0])
        self.ans = 0
        def search(i0, j0):
            # hor
            i, j = i0, j0
            h = 1
            if (i, j) not in hor:
                while j + 1 < n and M[i][j+1] == 1:
                    j += 1
                    h += 1
                    hor.add((i, j))
            self.ans = max(self.ans, h)
            # ver
            v = 1
            i, j = i0, j0
            if (i, j) not in ver:
                while i + 1 < m and M[i+1][j] == 1:
                    i += 1
                    v += 1
                    ver.add((i, j))
            self.ans = max(self.ans, v)
            # adig
            d = 1
            i, j = i0, j0
            if (i, j) not in dig:
                while i + 1 < m and j + 1 < n and M[i+1][j+1] == 1:
                    i += 1
                    j += 1
                    d += 1
                    dig.add((i, j))
            self.ans = max(self.ans, d)
            # adig
            ad = 1
            i, j = i0, j0
            if (i, j) not in adig:
                while i + 1 < m and j - 1 >= 0 and M[i+1][j-1] == 1:
                    i += 1
                    j -= 1
                    ad += 1
                    adig.add((i, j))
            self.ans = max(self.ans, ad)
        for i in range(m):
            for j in range(n):
                if M[i][j]:
                    search(i, j)
        return self.ans
        