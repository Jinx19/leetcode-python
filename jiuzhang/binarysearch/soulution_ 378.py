import heapq


class point():
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __lt__(self, value):
        return self.value < value.value


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        m, n = len(matrix), len(matrix[0])
        for i in range(n):
            heapq.heappush(heap, point(0, i, matrix[0][i]))

        for i in range(k - 1):
            smallpoint = heapq.heappop(heap)
            if smallpoint.x + 1 < m:
                x = smallpoint.x + 1
                y = smallpoint.y
                value = matrix[x][y]
                heapq.heappush(heap, point(x, y, value))
        return heapq.heappop(heap).value


if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    s = Solution()
    ans = s.kthSmallest(matrix, k)
    print(ans)
