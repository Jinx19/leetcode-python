class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed = ''
        j = len(s)
        for i in range(len(s) - 1, -1):
            if s[i] == ' ':
                j = i
            else:
                if i == 0 or s[i - 1] == ' ':
                    if len(reversed) != 0:
                        reversed.join(' ')
                    reversed.join(s[i:j])

        return reversed


s = Solution()
print(s.reverseWords("the sky is blue"))
