class Solution:
    def clumsy(self, N: int) -> int:
        remainder = N % 4
        nums = []
        first = True
        for i in range(N, 3, -4):
            curr = i * (i - 1) // (i-2)
            nums.append(curr if first else -curr)
            nums.append(i-3)
            first = False
        if remainder == 3:
            nums.append(6 if first else -6)
        if remainder == 2:
            nums.append(2 if first else -2)
        if remainder == 1:
            nums.append(1 if first else -1)
        return sum(nums)
        
            
            
        