class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        def arr2num(arr):
            amplifier = 1
            ans = 0
            for x in arr[::-1]:
                ans += x * amplifier
                amplifier *= 10
            return ans
    
        ans = []
        def collect(curr):
            if len(curr) == N:
                ans.append(arr2num(curr))
            else:
                pre = curr[-1]
                if pre + K <= 9:
                    collect(curr + [pre + K])
                if K != 0 and pre - K >= 0:
                    collect(curr + [pre - K])
                        
        for i in range(0 if N == 1 else 1, 10):
            collect([i])
        return ans
                