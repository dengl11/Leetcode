class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        bAdded = (sum(A) + sum(B)) // 2 - sum(B)
        a, b = set(A), set(B)
        for sa in a:
            if (sa - bAdded) in b:
                return [sa, sa - bAdded]