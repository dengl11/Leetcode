class Solution(object):
    def maxSubarraySumCircular(self, A):
        def kadane(gen):
            # Maximum non-empty subarray sum
            ans = cur = None
            for x in gen:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans

        S = sum(A)
        ans1 = kadane(iter(A))
        ans2 = S + kadane(-A[i] for i in xrange(1, len(A)-1))
        return max(ans1, ans2)