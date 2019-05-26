class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        accC = [0]
        n = len(customers)
        for x in customers:
            accC.append(x + accC[-1])
        for i, x in enumerate(grumpy):
            if x == 1: customers[i] = 0
        accCG = [0]   
        for x in customers:
            accCG.append(x + accCG[-1])
        return max(accC[min(i+X-1, n)]-accC[i-1] + accCG[-1] - (accCG[min(i+X-1, n)]-accCG[i-1]) for i in range(1, n+1))