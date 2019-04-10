class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        popped = 0
        while self.stack and self.stack[-1][0] <= price:
            pre, n = self.stack.pop()
            popped += n
        self.stack.append((price, popped + 1))
        return popped + 1
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)