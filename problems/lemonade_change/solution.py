class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5 = c10 = 0
        for x in bills:
            if x == 5:
                c5 += 1
            elif x == 10:
                c5 -= 1
                c10 += 1
            else:
                if c10 > 0:
                    c10 -= 1
                    c5 -= 1
                else:
                    c5 -= 3
            if c5 < 0: return False
        return True
                
        