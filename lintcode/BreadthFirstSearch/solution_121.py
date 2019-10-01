from collections import deque


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def bfs(self, map, distance, start, end, dict):
        q = deque([start])
        distance[start] = 0
        for s in dict:
            map[s] = []

        while q:
            crt = q.popleft()
            nextlist = dict & set(crt[:index] + ch + crt[index + 1:]
                                  for index in range(len(crt))
                                  for ch in 'abcdefghijklmnopqrstuvwxyz')
            nextlist -= set([crt])
            for next in nextlist:
                map[next].append(crt)
                if next not in distance:
                    distance[next] = distance[crt] + 1
                    q.append(next)

    def dfs(self, ladders, path, crt, start, distance, map):
        path.append(crt)
        if crt == start:
            path.reverse()
            ladders.append(list(path))
            path.reverse()
        else:
            for pre in map[crt]:
                if pre in distance and distance[crt] == distance[pre] + 1:
                    self.dfs(ladders, path, pre, start, distance, map)
        path.pop()

    def findLadders(self, start, end, dict):
        # write your code here
        dict |= set([start])
        dict |= set([end])
        ladders = []
        map = {}
        distance = {}
        self.bfs(map, distance, start, end, dict)
        path = []
        self.dfs(ladders, path, end, start, distance, map)
        print(ladders)


solution = Solution()
start = "a"
end = "c"
dict = set(["a", "b", "c"])
solution.findLadders(start, end, dict)
