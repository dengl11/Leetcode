class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        def partner(i):
            return i-1 if i%2 else i+1
            
        pos = {x:i for (i, x) in enumerate(row)}
        ans = 0
        for i in range(0, n*2, 2):
            p = partner(row[i])
            if row[i+1] != p:
                j = pos[p]
                pos[row[i+1]] = j
                row[i+1], row[j] = row[j], row[i+1]
                ans += 1
        return ans