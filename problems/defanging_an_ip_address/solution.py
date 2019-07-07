class Solution(object):
    def defangIPaddr(self, add):
        """
        :type address: str
        :rtype: str
        """
        return add.replace(".", "[.]")
        