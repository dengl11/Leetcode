class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max = None
        self.pos = []
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.max is None or self.max < x:
            self.max = x
            self.pos = [len(self.stack)-1]
        elif self.max == x:
            self.pos.append(len(self.stack)-1)
        

    def pop(self) -> int:
        if self.stack[-1] == self.max:
            return self.popMax()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def peekMax(self) -> int:
        return self.max

    def refresh(self):
        self.max = max(self.stack, default = None)
        self.pos = [i for (i, x) in enumerate(self.stack) if x == self.max]
        

    def popMax(self) -> int:
        ans = self.peekMax()
        idx = self.pos.pop()
        del self.stack[idx]
        if not self.pos:
            self.refresh()
        return ans
            
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()