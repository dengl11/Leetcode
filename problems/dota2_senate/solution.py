from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ans = None
        
        while ans is None:
            rpower = 0
            rs, ds = deque([]), deque([])
            for i, x in enumerate(senate):
                if x == "R":
                    if rpower < 0:
                        rpower +=1
                    else:
                        rpower += 1
                        rs.append(i)
                else:
                    if rpower > 0:
                        rpower -=1
                    else:
                        rpower -= 1
                        ds.append(i)
            for _ in range(0, rpower):
                if ds: ds.popleft()
            for _ in range(0, -rpower):
                if rs: rs.popleft()
            if not rs:
                ans = "Dire"
            if not ds:
                ans = "Radiant"
            if ans is None:
                senate = ""
                while rs and ds:
                    if rs[0] < ds[0]: 
                        rs.popleft()
                        senate += "R"
                    else: 
                        ds.popleft()
                        senate += "D"
                if rs: senate += "R" * len(rs)
                if ds: senate += "D" * len(ds)
        return ans
                
        
        