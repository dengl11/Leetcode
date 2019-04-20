class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        s = str(N)
        ans = [int(s[0])]
        for i in range(1, len(s)):
            if s[i] < s[i-1]:
                if len(ans) <= 1 or ans[-1]-1 >= ans[-2]:
                    ans[-1] -= 1
                else:
                    j = len(ans) - 1
                    while j > 0 and ans[j] == ans[j-1]:
                        ans[j] = 9
                        j -= 1
                    ans[j] -= 1
                    while j >= 0:
                        ans[j] = min(ans[j+1], ans[j]) 
                        j -= 1
                m = "".join(str(x) for x in ans) + "9" * (len(s) - i)
                return int(m[1:]) if m[0] == "0" else int(m)
            ans.append(int(s[i]))
        return N
                
                
            
        
        