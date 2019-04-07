from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        needed = [0]*26
        for b in B:
            for c, cc in Counter(b).items():
                i = ord(c) - ord('a')
                needed[i] = max(needed[i], cc)
                
        ans = []
        def ok(a):
            counter = Counter(a)
            for i in range(26):
                have = counter[chr(97 + i)]
                if have < needed[i]:return False
            return True
            
        
        for a in A:
            if ok(a):
                ans.append(a)
        return ans
            