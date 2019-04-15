from collections import deque
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = deque(sorted(zip(difficulty, profit))) # [(diff, prof)]
        maxProf = 0
        worker.sort()
        total = 0
        for w in worker:
            while jobs and jobs[0][0] <= w:
                _, prof = jobs.popleft()
                maxProf = max(maxProf, prof)
            total += maxProf
        return total