import heapq


def trapRainWater(heightMap):
    if heightMap is None or len(heightMap) == 0 or len(heightMap[0]) == 0:
        return 0

    m, n = len(heightMap), len(heightMap[0])

    heap = []
    visited = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):
        heapq.heappush(heap, (heightMap[i][0], i, 0))
        heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
        visited[i][0] = 1
        visited[i][n - 1] = 1

    for j in range(n):
        heapq.heappush(heap, (heightMap[0][j], 0, j))
        heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))

        visited[0][j] = 1
        visited[m - 1][j] = 1

    dirX = [0, 0, -1, 1]
    dirY = [-1, 1, 0, 0]

    water = 0

    while len(heap) > 0:
        cell = heapq.heappop(heap)
        for i in range(4):
            x = cell[1] + dirX[i]
            y = cell[2] + dirY[i]

            if x < m and x >= 0 and y < n and y >= 0 and visited[x][y] != 1:
                heapq.heappush(heap, (max(cell[0], heightMap[x][y]), x, y))
                visited[x][y] = 1
                water += max(0, cell[0] - heightMap[x][y])
    return water


heapMap = [
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 1]
]

ans = trapRainWater(heapMap)
print(ans)
