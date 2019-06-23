class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        starts = sorted((t[1],t[0]) for t in trips)
        ends = sorted((t[2],t[0]) for t in trips)
        i = 0
        for e, n in ends:
            while i < len(starts) and starts[i][0] < e: 
                capacity -= starts[i][1]
                i += 1
            if capacity < 0: return False
            capacity += n
        return True
        