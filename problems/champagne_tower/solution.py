class Solution:
    def champagneTower(self, poured: int, row: int, col: int) -> float:
        cups = [poured]
        while row > len(cups)-1:
            nexts = [0] * (len(cups) + 1)
            for i in range(len(cups)):
                if cups[i] >= 1:
                    x = cups[i]-1
                    nexts[i] += x/2
                    nexts[i+1] += x/2
            cups = nexts
        return min(1, cups[col])
            