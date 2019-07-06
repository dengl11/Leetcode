from collections import Counter, defaultdict
class Solution(object):
    def topKFrequent(self, nums, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        inv = defaultdict(list)
        for k, v in c.items():
            inv[v].append(k)
            
        ans = []
        for k in sorted(inv.keys(), reverse=True):
            if not K: break
            curr = inv[k][:K]
            K -= len(curr)
            ans += curr
        return ans
            
            
        