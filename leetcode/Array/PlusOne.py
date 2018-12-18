class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits) - 1
        while l >= 0:
            digit = digits[l]
            if digit < 9:
                digits[l] += 1
                return digits
            else:
                digits[l] = 0
                l -= 1
        digits.append(0)
        digits[0] = 1
        return digits

s = Solution()
s.plusOne([9])
