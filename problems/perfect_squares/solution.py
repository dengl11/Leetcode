class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2: return n
        squares = set()
        i = 1
        while i ** 2 <= n:
            squares.add(i ** 2)
            i += 1
        q = [n]
        cnt = 1
        while q:
            nq = []
            for x in q:
                if x in squares: return cnt
                for y in squares:
                    if x > y:
                        nq.append(x - y)
            cnt += 1
            q = nq