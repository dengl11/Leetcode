class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digLogs, letLogs = [], []
        for l in logs:
            last = l.split()[-1]
            if last.isdigit():
                digLogs.append(l)
            else:
                letLogs.append(l)
        def getKey(l):
            words = l.split()
            return (" ".join(words[1:]), words[0])
        letLogs.sort(key = getKey)
        return letLogs + digLogs