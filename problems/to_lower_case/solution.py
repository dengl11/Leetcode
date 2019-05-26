class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join(chr(ord(c) | (1<<5)) for c in str)
        