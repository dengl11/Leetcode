class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        di = min(b-a for (a, b) in zip(arr, arr[1:]))
        return [[a, b] for (a, b) in zip(arr, arr[1:]) if b-a == di]
        