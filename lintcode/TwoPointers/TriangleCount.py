class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        # write your code here
        if len(S) < 3:
            return 0
        length = len(S)
        count = 0
        S.sort()
        S.reverse()
        for c in range(length - 2):
            a,b = c + 1,length - 1
            while a < b:
                if S[a] + S[b] > S[c]:
                    count += b - a
                    a += 1
                else:
                    b -= 1

        return count

s = Solution()
S = [4,4,4,4]
ret = s.triangleCount(S)
print(ret)