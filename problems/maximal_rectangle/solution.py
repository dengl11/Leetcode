class Solution:
    def maximalRectangle(self, M: List[List[str]]) -> int:
        if not M or not M[0]: return 0
        m, n = len(M), len(M[0])
        ans = 0
        left = [0]*n
        right = [n]*n
        heights = [0]*n
        for i in range(m):
            l , r = 0, n-1
            for j in range(n): 
                # height
                if M[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            for j in range(n): 
                # left
                if M[i][j] == "0":
                    left[j] = 0
                    l = j + 1
                else:
                    left[j] = max(left[j], l)
            for j in range(n-1, -1, -1):
                if M[i][j] == "0":
                    right[j] = n-1
                    r = j - 1
                else:
                    right[j] = min(right[j], r)
        
            for j in range(n): 
                ans = max(ans, (right[j] - left[j] + 1) * heights[j])
        return ans
                
                
            
