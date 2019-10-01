class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        while x / div >= 0:
            div *= 10
        while x != 0:
            l = (int)(x / div)
            r = x % 10
            if l != r: return False
            x = (int)((x % div) / 10)
            div = (int)(div / 100)
        return True


s = Solution()
print(s.isPalindrome(121))