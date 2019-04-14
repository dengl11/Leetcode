class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def search(i, expecting, parts):
            if parts[-1] > 2147483647: return []
            if i >= len(S): return parts
            if i + len(expecting) > len(S) or S[i:i+len(expecting)] != expecting: return []
            newExpect = str(parts[-1] + int(expecting))
            return search(i + len(expecting), newExpect, parts + [int(expecting)])
        
        for i in range(1, len(S) // 2 + 1):
            if S[0] == "0" and i >= 2: break
            x = int(S[:i])
            if x > 2147483647: break
            for j in range(i+1, len(S)):
                if S[i] == "0" and j-i >= 2: break
                y = int(S[i:j])
                ans = search(j, str(x + y), [x, y])
                if ans: return ans
        return []
            
            
        