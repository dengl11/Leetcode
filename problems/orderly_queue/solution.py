class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K > 1:
            return "".join(sorted(S))
        return min((S*2)[i:i+len(S)] for i in range(len(S)))