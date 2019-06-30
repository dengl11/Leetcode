from functools import lru_cache
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        @lru_cache(None)
        def query(i):
            if i < 0: return 0
            h = books[i][1]
            H = h + query(i-1)
            w = shelf_width - books[i][0]
            j = i - 1
            while j >= 0 and w >= books[j][0]:
                h = max(h, books[j][1])
                H = min(H, h + query(j-1))
                w -= books[j][0]
                j -= 1
            return H
        return query(len(books) - 1)
                