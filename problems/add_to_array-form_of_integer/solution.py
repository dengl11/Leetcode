class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = 0
        ans = []
        for i in range(len(A)-1, -1, -1):
            K, curr = divmod(K, 10)
            curr += carry + A[i]
            carry, curr = divmod(curr, 10)
            ans.append(curr)
        K += carry
        while K:
            K, curr = divmod(K, 10)
            ans.append(curr)
        return ans[::-1]
            