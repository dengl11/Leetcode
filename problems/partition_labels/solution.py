class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        pos = dict() # {ch: [start, end]}
        for i, c in enumerate(S):
            if c not in pos:
                pos[c] = [i, i]
            else:
                pos[c][1] = i
        ans = []
        i = 0
        j = 0
        l = 1
        while j < len(S):
            j = max(j, pos[S[i]][1])
            if i == j:
                ans.append(l)
                i = j + 1
                j = i
                l = 1
            else:
                i += 1
                l += 1
        return ans
                
            
            
            
        