class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        pi = [0] * len(B)
        k = 0
        for i in range(1, len(B)):
            while k and B[k] != B[i]:
                k = pi[k-1]
            if B[k] == B[i]:
                k += 1
            pi[i] = k
                
        def match(S, P):
            k = 0
            for i, c in enumerate(S):
                while k and P[k] != c:
                    k = pi[k-1]
                if P[k] == c:
                    k += 1
                if k == len(P):
                    return True
            return False
        
        n = -(-len(B)//len(A)) # round up
        for i in range(n, n+2):
            if match(A*i, B):
                return i
        return -1
                    
        