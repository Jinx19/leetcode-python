import sys
def minAreaRect(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    xy = {}
    hasMinArea = False
    minArea = sys.maxsize
    for point in points:
        if point[0] not in xy.keys():
            y = []
            y.append(point[1])
            xy[point[0]] = y
        else:
            xy[point[0]].append(point[1])

    for i in range(len(points)):
        for j in range(i + 1,len(points)):
            x0 = points[i][0]
            y0 = points[i][1]
            x1 = points[j][0]
            y1 = points[j][1]

            if x0 == x1 or  y0 == y1:
                continue

            area = abs(x0 - x1) * abs(y0 - y1)

            if area > minArea:
                continue

            if (y1 not in xy[x0] or y0 not in xy[x1]):
                continue
            hasMinArea = True
            minArea = area

    if hasMinArea:
        return minArea
    else:
        return 0

points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
minarea = minAreaRect(points)
print(minarea)
