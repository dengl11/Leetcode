class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n = len(target)
        if len(stamp) > n: return []
        S = list(target)
        steps = []
        def updated(i):
            ans = False
            for j in range(len(stamp)):
                if S[i+j] == "*": continue
                if S[i+j] != stamp[j]: return False
                ans = True
            if ans:
                steps.append(i)
                for j in range(len(stamp)):
                    S[i+j] = "*"
            return ans
        updating = True
        while updating:
            curr = False
            for i in range(n-len(stamp)+1):
                curr = curr or updated(i)
            updating = curr
        if all(x=="*" for x in S): return steps[::-1]
        return []
                
                