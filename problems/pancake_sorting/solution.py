class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        flips = []
        curr = A
        for i in range(len(A) - 1, 0, -1):
            _, pos = max((x, i) for (i, x) in enumerate(curr))
            flips.append(pos + 1)
            flips.append(i + 1)
            curr = curr[:pos:-1] + curr[:pos]
        return flips
            
        