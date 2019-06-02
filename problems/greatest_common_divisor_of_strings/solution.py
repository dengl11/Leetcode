class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) < len(str1): str2, str1 = str1, str2
        n1, n2 = len(str1), len(str2)
        i = n1
        while i:
            if n1 % i == 0 and n2 % i == 0:
                g = str1[:i]
                g1, g2 = n1//i, n2//i
                if str1 == g * g1 and str2 == g * g2:
                    return g
            i -= 1
        return ""
        