class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        ans = 0
        i = 0
        sentence = [len(x) for x in sentence]
        starts = {} # {i^th word: (completed, rows)}
        R = 1
        while R <= rows:
            if i in starts: 
                T = R - starts[i][1] # period
                finished = ans - starts[i][0]
                x = (rows - R) // T
                ans += x * finished
                R += x * T
            starts[i] = (ans, R)
            r = cols
            while r >= sentence[i]:
                r -= sentence[i] + 1
                i += 1
                if i >= len(sentence):
                    i = 0
                    ans += 1
            R += 1
        return ans