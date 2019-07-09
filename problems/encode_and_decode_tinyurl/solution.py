from string import ascii_letters
from random import choice
class Codec:
    alphabet = ascii_letters + "0123456789"
    
    def __init__(self):
        self.code2url = dict()
        self.url2code = dict()
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.url2code:
            code = None
            while code is None or code in self.code2url:
                code = "".join(choice(Codec.alphabet) for _ in range(6))
            self.code2url[code] = longUrl
            self.url2code[longUrl] = code
        return "http://tinyurl.com/" + self.url2code[longUrl]
            
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))