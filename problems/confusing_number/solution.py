class Solution:
    def confusingNumber(self, N: int) -> bool:
        same = {1, 0, 8}
        diff = {6:9, 9:6}
        N = str(N).rstrip("0")
        ans = ""
        for x in N:
            i = int(x)
            if i in same: 
                ans += x
            elif i in diff: 
                ans += str(diff[i])
            else:
                return False
        return N != ans[::-1]