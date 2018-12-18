class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return -1
        accurant = [ - 1 for i in range(256)]
        for i in range(len(s)):
            if accurant[i] == -1:
                accurant[i] == 0
            else:
                accurant[i] == -2

        for i in range(len(s)):
            if accurant[i] == 0:
                return i
        return -1

