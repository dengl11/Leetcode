from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = Counter(moves)
        return moves['U'] == moves['D'] and moves['R'] == moves['L']
        