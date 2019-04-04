class Solution:
    def knightDialer(self, N: int) -> int:
        self.ans = 0
        nexts = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        arr = [1]*10
        for _ in range(N-1):
            newArr = [0] * 10
            for i in range(10):
                newArr[i] = sum(arr[x] for x in nexts[i])
            arr = newArr
        return sum(arr) % (10**9 + 7)
            