from collections import defaultdict
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        Trie = lambda: defaultdict(Trie)
        root = Trie()
        
        for x in nums:
            node = root
            for i in range(31, -1, -1):
                node = node[(x >> i) & 1]
                
        ans = 0
        for x in nums:
            node = root
            A = 0
            for i in range(31, -1, -1):
                A <<= 1
                curr = (x >> i) & 1
                if (1^curr) in node:
                    A += 1
                    node = node[1^curr]
                else:
                    node = node[curr]
            ans = max(ans, A)
        return ans
                    
                
        