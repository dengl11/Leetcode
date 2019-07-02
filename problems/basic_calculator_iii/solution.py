class Solution:
    def calculate(self, s: str) -> int:
        """
		:type s: str
		:rtype: int
		"""
        self.i = 0
        self.ans = 0
        s = "(" + s.replace(" ", "") + ')'
        def div(x, y):
            if x * y > 0: return x // y
            return -(abs(x) // abs(y))
        def expr():
            c = s[self.i]
            # print("-=-=-=-=-=")
            # print(c)
            if c in " ":
                self.i += 1
                return expr()
            if c == "(":
                self.i += 1
                stack = []
                stack.append(expr())
                while s[self.i]!=")":
                    # print(stack)
                    if s[self.i] in "*/":
                        c = s[self.i]
                        self.i += 1
                        # print("s[self.i] = ", s[self.i])
                        if c == "*":
                            stack.append(stack.pop() * expr())
                        else:
                            stack.append(div(stack.pop(), expr()))
                    elif s[self.i] in "+-":
                        stack.append(expr())
                self.i += 1 
                # print(s[self.i], stack)
                return sum(stack)
            if c in "+-":
                self.i += 1
                ans = expr()
                return ans if c == "+" else -ans
            if c.isdigit():
                j = self.i
                while self.i <len(s) and s[self.i].isdigit():
                    self.i += 1
                return int(s[j:self.i])
        return expr()