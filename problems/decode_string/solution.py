class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        s = "1[" + s + "]"
        
        def decode():
            if self.i >= len(s): return ""
            if s[self.i].isdigit():
                j = self.i
                while s[self.i].isdigit():
                    self.i += 1
                k = int(s[j:self.i])
                assert s[self.i] == '['
                self.i += 1
                ans = ""
                while 1:
                    curr = decode()
                    if curr == "": break
                    ans += curr
                    if s[self.i] == ']':
                        self.i += 1
                        break
                return k * ans
            else:
                j = self.i
                while self.i < len(s) and s[self.i].isalpha():
                    self.i += 1
                curr = s[j:self.i]
                if self.i >= len(s) or s[self.i] == ']': return curr
                return curr + decode()
        
        return decode()
