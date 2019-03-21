class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        arr = []
        curr = sum(x for x in A if x%2 == 0)
        for val, i in queries:
            old = A[i]
            A[i] += val
            if old % 2 == 0:
                curr -= old
            if (val + old) % 2 == 0:
                curr += val + old
            arr.append(curr)
        return arr
        