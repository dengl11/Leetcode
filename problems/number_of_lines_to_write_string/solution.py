class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines = 1
        curr = 0
        for c in S:
            n = widths[ord(c) - 97]
            if n + curr > 100:
                lines += 1
                curr = n
            else:
                curr += n
        return lines, curr
        