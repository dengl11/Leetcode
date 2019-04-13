class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = layer = 0
        for a, b in zip(S, S[1:]):
            if a + b == "()":
                ans += 1 << layer
            layer += 2 * (a == '(') - 1
        return ans