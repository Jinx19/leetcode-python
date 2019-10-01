class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and (not s[i:i + 1].isalnum()):
                i += 1
            while i < j and (not s[j:j + 1].isalnum()):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


s = Solution()
print(s.isPalindrome('A man, a plan, a canal: Panama'))
