class Solution:
    def calculate(self, s: str) -> int:
        self.i = 0
        self.sign = [1]
        s = "(" + s + ")"
        def expr():
            c = s[self.i]
            if c == " ":
                self.i += 1
                return expr()
            if c.isdigit():
                j = self.i
                while self.i < len(s) and s[self.i].isdigit():
                    self.i += 1
                return int(s[j:self.i])
            if c == '(':
                self.i += 1
                ans = 0
                while s[self.i] != ')':
                    ans += expr()
                self.i += 1
                return ans
            if c in "+-":
                self.i += 1
                ans = expr()
                return ans if c == "+" else -ans
            return 0
                
        return expr()