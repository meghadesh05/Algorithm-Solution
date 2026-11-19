class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s:
            return 0

        sign = 1
        i =0

        if s[0] == "-":
            sign = -1
            i +=1
        elif s[0] == "+":
            sign = 1
            i +=1

        num = 0

        for j in range(i, len(s)):
            if s[j].isdigit():
                digit = int(s[j])
                num = num * 10 + digit
            else:
                break

        num = num * sign

        INT_MIN = -(2**31)
        INT_MAX = (2**31) - 1

        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX

        return num        
