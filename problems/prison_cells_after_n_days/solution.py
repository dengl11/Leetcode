class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def print_config(x):
            ans = []
            for i in range(7, -1, -1):
                ans.append(1 if (x & (1 << i)) else 0)
            print(ans)
            
        x = 0
        for i in range(8):
            x += cells[~i] << i
            
        # print_config(x)
        seen = {x: 0}
        i = 1
        while i <= N:
            x = (x ^ (x << 2)) >> 1
            x = ~x
            x &= 126
            if x not in seen:
                seen[x] = i
                i += 1
            else:
                cycle = i - seen[x]
                break
            # print_config(x)
        if i <= N:
            i = (N - i) % cycle
        else:
            i = 0
        while i > 0:
            x = (x ^ (x << 2)) >> 1
            x = ~x
            x &= 126
            i -= 1
            
            
        
        ans = []
        for i in range(7, -1, -1):
            ans.append(1 if (x & (1 << i)) else 0)
        return ans
        