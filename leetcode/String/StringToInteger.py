import sys
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        maxDiv10 = (int)(2147483647/10)
        i,n = 0,len(str)
        while i<n and str[i].isspace(): i += 1
        sign = 1
        if i < n and str[i] == '+':
            i += 1
        elif i < n and str[i] == '-':
            sign = -1
            i += 1
        num = 0
        while i < n and str[i].isnumeric():
            digit = (int)(str[i])
            if num > maxDiv10 or num == maxDiv10 and digit > 7:
                return 2147483647 if sign == 1 else -2147483648
            num = num * 10 + digit
            i += 1
        return sign * num

s = Solution()
print(s.myAtoi(' -43'))