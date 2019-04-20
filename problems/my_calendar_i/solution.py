from bisect import bisect_right, insort
class MyCalendar:

    def __init__(self):
        self.events = [(0,0), (float('inf'), float('inf'))]

    def book(self, start: int, end: int) -> bool:
        pos = bisect_right(self.events, (start, end))
        pre_end = self.events[pos - 1][1]
        next_start = self.events[pos][0]
        if pre_end > start or end > next_start: return False
        insort(self.events, (start, end))
        return True
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)