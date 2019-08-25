class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = [[]]
        self.left = self.right = -1
        self.cap = capacity
        

    def push(self, val: int) -> None:
        self.stacks[self.left].append(val)
        if self.left > self.right:
            self.right = self.left
        while self.left < len(self.stacks) and len(self.stacks[self.left]) == self.cap:
            self.left += 1
            
        if self.left >= len(self.stacks):
            self.stacks.append([])
            
        # print("push: ", val, self.stacks)


    def pop(self) -> int:
        # print(self.right)
        if not self.stacks[self.right]: return -1
        ans = self.stacks[self.right].pop()
        while self.right and not self.stacks[self.right]:
            self.right -= 1
        # print("pop: ", ans, self.stacks)
        return ans
        

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]: return -1
        ans = self.stacks[index].pop()
        if index < self.left:
            self.left = index
        # while len(self.stacks[self.left]) == self.cap and self.left + 1 < len(self.stacks):
        #     self.left += 1
        # print("popAtStack: ", index, ans, self.stacks, self.left)
        return ans
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)