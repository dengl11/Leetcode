class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        n = len(A)
        tags = [0] * n
        for i, x in enumerate(A):
            if x > R: tags[i] = 1
            elif x < L: tags[i] = -1
        
        i = 0
        ans = 0
        def add(i, j):
            if i >= j or not anchors: return 0
            x = j-i
            ans = x * (x + 1) // 2
            pre = i
            for x in anchors:
                ans -= (x-pre) * (x-pre + 1) // 2
                pre = x+1
            ans -= (j-pre) * (j-pre + 1) // 2
            return ans
            
            
            
        anchors = []
        for j, x in enumerate(A):
            if tags[j] > 0:
                ans += add(i, j)
                anchors = []
                i = j + 1
            elif tags[j] == 0:
                anchors.append(j)
                
        ans += add(i, n)
        return ans
        