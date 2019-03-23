from collections import defaultdict
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        EM = set()
        lowercases = defaultdict(list) # {w: [...]}
        nonVowels = defaultdict(list)  # {(w, n): [...]}
        vowels = {'a', 'e', 'i', 'o', 'u'}
        def trim(w):
            curr = ""
            for ch in w.lower():
                if ch in vowels: 
                    curr += '*'
                else:
                    curr += ch
            return curr
        
        for w in wordlist:
            EM.add(w)
            lowercases[w.lower()].append(w)
            nonVowels[trim(w)].append(w)
            
        ans = []
        for w in queries:
            if w in EM:
                ans.append(w)
            elif w.lower() in lowercases:
                ans.append(lowercases[w.lower()][0])
            else:
                key = trim(w)
                if key in nonVowels:
                    # print(key, nonVowels[key])
                    ans.append(nonVowels[key][0])
                else:
                    ans.append("")
        return ans
                    
                
        