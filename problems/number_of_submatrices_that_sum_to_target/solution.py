from collections import Counter
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        rowPrefix = [[0]*(n+1) for _ in range(m)]
        for i, r in enumerate(matrix):
            for j, v in enumerate(r):
                rowPrefix[i][j+1] = rowPrefix[i][j] + v
        
        ans = 0
        for j1 in range(n):
            for j2 in range(j1, n):
                c = Counter()
                c[target] = 1
                acc = 0
                for i in range(m):
                    acc += rowPrefix[i][j2+1] - rowPrefix[i][j1]
                    ans += c[acc]
                    c[acc + target] += 1
        return ans
                    
                
        