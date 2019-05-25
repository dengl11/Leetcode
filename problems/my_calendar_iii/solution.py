from collections import Counter
class MyCalendarThree:

    def __init__(self):
        self.timeline = Counter()
        self.k = 0
        

    def book(self, start: int, end: int) -> int:
        self.timeline[start] += 1
        self.timeline[end] -= 1
        curr = 0
        for k in sorted(self.timeline.keys()):
            v = self.timeline[k]
            curr += v
            self.k = max(self.k, curr)
        return self.k
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)