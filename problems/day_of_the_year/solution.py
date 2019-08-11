class Solution:
    def dayOfYear(self, date: str) -> int:
        def special(year):
            if year % 4: return False
            if year % 100 == 0:
                if year % 400 == 0: return True
                return False
            return True
        y, m, d = date.split("-")
        y, m, d = int(y), int(m), int(d)
        ans = d
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        ans += sum(days[:m]) + (m > 2 and special(y))
        return ans