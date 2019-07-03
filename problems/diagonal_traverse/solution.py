class Solution:
    def findDiagonalOrder(self, M: List[List[int]]) -> List[int]:
        ans = []
        if not M or not M[0]: return ans
        m, n = len(M), len(M[0])
        i = j = 0
        up = 1
        for _ in range(m * n):
            ans.append(M[i][j])
            if up:
                if i == 0:
                    up = 1- up
                    if j == n-1:
                        i += 1
                    else:
                        j += 1
                else:
                    if j == n-1:
                        i += 1
                        up = 1- up
                    else:
                        i -= 1
                        j += 1
            else:
                if j == 0:
                    up = 1- up
                    if i == m-1:
                        j += 1
                    else:
                        i += 1
                else:
                    if i == m-1:
                        up = 1- up
                        j += 1
                    else:
                        j -= 1
                        i += 1
        return ans