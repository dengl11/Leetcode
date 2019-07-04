class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(curr, left):
            if len(curr) == n * 2:
                if left == 0:
                    ans.append(curr)
            else:
                if left > 0:
                    dfs(curr + ")", left - 1)
                dfs(curr + "(", left + 1)
        dfs("", 0)
        return ans
            