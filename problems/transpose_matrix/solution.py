class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return list(list(c) for c in zip(*A))
        