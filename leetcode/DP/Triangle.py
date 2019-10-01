'''

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

dp[1] =

'''


class Solution:
    def helper(self, prev, triangle, level, sum):
        if level == len(triangle):
            return sum
        i = level
        left, right = prev, prev + 1
        if left >= 0 and right <= i:
            return min(
                self.helper(left, triangle, level + 1,
                            sum + triangle[i][left]),
                self.helper(right, triangle, level + 1,
                            sum + triangle[i][right]))
        elif left < 0:
            return self.helper(right, triangle, level + 1,
                               sum + triangle[i][right])
        else:
            return self.helper(left, triangle, level + 1,
                               sum + triangle[i][left])

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [-1 for i in range(len(triangle))]
        dp[0] = 0
        sum = triangle[0][dp[0]]
        return self.helper(0, triangle, 1, sum)

    def minimumTotal2(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [[0 for i in range(len(triangle))] for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j - 1 >= 0 and j <= i - 1:
                    dp[i][j] = min(dp[i - 1][j] + triangle[i][j],
                                   dp[i - 1][j - 1] + triangle[i][j])
                elif j - 1 >= 0:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
        return min(list(dp[len(triangle) - 1]))


s = Solution()
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
res = s.minimumTotal2(triangle)
print(res)