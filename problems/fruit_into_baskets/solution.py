from collections import defaultdict
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        c = defaultdict(int)
        c[tree[0]] = 1
        ans = 1
        i = 0
        j = 1
        while j < len(tree):
            c[tree[j]] += 1
            while len(c) > 2:
                c[tree[i]] -= 1
                if c[tree[i]] == 0:
                    del c[tree[i]]
                i += 1
            ans = max(j - i + 1, ans)
            j += 1
        return ans
            
            
        
        