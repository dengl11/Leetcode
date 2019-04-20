from bisect import bisect_right, insort, bisect_left
class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.overlaps = []
        
    def book(self, start: int, end: int) -> bool:
        for s, t in self.overlaps:
            if t > start and s < end: return False
        for (s, t) in self.events:
            if (s < end and t > start):
                self.overlaps.append((max(s, start), min(t, end)))
        self.events.append((start, end))
        return True