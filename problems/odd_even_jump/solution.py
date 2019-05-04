from bisect import bisect, insort
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        nextB, nextS = [0]*n, [0]*n
        q1 = [(A[-1], n-1)]
        q2 = [(A[-1], -n+1)]
        
        for i in range(n-2, -1, -1):
            j = bisect(q1, (A[i], i))
            if j < len(q1): 
                nextB[i] = q1[j][1]
            j = bisect(q2, (A[i], -i))
            if j > 0: nextS[i] = -q2[j-1][1]
            insort(q1, (A[i], i))
            insort(q2, (A[i], -i))
            
            
        odds, evens = [False]*n, [False]*n
        odds[-1] = evens[-1] = True
        for i in range(n-2, -1, -1):
            odds[i] = evens[nextB[i]]
            evens[i] = odds[nextS[i]]
        return sum(odds)