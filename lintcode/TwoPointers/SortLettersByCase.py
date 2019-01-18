import string
class Solution:
    def sortLetters(self,chars):
        left,right = 0,len(chars) - 1
        while left <= right:
            while left <= right and str(chars[left]).islower():
                left += 1
            while left <= right and str(chars[right]).isupper():
                right -= 1
            if left < right:
                temp = chars[left]
                chars =  chars[:left]  + chars[right] + chars[left + 1:]
                chars = chars[:right] + temp + chars[right + 1:]
                left += 1
                right -= 1
        print(chars)

chars = 'Ca'
s = Solution()
s.sortLetters(chars)
