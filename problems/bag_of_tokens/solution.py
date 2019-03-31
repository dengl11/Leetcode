from collections import deque
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort(reverse = True)
        tokens = deque(tokens)
        score = 0
        while tokens:
            while tokens and P >= tokens[-1]:
                P -= tokens.pop()
                score += 1
            if score > 0:
                if len(tokens) >= 2:
                    P += tokens.popleft() - tokens.pop()
                else:
                    return score
            else:
                return score
        return score
