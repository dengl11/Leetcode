class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if len(expression) == 1: return expression == 't'
        op = expression[0]
        if op == "!": return not self.parseBoolExpr(expression[2:-1])
        left = 0
        i = 2
        if ")" not in expression[i:-1]:
            parts = [x == "t" for x in expression[i:-1].split(",")]
        else:
            parts = []
            for j in range(2, len(expression)):
                if expression[j] == '(':
                    left += 1
                if expression[j] == ')':
                    left -= 1
                if left == 0 and expression[j] == ")":
                    s = expression[i: j+1]
                    parts.append(self.parseBoolExpr(s))
                    i = j + 2
        return all(parts) if op == "&" else any(parts)