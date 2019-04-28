from math import gcd
class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0] != "-":
            expression = "+" + expression
        pre = None
        signs = []
        for i in range(len(expression)):
            if expression[i] in ['+', '-']:
                signs.append(i)
        
        for i, idx in enumerate(signs):
            if i == len(signs) - 1:
                end = len(expression)
            else:
                end = signs[i+1]
            
            curr = expression[idx:end]
            # print(idx)
            # print(curr)
            enu, den = curr.split("/")
            if pre is None:
                pre = (int(enu), int(den))
            else:
                new_enu = int(enu) * pre[1] + int(den) * pre[0]
                new_den = int(den) * pre[1]
                g = gcd(new_enu, new_den)
                pre = (new_enu//g, new_den//g)
        return "{}/{}".format(*pre)
                
            