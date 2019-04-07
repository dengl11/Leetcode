class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U'}
        def transform(w):
            if w[0] in vowels:
                return w + "ma"
            return w[1:] + w[0] + "ma"
        
        words = S.split()
        for i, w in enumerate(words):
            words[i] = transform(w) + 'a' * (i + 1)
        return " ".join(words)
            