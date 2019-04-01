class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans = 0
        obstacles = set(tuple(x) for x in obstacles)
        x = y = 0
        direction = 0
        for c in commands:
            if c == -2:
                direction = (direction + 1) % 4
            elif c == -1:
                direction = (direction + 3) % 4
            else:
                dx = dy = 0
                if direction == 0: dy = 1
                elif direction == 1: dx = -1
                elif direction == 2: dy = -1
                else: dx = 1
                    
                for _ in range(c):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x += dx
                    y += dy
                ans = max(ans, x ** 2 + y ** 2)
        return ans