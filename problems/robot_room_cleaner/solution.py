# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, r):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        def dfs(i, j, angle):
            if (i, j) in visited: return
            visited.add((i, j))
            r.clean()
            for _ in range(4):
                if r.move():
                    di = dj = 0
                    if angle == 0: dj = 1
                    if angle == 90: di = 1
                    if angle == 180: dj = -1
                    if angle == 270: di = -1
                    dfs(i+di, j+dj, angle)
                    r.turnRight()
                    r.turnRight()
                    r.move()
                    r.turnRight()
                    r.turnRight()
                r.turnRight()
                angle = (angle + 90) % 360
        
        dfs(0, 0, 0)
                    
        