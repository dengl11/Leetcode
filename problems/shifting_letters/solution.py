class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        S = S[::-1]
        shifts = shifts[::-1]
        arr = []
        curr = 0
        for s, c in zip(shifts, S):
            curr += s
            arr.append((ord(c) + curr - 97) % 26)
        return "".join(chr(c + 97) for c in arr[::-1])
            
        
        