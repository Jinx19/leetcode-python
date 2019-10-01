class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, n = 0, len(s)
        while i < n and s[i].isspace():
            i += 1
        if i < n and s[i] == '+' or s[i] == '-':
            i += 1
        isNumber = False
        while i < n and s[i].isnumeric():
            isNumber = True
            i += 1
        if i < n and s[i] == '.':
            i += 1
            while i < n and s[i].isnumeric():
                i += 1
                isNumber = True
        if i < n and s[i] == 'e':
            i += 1
            isNumber = False
            if i < n and (s[i] == '+' or s[i] == '-'):
                i += 1
            while i < n and s[i].isnumeric():
                i += 1
                isNumber = True

        while i < n and s[i].isspace():
            i += 1
        return isNumber and i == n


s = Solution()
print(s.isNumber('e'))
