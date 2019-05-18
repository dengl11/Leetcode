class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        ans = 0
        q = [(A, 0)]
        visited= set([A])
        n = len(A)
        for x, ans in q:
            perfect = True
            for i in range(len(x)):
                if B[n-len(x)+i] == x[i]: continue
                for j in range(i+1, len(x)):
                    if B[n-len(x)+i] == x[j]:
                        c = x[:i]+x[j]+x[i+1:j] + x[i]+ x[j+1:]
                        c = c[1:]
                        if c not in visited:
                            q.append((c, ans + 1))        
                            visited.add(c)
                perfect = False
                break
            if perfect: return ans