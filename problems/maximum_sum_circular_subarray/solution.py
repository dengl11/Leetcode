class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        ans = curr = A[0]
        n = len(A)
        for x in A[1:]:
            curr = x + max(curr, 0)
            ans = max(ans, curr)
        postfix = [0] * (n - 1)
        prefix = postfix[:]
        presum = prefix[0] = A[0]
        for i in range(1, n-1):
            presum += A[i]
            prefix[i] = max(presum, prefix[i-1])
        postfix[0] = postsum = A[-1]
        for i in range(1, n-1):
            postsum += A[~i]
            postfix[i] = max(postsum, postfix[i-1])
        for i in range(1, n):
            ans = max(ans, prefix[i-1] + postfix[n - i - 1])
        return ans
            
            
        
            
            