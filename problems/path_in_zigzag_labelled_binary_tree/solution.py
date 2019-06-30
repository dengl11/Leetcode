from math import sqrt
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = []
        D = 1 # Depth of label
        while (1 << D) - 1 < label:
            D += 1
            
        while label != 1:
            ans.append(label)
            label //= 2
            D -= 1
            # same as label ^= 1<< highest_on_bit(label)
            label = (1 << D) + (1 << (D-1)) - 1 - label
            
        return [1] + ans[::-1]
            