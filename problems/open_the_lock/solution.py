class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadends = set(deadends)
        if "0000" in deadends: return -1
        q = ["0000"]
        deadends.add("0000")
        
        steps = 0
        while q:
            newq = []
            for x in q:
                if x == target: return steps
                for i in range(4):
                    for diff in [1, -1]:
                        newx = x[:i] + str((int(x[i]) + diff + 10)%10) + x[i+1:]
                        if newx not in deadends:
                            deadends.add(newx)
                            newq.append(newx)
            q = newq
            steps += 1
        return -1
            
                