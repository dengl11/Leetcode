class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i = 1
        ans = ""
        while i <= len(num1) or i <= len(num2):
            x1 = int(num1[-i]) if i <= len(num1) else 0
            x2 = int(num2[-i]) if i <= len(num2) else 0
            carry, curr = divmod(x1 + x2 + carry, 10)
            ans += str(curr)
            i += 1
        if carry:
            ans += str(carry)
        return ans[::-1]
            
        
        