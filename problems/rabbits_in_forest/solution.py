from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        s = sum(answers) + len(answers)
        for k, v in c.items():
            g = k+1 # graoup size
            G = ((v-1)//g + 1)
            s -= (v-G)*g
        return s