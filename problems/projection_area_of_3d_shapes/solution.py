class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        bottom = sum(sum(x != 0 for x in row) for row in grid)
        row = sum(max(row) for row in grid)
        col = sum(max(row) for row in zip(*grid))
        return bottom + row + col
        