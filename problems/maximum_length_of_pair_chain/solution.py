class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1]) # sort by end
        ans = 1
        end = pairs[0][1]
        for curr in range(1, len(pairs)):
            if pairs[curr][0] <= end: 
                continue
            ans += 1
            end = pairs[curr][1]
        return ans
            
            