class Solution:
    def rotatedDigits(self, N: int) -> int:
        ans = set()
        frontier = {'2', '5', '6', '9'}
        while True:
            add = {int(x) for x in frontier if int(x)<= N and x[0]!="0"}
            if not add: return len(ans)
            ans |= add
            new = set()
            for x in frontier:
                new |= {x + str(i) for i in [0, 1, 2, 5, 6, 9, 8]}
                new |= {str(i) + x for i in [0, 1, 2, 5, 6, 9, 8]}
            frontier = new
            