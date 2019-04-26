class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(s):
            nx = val = 0
            sign = 1
            i = 0
            while i < len(s):
                if s[i] in ['+', '-']:
                    sign = 1 if s[i] == '+' else -1
                    i += 1
                else:
                    j = i
                    while j+1 < len(s) and s[j+1] not in ['+', '-']:
                        j += 1
                    if s[j] == 'x':
                        nx += sign * (int(s[i:j]) if j > i else 1)
                    else:
                        val += sign * int(s[i:j+1])
                    i = j+1
            return (nx, val)
        nx1, val1 = parse(equation[:equation.index('=')])
        nx2, val2 = parse(equation[equation.index('=')+1:])
        nx = nx1 - nx2
        val = val2 - val1
        if nx == 0:
            return "Infinite solutions" if val == 0 else  "No solution"
        return "x={}".format(val // nx)
                        
                    
