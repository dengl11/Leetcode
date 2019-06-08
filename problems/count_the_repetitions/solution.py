class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        pass2s = [-1]*(len(s2) + 1)
        index2s = [-1]*(len(s2) + 1)
        pass2s[0] = index2s[0] = 0
        index2 = 0
        pass2 = 0
        for pass1 in range(1, n1+1):
            for index1 in range(len(s1)):
                if s1[index1] == s2[index2]:
                    # print(index1, index2, s2[index2], len(index2s))
                    # print(pass1)
                    index2 += 1
                    if index2 == len(s2):
                        index2 = 0
                        pass2 += 1
            index2s[pass1] = index2
            pass2s[pass1] = pass2
            # detect repeating pattern
            for i in range(pass1):
                if index2s[i] == index2:
                    repeating_counts, remain = divmod(n1 - i, pass1 - i)
                    ans = repeating_counts * (pass2s[pass1]-pass2s[i])
                    ans += pass2s[i + remain]
                    return ans // n2
        return pass2s[n1] // n2
                    
        