class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def changedir(d, ins):
            if ins == "R":
                if d[0] == 0: return (d[1], 0)
                return (0, -d[0])
            else:
                if d[0] == 0: return (-d[1], 0)
                return (0, d[0])
        (dx, dy) = (0,1)
        x = y = 0
        for c in instructions*4:
            if c == "G":
                x += dx
                y += dy
            else:
                (dx, dy) = changedir((dx, dy), c)
        return x == 0 and y == 0
            
                