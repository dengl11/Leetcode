class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        presum = [0]
        for x in cardPoints:
            presum.append(presum[-1] + x)
        n = len(cardPoints)
        
        return presum[-1] - min(presum[i + n-k] - presum[i] for i in range(k+1))
