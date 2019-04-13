class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        needs = [(target - pos) / s for (s, pos) in zip(speed, position)]
        cars = sorted(list(zip(position, needs)), reverse = True)
        ans = 0
        curr = 0
        for c in cars:
            if c[1] > curr:
                ans, curr = ans + 1, c[1]
        return ans
        