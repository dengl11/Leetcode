class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        # def depth(arr):
        #     left = 0
        #     d = 0
        #     ans = 0
        #     for c in arr:
        #         if c == "(": 
        #             left += 1
        #         else: 
        #             left -= 1
        #             d += 1
        #             ans = max(ans, d)
        #         if left == 0:
        #             d = 0
        #         return ans
        A, B = [], []
        open = [0, 0]
        for i, c in enumerate(seq):
            if c == "(":
                if open[0] < open[1]:
                    A.append(i)
                    open[0] += 1
                else:
                    B.append(i)
                    open[1] += 1
            else:
                if open[0] > 0:
                    A.append(i)
                    open[0] -= 1
                else:
                    B.append(i)
                    open[1] -= 1
        ans = [0] * len(seq)
        for x in A:
            ans[x] = 1
        return ans
