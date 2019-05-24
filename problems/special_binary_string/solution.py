class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = count = 0
        parts = []
        for j, c in enumerate(S):
            count += 1 if c == '1' else -1
            if count == 0:
                parts.append("1" + self.makeLargestSpecial(S[i+1:j]) + "0")
                i = j + 1
        return "".join(sorted(parts, reverse=True))
                