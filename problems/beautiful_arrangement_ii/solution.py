class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = []
        arr = list(range(1, k+2))
        i, j = 0, k
        while i <= j:
            ans.append(arr[i])
            if j > i:
                ans.append(arr[j])
            i += 1
            j -= 1
        return ans + list(range(k+2, n + 1))
        
        