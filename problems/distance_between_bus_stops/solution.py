class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, dst: int) -> int:
        if start > dst: start, dst = dst, start
        d = sum(distance[start: dst])
        return min(d, sum(distance) - d)