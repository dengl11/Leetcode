from heapq import heappush, heappop
class ExamRoom:

    def __init__(self, N: int):
        self.slots = [(-N, 0, 0, N - 1)]
        self.N = N
        self.starts = {0: (0, N-1)} # {start: (i, j)}
        self.ends = {N-1: (0, N-1)} # {ends: (i, j)}
        

    def seat(self) -> int:
        # print(self.slots)
        while self.slots:
            _, _, i, j = heappop(self.slots)
            if i not in self.starts or j != self.starts[i][-1]: continue
            if i == 0: seat = 0
            elif j == self.N -1: seat = j
            else: seat = (i + j) // 2
                
            del self.starts[i]
            del self.ends[j]
            if seat > i:
                self.push(i, seat - 1)
            if seat < j:
                self.push(seat+1, j)
            return seat
        
    def push(self, left, right):
        d = (right + left) // 2 - left
        if left == 0:
            d = right
        if right == self.N-1:
            d = self.N-1 - left
        heappush(self.slots, (-d, left, left, right))  
        self.starts[left] = (left, right)
        self.ends[right] = (left, right)
        
        

    def leave(self, p: int) -> None:
        left = right = p
        if p > 0 and (p-1) in self.ends:
            left = self.ends[p-1][0]
            del self.ends[p-1]
        if p < self.N-1 and (p + 1) in self.starts:
            right = self.starts[p+1][1]
            del self.starts[p+1]
        self.push(left, right)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)