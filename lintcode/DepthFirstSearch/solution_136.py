class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def isPalidrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right - 1
        return True

    def dfs(self, s, start, result, path):
        if start == len(s) and path not in result:
            result.append(list(path))
            return
        for i in range(start, len(s)):
            if not self.isPalidrome(s[start:i + 1]):
                continue
            path.append(s[start:i + 1])
            self.dfs(s, i + 1, result, path)
            path.pop()

    def partition(self, s):
        # write your code here
        result = list()
        path = list()
        self.dfs(s, 0, result, path)
        return result


#
# class Solution:
#
#     def partition(self, s):
#         results = []
#         self.dfs(s, [], results)
#         return results
#
#     def dfs(self, s, stringlist, results):
#         if len(s) == 0:
#             results.append(stringlist)
#             # results.append(list(stringlist))
#             return
#
#         for i in range(1, len(s) + 1):
#             prefix = s[:i]
#             if self.is_palindrome(prefix):
#                 self.dfs(s[i:], stringlist + [prefix], results)
#                 # stringlist.append(prefix)
#                 # self.dfs(s[i:], stringlist, results)
#                 # stringlist.pop()
#
#     def is_palindrome(self, s):
#         return s == s[::-1]
# test
s = "cbbbcc"
solution = Solution()
print(solution.partition(s))
