class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        stack = []
        for x in asteroids:
            if x < 0:
                exploded = False
                while stack and stack[-1] <= -x:
                    pre = stack.pop()
                    if x == -pre: 
                        exploded = True
                        break
                if stack: exploded = True
                if not exploded:
                    ans.append(x)
            else:
                stack.append(x)
        return ans + stack
                    
        