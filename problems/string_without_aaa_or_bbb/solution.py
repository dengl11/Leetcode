class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        a, b = 'a', 'b'
        if A < B:
            a, b = 'b', 'a'
            A, B = B, A
        if A == 0: return b * B
        # now A >= B
        n, remainA = divmod(A, 2)
        segments = []
        if n <= 1:
            return "".join([a * n * 2, b * (B - B//2) , a * remainA, b * (B//2)])
        else:
            if remainA == 0:
                n -= 1
                remainA = 2

            segments = [a * 2 + b] * n + [a * remainA]
            B -= n
            if B > 0:
                for i in range(len(segments)):
                    segments[i] += b
                    B -= 1
                    if B == 0: break
            return "".join([b] * B + segments)