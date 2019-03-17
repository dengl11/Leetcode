class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for r in A:
            r.reverse()
        return [[(1-x) for x in r] for r in A]
        