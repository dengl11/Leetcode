from collections import defaultdict
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def trim(name):
            name = name.replace(".", "")
            return name[:name.find("+")]
        
        uniqEmails = defaultdict(set)
        for e in emails:
            localName, domainName = e.split('@')
            uniqEmails[domainName].add(trim(localName))
        return sum(len(x) for x in uniqEmails.values()) if uniqEmails else 0
            