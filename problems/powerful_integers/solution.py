class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = []
        stack = [(0, 0)]
        while stack:
            i, j = stack.pop()
            # print(i, j)
            curr = x ** i + y ** j
            if curr > bound: continue
            ans.append(curr)
            if x > 1:
                stack.append((i + 1, j))
            if y > 1:
                stack.append((i, j + 1))
        return list(set(ans))
            