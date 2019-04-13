class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        used = [False] * len(A)
        B = sorted((x, i) for i, x in enumerate(B))
        a = []
        i = 0
        for b, _ in B:
            while i < len(A) and A[i] <= b:
                i += 1
            if i >= len(A): break
            a.append(A[i])
            used[i] = True
            i += 1
        for i in range(len(A)):
            if not used[i]:
                a.append(A[i])
        ans = [None] * len(A)
        for i, val in enumerate(a):
            ans[B[i][1]] = val
        return ans
            
            
        