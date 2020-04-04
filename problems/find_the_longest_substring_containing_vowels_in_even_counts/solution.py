class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def hash(arr):
            return sum(x*y for (x, y) in zip(arr, [1, 10, 100, 1000, 10000]))
        
        earliest = {0: -1}
        curr = [0, 0, 0, 0, 0]
        d = {'a':0 , 'e':1,  'i':2 ,'o': 3,  'u': 4}
        for i, x in enumerate(s):
            if x not in d: continue
            curr[d[x]] ^= 1
            h = hash(curr)
            if h not in earliest:
                earliest[h] = i
        # print(earliest)
        ans = 0
        for i in range(len(s)-1, -1, -1):
            x = s[i]
            h = hash(curr)
            if h in earliest:
                ans = max(ans, i - earliest[h])
                # print(i, earliest[h])
            if x in d: 
                curr[d[x]] ^= 1
        return ans
        
            
        