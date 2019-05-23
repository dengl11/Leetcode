class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if (tx == sx): return ty >= sy and (ty-sy)%sx == 0
        if (ty == sy): return tx >= sx and (tx-sx)%sy == 0
        stack = [(tx, ty)]
        while stack:
            x, y = stack.pop()
            if x > y and (x - y) >= sx:
                stack.append((x-y, y))
                if (x-y, y) == (sx, sy): return True
            if y > x and (y - x) >= sy:
                stack.append((x, y-x))
                if (x, y-x) == (sx, sy): return True
        return False
            