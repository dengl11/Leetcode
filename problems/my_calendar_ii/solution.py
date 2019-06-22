from bisect import insort
class MyCalendarTwo:

    def __init__(self):
        self.starts = []
        self.ends = []
        

    def book(self, start: int, end: int) -> bool:
        insort(self.starts, start)
        insort(self.ends, end)
        curr = 0
        i = 0
        for j, e in enumerate(self.ends):
            while i < len(self.starts) and self.starts[i] < e:
                curr += 1
                i += 1
            if curr >= 3: 
                self.starts.remove(start)
                self.ends.remove(end)
                return False
            curr -= 1
        return True
        
