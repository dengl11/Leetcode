class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        lastTurnedOn = -1
        on = [False] * len(light)
        ans = 0
        light = [x-1 for x in light]
        for i, x in enumerate(light):
            on[x] = True
            if lastTurnedOn == x-1:        
                while lastTurnedOn + 1 < len(light) and on[lastTurnedOn+1]:
                    lastTurnedOn += 1
                if i == lastTurnedOn:
                    ans += 1
        return ans
                
        