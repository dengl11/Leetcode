class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        curr = A[0]
        ans = [curr % 5 == 0]
        for x in A[1:]:
            curr = curr*2 + x
            ans.append(curr % 5 == 0)
        return ans