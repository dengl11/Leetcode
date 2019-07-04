S = 1
M = 60
H = 60 * M
D = 24 * H
MM = 100 * D
Y = 100 * MM

d = {"Second": 6, "Minute": 5, "Hour": 4, "Day":3, "Month": 2, "Year": 1}
def parse(s, gra = "Second", roundUp = False):
    domains = [int(x) for x in s.split(":")]
    end = d[gra]
    if roundUp and gra != "Second":
        domains[end-1] += 1
    for i in range(end, len(domains)):
        domains[i] = 0
    ans = sum(x * y for (x, y) in zip([Y, MM, D, H, M, S], domains))
    return ans

from bisect import bisect_left as bl, bisect_right as br, insort
class LogSystem:

    def __init__(self):
        self.logs = []
        
    def put(self, id: int, timestamp: str) -> None:
        t = parse(timestamp)
        insort(self.logs, (t, id))

    def retrieve(self, s0: str, e0: str, gra: str) -> List[int]:
        s, e = parse(s0, gra), parse(e0, gra, roundUp = True)
        left = bl(self.logs, (s, 0))
        right = br(self.logs, (e, float("inf")))
        ans = [x[1] for x  in self.logs[left:right]]
        return ans


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)