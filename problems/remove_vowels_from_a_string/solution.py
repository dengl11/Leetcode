class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        v = "aeiou"
        return "".join(c for c in S if c not in v)