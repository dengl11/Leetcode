class Solution:
    def maskPII(self, S: str) -> str:
        def formatEmail(e):
            name, domain = e.lower().split("@")
            return name[0] + "*****" + name[-1] + "@" + domain
        
        def formatPhone(no):
            digits = [c for c in no if c.isdigit()]
            local = "".join(digits[-4:])
            ans = "***-***-"+local
            countryCode = len(digits) - 10
            # if "-" in no:
            #     if no[0] == "+":
            #         countryCode = min(no.find("-") - 1, 3)
            #     elif no.find("-") <= 3:
            #         countryCode = no.find("-")  
            if not countryCode:
                return ans
            return "+"+ "*" * countryCode + "-" + ans
        if "@" in S: 
            return formatEmail(S)
        return formatPhone(S)

        