from collections import deque
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.W = width
        self.H = height
        self.body = deque([(0, 0)])
        self.set = set([(0, 0)])
        self.score = 0
        self.food = [tuple(x) for x in food][::-1]

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        dx, dy = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}[direction]
        x, y = self.body[0]
        x += dx
        y += dy
        if x < 0 or x >= self.H or y < 0 or y >= self.W:
            return -1
        
        if self.food and self.food[-1] == (x, y):
            self.score += 1
            self.food.pop()
        else:
            self.set.remove(self.body.pop())
        
        self.body.appendleft((x, y))
        if (x, y) in self.set: 
            return -1
        self.set.add((x, y))
        
        return self.score
        
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)