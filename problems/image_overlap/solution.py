class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        def getOnes(mat):
            return [(i, j) for i in range(n) for j in range(n) if mat[i][j] == 1]
        aOnes = getOnes(A)
        bOnes = getOnes(B)
        bs = set(bOnes)
        translations = set()
        ans = 0
        for pi in aOnes:
            for pj in bOnes:
                dx, dy = pj[0] - pi[0], pj[1] - pi[1]
                if (dx, dy) in translations: continue
                translations.add((dx, dy))
                newAs = [(x+dx, y + dy) for (x, y) in aOnes if (x+dx) >= 0 and (x+dx) < n and (y + dy) >= 0 and (y + dy) < n]
                ans = max(ans, len(set(newAs) & bs))
        return ans
        